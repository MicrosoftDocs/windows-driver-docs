---
title: Bug Check 0x11C ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE
description: The ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE bug check has a value of 0x0000011C that indicates that a write was attempted to the protected storage of the configuration manager.
ms.assetid: 5a322457-51d7-4832-8eeb-1fdc99f313e8
keywords: ["Bug Check 0x11C ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE", "ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x11C: ATTEMPTED\_WRITE\_TO\_CM\_PROTECTED\_STORAGE


The ATTEMPTED\_WRITE\_TO\_CM\_PROTECTED\_STORAGE bug check has a value of 0x0000011C. This bug check indicates that an attempt was made to write to the read-only protected storage of the configuration manager.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ATTEMPTED\_WRITE\_TO\_CM\_PROTECTED\_STORAGE Parameters


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
<td align="left"><p>Virtual address for the attempted write</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>PTE contents</p></td>
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

 

Remarks
-------

When it is possible, the name of the driver that is attempting the write operation is printed as a Unicode string on the bug check screen and then saved in KiBugCheckDriver.

 

 




