---
title: Bug Check 0xC8 IRQL_UNEXPECTED_VALUE
description: The IRQL_UNEXPECTED_VALUE bug check has a value of 0x000000C8. This indicates that the processor's IRQL is not what it should be at this time.
ms.assetid: eff166ab-e245-48ea-ab9e-9bb722814acf
keywords: ["Bug Check 0xC8 IRQL_UNEXPECTED_VALUE", "IRQL_UNEXPECTED_VALUE"]
ms.author: domars
ms.date: 05/23/2017
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

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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
<td align="left"><p>2</p></td>
<td align="left"><p>Zero, or <strong>APC-&gt;KernelRoutine</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Zero, or <strong>APC</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Zero, or <strong>APC-&gt;NormalRoutine</strong></p></td>
</tr>
</tbody>
</table>

 

You can determine "UniqueValue" by computing (Parameter 1 AND 0xFF). If "UniqueValue" is either zero or one, Parameter 2, Parameter 3, and Parameter 4 will equal the indicated APC pointers. Otherwise, these parameters will equal zero.

Cause
-----

This error is usually caused by a device driver or another lower-level program that changed the IRQL for some period and did not restore the original IRQL at the end of that period. For example, the routine may have acquired a spin lock and failed to release it.

 

 




