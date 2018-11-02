---
title: Bug Check 0x7E SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
description: The SYSTEM_THREAD_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000007E. This bug check indicates that a system thread generated an exception that the error handler did not catch.
ms.assetid: 2ecea74f-21d6-4436-beed-d8cf8ef6b169
keywords: ["Bug Check 0x7E SYSTEM_THREAD_EXCEPTION_NOT_HANDLED", "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x7E: SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED


The SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED bug check has a value of 0x0000007E. This bug check indicates that a system thread generated an exception that the error handler did not catch.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED Parameters


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
<td align="left"><p>The exception code that was not handled</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address where the exception occurred</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the exception record</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The address of the context record</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED bug check is a common bug check. To interpret it, you must identify which exception was generated.

Common exception codes include the following:

-   0x80000002: STATUS\_DATATYPE\_MISALIGNMENT indicates an unaligned data reference was encountered.

-   0x80000003: STATUS\_BREAKPOINT indicates a breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

-   0xC0000005: STATUS\_ACCESS\_VIOLATION indicates a memory access violation occurred.

For a complete list of exception codes, see the Ntstatus.h file that is located in the inc directory of the Microsoft Windows Driver Kit (WDK).

Resolution
----------

If you are not equipped to use the Windows debugger to work on this problem, you should use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing bug check 0x7E.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Check with your hardware vendor for any BIOS updates. Hardware issues, such as BIOS incompatibilities, memory conflicts, and IRQ conflicts can also generate this error.

-   You can also disable memory caching/shadowing of the BIOS might to try to resolve the error. You should also run hardware diagnostics, that the system manufacturer supplies.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

**If you plan to debug this problem,** Parameter 2 (the exception address) should identify the driver or function that caused this problem.

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

If exception code 0x80000003 occurs, a hard-coded breakpoint or assertion was hit, but the system was started with the **/NODEBUG** switch. This problem should not occur frequently. If it occurs repeatedly, make sure that a kernel debugger is connected and the system is started with the **/DEBUG** switch.

If exception code 0x80000002 occurs, the trap frame supplies additional information.

If a driver is listed by name within the bug check message, disable or remove that driver. If the issue is narrowed down to a single driver, set breakpoints and single step in code to work to locate the failure and gain insight into events leading up to the crash.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md)

 

 




