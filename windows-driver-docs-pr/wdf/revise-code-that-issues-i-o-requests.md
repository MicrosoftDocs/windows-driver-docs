---
title: Revise Code That Issues I/O Requests
description: Revise Code That Issues I/O Requests
ms.assetid: 39E4B6B2-45C8-42B7-811A-EEDCCCB056EF
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548604" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForIoctl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548604)"><strong>WdfIoTargetFormatRequestForIoctl</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548595" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548595)"><strong>WdfIoTargetFormatRequestForInternalIoctl</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548599" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctlOthers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548599)"><strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong></a></p></td>
<td align="left">Similar to manually formatting the next I/O stack location.</td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548612" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForRead&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548612)"><strong>WdfIoTargetFormatRequestForRead</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548620" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548620)"><strong>WdfIoTargetFormatRequestForWrite</strong></a></p></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548310" data-raw-source="[&lt;strong&gt;IoBuildAsynchronousFsdRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548310)"><strong>IoBuildAsynchronousFsdRequest</strong></a>.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548660" data-raw-source="[&lt;strong&gt;WdfIoTargetSendIoctlSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548660)"><strong>WdfIoTargetSendIoctlSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548656" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548656)"><strong>WdfIoTargetSendInternalIoctlSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548651" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlOthersSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548651)"><strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong></a></p></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548318" data-raw-source="[&lt;strong&gt;IoBuildDeviceIoControlRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548318)"><strong>IoBuildDeviceIoControlRequest</strong></a>, followed by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>.</td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548669" data-raw-source="[&lt;strong&gt;WdfIoTargetSendReadSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548669)"><strong>WdfIoTargetSendReadSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548672" data-raw-source="[&lt;strong&gt;WdfIoTargetSendWriteSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548672)"><strong>WdfIoTargetSendWriteSynchronously</strong></a></p></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548330" data-raw-source="[&lt;strong&gt;IoBuildSynchronousFsdRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548330)"><strong>IoBuildSynchronousFsdRequest</strong></a>, followed by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549941" data-raw-source="[&lt;strong&gt;WdfRequestCancelSentRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549941)"><strong>WdfRequestCancelSentRequest</strong></a></p></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548338" data-raw-source="[&lt;strong&gt;IoCancelIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548338)"><strong>IoCancelIrp</strong></a> for a PIRP that was sent with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>. The framework provides locks to ensure that the PIRP is not completed or freed between the calls to <strong>IoCallDriver</strong> and <strong>IoCancelIrp</strong>.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549951" data-raw-source="[&lt;strong&gt;WdfRequestCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549951)"><strong>WdfRequestCreate</strong></a></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548257" data-raw-source="[&lt;strong&gt;IoAllocateIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548257)"><strong>IoAllocateIrp</strong></a>. Creates a new WDFREQUEST object, sets attributes, and returns handle to caller.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549955" data-raw-source="[&lt;strong&gt;WdfRequestFormatRequestUsingCurrentType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549955)"><strong>WdfRequestFormatRequestUsingCurrentType</strong></a></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549100" data-raw-source="[&lt;strong&gt;IoForwardIrpSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549100)"><strong>IoForwardIrpSynchronously</strong></a> but does not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>; driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a>.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a></td>
<td align="left">Similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549100" data-raw-source="[&lt;strong&gt;IoForwardIrpSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549100)"><strong>IoForwardIrpSynchronously</strong></a> but does not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>; driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a>.</td>
</tr>
</tbody>
</table>

 

To send a request to another device stack, a WDF driver uses a remote I/O target. For information about how to initialize a remote I/O target, see [Initializing a General I/O Target](initializing-a-general-i-o-target.md).

To get the completion status for an asynchronous request or for any request that is sent by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027), the driver calls [**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974). For a synchronous request, it can retrieve status immediately. For an asynchronous request, the driver’s I/O completion callback typically retrieves status. For more information about sending requests synchronously or asynchronously, see [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md).

 

 





