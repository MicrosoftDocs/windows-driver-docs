---
title: Bug Check 0x8E KERNEL_MODE_EXCEPTION_NOT_HANDLED
description: The KERNEL_MODE_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000008E. This bug check indicates that a kernel-mode application generated an exception that the error handler did not catch.
ms.assetid: 987ee868-5622-44e4-979c-3ae93a98b5b1
keywords: ["Bug Check 0x8E KERNEL_MODE_EXCEPTION_NOT_HANDLED", "KERNEL_MODE_EXCEPTION_NOT_HANDLED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_MODE_EXCEPTION_NOT_HANDLED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x8E: KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED


The KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED bug check has a value of 0x0000008E. This bug check indicates that a kernel-mode application generated an exception that the error handler did not catch.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED Parameters


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
<td align="left"><p>The trap frame</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED bug check is a very common bug check. To interpret it, you must identify which exception was generated.

Common exception codes include the following:

-   0x80000002: STATUS\_DATATYPE\_MISALIGNMENT indicates that an unaligned data reference was encountered.

-   0x80000003: STATUS\_BREAKPOINT indicates that a breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

-   0xC0000005: STATUS\_ACCESS\_VIOLATION indicates that a memory access violation occurred.

For a complete list of exception codes, see the Ntstatus.h file that is located in the inc directory of the Microsoft Windows Driver Kit (WDK).

Resolution
----------

The [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be very helpful in determining the root cause.
If you are not equipped to debug this problem, you should use some basic troubleshooting techniques:

-   Make sure you have enough disk space.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Try changing video adapters.

-   Check with your hardware vendor for any BIOS updates.

-   Disable BIOS memory options such as caching or shadowing.

If you plan to debug this problem, you might find it difficult to obtain a stack trace. Parameter 2 (the exception address) should identify the driver or function that caused this problem.

If exception code 0x80000003 occurs, a hard-coded breakpoint or assertion was hit, but the computer was started with the **/NODEBUG** switch. This problem should rarely occur. If it occurs repeatedly, make sure that a kernel debugger is connected and that the computer is started with the **/DEBUG** switch.

If exception code 0x80000002 occurs, the trap frame supplies additional information.

If you do not know the specific cause of the exception, consider the following items:

-   Hardware incompatibility. Make sure that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about compatibility with Windows 7 at the [Windows 7 Compatibility Center](https://go.microsoft.com/fwlink/p/?LinkID=246806).

-   Faulty device driver or system service. A faulty device driver or system service might be responsible for this error. Hardware issues, such as BIOS incompatibilities, memory conflicts, and IRQ conflicts can also generate this error.

If the bug check message lists a driver by name , disable or remove that driver. Also, disable or remove any drivers or services that were recently added. If the error occurs during the startup sequence and the system partition is formatted with NTFS file system, you might be able to use Safe Mode to rename or delete the faulty driver. If the driver is used as part of the system startup process in Safe Mode, you have to start the computer by using the Recovery Console to access the file.

If the problem is associated with Win32k.sys, the source of the error might be a third-party remote control program. If such software is installed, you can remove the service by starting the system by using the Recovery Console and then deleting the offending system service file.

Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing bug check 0x8E. You can disable memory caching of the BIOS to try to resolve the error. You should also run hardware diagnostics, especially the memory scanner, that the system manufacturer supplies. For more information about these procedures, see the owner's manual for your computer.

The error that generates this message can occur after the first restart during Windows Setup, or after Setup is finished. A possible cause of the error is lack of disk space for installation and system BIOS incompatibilities. For problems during Windows installation that are associated with lack of disk space, reduce the number of files on the target hard disk drive. Check for and delete any temporary files that you do not have to have, Internet cache files, application backup files, and .chk files that contain saved file fragments from disk scans. You can also use another hard disk drive with more free space for the installation.

You can resolve BIOS problems by upgrading the system BIOS version.

 

 




