---
title: Debugging a Stack Overflow
description: Debugging a Stack Overflow
ms.assetid: fc67effa-88c9-4915-a5a8-8c094595c6c5
keywords: ["stack overflow", "call stack, debugging a stack overflow"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Stack Overflow


## <span id="ddk_debugging_a_stack_overflow_dbg"></span><span id="DDK_DEBUGGING_A_STACK_OVERFLOW_DBG"></span>


A stack overflow is an error that user-mode threads can encounter. There are three possible causes for this error:

-   A thread uses the entire stack reserved for it. This is often caused by infinite recursion.

-   A thread cannot extend the stack because the page file is maxed out, and therefore no additional pages can be committed to extend the stack.

-   A thread cannot extend the stack because the system is within the brief period used to extend the page file.

When a function running on a thread allocates local variables, the variables are put on the thread's call stack. The amount of stack space required by the function could be as large as the sum of the sizes of all the local variables. However, the compiler usually performs optimizations that reduce the stack space required by a function. For example, if two variables are in different scopes, the compiler can use the same stack memory for both of those variables. The compiler might also be able to eliminate some local variables entirely by optimizing calculations.

The amount of optimization is influenced by compiler settings applied at build time. For example, a Debug build and a Release build have different levels of optimization. The amount of stack space required by a function in a Debug build might be larger than the amount of stack space required by that same function in a Release build.

Here is an example of how to debug a stack overflow. In this example, NTSD is running on the same computer as the target application and is redirecting its output to KD on the host computer. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

The first step is see what event caused the debugger to break in:

```dbgcmd
0:002> .lastevent 
Last event: Exception C00000FD, second chance 
```

You can look up exception code 0xC00000FD in ntstatus.h, which can be found in the Microsoft Windows SDK and the Windows Driver Kit (WDK). This exception code is STATUS\_STACK\_OVERFLOW.

To double-check that the stack overflowed, you can use the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command:

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

The target thread has broken into COMCTL32!\_chkstk, which indicates a stack problem. Now you should investigate the stack usage of the target process. The process has multiple threads, but the important one is the one that caused the overflow, so identify this thread first:

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

The stack information is contained in the TEB (Thread Environment Block) at 0x7FFDC000. The easiest way to list it is using [**!teb**](-teb.md). However, this requires you to have the proper symbols. For maximum versatility, assume you have no symbols:

```dbgcmd
0:002> dd 7ffdc000 L4 
7ffdc000   009fdef0 00a00000 009fc000 00000000 
```

To interpret this, you need to look up the definition of the TEB data structure. If you had complete symbols, you could use [**dt TEB**](dt--display-type-.md) to do this. But in this case, you will need to look at the ntpsapi.h file in the Microsoft Windows SDK. For Windows XP and later versions of Windows, this file contains the following information:

```cpp
typedef struct _TEB {
    NT_TIB NtTib;
    PVOID  EnvironmentPointer;
    CLIENT_ID ClientId;
    PVOID ActiveRpcHandle;
    PVOID ThreadLocalStoragePointer;
    PPEB ProcessEnvironmentBlock;
    ULONG LastErrorValue;
    .....
    PVOID DeallocationStack;
    .....
} TEB;

typedef struct _NT_TIB {
    struct _EXCEPTION_REGISTRATION_RECORD *ExceptionList;
    PVOID StackBase;
    PVOID StackLimit;
    .....
} NT_TIB; 
```

This indicates that the second and third DWORDs in the TEB structure point to the bottom and top of the stack, respectively. In this case, these addresses are 0x00A00000 and 0x009FC000. (The stack grows downward in memory.) You can calculate the stack size using the [**? (Evaluate Expression)**](---evaluate-expression-.md) command:

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

Now break into KD and look at the overall system memory usage with the [**!vm**](-vm.md) extension command:

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

### <span id="analyzing_a_single_function_call"></span><span id="ANALYZING_A_SINGLE_FUNCTION_CALL"></span>Analyzing a Single Function Call

It can also be useful to find out exactly how much stack space a certain function call is allocating.

To do this, disassemble the first few instructions and look for the instruction `sub esp`*number*. This moves the stack pointer, effectively reserving *number* bytes for local data.

Here is an example:

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

 

 





