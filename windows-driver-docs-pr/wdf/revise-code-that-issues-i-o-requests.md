---
title: Revise Code That Issues I/O Requests
author: windows-driver-content
description: Revise Code That Issues I/O Requests
ms.assetid: 39E4B6B2-45C8-42B7-811A-EEDCCCB056EF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Revise Code That Issues I/O Requests


WDF defines several methods that a driver can use to create and format I/O requests. The following table summarizes these methods:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KMDF method</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>WdfIoTargetFormatRequestForIoctl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548604)</p>
<p>[<strong>WdfIoTargetFormatRequestForInternalIoctl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548595)</p>
<p>[<strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548599)</p></td>
<td align="left">Similar to manually formatting the next I/O stack location.</td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WdfIoTargetFormatRequestForRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548612)</p>
<p>[<strong>WdfIoTargetFormatRequestForWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548620)</p></td>
<td align="left">Similar to [<strong>IoBuildAsynchronousFsdRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548310).</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WdfIoTargetSendIoctlSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548660)</p>
<p>[<strong>WdfIoTargetSendInternalIoctlSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548656)</p>
<p>[<strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548651)</p></td>
<td align="left">Similar to [<strong>IoBuildDeviceIoControlRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548318), followed by [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336).</td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WdfIoTargetSendReadSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548669)</p>
<p>[<strong>WdfIoTargetSendWriteSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548672)</p></td>
<td align="left">Similar to [<strong>IoBuildSynchronousFsdRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548330), followed by [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336).</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WdfRequestCancelSentRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549941)</p></td>
<td align="left">Similar to [<strong>IoCancelIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548338) for a PIRP that was sent with [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336). The framework provides locks to ensure that the PIRP is not completed or freed between the calls to <strong>IoCallDriver</strong> and <strong>IoCancelIrp</strong>.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WdfRequestCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549951)</td>
<td align="left">Similar to [<strong>IoAllocateIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548257). Creates a new WDFREQUEST object, sets attributes, and returns handle to caller.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WdfRequestFormatRequestUsingCurrentType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549955)</td>
<td align="left">Similar to [<strong>IoForwardIrpSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549100) but does not call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336); driver must call [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027).</td>
</tr>
<tr class="even">
<td align="left">[<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027)</td>
<td align="left">Similar to [<strong>IoForwardIrpSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549100) but does not call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336); driver must call [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027).</td>
</tr>
</tbody>
</table>

 

To send a request to another device stack, a WDF driver uses a remote I/O target. For information about how to initialize a remote I/O target, see [Initializing a General I/O Target](initializing-a-general-i-o-target.md).

To get the completion status for an asynchronous request or for any request that is sent by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027), the driver calls [**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974). For a synchronous request, it can retrieve status immediately. For an asynchronous request, the driver’s I/O completion callback typically retrieves status. For more information about sending requests synchronously or asynchronously, see [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md).

 

 





