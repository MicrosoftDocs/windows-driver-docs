---
title: Bug Check 0x1 APC_INDEX_MISMATCH
description: Learn about bug check 0x00000001, which indicates a mismatch in the APC state index.
keywords: ["Bug check 0x1 APC_INDEX_MISMATCH", "APC_INDEX_MISMATCH"]
ms.date: 10/02/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- APC_INDEX_MISMATCH
api_type:
- NA
---

# Bug Check 0x1: APC_INDEX_MISMATCH

The APC_INDEX_MISMATCH bug check has a value of 0x00000001. The bug check indicates a mismatch in the asynchronous procedure calls (APC) state index.

> [!IMPORTANT]
> This article is for programmers. If you're a Microsoft customer and your computer displays a blue screen error code, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## APC_INDEX_MISMATCH parameters

| Parameter | Description |
| --- | --- |
| 1 | The address of the system function (system call) or worker routine. |
| 2 | The value of the current thread's **ApcStateIndex** field. |
| 3 | The value of current thread's **CombinedApcDisable** field. This field consists of two separate 16-bit fields: (*Thread* >**SpecialApcDisable** < <  16) \| *Thread* >**KernelApcDisable**. |
| 4 | Call type:<br />0 - System call<br />1 - Worker routine |

## Cause

The most common cause of this bug check is when a file system or driver has a mismatched sequence of calls to disable and re-enable APCs. The key data item is the *Thread* >**CombinedApcDisable** field. The **CombinedApcDisable** field consists of two separate 16-bit fields: **SpecialApcDisable** and **KernelApcDisable**. A negative value of either field indicates that a driver has disabled special or normal APCs (respectively) without re-enabling them. A positive value indicates that a driver has enabled special or normal APCs too many times.

## Resolution

You can resolve this problem by using WinDbg or by using basic troubleshooting techniques.

### Debug by using WinDbg

The [!analyze](../debuggercmds/-analyze.md) debugger extension displays information about the bug check and can help you determine the root cause.

You can use the [!apc](../debuggercmds/-apc.md) extension to display the contents of one or more APCs.

You also can set a breakpoint in the code that precedes this stop code and attempt to single-step forward into the faulting code.

For more information about using WinDbg, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

### Debug without using WinDbg

If you aren't equipped to use the Windows debugger to work on this problem:

- In Event Viewer, check System Log for more error messages that might help you identify the device or driver that's causing this bug check.

- If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

- Confirm that any new hardware that's installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

For more general troubleshooting information, see [Blue screen data](blue-screen-data.md).

## Remarks

This bug check is the result of an internal error in the kernel. This error occurs on exit from a system call. A possible cause for this bug check is a file system or driver that has a mismatched sequence of system calls to enter or leave guarded or critical regions. For example, each call to [KeEnterCriticalRegion](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) must have a matching call to [KeLeaveCriticalRegion](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion).

If you're developing a driver, you can use [Static Driver Verifier](../devtest/static-driver-verifier.md), a static analysis tool available in Windows Driver Kit, to detect problems in your code before you ship your driver. Run Static Driver Verifier with the [CriticalRegions](../devtest/wdm-criticalregions.md) rule to verify that your source code uses these system calls in correct sequence.

## See also

[Bug check code reference](bug-check-code-reference2.md)
