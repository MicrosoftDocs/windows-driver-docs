---
title: Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA
description: The PAGE_FAULT_IN_NONPAGED_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. 
ms.assetid: 63b4ab82-f7a9-4e14-bf7c-707a22d7e251
keywords: ["Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA", "PAGE_FAULT_IN_NONPAGED_AREA"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PAGE_FAULT_IN_NONPAGED_AREA
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x50: PAGE\_FAULT\_IN\_NONPAGED\_AREA


The PAGE\_FAULT\_IN\_NONPAGED\_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. Typically the memory address is wrong or the memory address is pointing at freed memory.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).


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
<td align="left"><p><strong>0:</strong> Read operation</p>
<p><strong>1:</strong> Write operation</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address that referenced memory (if known)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

Cause
-----

Bug check 0x50 can occur after the installation of faulty hardware or in the event of failure of installed hardware (usually related to defective RAM, be it main memory, L2 RAM cache, or video RAM).

Another possible cause is the installation of a faulty system service or faulty driver code.

Antivirus software can also trigger this error, as can a corrupted NTFS volume.

Remarks
----------

**Gather Information**

Examine the name of the driver if that was listed on the blue screen.

Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

**Windows Memory Diagnostics**

Run the Windows Memory Diagnostics tool, to test the memory. Click the Start button, and then clicking Control Panel. In the search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

**Resolving a faulty hardware problem:** If hardware has been added to the system recently, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. You should run hardware diagnostics supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer.

**Resolving a faulty system service problem:** Disable the service and confirm that this resolves the error. If so, contact the manufacturer of the system service about a possible update. If the error occurs during system startup, investigate the Windows repair options. For more information, see [Recovery options in Windows 10](https://windows.microsoft.com/windows-10/windows-10-recovery-options).

**Resolving an antivirus software problem:** Disable the program and confirm that this resolves the error. If it does, contact the manufacturer of the program about a possible update.

**Resolving a corrupted NTFS volume problem:** Run **Chkdsk /f /r** to detect and repair disk errors. You must restart the system before the disk scan begins on a system partition. Contact the manufacture of the hard driver system to locate any diagnostic tools that they provide for the hard drive sub system.

For general blue screen troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

Resolution
-------

Typically, this address is in freed memory or is simply invalid.

This cannot be protected by a **try - except** handler -- it can only be protected by a probe or similar techniques.


The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

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

Look at all of the output to gain information about what was going on when the bug check occurred. Examine MODULE_NAME: the FAULTING_MODULE:

Parameter 2 indicates that the bug check occurred when an area of memory was being read. 


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

Use the [!address](-address.md) command to look at parameter 3 which is the address of the the instruction  which referenced the bad memory.

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

Use the [r (Registers)](r--registers-) command to examine what was being executed as the system bug checked. 

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

Look at the STACK TEXT for clues on what was running when the failure occurred. If multiple dump files are available, compare information to look for common code that is in the stack. Use debugger commands such as use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to investigate the faulting code.


Use `!memusage` and to examine the general state of the system memory.

Use the `lm t n` to look at what was loaded in the memory. 


**Time Travel Trace**

If the bug check can be reproduced on demand, investigate the possibility of taking a time travel trace using WinDbg Preview. For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


 

 




