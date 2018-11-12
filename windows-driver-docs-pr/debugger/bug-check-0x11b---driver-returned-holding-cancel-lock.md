---
title: Bug Check 0x11B DRIVER_RETURNED_HOLDING_CANCEL_LOCK
description: The DRIVER_RETURNED_HOLDING_CANCEL_LOCK bug check has a value of 0x0000011B.
ms.assetid: 8728dc74-cf21-490f-b3b0-1513d2310461
keywords: ["Bug Check 0x11B DRIVER_RETURNED_HOLDING_CANCEL_LOCK", "DRIVER_RETURNED_HOLDING_CANCEL_LOCK"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_RETURNED_HOLDING_CANCEL_LOCK
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x11B: DRIVER\_RETURNED\_HOLDING\_CANCEL\_LOCK


The DRIVER\_RETURNED\_HOLDING\_CANCEL\_LOCK bug check has a value of 0x0000011B. This bug check indicates that a driver has returned from a *cancel* routine that holds the global cancel lock. This causes all later cancellation calls to fail, and results in either a deadlock or another bug check.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_RETURNED\_HOLDING\_CANCEL\_LOCK Parameters


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
<td align="left"><p>The address of the IRP that was canceled (might not be valid).</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the <em>cancel</em> routine.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The cancel spin lock should have been released by the *cancel* routine.

The driver calls the IoCancelIrpIoCancelIrp function to cancel an individual I/O request packet (IRP). This function acquires the cancel spin lock, sets the cancel flag in the IRP, and then calls the *cancel* routine specified by the appropriate field in the IRP, if a routine was specified. The *cancel* routine is expected to release the cancel spin lock. If there is no *cancel* routine, the cancel spin lock is released.

 

 




