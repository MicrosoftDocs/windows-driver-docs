---
title: Bug Check 0xBD INVALID_HIBERNATED_STATE
description: The INVALID_HIBERNATED_STATE bug check has a value of 0x000000BD.
keywords: ["Bug Check 0xBD INVALID_HIBERNATED_STATE", "INVALID_HIBERNATED_STATE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- INVALID_HIBERNATED_STATE
api_type:
- NA
---

# Bug Check 0xBD: INVALID\_HIBERNATED\_STATE


The INVALID\_HIBERNATED\_STATE bug check has a value of 0x000000BD. This indicates that the hibernated memory image does not match the current hardware configuration. This bugcheck occurs when a system resumes from hibernate and discovers that the hardware has been changed while the system was hibernated.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INVALID\_HIBERNATED\_STATE Parameters


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
<td align="left"><p>Hardware that was invalid.</p>
<p>1 : Number of installed processors is less than before the hibernation</p>
<p>Value in Param 2: Number of processors before hibernation</p>
<p>Value in Param 3: Number of processors after hibernation</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Per Parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Per Parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




