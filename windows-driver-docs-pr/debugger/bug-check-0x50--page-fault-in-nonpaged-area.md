---
title: Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA
description: The PAGE_FAULT_IN_NONPAGED_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. 
keywords: ["Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA", "PAGE_FAULT_IN_NONPAGED_AREA"]
ms.date: 04/18/2019
topic_type:
- apiref
api_name:
- PAGE_FAULT_IN_NONPAGED_AREA
api_type:
- NA
ms.localizationpriority: high 
---

# Bug Check 0x50: PAGE\_FAULT\_IN\_NONPAGED\_AREA


The PAGE\_FAULT\_IN\_NONPAGED\_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. Typically the memory address is wrong or the memory address is pointing at freed memory.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## PAGE\_FAULT\_IN\_NONPAGED\_AREA Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
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
<td align="left"><p>Memory address referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left">
<p><i>After Windows 1507 (TH1) Version - x64 </i> </p>
<p><strong>0:</strong> Read operation</p>
<p><strong>2:</strong> Write operation</p>
<p><strong>10:</strong> Execute operation</p>

<p><i> After Windows 1507 (TH1) Version - x86 </i></p>
<p><strong>0:</strong> Read operation</p>
<p><strong>2:</strong> Write operation</p>
<p><strong>10:</strong> Execute operation</p>

<p><i> After Windows 1507 (TH1) Version - ARM </i></p>
<p><strong>0:</strong> Read operation</p>
<p><strong>1:</strong> Write operation</p>
<p><strong>8:</strong> Execute operation</p>

<p><i> Before Windows 1507 (TH1) Version x64 / x86 </i></p>
<p><strong>0:</strong> Read operation</p>
<p><strong>1:</strong> Write operation</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address that referenced memory (if known)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Type of page fault</p>
<p>0x03 - NONPAGED_BUGCHECK_WRONG_SESSION - An attempted reference to a session space address was made in the context of a process that has no session.  Typically this means the caller is improperly trying to access a session address without correctly obtaining an object reference to the correct process and attaching to it first. This bugcheck & subtype was last used in Windows 10 RS3.  In Windows 10 RS4 and above, this error is instead surfaced as 0x02 (NONPAGED_BUGCHECK_NOT_PRESENT_PAGE_TABLE).</p>
<p>0x04 - NONPAGED_BUGCHECK_VA_NOT_CANONICAL - An attempted reference to a non-canonical (illegal) virtual address (Parameter 1) was attempted.  The caller should not ever be trying to access this address.</p>
</td>
</tr>
</tbody>
</table>

 
If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**. You can use the debugger dx command to display this - `dx KiBugCheckDriver`.

## Cause

Bug check 0x50 can be caused by the installation of a faulty system service or faulty driver code. Antivirus software can also trigger this error, as can a corrupted NTFS volume.

It could also occur after the installation of faulty hardware or in the event of failure of installed hardware (usually related to defective RAM, be it main memory, L2 RAM cache, or video RAM).


## Remarks---

**Event Log:**
Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://support.microsoft.com/hub/4338813/windows-help#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

**Resolving a faulty driver:** 
Examine the name of the driver if that was listed on the blue screen or is present in the event log. Contact the driver vendor to see if an updated driver is available. 

**Resolving a faulty system service problem:** Disable the service and confirm that this resolves the error. If so, contact the manufacturer of the system service about a possible update. If the error occurs during system startup, investigate the Windows repair options. For more information, see [Recovery options in Windows 10](https://support.microsoft.com/help/12415/windows-10-recovery-options).

**Resolving an antivirus software problem:** Disable the program and confirm that this resolves the error. If it does, contact the manufacturer of the program about a possible update.

**Resolving a corrupted NTFS volume problem:** Run **Chkdsk /f /r** to detect and repair disk errors. You must restart the system before the disk scan begins on a system partition. Contact the manufacture of the hard driver system to locate any diagnostic tools that they provide for the hard drive sub system.

**Windows Memory Diagnostics:**
Run the Windows Memory Diagnostics tool, to test the physical memory. Select the Start button, and then select the Control Panel. In the search box, type Memory, and then select *Diagnose your computer's memory problems*.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

**Resolving a faulty hardware problem:** If hardware has been added to the system recently, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. You should run hardware diagnostics supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer.

For general blue screen troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

## Resolution

Typically, the referenced address is in freed memory or is simply invalid. This cannot be protected by a **try - except** handler -- it can only be protected by a probe or similar programming techniques.

Use the [**!analyze**](-analyze.md) debug extension with the -v verbose option to display information about the bug check to work to determine the root cause.

```dbgcmd
2: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.  This cannot be protected by try-except.
Typically the address is just plain bad or it is pointing at freed memory.
Arguments:
Arg1: ffffffff00000090, memory referenced.
Arg2: 0000000000000000, value 0 = read operation, 1 = write operation.
Arg3: fffff80240d322f9, If non-zero, the instruction address which referenced the bad memory
	address.
Arg4: 000000000000000c, (reserved)
```

In this example Parameter 2 indicates that the bug check occurred when an area of memory was being read.

Look at all of the !analyze output to gain information about what was going on when the bug check occurred. Examine MODULE_NAME: and the FAULTING_MODULE: to see which code is involved in referencing the invalid system memory.

Look at the STACK TEXT for clues on what was running when the failure occurred. If multiple dump files are available, compare information to look for common code that is in the stack.

Use the .trap command provided in the !analyze output to set the context.

```dbgcmd
TRAP_FRAME:  fffff98112e8b3d0 -- (.trap 0xfffff98112e8b3d0)
```

 Use debugger commands such as use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to investigate the faulting code.

Use the `lm t n` to list modules that are loaded in the memory.

Use the [d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command to investigate the areas of memory referenced by parameter 1 and parameter 3.

```dbgcmd
2: kd> db ffffffff00000090
ffffffff`00000090  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000a0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000b0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000c0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000d0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000e0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`000000f0  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
ffffffff`00000100  ?? ?? ?? ?? ?? ?? ?? ??-?? ?? ?? ?? ?? ?? ?? ??  ????????????????
```
In this case doesn't look like there is data in this area of memory in parameter 1, which is the area of memory that was attempting to be read.

Use the [!address](-address.md) command to look at parameter 3 which is the address of the the instruction which referenced the bad memory.

```dbgcmd
2: kd> !address fffff80240d322f9
Usage:                  Module
Base Address:           fffff802`40ca8000
End Address:            fffff802`415fb000
Region Size:            00000000`00953000
VA Type:                BootLoaded
Module name:            ntoskrnl.exe
Module path:            [\SystemRoot\system32\ntoskrnl.exe]
```

Use [u, ub, uu (Unassemble)Dissasemble](u--unassemble-.md) with parameter 3, to examine the which referenced the bad memory. For more information on X64 processor and assembly language see [The x64 Processor](the-x64-processor.md). 

```dbgcmd
2: kd> u fffff80240d322f9 
nt!RtlSubtreePredecessor+0x9:
fffff802`40d322f9 488b4810        mov     rcx,qword ptr [rax+10h]
fffff802`40d322fd eb07            jmp     nt!RtlSubtreePredecessor+0x16 (fffff802`40d32306)
fffff802`40d322ff 488bc1          mov     rax,rcx
fffff802`40d32302 488b4910        mov     rcx,qword ptr [rcx+10h]
fffff802`40d32306 4885c9          test    rcx,rcx
fffff802`40d32309 75f4            jne     nt!RtlSubtreePredecessor+0xf (fffff802`40d322ff)
fffff802`40d3230b c3              ret
fffff802`40d3230c c3              ret
```

Use `ub` to dissassemble backwards from the a given address.

Use the [r (Registers)](r--registers-.md) command to examine what was being executed as the system bug checked. 

```dbgcmd
2: kd> r
Last set context:
rax=ffffffff00000080 rbx=0000000000000000 rcx=ffffa68337cb7028
rdx=7a107838c48dfc00 rsi=0000000000000000 rdi=0000000000000000
rip=fffff80240d322f9 rsp=ffff840c96510958 rbp=ffffffffffffffff
 r8=ffffffffffffffff  r9=0000000000000000 r10=7ffffffffffffffc
r11=ffff840c96510a10 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
iopl=0         nv up ei ng nz na pe nc
cs=0010  ss=0018  ds=0000  es=0000  fs=0000  gs=0000             efl=00010282
nt!RtlSubtreePredecessor+0x9:
fffff802`40d322f9 488b4810        mov     rcx,qword ptr [rax+10h] ds:ffffffff`00000090=????????????????
```

In this case `fffff80240d322f9` is in the instruction pointer register, rip.

The `!pte` and `!pool` command may also be used to examine memory.

Use `!memusage` and to examine the general state of the system memory. 

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it sees errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifier* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](../devtest/driver-verifier.md).
