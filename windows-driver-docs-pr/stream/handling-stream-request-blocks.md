---
title: Handling Stream Request Blocks
description: Handling Stream Request Blocks
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , SRBs
- streaming minidrivers WDK Windows 2000 Kernel , SRBs
- minidrivers WDK Windows 2000 Kernel Streaming , SRBs
- SRBs WDK streaming minidriver
- stream request blocks See SRB or SRBs
ms.date: 04/20/2017
---

# Handling Stream Request Blocks





The operating system dispatches all I/O requests on the device to the class driver. The class driver in turn requests hardware-specific information from the minidriver by passing SRBs to the minidriver. The class driver specifies the operation it requests in the **Command** member of the stream request block.

Both the minidriver as a whole, and each stream within the minidriver, may receive I/O requests. The minidriver must provide a [*StrMiniReceiveDevicePacket*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) routine to handle device-wide requests. Each stream must support two routines to handle I/O requests: one for data requests, and one for control requests. The class driver calls the data request callback, [*StrMiniReceiveStreamDataPacket*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb), to handle all read and write requests on a stream. All other requests for a stream are passed to [**StrMiniReceiveStreamControlPacket**](/previous-versions/ff568467(v=vs.85)).

If the class driver is handling synchronization for the minidriver, it queues stream requests, and dispatches them to the minidriver one at a time. The class driver maintains three separate queues -- one for device requests, and one each for stream data and control requests. The minidriver may signal that it is ready for a new request from one of these queues as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Request Type</th>
<th>Routine</th>
<th>NotificationType Parameter of Routine</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>device request</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassdevicenotification" data-raw-source="[&lt;strong&gt;StreamClassDeviceNotification&lt;/strong&gt;](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassdevicenotification)"><strong>StreamClassDeviceNotification</strong></a></p></td>
<td><p>ReadyForNextDeviceRequest</p></td>
</tr>
<tr class="even">
<td><p>stream control request</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassstreamnotification" data-raw-source="[&lt;strong&gt;StreamClassStreamNotification&lt;/strong&gt;](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassstreamnotification)"><strong>StreamClassStreamNotification</strong></a></p></td>
<td><p>ReadyForNextStreamControlRequest</p></td>
</tr>
<tr class="odd">
<td><p>stream data request</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassstreamnotification" data-raw-source="[&lt;strong&gt;StreamClassStreamNotification&lt;/strong&gt;](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassstreamnotification)"><strong>StreamClassStreamNotification</strong></a></p></td>
<td><p>ReadyForNextStreamDataRequest</p></td>
</tr>
</tbody>
</table>

 

When the class driver calls **StrMiniReceive*XXX*Packet**, it hands off the stream request block to the minidriver. The minidriver's routine has sole access to the stream request block until it signals to the class driver it has completed the request.

When the minidriver finishes processing a request, it should signal the class driver it has completed the request as follows:

1.  The minidriver should set the status of the request in the **Status** field of the stream request block.

2.  The minidriver should signal it has completed the request, by calling [**StreamClassDeviceNotification**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassdevicenotification) or [**StreamClassStreamNotification**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassstreamnotification). To complete a device request, the minidriver calls **StreamClassDeviceNotification** with a *NotificationType* parameter of DeviceRequestComplete. To complete a stream request, the minidriver calls **StreamClassStreamNotification** with a *NotificationType* parameter of StreamRequestComplete.

3.  If the class driver is handling synchronization, and if the minidriver has not yet signaled the class driver that it is ready for another request on this queue, it should do so now.

The minidriver can combine 2 and 3 by calling [**StreamClassCompleteRequestAndMarkQueueReady**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclasscompleterequestandmarkqueueready).

The minidriver processes requests asynchronously, so the class driver may need to cancel or time out a request. For these purposes, the minidriver must provide a [*StrMiniCancelPacket*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_cancel_srb) and a [*StrMiniRequestTimeout*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_request_timeout_handler) routine. The class driver calls the respective minidriver routine when it cancels or times out a request.

The class driver cancels a request when the underlying I/O request is canceled by the operating system. The class driver times out requests that take too long to process -- it decrements a counter of how many seconds until it times out a request in the **TimeoutCounter** member of the stream request block. If the minidriver must defer processing on a request for a long period of time, it should set the **TimeoutCounter** member to zero -- the class driver then will not time out the request. Once the minidriver resumes processing of the request, it should reset **TimeoutCounter** to be equal to the **TimeoutOriginal** member of the stream request block. The minidriver can reset **TimeoutOriginal** to change the length of time before the request times out. See [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block) for details.

