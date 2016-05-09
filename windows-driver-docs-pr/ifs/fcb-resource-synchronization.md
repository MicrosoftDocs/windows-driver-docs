---
title: FCB Resource Synchronization
description: FCB Resource Synchronization
ms.assetid: 8355907e-e313-4e54-a63f-a82d9ce0d31b
keywords: ["RDBSS WDK file systems , FCB resource synchronization", "Redirected Drive Buffering Subsystem WDK file systems , FCB resource synchronization", "FCB resource synchronization WDK RDBSS", "paging I/O WDK RDBSS", "synchronization WDK RDBSS", "file control block structure WDK RDBSS"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20FCB%20Resource%20Synchronization%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




