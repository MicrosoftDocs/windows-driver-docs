---
title: Bug Check 0x19B TTM_FATAL_ERROR
description: The TTM_FATAL_ERROR bug check has a value of 0x0000019B. This indicates that the terminal topology manager experienced a fatal error.
ms.assetid: 993A3A57-A303-4FEB-98F4-68802F4151D4
keywords: ["Bug Check 0x19B TTM_FATAL_ERROR", "TTM_FATAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- TTM_FATAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x19B: TTM\_FATAL\_ERROR


The TTM\_FATAL\_ERROR bug check has a value of 0x0000019B. This indicates that the terminal topology manager experienced a fatal error.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TTM\_FATAL\_ERROR Parameters


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
<td align="left"><p>Failure type</p>
<p>0x1 : An terminal object could not be generated.</p>
2 - The NT status code of the failure
3 - Reserved
4 - Reserved</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>

 

 

 




