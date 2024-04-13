---
title: Bug Check 0xE1 WORKER_THREAD_RETURNED_AT_BAD_IRQL
description: The WORKER_THREAD_RETURNED_AT_BAD_IRQL bug check has a value of 0x000000E1. This indicates that a worker thread completed and returned with IRQL DISPATCH_LEVEL.
keywords: ["Bug Check 0xE1 WORKER_THREAD_RETURNED_AT_BAD_IRQL", "WORKER_THREAD_RETURNED_AT_BAD_IRQL"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- WORKER_THREAD_RETURNED_AT_BAD_IRQL
api_type:
- NA
---

# Bug Check 0xE1: WORKER\_THREAD\_RETURNED\_AT\_BAD\_IRQL


The WORKER\_THREAD\_RETURNED\_AT\_BAD\_IRQL bug check has a value of 0x000000E1. This indicates that a worker thread completed and returned with IRQL &gt;= DISPATCH\_LEVEL.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## WORKER\_THREAD\_RETURNED\_AT\_BAD\_IRQL Parameters


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
<td align="left"><p>Address of the worker routine</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL that the worker thread returned at</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Work item parameter</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Work item address</p></td>
</tr>
</tbody>
</table>

 

## Cause

A worker thread completed and returned with IRQL &gt;= DISPATCH\_LEVEL.

## Resolution

To find the driver that caused the error, use the [**ln (List Nearest Symbols)**](../debuggercmds/ln--list-nearest-symbols-.md) debugger command:

```dbgcmd
kd> ln address
```

where *address* is the worker routine address given in Parameter 1.

 

 




