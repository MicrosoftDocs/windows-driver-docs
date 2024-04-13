---
title: Bug Check 0xEC SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT
description: The SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT bug check has a value of 0x000000EC. This indicates that a session unload occurred while a session driver still held memory.
keywords: ["Bug Check 0xEC SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT", "SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT
api_type:
- NA
---

# Bug Check 0xEC: SESSION\_HAS\_VALID\_SPECIAL\_POOL\_ON\_EXIT


The SESSION\_HAS\_VALID\_SPECIAL\_POOL\_ON\_EXIT bug check has a value of 0x000000EC. This indicates that a session unload occurred while a session driver still held memory.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SESSION\_HAS\_VALID\_SPECIAL\_POOL\_ON\_EXIT Parameters


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
<td align="left"><p>The session ID</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The number of special pool pages that are leaking</p></td>
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

This error is caused by a session driver not freeing its special pool allocations prior to a session unload. This indicates a bug in win32k.sys, atmfd.dll, rdpdd.dll, or a video driver.

 

 




