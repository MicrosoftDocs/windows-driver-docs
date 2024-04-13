---
title: Bug Check 0x7E SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
description: The SYSTEM_THREAD_EXCEPTION_NOT_HANDLED bug check indicates that a system thread generated an exception that the error handler didn't catch.
keywords: ["Bug Check 0x7E SYSTEM_THREAD_EXCEPTION_NOT_HANDLED", "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED"]
ms.date: 12/08/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
api_type:
- NA
---

# Bug Check 0x7E: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED

The SYSTEM_THREAD_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000007E. This bug check indicates that a system thread generated an exception that the error handler didn't catch.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## SYSTEM_THREAD_EXCEPTION_NOT_HANDLED parameters

| Parameter | Description |
|---|---|
| 1 | The exception code that wasn't handled. |
| 2 | The address where the exception occurred. |
| 3 | The address of the exception record. |
| 4 | The address of the context record. |

## Cause

This bug check indicates that a system thread generated an exception that the error handler didn't catch. To interpret it, you must identify which exception was generated.

Common exception codes include the following:

- 0x80000002: STATUS_DATATYPE_MISALIGNMENT indicates an unaligned data reference was encountered.

- 0x80000003: STATUS_BREAKPOINT indicates a breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

- 0xC0000005: STATUS_ACCESS_VIOLATION indicates a memory access violation occurred.

For a complete list of exception codes, see [NTSTATUS values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55). The exception codes are defined in *ntstatus.h*, a header file provided by the [Windows Driver Kit](../index.yml). For more information, see [Header files in the Windows Driver Kit](../gettingstarted/header-files-in-the-windows-driver-kit.md).

## Resolution

If you plan to debug this problem, the exception address (parameter 2) should identify the driver or function that caused this problem.

If a driver is listed by name within the bug check message, disable or remove that driver. If the issue is narrowed down to a single driver, set breakpoints and single-step forward in code to locate the failure and gain insight into events leading up to the crash.

The [!analyze](../debuggercmds/-analyze.md) debugger extension displays information about the bug check and can be helpful in determining the root cause.

More analysis can be done by using the [!thread](../debuggercmds/-thread.md) extension, and the [dds, dps, and dqs (display words and symbols)](../debuggercmds/dds--dps--dqs--display-words-and-symbols-.md) commands. This technique is reasonable when WinDbg reports "Probably caused by : ntkrnlmp.exe."

If exception code 0x80000003 occurs, a hard-coded breakpoint or assertion was hit, but the system was started with the **/NODEBUG** switch. This problem shouldn't occur frequently. If it occurs repeatedly, make sure that a kernel debugger is connected and the system is started with the **/DEBUG** switch.

If exception code 0x80000002 occurs, the trap frame supplies additional information.

For more information about WinDbg and **!analyze**, see:

- [Analyze crash dump files by using WinDbg](crash-dump-files.md)

- [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)

## Remarks

If you're not equipped to use the Windows debugger to work on this problem, you should use some basic troubleshooting techniques:

- Check the System Log in Event Viewer for more error messages that might help identify the device or driver that is causing bug check 0x7E.

- If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

- Check with your hardware vendor for any ACPI or other firmware updates. Hardware issues, such as system incompatibilities, memory conflicts, and IRQ conflicts can also generate this error.

- Disable memory caching/shadowing of the BIOS to try to resolve the error. You can also run hardware diagnostics that the system manufacturer supplies.

- Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

For more general troubleshooting information, see [Blue screen data](blue-screen-data.md).
