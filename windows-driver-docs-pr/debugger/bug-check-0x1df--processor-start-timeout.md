---
title: Bug Check 0x1DF PROCESSOR_START_TIMEOUT
description: The PROCESSOR_START_TIMEOUT bug check has a value of 0x000001DF. This indicates a processor failed to start in the allowed time.
keywords: ["Bug Check 0x1DF PROCESSOR_START_TIMEOUT", "PROCESSOR_START_TIMEOUT"]
ms.date: 06/16/2023
topic_type:
- apiref
api_name:
- PROCESSOR_START_TIMEOUT
api_type:
- NA
---

# Bug Check 0x1DF: PROCESSOR_START_TIMEOUT

The PROCESSOR_START_TIMEOUT bug check has a value of 0x000001DF. This indicates a processor failed to start in the allowed time. The processor start occurs very early in the operating system initialization.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## PROCESSOR_START_TIMEOUT Parameters

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
<td align="left">1</td>
<td align="left"><p>Virtual address of the processor state.</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved.</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">NT processor number.</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Local unit ID for the processor.</td>
</tr>
</tbody>
</table>

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

## See also

[Bug Check Code Reference](bug-check-code-reference2.md)
