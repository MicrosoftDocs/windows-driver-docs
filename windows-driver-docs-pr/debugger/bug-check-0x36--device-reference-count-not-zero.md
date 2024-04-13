---
title: Bug Check 0x36 DEVICE_REFERENCE_COUNT_NOT_ZERO
description: The DEVICE_REFERENCE_COUNT_NOT_ZERO bug check has a value of 0x00000036. This indicates that a driver attempted to delete a device object that still had a positive reference count.
keywords: ["Bug Check 0x36 DEVICE_REFERENCE_COUNT_NOT_ZERO", "DEVICE_REFERENCE_COUNT_NOT_ZERO"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DEVICE_REFERENCE_COUNT_NOT_ZERO
api_type:
- NA
---

# Bug Check 0x36: DEVICE\_REFERENCE\_COUNT\_NOT\_ZERO


The DEVICE\_REFERENCE\_COUNT\_NOT\_ZERO bug check has a value of 0x00000036. This indicates that a driver attempted to delete a device object that still had a positive reference count.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DEVICE\_REFERENCE\_COUNT\_NOT\_ZERO Parameters


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
<td align="left"><p>The address of the device object</p></td>
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

A device driver has attempted to delete one of its device objects from the system, but the reference count for that object was non-zero.

This means there are still outstanding references to the device. (The reference count indicates the number of reasons why this device object cannot be deleted.)

This is a bug in the calling device driver.

 

 




