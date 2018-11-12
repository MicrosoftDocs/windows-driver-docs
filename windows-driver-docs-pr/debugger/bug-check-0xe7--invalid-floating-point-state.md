---
title: Bug Check 0xE7 INVALID_FLOATING_POINT_STATE
description: The INVALID_FLOATING_POINT_STATE bug check has a value of 0x000000E7. This indicates that a thread's saved floating-point state is invalid.
ms.assetid: 71a61132-cb7f-4618-b3d5-95602e52c098
keywords: ["Bug Check 0xE7 INVALID_FLOATING_POINT_STATE", "INVALID_FLOATING_POINT_STATE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_FLOATING_POINT_STATE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE7: INVALID\_FLOATING\_POINT\_STATE


The INVALID\_FLOATING\_POINT\_STATE bug check has a value of 0x000000E7. This indicates that a thread's saved floating-point state is invalid.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_FLOATING\_POINT\_STATE Parameters


Parameter 1 indicates which validity check failed. Parameter 4 is not used. The meaning of the other parameters depends on the value of Parameter 1.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>The flags field</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The saved context flags field is invalid. Either FLOAT_SAVE_VALID is not set, or some reserved bits are nonzero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The saved IRQL</p></td>
<td align="left"><p>The current IRQL</p></td>
<td align="left"><p>The current processor&#39;s IRQL is not the same as when the floating-point context was saved.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The saved address of the thread that owns this floating-point context</p></td>
<td align="left"><p>The current thread</p></td>
<td align="left"><p>The saved context does not belong to the current thread.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

While restoring the previously-saved floating-point state for a thread, the state was found to be invalid.

Parameter 1 indicates which validity check failed.

 

 




