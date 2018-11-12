---
title: Bug Check 0xC5 DRIVER_CORRUPTED_EXPOOL
description: The DRIVER_CORRUPTED_EXPOOL bug check has a value of 0x000000C5. This indicates that the system attempted to access invalid memory at a process IRQL that was too high.
ms.assetid: e375e7d3-9cb1-474f-ade2-1bc65dd79864
keywords: ["Bug Check 0xC5 DRIVER_CORRUPTED_EXPOOL", "DRIVER_CORRUPTED_EXPOOL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_CORRUPTED_EXPOOL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC5: DRIVER\_CORRUPTED\_EXPOOL


The DRIVER\_CORRUPTED\_EXPOOL bug check has a value of 0x000000C5. This indicates that the system attempted to access invalid memory at a process IRQL that was too high.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_CORRUPTED\_EXPOOL Parameters


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
<td align="left"><p>Memory referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of reference</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address that referenced memory</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The kernel attempted to access pageable memory (or perhaps completely invalid memory) when the IRQL was too high. The ultimate cause of this problem is almost certainly a driver that has corrupted the system pool.

In most cases, this bug check results if a driver corrupts a small allocation (less than PAGE\_SIZE). Larger allocations result in [**bug check 0xD0**](bug-check-0xd0--driver-corrupted-mmpool.md) (DRIVER\_CORRUPTED\_MMPOOL).

Resolution
----------

If you have recently installed any new software, check to see if it is properly installed. Check for updated drivers on the manufacturer's website.

To debug this error, use the special pool option of Driver Verifier. If this fails to reveal the driver that caused the error, use the Global Flags utility to enable the special pool by pool tag.

For information about the special pool, consult the Driver Verifier section of the Windows Driver Kit.

 

 




