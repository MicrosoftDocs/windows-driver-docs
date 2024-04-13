---
title: Bug Check 0x67 CONFIG_INITIALIZATION_FAILED
description: The CONFIG_INITIALIZATION_FAILED bug check has a value of 0x00000067. This bug check indicates that the registry configuration failed.
keywords: ["Bug Check 0x67 CONFIG_INITIALIZATION_FAILED", "CONFIG_INITIALIZATION_FAILED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CONFIG_INITIALIZATION_FAILED
api_type:
- NA
---

# Bug Check 0x67: CONFIG\_INITIALIZATION\_FAILED


The CONFIG\_INITIALIZATION\_FAILED bug check has a value of 0x00000067. This bug check indicates that the registry configuration failed.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CONFIG\_INITIALIZATION\_FAILED Parameters


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
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The location selector</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The NT status code</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

The registry could not allocate the pool that it needed to contain the registry files. This situation should never occur, because the register allocates this pool early enough in system initialization so that plenty of paged pool should be available.

 

 




