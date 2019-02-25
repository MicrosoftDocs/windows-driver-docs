---
title: Which Data Types Need Thunking
description: Which Data Types Need Thunking
ms.assetid: af1d7986-7bf2-4587-b487-91658e7a3b19
keywords: ["thunking WDK", "WOW64 thunking layer WDK", "32-bit I/O support WDK 64-bit , thunking", "data types WDK 64-bit", "pointer precision WDK 64-bit", "fixed-precision data types WDK 64-bit"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Which Data Types Need Thunking





The following table lists common data types that require thunking, along with their thunked equivalents.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Pointer-precision data type (before thunking)</th>
<th>Equivalent 32-bit fixed-precision data type (after thunking)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HANDLE</p></td>
<td><p>VOID * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>INT_PTR</p></td>
<td><p>INT32</p></td>
</tr>
<tr class="odd">
<td><p>LONG_PTR</p></td>
<td><p>LONG32</p></td>
</tr>
<tr class="even">
<td><p>LPARAM</p></td>
<td><p>LONG32</p></td>
</tr>
<tr class="odd">
<td><p>PCHAR</p></td>
<td><p>Char * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PDWORD</p></td>
<td><p>DWORD * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>PHANDLE</p></td>
<td><p>VOID ** POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PULONG</p></td>
<td><p>ULONG * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>PVOID</p></td>
<td><p>VOID * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PWORD</p></td>
<td><p>WORD * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>SIZE_T</p></td>
<td><p>INT32</p></td>
</tr>
<tr class="even">
<td><p>ULONG_PTR</p></td>
<td><p>ULONG32</p></td>
</tr>
<tr class="odd">
<td><p>UNICODE_STRING</p></td>
<td><p>UNICODE_STRING32</p></td>
</tr>
</tbody>
</table>

 

 

 




