---
title: Bug Check 0x13B PASSIVE_INTERRUPT_ERROR
description: The PASSIVE_INTERRUPT_ERROR bug check has a value of 0x0000013B. This indicates that the kernel has detected issues with the passive-level interrupt.
ms.assetid: 6C921FCB-B945-4909-BAD3-1DBD6E3CAA54
keywords: ["Bug Check 0x13B PASSIVE_INTERRUPT_ERROR", "PASSIVE_INTERRUPT_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PASSIVE_INTERRUPT_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x13B: PASSIVE\_INTERRUPT\_ERROR


The PASSIVE\_INTERRUPT\_ERROR bug check has a value of 0x0000013B. This indicates that the kernel has detected issues with the passive-level interrupt.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PASSIVE\_INTERRUPT\_ERROR Parameters


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
<td align="left"><p>Type of error detected</p>
0x1 : A driver tried to acquire an interrupt spinlock but passed in a passive-level interrupt object.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Address of the KINTERRUPT object for the passive-level interrupt.</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




