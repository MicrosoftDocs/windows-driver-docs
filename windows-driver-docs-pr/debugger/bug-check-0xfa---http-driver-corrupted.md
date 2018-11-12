---
title: Bug Check 0xFA HTTP_DRIVER_CORRUPTED
description: The HTTP_DRIVER_CORRUPTED bug check has a value of 0x000000FA. This indicates that the HTTP kernel driver (Http.sys) has reached a corrupted state and cannot recover.
ms.assetid: f7e3c1bf-2259-4aa6-af19-267b537dedfe
keywords: ["Bug Check 0xFA HTTP_DRIVER_CORRUPTED", "HTTP_DRIVER_CORRUPTED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- HTTP_DRIVER_CORRUPTED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xFA: HTTP\_DRIVER\_CORRUPTED


The HTTP\_DRIVER\_CORRUPTED bug check has a value of 0x000000FA. This indicates that the HTTP kernel driver (Http.sys) has reached a corrupted state and cannot recover.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## HTTP\_DRIVER\_CORRUPTED Parameters


Parameter 1 identifies the exact state of the HTTP kernel driver.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Name of the file that contains the work item check</p></td>
<td align="left"><p>Line number of the work item check within the file</p></td>
<td align="left"><p>A work item is invalid. This will eventually result in thread pool corruption and an access violation.</p></td>
</tr>
</tbody>
</table>

 

 

 




