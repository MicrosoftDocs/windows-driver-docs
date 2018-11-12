---
title: Bug Check 0x93 INVALID_KERNEL_HANDLE
description: The INVALID_KERNEL_HANDLE bug check has a value of 0x00000093. This bug check indicates that an invalid or protected handle was passed to NtClose.
ms.assetid: c8564da7-cdbf-40f5-94f4-b1fac23b8b42
keywords: ["Bug Check 0x93 INVALID_KERNEL_HANDLE", "INVALID_KERNEL_HANDLE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_KERNEL_HANDLE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x93: INVALID\_KERNEL\_HANDLE


The INVALID\_KERNEL\_HANDLE bug check has a value of 0x00000093. This bug check indicates that an invalid or protected handle was passed to **NtClose**.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_KERNEL\_HANDLE Parameters


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
<td align="left"><p>The handle that is passed to <strong>NtClose</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>0:</strong> The caller tried to close a protected handle</p>
<p><strong>1:</strong> The caller tried to close an invalid handle</p></td>
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

The INVALID\_KERNEL\_HANDLE bug check indicates that some kernel code (for example, a server, redirector, or another driver) tried to close an invalid handle or a protected handle.

 

 




