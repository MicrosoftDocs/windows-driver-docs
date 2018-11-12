---
title: Bug Check 0x20 KERNEL_APC_PENDING_DURING_EXIT
description: The KERNEL_APC_PENDING_DURING_EXIT bug check has a value of 0x00000020. This indicates that an asynchronous procedure call (APC) was still pending when a thread exited.
ms.assetid: 0ef7c2b2-0864-4206-b786-bac9df9cedc7
keywords: ["Bug Check 0x20 KERNEL_APC_PENDING_DURING_EXIT", "KERNEL_APC_PENDING_DURING_EXIT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_APC_PENDING_DURING_EXIT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x20: KERNEL\_APC\_PENDING\_DURING\_EXIT


The KERNEL\_APC\_PENDING\_DURING\_EXIT bug check has a value of 0x00000020. This indicates that an asynchronous procedure call (APC) was still pending when a thread exited.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_APC\_PENDING\_DURING\_EXIT Parameters


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
<td align="left"><p>The address of the APC found pending during exit</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The thread&#39;s APC disable count</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The current IRQL</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The key data item is the APC disable count (Parameter 2) for the thread. If the count is nonzero, it will indicate the source of the problem.

The APC disable count is decremented each time a driver calls **KeEnterCriticalRegion**, **FsRtlEnterFileSystem**, or acquires a mutex.

The APC disable count is incremented each time a driver calls **KeLeaveCriticalRegion**, **KeReleaseMutex**, or **FsRtlExitFileSystem**.

Because these calls should always be in pairs, the APC disable count should be zero when a thread exits. A negative value indicates that a driver has disabled APC calls without re-enabling them. A positive value indicates that the reverse is true.

If you ever see this error, be very suspicious of all drivers installed on the machine -- especially unusual or non-standard drivers.

This current IRQL (Parameter 3) should be zero. If it is not, the driver's cancellation routine may have caused this bug check by returning at an elevated IRQL. In this case, carefully note what was running (and what was closing) at the time of the crash, and note all of the installed drivers at the time of the crash. The cause in this case is usually a severe bug in a driver.

 

 




