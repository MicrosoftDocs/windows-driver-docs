---
title: Bug Check 0x1C5 IO_THREADPOOL_DEADLOCK_LIVEDUMP
description: The IO_THREADPOOL_DEADLOCK_LIVEDUMP bug check has a value of 0x000001C5. This indicates a kernel mode threadpool encountered a deadlock situation.
ms.assetid: CBAB931F-E2A9-4843-9565-DC1CA3B557E6
keywords: ["Bug Check 0x1C5 IO_THREADPOOL_DEADLOCK_LIVEDUMP", "IO_THREADPOOL_DEADLOCK_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- IO_THREADPOOL_DEADLOCK_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1C5: IO\_THREADPOOL\_DEADLOCK\_LIVEDUMP


The IO\_THREADPOOL\_DEADLOCK\_LIVEDUMP bug check has a value of 0x000001C5. This indicates a kernel mode threadpool encountered a deadlock situation.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## IO\_THREADPOOL\_DEADLOCK\_LIVEDUMP Parameters


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
<td align="left">1</td>
<td align="left"><p>Pool Number.</p>
<p>0x0 : ExPoolUntrusted</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Pointer to the PEX_WORK_QUEUE</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




