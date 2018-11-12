---
title: Bug Check 0xC6 DRIVER_CAUGHT_MODIFYING_FREED_POOL
description: The DRIVER_CAUGHT_MODIFYING_FREED_POOL bug check has a value of 0x000000C6. This indicates that the driver attempted to access a freed memory pool.
ms.assetid: a5df3612-549d-4cf1-b3e1-4e5efad8ce88
keywords: ["Bug Check 0xC6 DRIVER_CAUGHT_MODIFYING_FREED_POOL", "DRIVER_CAUGHT_MODIFYING_FREED_POOL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_CAUGHT_MODIFYING_FREED_POOL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC6: DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL


The DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL bug check has a value of 0x000000C6. This indicates that the driver attempted to access a freed memory pool.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL Parameters


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
<td align="left"><p>Memory referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Kernel mode</p>
<p><strong>1:</strong> User mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The faulty component will be displayed in the current kernel stack. This driver should be either replaced or debugged.

 

 




