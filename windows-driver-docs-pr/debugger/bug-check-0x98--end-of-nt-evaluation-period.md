---
title: Bug Check 0x98 END_OF_NT_EVALUATION_PERIOD
description: The END_OF_NT_EVALUATION_PERIOD bug check has a value of 0x00000098. This bug check indicates that the trial period for the Microsoft Windows operating system has ended.
keywords: ["Bug Check 0x98 END_OF_NT_EVALUATION_PERIOD", "END_OF_NT_EVALUATION_PERIOD"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- END_OF_NT_EVALUATION_PERIOD
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x98: END\_OF\_NT\_EVALUATION\_PERIOD


The END\_OF\_NT\_EVALUATION\_PERIOD bug check has a value of 0x00000098. This bug check indicates that the trial period for the Microsoft Windows operating system has ended.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## END\_OF\_NT\_EVALUATION\_PERIOD Parameters


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
<td align="left"><p>The low-order 32 bits of the product expiration date</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The high-order 32 bits of the product expiration date</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

Your installation of the Windows operating system is an evaluation unit with an expiration date. The trial period is over.

 

 




