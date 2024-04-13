---
title: Bug Check 0x1E9 ILLEGAL_ATS_INITIALIZATION
description: The ILLEGAL_ATS_INITIALIZATION bug check has a value of 0x000001E9. This indicates that the driver has attempted to illegally enable the Address Translation Service (ATS) on a device which has been already been enabled for Shared Virtual Memory (SVM).
keywords: ["Bug Check 0x1E9 ILLEGAL_ATS_INITIALIZATION", "ILLEGAL_ATS_INITIALIZATION"]
ms.date: 08/03/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- ILLEGAL_ATS_INITIALIZATION
api_type:
- NA
---

# Bug Check 0x1E9: ILLEGAL\_ATS\_INITIALIZATION

The ILLEGAL\_ATS\_INITIALIZATION bug check has a value of 0x000001E9. This indicates that the driver has attempted to illegally enable the Address Translation Service (ATS) on a device which has been already been enabled for Shared Virtual Memory (SVM).


> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## ILLEGAL\_ATS\_INITIALIZATION Parameters


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
<td align="left">The physical device object.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved</td>
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


## Resolution

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bugcheck and can be helpful in determining the root cause.
