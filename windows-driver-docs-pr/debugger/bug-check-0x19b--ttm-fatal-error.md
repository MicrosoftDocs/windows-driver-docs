---
title: Bug Check 0x19B TTM_FATAL_ERROR
description: The TTM_FATAL_ERROR bug check has a value of 0x0000019B. This indicates that the terminal topology manager experienced a fatal error.
keywords: ["Bug Check 0x19B TTM_FATAL_ERROR", "TTM_FATAL_ERROR"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- TTM_FATAL_ERROR
api_type:
- NA
---

# Bug Check 0x19B: TTM\_FATAL\_ERROR


The TTM\_FATAL\_ERROR bug check has a value of 0x0000019B. This indicates that the terminal topology manager experienced a fatal error.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

 

 




