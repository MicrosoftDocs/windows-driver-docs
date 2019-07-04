---
title: Bug Check 0x3B SYSTEM_SERVICE_EXCEPTION
description: The SYSTEM_SERVICE_EXCEPTION bug check has a value of 0x0000003B. This indicates that an exception happened while executing a routine that transitions from non-privileged code to privileged code.
ms.assetid: 0e2c230e-d942-4f32-ae8e-7a54aceb4c19
keywords: ["Bug Check 0x3B SYSTEM_SERVICE_EXCEPTION", "SYSTEM_SERVICE_EXCEPTION"]
ms.date: 03/24/2019
topic_type:
- apiref
api_name:
- SYSTEM_SERVICE_EXCEPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x3B: SYSTEM\_SERVICE\_EXCEPTION


The SYSTEM\_SERVICE\_EXCEPTION bug check has a value of 0x0000003B. This indicates that an exception happened while executing a routine that transitions from non-privileged code to privileged code.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SYSTEM\_SERVICE\_EXCEPTION Parameters


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
<td align="left"><p>The exception that caused the bug check. </p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the instruction that caused the bug check</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the context record for the exception that caused the bug check</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The stop code indicates that executing code had an exception and the thread that was below it, is a system thread.

The exception information returned in parameter one is listed in [NTSTATUS Values](https://docs.microsoft.com/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) and is also available in the ntstatus.h file located in the inc directory of the Windows Driver Kit. 

Common exception codes include:

-   0x80000003: STATUS\_BREAKPOINT

    A breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

-   0xC0000005: STATUS\_ACCESS\_VIOLATION

    A memory access violation occurred. (Parameter 4 of the bug check is the address that the driver attempted to access.)

Resolution
----------

**To debug this problem:** 

Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md). You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code. Use the [u, ub, uu (Unassemble)]() command to see the assembly program code.


The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

```
SYSTEM_SERVICE_EXCEPTION (3b)
An exception happened while executing a system service routine.
Arguments:
Arg1: 00000000c0000005, Exception code that caused the bugcheck
Arg2: fffff802328375b0, Address of the instruction which caused the bugcheck
Arg3: ffff9c0a746c2330, Address of the context record for the exception that caused the bugcheck
Arg4: 0000000000000000, zero.
...
```

For more information see the following topics:

[Using the !analyze Extension](using-the--analyze-extension.md) 

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

If a driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**. You can use the debugger [**dx (Display Debugger Object Model Expression)**](https://docs.microsoft.com/windows-hardware/drivers/debugger/dx--display-visualizer-variables-) command to display this - `dx KiBugCheckDriver`.

Use the [!error](-error.md) extension to display information about the exception code in parameter 1.

```
2: kd> !error 00000000c0000005
Error code: (NTSTATUS) 0xc0000005 (3221225477) - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.
```

Look at the STACK TEXT for clues on what was running when the failure occurred. If multiple dump files are available, compare information to look for common code that is in the stack. Use debugger commands such as use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to investigate the faulting code.

Use the `lm t n` to list modules that are loaded in the memory. 

Use `!memusage` and to examine the general state of the system memory. The `!pte` and `!pool` command may also be used to examine specific areas of memory. 

In the past, this error has been linked to excessive paged pool usage and may occur due to user-mode graphics drivers crossing over and passing bad data to the kernel code. If you suspect this is the case, use the pool options in driver verifier to gather additional information.

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it sees errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier).


**Time Travel Trace**

If the bug check can be reproduced on demand, investigate the possibility of taking a time travel trace using WinDbg Preview. For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


Remarks
----------

For general troubleshooting of Windows bug check codes, follow these suggestions:

-   If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://support.microsoft.com/hub/4338813/windows-help#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).


 

 




