---
title: Bug Check 0x1 APC_INDEX_MISMATCH
description: 0x00000001.
keywords: ["Bug Check 0x1 APC_INDEX_MISMATCH", "APC_INDEX_MISMATCH"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- APC_INDEX_MISMATCH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1: APC\_INDEX\_MISMATCH

The APC\_INDEX\_MISMATCH bug check has a value of 0x00000001. This indicates that there has been a mismatch in the asynchronous procedure calls (APC) state index.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).


## APC\_INDEX\_MISMATCH parameters

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
<td align="left"><p>The address of the system function (system call) or worker routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left">The value of the current thread's <strong>ApcStateIndex</strong> field.</td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The value of current thread's <strong>CombinedApcDisable</strong> field. This field consists of two separate 16-bit fields: (<em>Thread</em> &gt;<strong>SpecialApcDisable</strong> &lt;&lt; 16) | <em>Thread</em> &gt;<strong>KernelApcDisable</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Call type:</p><ul><li>0 - System call</li><li>1 - Worker routine</li></ul></p></td>
</tr>
</tbody>
</table>

 
## Cause

The most common cause of this bug check is when a file system or driver has a mismatched sequence of calls to disable and re-enable APCs. The key data item is the *Thread* &gt;**CombinedApcDisable** field. The **CombinedApcDisable** field consists of two separate 16-bit fields: **SpecialApcDisable** and **KernelApcDisable**. A negative value of either field indicates that a driver has disabled special or normal APCs (respectively) without re-enabling them. A positive value indicates that a driver has enabled special or normal APCs too many times.


## Resolution

### Debugging with WinDbg

The [**!analyze**](-analyze.md) debugger extension displays information about the bug check and can be helpful in determining the root cause.

You can use the [**!apc**](-apc.md) extension to display the contents of one or more asynchronous procedure calls (APCs).

You can also set a breakpoint in the code that precedes this stop code and attempt to single-step forward into the faulting code.

For more information about using WinDbg, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).


### Debugging without WinDbg

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

For additional general troubleshooting information, see [Blue screen data](blue-screen-data.md).


## Remarks

This bug check is the result of an internal error in the kernel. This error occurs on exit from a system call. A possible cause for this bug check is a file system or driver that has a mismatched sequence of system calls to enter or leave guarded or critical regions. For example, each call to [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) must have a matching call to [**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion). 

If you are developing a driver, you can use [Static Driver Verifier](../devtest/static-driver-verifier.md), a static analysis tool available in the Windows Driver Kit, to detect problems in your code before you ship your driver. Run Static Driver Verifier with the [CriticalRegions](../devtest/wdm-criticalregions.md) rule to verify that your source code uses these system calls in correct sequence.
