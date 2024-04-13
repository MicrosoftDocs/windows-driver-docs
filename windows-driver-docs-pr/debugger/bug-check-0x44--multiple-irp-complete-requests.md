---
title: Bug Check 0x44 MULTIPLE_IRP_COMPLETE_REQUESTS
description: The MULTIPLE_IRP_COMPLETE_REQUESTS bug check has a value of 0x00000044. This indicates that a driver has tried to request an IRP be completed that is already complete.
keywords: ["Bug Check 0x44 MULTIPLE_IRP_COMPLETE_REQUESTS", "MULTIPLE_IRP_COMPLETE_REQUESTS"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- MULTIPLE_IRP_COMPLETE_REQUESTS
api_type:
- NA
---

# Bug Check 0x44: MULTIPLE\_IRP\_COMPLETE\_REQUESTS


The MULTIPLE\_IRP\_COMPLETE\_REQUESTS bug check has a value of 0x00000044. This indicates that a driver has tried to request an IRP be completed that is already complete.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## MULTIPLE\_IRP\_COMPLETE\_REQUESTS Parameters


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
<td align="left"><p>The address of the IRP</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
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

A driver has called **IoCompleteRequest** to ask that an IRP be completed, but the packet has already been completed.

## Resolution

This is a tough bug to find because the simplest case -- a driver that attempted to complete its own packet twice -- is usually not the source of the problem. More likely, two separate drivers each believe that they own the packet, and each has attempted to complete it. The first request succeeds, and the second fails, resulting in this bug check.

Tracking down which drivers in the system caused the error is difficult, because the trail of the first driver has been covered by the second. However, the driver stack for the current request can be found by examining the device object fields in each of the stack locations.

 

 




