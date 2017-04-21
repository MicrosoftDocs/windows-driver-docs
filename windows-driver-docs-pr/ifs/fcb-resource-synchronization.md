---
title: FCB Resource Synchronization
author: windows-driver-content
description: FCB Resource Synchronization
ms.assetid: 8355907e-e313-4e54-a63f-a82d9ce0d31b
keywords:
- RDBSS WDK file systems , FCB resource synchronization
- Redirected Drive Buffering Subsystem WDK file systems , FCB resource synchronization
- FCB resource synchronization WDK RDBSS
- paging I/O WDK RDBSS
- synchronization WDK RDBSS
- file control block structure WDK RDBSS
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FCB Resource Synchronization


## <span id="ddk_fcb_resource_synchronization_if"></span><span id="DDK_FCB_RESOURCE_SYNCHRONIZATION_IF"></span>


The synchronization resources of interest to mini-redirector drivers are primarily associated with the FCB. There is a paging I/O resource and a regular resource. The paging I/O resource is managed internally by RDBSS. The only resource accessible to mini-redirector drivers is the regular resource, which should be accessed using the following supplied routines:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>RxAcquireExclusiveFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553363)</p></td>
<td align="left"><p>This routine acquires the FCB resource in the exclusive mode. This routine will wait for the FCB resource to be free if it was previously acquired; this routine does not return control until the exclusive resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT structure associated with this FCB has been canceled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxAcquireSharedFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553372)</p></td>
<td align="left"><p>This routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be free if it was previously acquired exclusively; this routine does not return control until the shared resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT structure associated with this FCB has been canceled.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>RxAcquireSharedFcbResourceInMRxEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553375)</td>
<td align="left"><p>This routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be free if it was previously acquired exclusively; this routine does not return control until the shared resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT structure associated with this FCB has been canceled.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>RxReleaseFcbResourceForThreadInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554694)</td>
<td align="left"><p>This routine frees the FCB resource previously acquired using [<strong>RxAcquireSharedFcbResourceInMRxEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553375).</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxReleaseFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554699)</p></td>
<td align="left"><p>This routine frees the FCB resource previously acquired using [<strong>RxAcquireExclusiveFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553363) or [<strong>RxAcquireSharedFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553372).</p></td>
</tr>
</tbody>
</table>

 

The following macros are defined in the rxprocs.h header file to determine whether the current thread has access to the FCB regular resource.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxFcbAcquiredShared</strong> (<em>RXCONTEXT</em>, <em>FCB</em>)</p></td>
<td align="left"><p>This macro checks if the current thread has access to the regular resource in shared mode. This macro calls the [<strong>ExIsResourceAcquiredSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545477) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxIsFcbAcquiredShared</strong> (<em>FCB</em>)</p></td>
<td align="left"><p>This macro checks if the current thread has access to the regular resource in shared mode. This macro calls the [<strong>ExIsResourceAcquiredSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545477) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxIsFcbAcquiredExclusive</strong> (<em>FCB</em>)</p></td>
<td align="left"><p>This macro checks if the current thread has access to the regular resource in exclusive mode. This macro calls the [<strong>ExIsResourceAcquiredExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545458) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxIsFcbAcquired</strong> (<em>FCB</em>)</p></td>
<td align="left"><p>This macro checks if the current thread has access to the regular resource in either shared or exclusive mode. This macro calls the [<strong>ExIsResourceAcquiredSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545477) and [<strong>ExIsResourceAcquiredExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545458) routine.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


