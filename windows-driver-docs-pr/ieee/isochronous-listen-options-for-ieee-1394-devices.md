---
title: Isochronous Listen Options for IEEE 1394 Devices
description: Isochronous Listen Options for IEEE 1394 Devices
ms.assetid: a369b7f0-be85-49f0-bb09-d07cbd3d3558
keywords:
- isochronous I/O WDK IEEE 1394 bus , listen options
- listen options WDK IEEE 1394 bus
- packet-based DMA WDK IEEE 1394 bus
- stream-based DMA WDK IEEE 1394 bus
- DMA transfers WDK IEEE 1394 bus
- packet DMA WDK IEEE 1394 bus
- stripping packet headers
- headers WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Isochronous Listen Options for IEEE 1394 Devices





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

 

 

 




