---
title: Bug Check 0xCE DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS
description: The DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS bug check has a value of 0x000000CE. This indicates that a driver failed to cancel pending operations before unloading.
keywords: ["Bug Check 0xCE DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS", "DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS
api_type:
- NA
---

# Bug Check 0xCE: DRIVER\_UNLOADED\_WITHOUT\_CANCELLING\_PENDING\_OPERATIONS


The DRIVER\_UNLOADED\_WITHOUT\_CANCELLING\_PENDING\_OPERATIONS bug check has a value of 0x000000CE. This indicates that a driver failed to cancel pending operations before unloading.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_UNLOADED\_WITHOUT\_CANCELLING\_PENDING\_OPERATIONS Parameters


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
<td align="left"><p>Memory address referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address that referenced memory (if known)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

## Cause

This driver failed to cancel lookaside lists, DPCs, worker threads, or other such items before unload.

 
## Resolution

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 




