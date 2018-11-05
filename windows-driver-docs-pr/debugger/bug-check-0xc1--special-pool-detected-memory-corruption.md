---
title: Bug Check 0xC1 SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION
description: The SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION bug check has a value of 0x000000C1. This indicates that the driver wrote to an invalid section of the special pool.
ms.assetid: 4d5a3d95-de39-4e15-aba8-33257a6f0677
keywords: ["Bug Check 0xC1 SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION", "SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC1: SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION


The SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION bug check has a value of 0x000000C1. This indicates that the driver wrote to an invalid section of the special pool.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION Parameters


Parameter 4 indicates the type of violation.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0x20</p></td>
<td align="left"><p>A driver attempted to free pool which was not allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>Bytes requested</p></td>
<td align="left"><p>Bytes calculated (actually given to the caller)</p></td>
<td align="left"><p>0x21,</p>
<p>0x22</p></td>
<td align="left"><p>A driver attempted to free a bad address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>Address where bits are corrupted</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0x23</p></td>
<td align="left"><p>A driver freed an address, but nearby bytes within the same page have been corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>Address where bits are corrupted</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0x24</p></td>
<td align="left"><p>A driver freed an address, but bytes occurring after the end of the allocation have been overwritten.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Number of bytes</p></td>
<td align="left"><p>0x30</p></td>
<td align="left"><p>A driver attempted to allocate pool at an incorrect IRQL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>0x31</p></td>
<td align="left"><p>A driver attempted to free pool at an incorrect IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address that the driver tried to free</p></td>
<td align="left"><p>Address where one bit is corrupted</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0x32</p></td>
<td align="left"><p>A driver freed an address, but nearby bytes within the same page have a single bit error.</p></td>
</tr>
</tbody>
</table>

 

The \_POOL\_TYPE codes are enumerated in ntddk.h. In particular, zero indicates nonpaged pool and one indicates paged pool.

Cause
-----

A driver has written to an invalid section of the special pool.

Resolution
----------

Obtain a backtrace of the current thread. This backtrace will usually reveal the source of the error.

For information about the special pool, consult the Driver Verifier section of the Windows Driver Kit.

 

 




