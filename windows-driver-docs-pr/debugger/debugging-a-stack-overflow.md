---
title: Debugging a Stack Overflow
description: This topic describes debugging a use mode stack overflow
keywords: ["stack overflow", "call stack, debugging a stack overflow"]
ms.date: 09/30/2021
---

# Debugging a Stack Overflow

A stack overflow is an error that user-mode threads can encounter. There are three possible causes for this error:

-   A thread uses the entire stack reserved for it. This is often caused by infinite recursion.

-   A thread cannot extend the stack because the page file is maxed out, and therefore no additional pages can be committed to extend the stack.

-   A thread cannot extend the stack because the system is within the brief period used to extend the page file.

When a function running on a thread allocates local variables, the variables are put on the thread's call stack. The amount of stack space required by the function could be as large as the sum of the sizes of all the local variables. However, the compiler usually performs optimizations that reduce the stack space required by a function. For example, if two variables are in different scopes, the compiler can use the same stack memory for both of those variables. The compiler might also be able to eliminate some local variables entirely by optimizing calculations.

The amount of optimization is influenced by compiler settings applied at build time. For example, by the [/F (Set Stack Size) - C++ Compiler Option](/cpp/build/reference/f-set-stack-size).

This topic assumes general knowledge of concepts, such as threads, thread blocks, stack and heap. For additional information on these base concepts, refer to *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Debugging a stack overflow without symbols

Here is an example of how to debug a stack overflow. In this example, NTSD is running on the same computer as the target application and is redirecting its output to KD on the host computer. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

The first step is see what event caused the debugger to break in:

```dbgcmd
0:002> .lastevent 
Last event: Exception C00000FD, second chance 
```

You can look up exception code 0xC00000FD in ntstatus.h, This exception code is STATUS\_STACK\_OVERFLOW, which indicates *A new guard page for the stack cannot be created.* All of the status codes are listed in [2.3.1 NTSTATUS Values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55).

You can also use the [!error](../debuggercmds/-error.md) command to look up errors in the Windows Debugger.

```dbgcmd
0:002> !error 0xC00000FD
Error code: (NTSTATUS) 0xc00000fd (3221225725) - A new guard page for the stack cannot be created.
```

To double-check that the stack overflowed, you can use the [k (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command:

```dbgcmd
0:002> k 
ChildEBP RetAddr
009fdd0c 71a32520 COMCTL32!_chkstk+0x25
009fde78 77cf8290 COMCTL32!ListView_WndProc+0x4c4
009fde98 77cfd634 USER32!_InternalCallWinProc+0x18
009fdf00 77cd55e9 USER32!UserCallWinProcCheckWow+0x17f
009fdf3c 77cd63b2 USER32!SendMessageWorker+0x4a3
009fdf5c 71a45b30 USER32!SendMessageW+0x44
009fdfec 71a45bb0 COMCTL32!CCSendNotify+0xc0e
009fdffc 71a1d688 COMCTL32!CICustomDrawNotify+0x2a
009fe074 71a1db30 COMCTL32!Header_Draw+0x63
009fe0d0 71a1f196 COMCTL32!Header_OnPaint+0x3f
009fe128 77cf8290 COMCTL32!Header_WndProc+0x4e2
009fe148 77cfd634 USER32!_InternalCallWinProc+0x18
009fe1b0 77cd4490 USER32!UserCallWinProcCheckWow+0x17f
009fe1d8 77cd46c8 USER32!DispatchClientMessage+0x31
009fe200 77f7bb3f USER32!__fnDWORD+0x22
009fe220 77cd445e ntdll!_KiUserCallbackDispatcher+0x13
009fe27c 77cfd634 USER32!DispatchMessageWorker+0x3bc
009fe2e4 009fe4a8 USER32!UserCallWinProcCheckWow+0x17f
00000000 00000000 0x9fe4a8 
```

The target thread has broken into COMCTL32!\_chkstk, which indicates a stack problem. Now you should investigate the stack usage of the target process. The process has multiple threads, but the important one is the one that caused the overflow, so identify this thread first using the [~ (Thread Status)](../debuggercmds/---thread-status-.md) command:

```dbgcmd
0:002> ~*k

   0  id: 570.574   Suspend: 1 Teb 7ffde000 Unfrozen
   .....

   1  id: 570.590   Suspend: 1 Teb 7ffdd000 Unfrozen
   .....

. 2  id: 570.598   Suspend: 1 Teb 7ffdc000 Unfrozen
ChildEBP RetAddr
 009fdd0c 71a32520 COMCTL32!_chkstk+0x25 
.....

   3  id: 570.760   Suspend: 1 Teb 7ffdb000 Unfrozen 
```

Now you need to investigate thread 2. The period at the left of this line indicates that this is the current thread.

The stack information is contained in the TEB (Thread Environment Block) at 0x7FFDC000. The easiest way to list it is using [!teb](../debuggercmds/-teb.md). 

```dbgcmd
0:000> !teb
TEB at 000000c64b95d000
    ExceptionList:        0000000000000000
    StackBase:            000000c64ba80000
    StackLimit:           000000c64ba6f000
    SubSystemTib:         0000000000000000
    FiberData:            0000000000001e00
    ArbitraryUserPointer: 0000000000000000
    Self:                 000000c64b95d000
    EnvironmentPointer:   0000000000000000
    ClientId:             0000000000003bbc . 0000000000004ba0
    RpcHandle:            0000000000000000
    Tls Storage:          0000027957243530
    PEB Address:          000000c64b95c000
    LastErrorValue:       0
    LastStatusValue:      0
    Count Owned Locks:    0
    HardErrorMode:        0```
```


However, this requires you to have the proper symbols. A more difficult situation is when you have no symbols and need to use the [dd (Display Memory)](../debuggercmds/d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command to display the raw values at that location:

```dbgcmd
0:002> dd 7ffdc000 L4 
7ffdc000   009fdef0 00a00000 009fc000 00000000 
```

To interpret this, you need to look up the definition of the TEB data structure. Use the [dt Display Type](../debuggercmds/dt--display-type-.md) command to do this on a system where symbols are available. 

```dbgcmd
0:000> dt _TEB
ntdll!_TEB
   +0x000 NtTib            : _NT_TIB
   +0x01c EnvironmentPointer : Ptr32 Void
   +0x020 ClientId         : _CLIENT_ID
   +0x028 ActiveRpcHandle  : Ptr32 Void
   +0x02c ThreadLocalStoragePointer : Ptr32 Void
   +0x030 ProcessEnvironmentBlock : Ptr32 _PEB
   +0x034 LastErrorValue   : Uint4B
   +0x038 CountOfOwnedCriticalSections : Uint4B
   +0x03c CsrClientThread  : Ptr32 Void
   +0x040 Win32ThreadInfo  : Ptr32 Void
   +0x044 User32Reserved   : [26] Uint4B
   +0x0ac UserReserved     : [5] Uint4B
   +0x0c0 WOW32Reserved    : Ptr32 Void
...
```

**Thread Data Structures**

To learn more about threads, you can also display information about the  thread control block related structures ethread and kthread. (Note that 64 bit examples are shown here.)

```dbgcmd
0:001> dt nt!_ethread
ntdll!_ETHREAD
   +0x000 Tcb              : _KTHREAD
   +0x430 CreateTime       : _LARGE_INTEGER
   +0x438 ExitTime         : _LARGE_INTEGER
   +0x438 KeyedWaitChain   : _LIST_ENTRY
   +0x448 PostBlockList    : _LIST_ENTRY
   +0x448 ForwardLinkShadow : Ptr64 Void
   +0x450 StartAddress     : Ptr64 Void
...
```

```dbgcmd
0:001> dt nt!_kthread
ntdll!_KTHREAD
   +0x000 Header           : _DISPATCHER_HEADER
   +0x018 SListFaultAddress : Ptr64 Void
   +0x020 QuantumTarget    : Uint8B
   +0x028 InitialStack     : Ptr64 Void
   +0x030 StackLimit       : Ptr64 Void
   +0x038 StackBase        : Ptr64 Void
```

Refer to *Microsoft Windows Internals* for more information about thread data structures.

Looking at a 32 bit version of the _TEB structure, it indicates that the second and third DWORDs in the TEB structure point to the bottom and top of the stack, respectively. In this example, these addresses are 0x00A00000 and 0x009FC000. (The stack grows downward in memory.) You can calculate the stack size using the [? (Evaluate Expression)](../debuggercmds/---evaluate-expression-.md) command:

```dbgcmd
0:002> ? a00000-9fc000
Evaluate expression: 16384 = 00004000 
```

This shows that the stack size is 16 K. The maximum stack size is stored in the field **DeallocationStack**. After some calculation, you can determine that this field's offset is 0xE0C.

```dbgcmd
0:002> dd 7ffdc000+e0c L1 
7ffdce0c   009c0000 

0:002> ? a00000-9c0000 
Evaluate expression: 262144 = 00040000 
```

This shows that the maximum stack size is 256 K, which means more than adequate stack space is left.

Furthermore, this process looks clean -- it is not in an infinite recursion or exceeding its stack space by using excessively large stack-based data structures.

Now break into KD and look at the overall system memory usage with the [!vm](../debuggercmds/-vm.md) extension command:

```dbgcmd
0:002> .breakin 
Break instruction exception - code 80000003 (first chance)
ntoskrnl!_DbgBreakPointWithStatus+4:
80148f9c cc               int     3

kd> !vm 

*** Virtual Memory Usage ***
        Physical Memory:     16268   (   65072 Kb)
        Page File: \??\C:\pagefile.sys
           Current:    147456Kb Free Space:     65988Kb
           Minimum:     98304Kb Maximum:       196608Kb
        Available Pages:      2299   (    9196 Kb)
        ResAvail Pages:       4579   (   18316 Kb)
        Locked IO Pages:        93   (     372 Kb)
        Free System PTEs:    42754   (  171016 Kb)
        Free NP PTEs:         5402   (   21608 Kb)
        Free Special NP:       348   (    1392 Kb)
        Modified Pages:        757   (    3028 Kb)
        NonPagedPool Usage:    811   (    3244 Kb)
        NonPagedPool Max:     6252   (   25008 Kb)
        PagedPool 0 Usage:    1337   (    5348 Kb)
        PagedPool 1 Usage:     893   (    3572 Kb)
        PagedPool 2 Usage:     362   (    1448 Kb)
        PagedPool Usage:      2592   (   10368 Kb)
        PagedPool Maximum:   13312   (   53248 Kb)
        Shared Commit:        3928   (   15712 Kb)
        Special Pool:         1040   (    4160 Kb)
        Shared Process:       3641   (   14564 Kb)
        PagedPool Commit:     2592   (   10368 Kb)
        Driver Commit:         887   (    3548 Kb)
        Committed pages:     45882   (  183528 Kb)
        Commit limit:        50570   (  202280 Kb)

        Total Private:       33309   (  133236 Kb)
         ..... 
```

First, look at nonpaged and paged pool usage. Both are well within limits, so these are not the cause of the problem.

Next, look at the number of committed pages: 183528 out of 202280. This is very close to the limit. Although this display does not show this number to be completely at the limit, you should keep in mind that while you are performing user-mode debugging, other processes are running on the system. Each time an NTSD command is executed, these other processes are also allocating and freeing memory. That means you do not know exactly what the memory state was like at the time the stack overflow occurred. Given how close the committed page number is to the limit, it is reasonable to conclude that the page file was used up at some point and this caused the stack overflow.

This is not an uncommon occurrence, and the target application cannot really be faulted for this. If it happens frequently, you may want to consider raising the initial stack commitment for the failing application.

## Analyzing a Single Function Call

It can also be useful to find out exactly how much stack space a certain function call is allocating.

To do this, disassemble the first few instructions and look for the instruction `sub esp`*number*. This moves the stack pointer, effectively reserving *number* bytes for local data.

Here is an example. First use the k command to look at the stack.

```dbgcmd
0:002> k 
ChildEBP RetAddr
009fdd0c 71a32520 COMCTL32!_chkstk+0x25
009fde78 77cf8290 COMCTL32!ListView_WndProc+0x4c4
009fde98 77cfd634 USER32!_InternalCallWinProc+0x18
009fdf00 77cd55e9 USER32!UserCallWinProcCheckWow+0x17f
009fdf3c 77cd63b2 USER32!SendMessageWorker+0x4a3
009fdf5c 71a45b30 USER32!SendMessageW+0x44
009fdfec 71a45bb0 COMCTL32!CCSendNotify+0xc0e
009fdffc 71a1d688 COMCTL32!CICustomDrawNotify+0x2a
009fe074 71a1db30 COMCTL32!Header_Draw+0x63
009fe0d0 71a1f196 COMCTL32!Header_OnPaint+0x3f
009fe128 77cf8290 COMCTL32!Header_WndProc+0x4e2
```

Then use the [u, ub, uu (Unassemble)](../debuggercmds/u--unassemble-.md) command to look at the assembler code at that address. 

```dbgcmd
0:002> u COMCTL32!Header_Draw
 COMCTL32!Header_Draw :
71a1d625 55               push    ebp
71a1d626 8bec             mov     ebp,esp
71a1d628 83ec58           sub     esp,0x58
71a1d62b 53               push    ebx
71a1d62c 8b5d08           mov     ebx,[ebp+0x8]
71a1d62f 56               push    esi
71a1d630 57               push    edi
71a1d631 33f6             xor     esi,esi 
```

This shows that **Header\_Draw** allocated 0x58 bytes of stack space.

The [r (Registers)](../debuggercmds/r--registers-.md) command provides information on the current contents of the registers, such as esp.

## Debugging stack overflow when symbols are available  

Symbols provide labels to items stored in memory, and when available, can make examining code easier. For an overview of symbols, see [Using Symbols](using-symbols.md). For information on setting the symbols path, see [.sympath (Set Symbol Path)](../debuggercmds/-sympath--set-symbol-path-.md).

To create a stack overflow, we can use this code, which continues to call a subroutine until the stack is exhausted.

```cpp
// StackOverFlow1.cpp 
// This program calls a sub routine using recursion too many times
// This causes a stack overflow
//

#include <iostream>

void Loop2Big()
{
    const char* pszTest = "My Test String";
    for (int LoopCount = 0; LoopCount < 10000000; LoopCount++)
    {
        std::cout << "In big loop \n";
        std::cout << (pszTest), "\n";
        std::cout << "\n";
        Loop2Big();
    }
}


int main()
{
    std::cout << "Calling Loop to use memory \n";
    Loop2Big();
}
```

When the code is compiled and ran under WinDbg, it will loop for some number of times and then throw a stack overflow exception.

```dbgcmd
(336c.264c): Break instruction exception - code 80000003 (first chance)
eax=00000000 ebx=00000000 ecx=0fa90000 edx=00000000 esi=773f1ff4 edi=773f25bc
eip=77491a02 esp=010ffa0c ebp=010ffa38 iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000246
ntdll!LdrpDoDebuggerBreak+0x2b:
77491a02 cc              int     3
0:000> g
(336c.264c): Stack overflow - code c00000fd (first chance)
```

Use the [!analyze](../debuggercmds/-analyze.md) command to check that we have indeed have a problem with our loop.

```dbgcmd
...

FAULTING_SOURCE_LINE_NUMBER:  25

FAULTING_SOURCE_CODE:  
    21: int main()
    22: {
    23:     std::cout << "Calling Loop to use memory \n";
    24:     Loop2Big();
>   25: }
    26: 
```

Using the kb command we see that there are many instances of our loop program each using memory.

```dbgcmd
0:000> kb
 # ChildEBP RetAddr      Args to Child      
...
0e 010049b0 00d855b5     01004b88 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x57 [C:\StackOverFlow1\StackOverFlow1.cpp @ 13] 
0f 01004a9c 00d855b5     01004c74 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
10 01004b88 00d855b5     01004d60 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
11 01004c74 00d855b5     01004e4c 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
12 01004d60 00d855b5     01004f38 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
13 01004e4c 00d855b5     01005024 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
14 01004f38 00d855b5     01005110 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
15 01005024 00d855b5     010051fc 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
16 01005110 00d855b5     010052e8 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
17 010051fc 00d855b5     010053d4 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
18 010052e8 00d855b5     010054c0 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
19 010053d4 00d855b5     010055ac 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
1a 010054c0 00d855b5     01005698 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 
1b 010055ac 00d855b5     01005784 00d81023 00ff5000 StackOverFlow1!Loop2Big+0x85 [C:\StackOverFlow1\StackOverFlow1.cpp @ 17] 

...

```

If symbols are available the  [dt _TEB](../debuggercmds/dt--display-type-.md) can be used to display information about the thread block. For more information about thread memory, see [Thread Stack Size](/windows/win32/procthread/thread-stack-size).

```dbgcmd
0:000> dt _TEB
ntdll!_TEB
   +0x000 NtTib            : _NT_TIB
   +0x01c EnvironmentPointer : Ptr32 Void
   +0x020 ClientId         : _CLIENT_ID
   +0x028 ActiveRpcHandle  : Ptr32 Void
   +0x02c ThreadLocalStoragePointer : Ptr32 Void
   +0x030 ProcessEnvironmentBlock : Ptr32 _PEB
   +0x034 LastErrorValue   : Uint4B
   +0x038 CountOfOwnedCriticalSections : Uint4B
   +0x03c CsrClientThread  : Ptr32 Void
   +0x040 Win32ThreadInfo  : Ptr32 Void
   +0x044 User32Reserved   : [26] Uint4B
   +0x0ac UserReserved     : [5] Uint4B
   +0x0c0 WOW32Reserved    : Ptr32 Void
```

We can also use the [!teb](../debuggercmds/-teb.md) command that displays the StackBase abd StackLimit.

```dbgcmd
0:000> !teb
TEB at 00ff8000
    ExceptionList:        01004570
    StackBase:            01100000
    StackLimit:           01001000
    SubSystemTib:         00000000
    FiberData:            00001e00
    ArbitraryUserPointer: 00000000
    Self:                 00ff8000
    EnvironmentPointer:   00000000
    ClientId:             0000336c . 0000264c
    RpcHandle:            00000000
    Tls Storage:          00ff802c
    PEB Address:          00ff5000
    LastErrorValue:       0
    LastStatusValue:      c00700bb
    Count Owned Locks:    0
    HardErrorMode:        0
```

We can calculate the stack size, using this command.

```dbgcmd
0:000> ?? int(@$teb->NtTib.StackBase) - int(@$teb->NtTib.StackLimit)
int 0n1044480
```

## Summary of commands

- [k (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)
- [~ (Thread Status)](../debuggercmds/---thread-status-.md)
- [d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](../debuggercmds/d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md)
- [u, ub, uu (Unassemble)](../debuggercmds/u--unassemble-.md)
- [r (Registers)](../debuggercmds/r--registers-.md)
- [.sympath (Set Symbol Path)](../debuggercmds/-sympath--set-symbol-path-.md) 
- [x (Examine Symbols)](../debuggercmds/x--examine-symbols-.md)
- [dt (Display Type)](../debuggercmds/dt--display-type-.md)
- [!analyze](../debuggercmds/-analyze.md)
- [!teb](../debuggercmds/-teb.md) 

## See also

[Getting Started with WinDbg (User-Mode)](getting-started-with-windbg.md) 

[/F (Set Stack Size) - C++ Compiler Option](/cpp/build/reference/f-set-stack-size) 

 
