---
title: Bug Check 0x35 NO_MORE_IRP_STACK_LOCATIONS
description: The NO_MORE_IRP_STACK_LOCATIONS bug check has a value of 0x00000035. This bug check occurs when the IoCallDriver packet has no more stack locations remaining.
ms.assetid: 1a8d5a1b-70aa-4846-bafe-0fef041570c1
keywords: ["Bug Check 0x35 NO_MORE_IRP_STACK_LOCATIONS", "NO_MORE_IRP_STACK_LOCATIONS"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NO_MORE_IRP_STACK_LOCATIONS
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x35: NO\_MORE\_IRP\_STACK\_LOCATIONS


The NO\_MORE\_IRP\_STACK\_LOCATIONS bug check has a value of 0x00000035. This bug check occurs when the **IoCallDriver** packet has no more stack locations remaining.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NO\_MORE\_IRP\_STACK\_LOCATIONS Parameters


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
<td align="left"><p>Address of the IRP</p></td>
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

A higher-level driver has attempted to call a lower-level driver through the **IoCallDriver** interface, but there are no more stack locations in the packet. This will prevent the lower-level driver from accessing its parameters.

This is a disastrous situation, since the higher level driver is proceeding as if it has filled in the parameters for the lower level driver (as required). But since there is no stack location for the latter driver, the former has actually written off the end of the packet. This means that some other memory has been corrupted as well.

 

 




