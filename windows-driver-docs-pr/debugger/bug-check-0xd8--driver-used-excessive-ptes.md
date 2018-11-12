---
title: Bug Check 0xD8 DRIVER_USED_EXCESSIVE_PTES
description: The DRIVER_USED_EXCESSIVE_PTES bug check has a value of 0x000000D8. This indicates that there are no more system page table entries (PTE) remaining.
ms.assetid: a11212eb-8dd7-49f3-9b23-237ed88b9cff
keywords: ["Bug Check 0xD8 DRIVER_USED_EXCESSIVE_PTES", "DRIVER_USED_EXCESSIVE_PTES"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_USED_EXCESSIVE_PTES
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD8: DRIVER\_USED\_EXCESSIVE\_PTES


The DRIVER\_USED\_EXCESSIVE\_PTES bug check has a value of 0x000000D8. This indicates that there are no more system page table entries (PTE) remaining.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_USED\_EXCESSIVE\_PTES Parameters


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
<td align="left"><p>Pointer to the name of the driver that caused the error (Unicode string), or zero</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Number of PTEs used by the driver that caused the error (if Parameter 1 is nonzero)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Total free system PTEs</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Total system PTEs</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

Cause
-----

This is usually caused by a driver not cleaning up its memory use properly. Parameter 1 shows the driver which has consumed the most PTEs. The call stack will reveal which driver actually caused the bug check.

Resolution
----------

Both drivers may need to be fixed. The total number of system PTEs may also need to be increased.

 

 




