---
title: Bug Check 0x48 CANCEL_STATE_IN_COMPLETED_IRP
description: The CANCEL_STATE_IN_COMPLETED_IRP bug check has a value of 0x00000048. This indicates that an I/O request packet (IRP) was completed, and then was subsequently canceled.
keywords: ["Bug Check 0x48 CANCEL_STATE_IN_COMPLETED_IRP", "CANCEL_STATE_IN_COMPLETED_IRP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CANCEL_STATE_IN_COMPLETED_IRP
api_type:
- NA
---

# Bug Check 0x48: CANCEL\_STATE\_IN\_COMPLETED\_IRP


The CANCEL\_STATE\_IN\_COMPLETED\_IRP bug check has a value of 0x00000048. This indicates that an I/O request packet (IRP) was completed, and then was subsequently canceled.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CANCEL\_STATE\_IN\_COMPLETED\_IRP Parameters


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
<td align="left"><p>A pointer to the IRP</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The cancel routine set by the driver</p></td>
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

An IRP that had a *Cancel* routine set was completed normally, without cancellation. But after it was complete, a driver called the IRP's *Cancel* routine.

This could be caused by a driver that completed the IRP and then attempted to cancel it.

It could also be caused by two drivers each trying to access the same IRP in an improper way.

## Resolution

The cancel routine parameter can be used to determine which driver or stack caused the bug check.

 

 




