---
title: Bug Check 0x75 CANNOT_WRITE_CONFIGURATION
description: The CANNOT_WRITE_CONFIGURATION bug check has a value of 0x00000075. This bug check indicates that the SYSTEM registry hive file cannot be converted to a mapped file.
keywords: ["Bug Check 0x75 CANNOT_WRITE_CONFIGURATION", "CANNOT_WRITE_CONFIGURATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CANNOT_WRITE_CONFIGURATION
api_type:
- NA
---

# Bug Check 0x75: CANNOT\_WRITE\_CONFIGURATION


The CANNOT\_WRITE\_CONFIGURATION bug check has a value of 0x00000075. This bug check indicates that the SYSTEM registry hive file cannot be converted to a mapped file.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

## Cause

The CANNOT\_WRITE\_CONFIGURATION bug check typically occurs if the system is out of pool and the Windows operating system cannot reopen the hive.

This bug check should almost never occur, because the conversion of the hive file occurs early enough during system initialization so that enough pool should be available.

 

 




