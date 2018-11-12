---
title: Bug Check 0xBA SESSION_HAS_VALID_VIEWS_ON_EXIT
description: The SESSION_HAS_VALID_VIEWS_ON_EXIT bug check has a value of 0x000000BA. This indicates that a session driver still had mapped views when the session unloaded.
ms.assetid: e0ef7d0e-8a3e-41ca-b0c1-c0f0bb298ef1
keywords: ["Bug Check 0xBA SESSION_HAS_VALID_VIEWS_ON_EXIT", "SESSION_HAS_VALID_VIEWS_ON_EXIT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SESSION_HAS_VALID_VIEWS_ON_EXIT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBA: SESSION\_HAS\_VALID\_VIEWS\_ON\_EXIT


The SESSION\_HAS\_VALID\_VIEWS\_ON\_EXIT bug check has a value of 0x000000BA. This indicates that a session driver still had mapped views when the session unloaded.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SESSION\_HAS\_VALID\_VIEWS\_ON\_EXIT Parameters


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
<td align="left"><p>The number of mapped views that are leaking</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of this session&#39;s mapped views table</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The size of this session&#39;s mapped views table</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This error is caused by a session driver not unmapping its mapped views prior to a session unload. This indicates a bug in win32k.sys, atmfd.dll, rdpdd.dll, or a video driver.

 

 




