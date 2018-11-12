---
title: Bug Check 0xAB SESSION_HAS_VALID_POOL_ON_EXIT
description: The SESSION_HAS_VALID_POOL_ON_EXIT bug check has a value of 0x000000AB. This bug check indicates that a session unload occurred while a session driver still held memory.
ms.assetid: fe4587cc-2567-4452-a3e7-22a53def76b2
keywords: ["Bug Check 0xAB SESSION_HAS_VALID_POOL_ON_EXIT", "SESSION_HAS_VALID_POOL_ON_EXIT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SESSION_HAS_VALID_POOL_ON_EXIT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xAB: SESSION\_HAS\_VALID\_POOL\_ON\_EXIT


The SESSION\_HAS\_VALID\_POOL\_ON\_EXIT bug check has a value of 0x000000AB. This bug check indicates that a session unload occurred while a session driver still held memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SESSION\_HAS\_VALID\_POOL\_ON\_EXIT Parameters


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
<td align="left"><p>The session ID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The number of paged pool bytes that are leaking.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The number of nonpaged pool bytes that are leaking.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The total number of paged and nonpaged allocations that are leaking. (The number of nonpaged allocations are in the upper half of this word, and paged allocations are in the lower half of this word.)</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The SESSION\_HAS\_VALID\_POOL\_ON\_EXIT bug check occurs because a session driver does not free its pool allocations before a session unload. This bug check can indicate a bug in Win32k.sys, Atmfd.dll, Rdpdd.dll, or a video or other driver.

 

 




