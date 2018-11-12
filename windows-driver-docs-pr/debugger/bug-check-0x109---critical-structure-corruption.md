---
title: Bug Check 0x109 CRITICAL_STRUCTURE_CORRUPTION
description: The CRITICAL_STRUCTURE_CORRUPTION bug check has a value of 0x00000109. This indicates that the kernel has detected critical kernel code or data corruption.
ms.assetid: 38d4d722-a915-4f17-899b-2a0b4aa69d95
keywords: ["Bug Check 0x109 CRITICAL_STRUCTURE_CORRUPTION", "CRITICAL_STRUCTURE_CORRUPTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CRITICAL_STRUCTURE_CORRUPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x109: CRITICAL\_STRUCTURE\_CORRUPTION


The CRITICAL\_STRUCTURE\_CORRUPTION bug check has a value of 0x00000109. This indicates that the kernel has detected critical kernel code or data corruption.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CRITICAL\_STRUCTURE\_CORRUPTION Parameters


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
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The type of the corrupted region. (See the following table later on this page.)</p></td>
</tr>
</tbody>
</table>

 

The value of Parameter 4 indicates the type of corrupted region.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 4</th>
<th align="left">Type of Corrupted Region, Type of Corruption, or Type of Action Taken That Caused the Corruption</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>A generic data region</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>A function modification or the Itanium-based function location</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>A processor interrupt dispatch table (IDT)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>A processor global descriptor table (GDT)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>A type-1 process list corruption</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>A type-2 process list corruption</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6</p></td>
<td align="left"><p>A debug routine modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7</p></td>
<td align="left"><p>A critical MSR modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>Object type</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9</p></td>
<td align="left"><p>A processor IVT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA</p></td>
<td align="left"><p>Modification of a system service function</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB</p></td>
<td align="left"><p>A generic session data region</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC</p></td>
<td align="left"><p>Modification of a session function or .pdata</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD</p></td>
<td align="left"><p>Modification of an import table</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xE</p></td>
<td align="left"><p>Modification of a session import table</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xF</p></td>
<td align="left"><p>Ps Win32 callout modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>Debug switch routine modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x11</p></td>
<td align="left"><p>IRP allocator modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x12</p></td>
<td align="left"><p>Driver call dispatcher modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x13</p></td>
<td align="left"><p>IRP completion dispatcher modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x14</p></td>
<td align="left"><p>IRP deallocator modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x15</p></td>
<td align="left"><p>A processor control register</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x16</p></td>
<td align="left"><p>Critical floating point control register modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x17</p></td>
<td align="left"><p>Local APIC modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x18</p></td>
<td align="left"><p>Kernel notification callout modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x19</p></td>
<td align="left"><p>Loaded module list modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1A</p></td>
<td align="left"><p>Type 3 process list corruption</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>Type 4 process list corruption</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1C</p></td>
<td align="left"><p>Driver object corruption</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1D</p></td>
<td align="left"><p>Executive callback object modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1E</p></td>
<td align="left"><p>Modification of module padding</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1F</p></td>
<td align="left"><p>Modification of a protected process</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>A generic data region</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21</p></td>
<td align="left"><p>A page hash mismatch</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x22</p></td>
<td align="left"><p>A session page hash mismatch</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23</p></td>
<td align="left"><p>Load config directory modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x24</p></td>
<td align="left"><p>Inverted function table modification</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x25</p></td>
<td align="left"><p>Session configuration modification</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x26</p></td>
<td align="left"><p>An extended processor control register</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x27</p></td>
<td align="left"><p>Type 1 pool corruption</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x28</p></td>
<td align="left"><p>Type 2 pool corruption</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x29</p></td>
<td align="left"><p>Type 3 pool corruption</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x101</p></td>
<td align="left"><p>General pool corruption</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x102</p></td>
<td align="left"><p>Modification of win32k.sys</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

There are generally three different causes for this bug check:

1.  A driver has inadvertently, or deliberately, modified critical kernel code or data. Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows for x64-based computers do not allow the kernel to be patched except through authorized Microsoft-originated hot patches. For more information, see [Patching Policy for x64-based Systems](https://go.microsoft.com/fwlink/p/?linkid=50719).

2.  A developer attempted to set a normal kernel breakpoint using a kernel debugger that was not attached when the system was started. Normal breakpoints ([**bp**](bp--bu--bm--set-breakpoint-.md)) can only be set if the debugger is attached at start time. Processor breakpoints ([**ba**](ba--break-on-access-.md)) can be set at any time.

3.  A hardware corruption occurred. For example, the kernel code or data could have been stored in memory that failed.

Resolution
----------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

To start, examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command. You can specify the processor number to examine the stacks on all processors.

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Run the Windows Memory Diagnostics tool, to test the memory. In the control panel search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




