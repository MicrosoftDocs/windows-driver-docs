---
title: Bug Check 0x2A INCONSISTENT_IRP
description: The INCONSISTENT_IRP bug check has a value of 0x0000002A. This indicates that an IRP was found to contain inconsistent information.
keywords: ["Bug Check 0x2A INCONSISTENT_IRP", "INCONSISTENT_IRP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- INCONSISTENT_IRP
api_type:
- NA
---

# Bug Check 0x2A: INCONSISTENT\_IRP


The INCONSISTENT\_IRP bug check has a value of 0x0000002A. This indicates that an IRP was found to contain inconsistent information.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INCONSISTENT\_IRP Parameters


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
<td align="left"><p>The address of the IRP that was found to be inconsistent</p></td>
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

An IRP was discovered to be in an inconsistent state. Usually this means some field of the IRP was inconsistent with the remaining state of the IRP. An example would be an IRP that was being completed, but was still marked as being queued to a driver's device queue.

## Remarks

This bug check code is not currently being used in the system, but exists for debugging purposes.

 

 




