---
title: Bug Check 0x1AB UNWIND_ON_INVALID_STACK
description: The UNWIND_ON_INVALID_STACK bug check has a value of 0x000001AB. It indicates that a memory access outside of the valid stack range occurred during a memory unwind operation.
keywords: ["Bug Check 0x1AB UNWIND_ON_INVALID_STACK", "UNWIND_ON_INVALID_STACK"]
ms.date: 07/29/2022
topic_type:
- apiref
api_name:
- UNWIND_ON_INVALID_STACK
api_type:
- NA
---

# Bug Check 0x1AB: UNWIND\_ON\_INVALID\_STACK

The UNWIND\_ON\_INVALID\_STACK bug check has a value of 0x000001AB. It indicates that an attempt was made to access memory outside of the valid kernel stack range. In particular, this BugCheck indicates that stack unwinding crossed over into an invalid kernel stack.  This might indicate that the kernel stack pointer has become
corrupted during exception dispatch or unwind (e.g. due to stack corruption of a frame pointer), or that a driver is executing off of a stack that is not a legal kernel stack.

At the time the invalid access occurred, the exception record was not available. 

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## UNWIND\_ON\_INVALID\_STACK Parameters

<table>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>A pointer to the current stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left">The Type of stack limit such as NormalStackLimits (3).  Because the
        stack is invalid, this represents the kernel's best estimation as to
        the type of kernel stack that should be active given the state of the
        machine. <p>Stack limit type:</p><ul>
<li>0x0 - Bugcheck stack (any stack if stack limits are computed during bugcheck time)</li>
<li>0x1 - A processor DPC stack</li>
<li>0x2 - A KeExpandKernelStackAndCallout(Ex) stack</li>
<li>0x3 - A normal kernel thread stack</li>
<li>0x4 - A kernel thread stack during thread context swap (ambiguous which thread is active)</li>
<li>0x5 - A win32k kernel/user callout stack</li>
<li>0x6 - A processor ISR stack</li>
<li>0x7 - Kernel debugger stack (any stack when the kernel debugger is handling KD I/O)</li>
<li>0x8 - A processor NMI handling stack</li>
<li>0x9 - A processor machine check handling stack</li>
<li>0xA - A processor exception stack (used to dispatch certain raised IRQL exceptions)</li>
</ul></p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>A pointer to the context record representing the context that was
        being unwound (or dispatched for an exception) when the invalid stack
        was encountered.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left">ExceptionRecord - Reserved and always 0 for UNWIND_ON_INVALID_STACK.</td>
</tr>
</tbody>
</table>

## Cause

An attempt to access an invalid stack occurred. As kernel stack is limited in size, the developer needs to be careful with tracking it limits, for example when using it to copy blocks of video memory.  For information about the Windows Kernel stack, see [Using the Kernel Stack](../kernel/using-the-kernel-stack.md).

## Resolution

Using a full kernel dump or an attached debugger, the following commands may be useful to gather information and track down the code that is incorrectly accessing memory.

First use the [!analyze](-analyze.md) command to gather information, in particular the bug check parameters. Also examine the faulting source line and module name, if available.

```dbgcmd
Arguments:
Arg1: 89344350fffff607
Arg2: 0000000000000003
Arg3: fffff607893436c4
Arg4: fffff60789343ea8
```

Use the provided [.trap](-trap.md) command link in the !analyze output to set the context to the trap frame.

```dbgcmd
TRAP_FRAME:  fffff60789343f50 -- (.trap 0xfffff60789343f50)
NOTE: The trap frame does not contain all registers.
Some register values may be zeroed or incorrect.
rax=fffff607893441e8 rbx=0000000000000000 rcx=0000000010000004
rdx=0000000000000002 rsi=0000000000000000 rdi=0000000000000000
rip=fffff8026dc296cf rsp=fffff607893440e8 rbp=fffff60789344350
 r8=fffff8028e7a08b2  r9=0000000000000008 r10=fffff8029e9c3980
r11=fffff607893440f8 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
```

Use the [!thread](-thread.md) command to gather information on what is running. In this example it looks like a video scheduler worker thread is running. 

```dbgcmd
2: kd> !thread
THREAD ffff8f8e9af25080  Cid 0004.0378  Teb: 0000000000000000 Win32Thread: 0000000000000000 RUNNING on processor 2
Not impersonating
DeviceMap                 ffffd601dbe63e30
Owning Process            ffff8f8e99ab4040       Image:         System
Attached Process          N/A            Image:         N/A
Wait Start TickCount      14361          Ticks: 0
Context Switch Count      64607          IdealProcessor: 1             
UserTime                  00:00:00.000
KernelTime                00:00:06.046
Win32 Start Address dxgmms2!VidSchiWorkerThread (0xfffff8027a70d100)
Stack Init fffff60789344c70 Current fffff607893445c0
Base fffff60789345000 Limit fffff6078933f000 Call 0000000000000000
Priority 16 BasePriority 16 PriorityDecrement 0 IoPriority 2 PagePriority 5
...
```

Then use [kb (Display Stack Backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) with the f option to display the stack and the memory usage to see if there is a large memory user. 

```dbgcmd
2: kd> kf
...
02       198 fffff607`89344460 fffff802`8e6b41d5     amdkmdag+0x2308b2
03       120 fffff607`89344580 fffff802`8e59eb35     amdkmdag+0x1441d5
04        30 fffff607`893445b0 fffff802`8e62b5e8     amdkmdag+0x2eb35
05        c0 fffff607`89344670 fffff802`8e623f6c     amdkmdag+0xbb5e8
...
```

If a specific part of the code looks suspicious, use the [u, ub, uu (Unassemble)](u--unassemble-.md) command to examine the associated assemble language code.

```dbgcmd
2: kd> u fffff607`893442c8 l10
fffff607`893442c8 d04234          rol     byte ptr [rdx+34h],1
fffff607`893442cb 8907            mov     dword ptr [rdi],eax
fffff607`893442cd f6ff            idiv    bh
fffff607`893442cf ff01            inc     dword ptr [rcx]
fffff607`893442d1 17              ???
fffff607`893442d2 c4              ???
fffff607`893442d3 9f              lahf
fffff607`893442d4 8e8fffff0060    mov     cs,word ptr [rdi+6000FFFFh]
fffff607`893442da 5a              pop     rdx
fffff607`893442db 9f              lahf
fffff607`893442dc 8e8fffff0000    mov     cs,word ptr [rdi+0FFFFh]
fffff607`893442e2 0000            add     byte ptr [rax],al
fffff607`893442e4 0000            add     byte ptr [rax],al
fffff607`893442e6 0000            add     byte ptr [rax],al
fffff607`893442e8 7527            jne     fffff607`89344311
fffff607`893442ea 6e              outs    dx,byte ptr [rsi]
```

Use the [.cxr (Display Context Record)](-cxr.md) command to display the context record, using the parameter 3 value provided by !analyze.

```dbgcmd
.cxr fffff607893436c4

```


Use the [!vm](-vm.md) command to examine memory usage, for example of to see how much of the Kernel Stacks memory is in use.

```dbgcmd
0: kd> !vm

Physical Memory:          1541186 (    6164744 Kb)
Available Pages:           470550 (    1882200 Kb)
ResAvail Pages:           1279680 (    5118720 Kb)

...

Kernel Stacks:              13686 (      54744 Kb)
```

Use the [!stacks](-stacks.md) command, with the 2 parameter to view  information about stacks. This command may take some time to run. Examine the output for repeated patterns of blocked execution that may point towards and area for further investigation.

## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)