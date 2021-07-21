---
title: Bug Check 0xC8 IRQL_UNEXPECTED_VALUE
description: The IRQL_UNEXPECTED_VALUE bug check has a value of 0x000000C8. This indicates that the processor's IRQL is not what it should be at this time.
keywords: ["Bug Check 0xC8 IRQL_UNEXPECTED_VALUE", "IRQL_UNEXPECTED_VALUE"]
ms.date: 12/07/2020
topic_type:
- apiref
api_name:
- IRQL_UNEXPECTED_VALUE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC8: IRQL\_UNEXPECTED\_VALUE

The IRQL\_UNEXPECTED\_VALUE bug check has a value of 0x000000C8. This indicates that the processor's IRQL is not what it should be at this time.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## IRQL\_UNEXPECTED\_VALUE Parameters

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
<td align="left"><p>The value of the following bit computation:</p>
<p>(Current IRQL &lt;&lt; 16) | (Expected IRQL &lt;&lt; 8) | UniqueValue</p></td>
</tr>
<tr class="even">
<td align="left"><p>2 - Depends on UniqueValue</p></td>
<td align="left">
<p>If UniqueValue is 0 or 1: APC->KernelRoutine.</p>
<p>If UniqueValue is 2: the callout routine</p>
<p>If UniqueValue is 3: the interrupt's ServiceRoutine</p>
<p>If UniqueValue is 0xfe: 1 if APCs are disabled</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>3- Depends on UniqueValue </p></td>
<td align="left">
<p>If UniqueValue is 0 or 1: APC</p>
<p>If UniqueValue is 2: the callout's parameter</p>
<p>If UniqueValue is 3: KINTERRUPT</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>4 - Depends on UniqueValue</p></td>
<td align="left">
<p>If UniqueValue is 0 or 1: APC->NormalRoutine</p>
</td>
</tr>
</tbody>
</table>

## Cause

This error is usually caused by a device driver or another lower-level program that changed the IRQL for some period and did not restore the original IRQL at the end of that period. For example, the routine may have acquired a spin lock and failed to release it.

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

## See also

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)
