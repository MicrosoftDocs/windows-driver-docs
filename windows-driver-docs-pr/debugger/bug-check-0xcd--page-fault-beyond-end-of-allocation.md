---
title: Bug Check 0xCD PAGE_FAULT_BEYOND_END_OF_ALLOCATION
description: The PAGE_FAULT_BEYOND_END_OF_ALLOCATION bug check has a value of 0x000000CD. This indicates that the system accessed memory beyond the end of some driver's pool allocation.
keywords: ["Bug Check 0xCD PAGE_FAULT_BEYOND_END_OF_ALLOCATION", "PAGE_FAULT_BEYOND_END_OF_ALLOCATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- PAGE_FAULT_BEYOND_END_OF_ALLOCATION
api_type:
- NA
---

# Bug Check 0xCD: PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION


The PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION bug check has a value of 0x000000CD. This indicates that the system accessed memory beyond the end of some driver's pool allocation.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION Parameters


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

The driver allocated *n* bytes of memory from the special pool. Subsequently, the system referenced more than *n* bytes from this pool. This usually indicates a system-driver synchronization problem.

For information about the special pool, consult the Driver Verifier section of the Windows Driver Kit.

## Remarks

This cannot be protected by a **try - except** handler -- it can only be protected by a probe.

 

 




