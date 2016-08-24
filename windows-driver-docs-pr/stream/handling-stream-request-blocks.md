---
title: Handling Stream Request Blocks
author: windows-driver-content
description: Handling Stream Request Blocks
MS-HAID:
- 'strmini-design\_722ff500-4a65-44c2-bdd4-c5accbb7649e.xml'
- 'stream.handling\_stream\_request\_blocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fb4fda0d-54e9-4f1b-a78c-276e770189d5
keywords: ["Stream.sys class driver WDK Windows 2000 Kernel , SRBs", "streaming minidrivers WDK Windows 2000 Kernel , SRBs", "minidrivers WDK Windows 2000 Kernel Streaming , SRBs", "SRBs WDK streaming minidriver", "stream request blocks See SRB or SRBs"]
---

# Handling Stream Request Blocks


## <a href="" id="ddk-handling-stream-request-blocks-ksg"></a>


The operating system dispatches all I/O requests on the device to the class driver. The class driver in turn requests hardware-specific information from the minidriver by passing SRBs to the minidriver. The class driver specifies the operation it requests in the **Command** member of the stream request block.

Both the minidriver as a whole, and each stream within the minidriver, may receive I/O requests. The minidriver must provide a [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) routine to handle device-wide requests. Each stream must support two routines to handle I/O requests: one for data requests, and one for control requests. The class driver calls the data request callback, [*StrMiniReceiveStreamDataPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568470), to handle all read and write requests on a stream. All other requests for a stream are passed to [**StrMiniReceiveStreamControlPacket**](https://msdn.microsoft.com/library/windows/hardware/ff568467).

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
<td><p>[<strong>StreamClassDeviceNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568239)</p></td>
<td><p>ReadyForNextDeviceRequest</p></td>
</tr>
<tr class="even">
<td><p>stream control request</p></td>
<td><p>[<strong>StreamClassStreamNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568266)</p></td>
<td><p>ReadyForNextStreamControlRequest</p></td>
</tr>
<tr class="odd">
<td><p>stream data request</p></td>
<td><p>[<strong>StreamClassStreamNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568266)</p></td>
<td><p>ReadyForNextStreamDataRequest</p></td>
</tr>
</tbody>
</table>

 

When the class driver calls **StrMiniReceive*XXX*Packet**, it hands off the stream request block to the minidriver. The minidriver's routine has sole access to the stream request block until it signals to the class driver it has completed the request.

When the minidriver finishes processing a request, it should signal the class driver it has completed the request as follows:

1.  The minidriver should set the status of the request in the **Status** field of the stream request block.

2.  The minidriver should signal it has completed the request, by calling [**StreamClassDeviceNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568239) or [**StreamClassStreamNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568266). To complete a device request, the minidriver calls **StreamClassDeviceNotification** with a *NotificationType* parameter of DeviceRequestComplete. To complete a stream request, the minidriver calls **StreamClassStreamNotification** with a *NotificationType* parameter of StreamRequestComplete.

3.  If the class driver is handling synchronization, and if the minidriver has not yet signaled the class driver that it is ready for another request on this queue, it should do so now.

The minidriver can combine 2 and 3 by calling [**StreamClassCompleteRequestAndMarkQueueReady**](https://msdn.microsoft.com/library/windows/hardware/ff568232).

The minidriver processes requests asynchronously, so the class driver may need to cancel or time out a request. For these purposes, the minidriver must provide a [*StrMiniCancelPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568448) and a [*StrMiniRequestTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff568473) routine. The class driver calls the respective minidriver routine when it cancels or times out a request.

The class driver cancels a request when the underlying I/O request is canceled by the operating system. The class driver times out requests that take too long to process -- it decrements a counter of how many seconds until it times out a request in the **TimeoutCounter** member of the stream request block. If the minidriver must defer processing on a request for a long period of time, it should set the **TimeoutCounter** member to zero -- the class driver then will not time out the request. Once the minidriver resumes processing of the request, it should reset **TimeoutCounter** to be equal to the **TimeoutOriginal** member of the stream request block. The minidriver can reset **TimeoutOriginal** to change the length of time before the request times out. See [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Handling%20Stream%20Request%20Blocks%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


