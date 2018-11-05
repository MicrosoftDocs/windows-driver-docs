---
title: Bug Check 0xBF MUTEX_ALREADY_OWNED
description: The MUTEX_ALREADY_OWNED bug check has a value of 0x000000BF. This indicates that a thread attempted to acquire ownership of a mutex it already owned.
ms.assetid: 0008c6eb-3add-4169-b29a-6fe4d77c5c9e
keywords: ["Bug Check 0xBF MUTEX_ALREADY_OWNED", "MUTEX_ALREADY_OWNED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MUTEX_ALREADY_OWNED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBF: MUTEX\_ALREADY\_OWNED


The MUTEX\_ALREADY\_OWNED bug check has a value of 0x000000BF. This indicates that a thread attempted to acquire ownership of a mutex it already owned.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MUTEX\_ALREADY\_OWNED Parameters


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
<td align="left"><p>The address of the mutex</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The thread that caused the error</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

 

 




