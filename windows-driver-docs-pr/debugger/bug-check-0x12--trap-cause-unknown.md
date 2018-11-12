---
title: Bug Check 0x12 TRAP_CAUSE_UNKNOWN
description: The TRAP_CAUSE_UNKNOWN bug check has a value of 0x00000012. This indicates that an unknown exception has occurred.
ms.assetid: 43cbcc34-9df0-4d5f-b823-1cc3cafaa811
keywords: ["Bug Check 0x12 TRAP_CAUSE_UNKNOWN", "TRAP_CAUSE_UNKNOWN"]
ms.author: domars
ms.date: 06/26/2018
topic_type:
- apiref
api_name:
- TRAP_CAUSE_UNKNOWN
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12: TRAP\_CAUSE\_UNKNOWN


The TRAP\_CAUSE\_UNKNOWN bug check has a value of 0x00000012. This indicates that an unknown exception has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TRAP\_CAUSE\_UNKNOWN Parameters


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
<td align="left"><p>Type of TRAP_CAUSE_UNKNOWN</p>
<p><B>VALUES</B></p>
<p>1 - Unexpected interrupt. (Parameter 2 – Interrupt Vector)</p>
<p>2 - Unknown floating point exception. </p>
<p>3 - The enabled and asserted status bits (see processor definition).</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Dependent on Arg1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

Resolution
----------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

To start, examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command. You can specify the processor number to examine the stacks on all processors. 

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

The [!idt](-idt.md) extension can be used to display the interrupt service routines (ISRs) for a specified interrupt dispatch table (IDT). 

Some of the techniques described in [Debugging an Interrupt Storm](debugging-an-interrupt-storm.md) can be used with the unexpected interrupts.

For general information about working with crash dumps, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 

 




