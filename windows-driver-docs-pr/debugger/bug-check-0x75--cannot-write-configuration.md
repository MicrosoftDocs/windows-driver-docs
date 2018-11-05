---
title: Bug Check 0x75 CANNOT_WRITE_CONFIGURATION
description: The CANNOT_WRITE_CONFIGURATION bug check has a value of 0x00000075. This bug check indicates that the SYSTEM registry hive file cannot be converted to a mapped file.
ms.assetid: 0190de02-8bd1-4c20-839d-bf9fb517567d
keywords: ["Bug Check 0x75 CANNOT_WRITE_CONFIGURATION", "CANNOT_WRITE_CONFIGURATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CANNOT_WRITE_CONFIGURATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x75: CANNOT\_WRITE\_CONFIGURATION


The CANNOT\_WRITE\_CONFIGURATION bug check has a value of 0x00000075. This bug check indicates that the SYSTEM registry hive file cannot be converted to a mapped file.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CANNOT\_WRITE\_CONFIGURATION Parameters


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
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The NT status code that led the Windows operating system to assume that it had failed to convert the hive</p></td>
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

 

Cause
-----

The CANNOT\_WRITE\_CONFIGURATION bug check typically occurs if the system is out of pool and the Windows operating system cannot reopen the hive.

This bug check should almost never occur, because the conversion of the hive file occurs early enough during system initialization so that enough pool should be available.

 

 




