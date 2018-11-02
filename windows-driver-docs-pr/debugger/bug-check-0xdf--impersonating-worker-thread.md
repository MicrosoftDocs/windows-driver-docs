---
title: Bug Check 0xDF IMPERSONATING_WORKER_THREAD
description: The IMPERSONATING_WORKER_THREAD bug check has a value of 0x000000DF. This indicates that a workitem did not disable impersonation before it completed.
ms.assetid: d8a68b5b-3aa8-4d02-8063-420834a47f1b
keywords: ["Bug Check 0xDF IMPERSONATING_WORKER_THREAD", "IMPERSONATING_WORKER_THREAD"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- IMPERSONATING_WORKER_THREAD
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xDF: IMPERSONATING\_WORKER\_THREAD


The IMPERSONATING\_WORKER\_THREAD bug check has a value of 0x000000DF. This indicates that a workitem did not disable impersonation before it completed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## IMPERSONATING\_WORKER\_THREAD Parameters


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
<td align="left"><p>The worker routine that caused this error</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The parameter passed to this worker routine</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>A pointer to the work item</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

A worker thread was impersonating another process, and failed to disable impersonation before it returned.

 

 




