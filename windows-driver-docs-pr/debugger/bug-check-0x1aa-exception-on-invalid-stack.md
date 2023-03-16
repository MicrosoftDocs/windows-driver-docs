---
title: Bug Check 0x1AA EXCEPTION_ON_INVALID_STACK
description: The EXCEPTION_ON_INVALID_STACK bug check has a value of 0x000001AA. It indicates a memory access outside of the valid stack range occurred.
keywords: ["Bug Check 0x1AA EXCEPTION_ON_INVALID_STACK", "EXCEPTION_ON_INVALID_STACK"]
ms.date: 07/29/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- EXCEPTION_ON_INVALID_STACK
api_type:
- NA
---

# Bug Check 0x1AA: EXCEPTION\_ON\_INVALID\_STACK

The EXCEPTION\_ON\_INVALID\_STACK bug check has a value of 0x000001AA. This BugCheck indicates that exception dispatch crossed over into an invalid kernel stack.  This might indicate that the kernel stack pointer has become
corrupted during exception dispatch or unwind (e.g. due to stack corruption of a frame pointer), or that a driver is executing off of a stack that is not a legal kernel stack.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received this error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## EXCEPTION\_ON\_INVALID\_STACK Parameters

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
<td align="left">Supplies an exception record representing the active exception that was being dispatched.</td>
</tr>
</tbody>
</table>



## Cause

An attempt to access an invalid stack occurred. As a kernel stack is limited in size, the developer needs to be careful with tracking it limits, for example when using it to copy blocks of video memory.  For information about the Windows Kernel stack, see [Using the Kernel Stack](../kernel/using-the-kernel-stack.md). 

## Resolution

Using a full kernel dump or an attached debugger, the following commands may be useful to gather information and track down the code that is incorrectly accessing memory.

First use the [!analyze](-analyze.md) command to gather information, in particular the bug check parameters. Also examine the faulting source line and module name, if available.

```dbgcmd
Arguments:
Arg1: 00000018940ffbe8
Arg2: 0000000000000003
Arg3: ffffe301c8db2900
Arg4: ffffdc0e9ee665d8
```

Use the provided [.trap](-trap.md) command link in the !analyze output to set the context to the trap frame.

```dbgcmd
2: kd> .trap 0xffffdc0e9ee66680
NOTE: The trap frame does not contain all registers.
Some register values may be zeroed or incorrect.
rax=003f8b813f20b6e0 rbx=0000000000000000 rcx=ee7defdd9c530000
rdx=ffffcb81660ea078 rsi=0000000000000000 rdi=0000000000000000
rip=fffff8002b7f8933 rsp=ffffdc0e9ee66810 rbp=ffffcb81511c3010
 r8=0000000000000001  r9=0000000000004014 r10=ffffdc0e9ee66910
r11=0000000000000000 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
iopl=0         nv up ei pl zr na po nc
dxgmms2!RemoveHeadList+0xd [inlined in dxgmms2!VidSchiSignalRegisteredSyncObjects+0x3f]:
fffff800`2b7f8933 48395808        cmp     qword ptr [rax+8],rbx ds:003f8b81`3f20b6e8=????????????????
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

This amount of memory used is less then available in this example.

Use the [!thread](-thread.md) command to gather information on what is running. In this example it looks like a video scheduler worker thread is running. 

```dbgcmd
2: kd> !thread
THREAD ffffcb816348b040  Cid 0c58.4a1c  Teb: 0000000000000000 Win32Thread: 0000000000000000 RUNNING on processor 2
Not impersonating
DeviceMap                 ffff840f38c04170
Owning Process            ffffcb81648980c0       Image:         YourPhone.exe
Attached Process          N/A            Image:         N/A
Wait Start TickCount      34501403       Ticks: 0
Context Switch Count      43             IdealProcessor: 3             
UserTime                  00:00:00.000
KernelTime                00:00:00.015
Win32 Start Address 0x00007fff34656d00
Stack Init ffffdc0e9ee675b0 Current ffffdc0e9ee66610
Base ffffdc0e9ee68000 Limit ffffdc0e9ee61000 Call 0000000000000000
Priority 8 BasePriority 8 PriorityDecrement 0 IoPriority 2 PagePriority 5
...
```

Then use [kb (Display Stack Backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) with the f option to display the stack and the memory usage to see if there is a large memory user. 

```dbgcmd
2: kd> kf
...
02        40 ffffdc0e`9ee66850 fffff800`2b7f8801     dxgmms2!VidSchiMarkDeviceAsError+0x4d  
...
```

If a specific part of the code looks suspicious, use the [u, ub, uu (Unassemble)](u--unassemble-.md) command to examine the associated assemble language code.

```dbgcmd
2: kd> u ffffdc0e`9ee66850 l10
ffffdc0e`9ee66850 1030            adc     byte ptr [rax],dh
ffffdc0e`9ee66852 1c51            sbb     al,51h
ffffdc0e`9ee66854 81cbffffc068    or      ebx,68C0FFFFh
ffffdc0e`9ee6685a e69e            out     9Eh,al
ffffdc0e`9ee6685c 0e              ???
ffffdc0e`9ee6685d dcff            fdiv    st(7),st
ffffdc0e`9ee6685f ff00            inc     dword ptr [rax]
ffffdc0e`9ee66861 0000            add     byte ptr [rax],al
ffffdc0e`9ee66863 0000            add     byte ptr [rax],al
ffffdc0e`9ee66865 0000            add     byte ptr [rax],al
ffffdc0e`9ee66867 000e            add     byte ptr [rsi],cl
ffffdc0e`9ee66869 0000            add     byte ptr [rax],al
ffffdc0e`9ee6686b 0000            add     byte ptr [rax],al
ffffdc0e`9ee6686d 0000            add     byte ptr [rax],al
ffffdc0e`9ee6686f 0010            add     byte ptr [rax],dl
ffffdc0e`9ee66871 301c51          xor     byte ptr [rcx+rdx*2],bl

```

Use the [.cxr (Display Context Record)](-cxr.md) command to display the context record, using the parameter 3 value provided by !analyze.

```dbgcmd
2: kd> .cxr ffffe301c8db2900
rax=003f8b813f20b6e0 rbx=ffffcb813f607650 rcx=ee7defdd9c530000
rdx=ffffcb81660ea078 rsi=0000000000000000 rdi=ffffcb81511c30a8
rip=fffff8002b7f8933 rsp=ffffdc0e9ee66810 rbp=ffffcb81511c3010
 r8=0000000000000001  r9=0000000000004014 r10=ffffdc0e9ee66910
r11=0000000000000000 r12=ffffdc0e9ee66910 r13=ffffcb814019c000
r14=0000000000000000 r15=ffffdc0e9ee66910
iopl=0         nv up ei pl zr na po nc
cs=0010  ss=0018  ds=002b  es=002b  fs=0053  gs=002b             efl=00050246
dxgmms2!RemoveHeadList+0xd [inlined in dxgmms2!VidSchiSignalRegisteredSyncObjects+0x3f]:
fffff800`2b7f8933 48395808        cmp     qword ptr [rax+8],rbx ds:002b:003f8b81`3f20b6e8=????????????????
```

Use the [.exr (Display Exception Record)](-exr--display-exception-record-.md) command to display the exception record, using the parameter 4 value provided by !analyze.

```dbgcmd
2: kd> .exr ffffdc0e9ee665d8
ExceptionAddress: fffff8002b7f8933 (dxgmms2!RemoveHeadList+0x000000000000000d)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000000
   Parameter[1]: ffffffffffffffff
Attempt to read from address ffffffffffffffff
```

The exception record indicates an attempt to read from and address of `ffffffffffffffff`, which would be an area to investigate further.


## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)
