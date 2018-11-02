---
title: Bug Check 0x39 SYSTEM_EXIT_OWNED_MUTEX
description: The SYSTEM_EXIT_OWNED_MUTEX bug check has a value of 0x00000039. This indicates that the worker routine returned without releasing the mutex object that it owned.
ms.assetid: 79257486-f65e-4d02-acf0-b7f0607a21cc
keywords: ["Bug Check 0x39 SYSTEM_EXIT_OWNED_MUTEX", "SYSTEM_EXIT_OWNED_MUTEX"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SYSTEM_EXIT_OWNED_MUTEX
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x39: SYSTEM\_EXIT\_OWNED\_MUTEX


The SYSTEM\_EXIT\_OWNED\_MUTEX bug check has a value of 0x00000039. This indicates that the worker routine returned without releasing the mutex object that it owned.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SYSTEM\_EXIT\_OWNED\_MUTEX Parameters


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
<td align="left"><p>The address of the worker routine that caused the error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The parameter passed to the worker routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the work item.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The worker routine returned while it still owned a mutex object. The current worker thread will proceed to run other unrelated work items, and the mutex will never be released.

Resolution
----------

A debugger is required to analyze this problem. To find the driver that caused the error, use the **ln** (List Nearest Symbols) debugger command:

kd&gt; ln address

Where address is the worker routine given in Parameter 1.

 

 




