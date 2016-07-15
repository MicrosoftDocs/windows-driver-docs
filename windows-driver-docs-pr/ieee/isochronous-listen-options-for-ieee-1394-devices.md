---
title: Isochronous Listen Options for IEEE 1394 Devices
description: Isochronous Listen Options for IEEE 1394 Devices
MS-HAID:
- '1394-isoch\_98e7dc15-b142-407d-9f7c-265e7dda75b9.xml'
- 'IEEE.isochronous\_listen\_options\_for\_ieee\_1394\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a369b7f0-be85-49f0-bb09-d07cbd3d3558
keywords: ["isochronous I/O WDK IEEE 1394 bus , listen options", "listen options WDK IEEE 1394 bus", "packet-based DMA WDK IEEE 1394 bus", "stream-based DMA WDK IEEE 1394 bus", "DMA transfers WDK IEEE 1394 bus", "packet DMA WDK IEEE 1394 bus", "stripping packet headers", "headers WDK IEEE 1394 bus"]
---

# Isochronous Listen Options for IEEE 1394 Devices


## <a href="" id="ddk-isochronous-listen-options-for-ieee-1394-devices-kg"></a>


This section describes the various isochronous listen options.

### Receiving or stripping packet headers

Host controllers may or may not automatically strip the headers off an isochronous packet. The bus driver sets the HOST\_INFO\_SUPPORTS\_RETURNING\_ISO\_HDR flag of **HostCapabilities** member of the [**GET\_LOCAL\_HOST\_INFO2**](https://msdn.microsoft.com/library/windows/hardware/ff537147) structure if the host controller does *not* automatically strip the headers off isochronous packets.

Also, host controllers may support configurable stripping of headers. The bus driver sets the HOST\_INFO\_SUPPORTS\_ISOCH\_STRIPPING flag of HostCapabilities if the host controller can be configured to strip headers. To actually configure the host controller to strip headers, the driver submits the [**REQUEST\_ISOCH\_ALLOCATE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537649) request with the RESOURCE\_STRIP\_ADDITIONAL\_QUADLETS flag set. The **nQuadletsToStrip** member specifies the number of quadlets to strip off the beginning of each packet. For example, **nQuadletsToStrip** = 1 would strip off the isochronous packet header.

### Stream versus packet-based DMA

The stream-based and packet-based DMA strategies require support from the underlying host controller. All host controllers support at least one of the DMA strategies, and OHCI-compliant host controllers support both.

Packet-based DMA and stream-based DMA have similar characteristics when all packets are of the same size. But the two sorts of DMA have very different characteristics when the packet size varies.

In stream-based DMA, the host controller ignores packet boundaries as it fills the I/O buffers, leaving no gaps in the data that it writes. In order to determine the location of a particular packet, you must know the lengths of all the previous packets.

In packet-based DMA, the host controller writes just one isochronous packet per buffer. Thus in packet mode, the host controller spaces the data it writes, so that each packet begins at a distance from the beginning of the I/O buffer that is an integral multiple of the maximum packet size. If a particular packet is smaller than the maximum, the data located between the end of that packet and the start of the next packet is undefined. So when packets are smaller than the maximum size, some buffer space is wasted. For example, a buffer large enough to hold 10 packets always holds exactly 10 packets, even if some packets are smaller than the maximum size allowed.

Regardless of which DMA mode you choose, some design tradeoffs apply. For example, the choice of buffer size affects the performance of your device, no matter which DMA mode you use. Large buffers provide efficiency because you avoid some of the overhead associated with initializing a large number of buffers. Also, fewer buffers mean that fewer DMA descriptors are required. On the other hand, larger buffers increase the latency between the beginning of an I/O operation and the moment in which the bus driver informs the function driver that the buffer is full.

If the host controller supports both types of DMA, the bus driver sets the host controller to default to stream-based DMA. To reset the host controller to packet-based DMA, the driver should set the RESOURCE\_USE\_PACKET\_BASED flag when it allocates the resource handle.

Drivers use the [**REQUEST\_GET\_LOCAL\_HOST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537644) bus request (with the **u.GetLocalHostInformation.nLevel** member of the IRB = GET\_HOST\_CAPABILITIES) to determine the characteristics of the host controller. The bus driver returns a [**GET\_LOCAL\_HOST\_INFO2**](https://msdn.microsoft.com/library/windows/hardware/ff537147) structure, and sets flags within the **HostCapabilities** member to indicate what the host controller supports:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>DMA type</th>
<th>HostCapabilities flag</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>stream-based</p></td>
<td><p>HOST_INFO_STREAM_BASED</p></td>
</tr>
<tr class="even">
<td><p>packet-based</p></td>
<td><p>HOST_INFO_PACKET_BASED</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Isochronous%20Listen%20Options%20for%20IEEE%201394%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




