---
title: Bug Check 0x92 UP_DRIVER_ON_MP_SYSTEM
description: The UP_DRIVER_ON_MP_SYSTEM bug check has a value of 0x00000092. This bug check indicates that a uniprocessor-only driver has been loaded on a multiprocessor system.
ms.assetid: 1e26c7b1-bfa5-4a32-a483-5ce8179ac6b7
keywords: ["Bug Check 0x92 UP_DRIVER_ON_MP_SYSTEM", "UP_DRIVER_ON_MP_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- UP_DRIVER_ON_MP_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x92: UP\_DRIVER\_ON\_MP\_SYSTEM


The UP\_DRIVER\_ON\_MP\_SYSTEM bug check has a value of 0x00000092. This bug check indicates that a uniprocessor-only driver has been loaded on a multiprocessor system.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UP\_DRIVER\_ON\_MP\_SYSTEM Parameters


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
<td align="left"><p>The base address of the driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
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

A driver that is compiled to work only on uniprocessor machines has been loaded, but the Microsoft Windows operating system is running on a multiprocessor system with more than one active processor.

 

 




