---
title: Supporting NVGRE in UDP Segmentation Offload (USO)
description: Learn how to support NVGRE in UDP segmentation offload (USO).
ms.date: 06/15/2023
---

# Supporting NVGRE in UDP Segmentation Offload (USO)

NDIS 6.85 introduces [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) with UDP segmentation offload (USO). NDIS miniport, protocol, and filter drivers, as well as NICs that perform USO, should support NVGRE and VXLAN encapsulations.

**Note**: This article presumes you're familiar with the information in [UDP Segmentation Offload (USO)](udp-segmentation-offload-uso-.md).

If [**NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info).**IsEncapsulatedPacket** is **TRUE** and the **UdpSegmentationOffloadInfo** out-of-band (OOB) information is valid, NVGRE and VXLAN support is required. The NIC must perform USO offload on the NVGRE/VXLAN-encapsulated packet with the following condition:

- The [**NDIS_UDP_SEGMENTATION_OFFLOAD_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/nbluso/ns-nbluso-ndis_udp_segmentation_offload_net_buffer_list_info).**Transmit**.**UdpHeaderOffset** member doesn't have the correct offset value and must not be used by the NIC or miniport driver.

To support NVGRE in USO, protocol and filter drivers must: 

- Adjust the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values in the [**NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info) structure to account for the encapsulation header. The **TcpHeaderRelativeOffset** refers to the UDP header.

NICs and miniport drivers may use the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values provided in the [**NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info) structure. The NIC or miniport driver may perform any needed header checks on the tunnel (outer) IP header or subsequent headers to validate these offsets.

Miniport drivers must handle the case where [**NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info).**InnerFrameOffset** may be in a different scatter-gather list than the beginning of the packet. The protocol driver will guarantee that all the prepended encapsulation headers (ETH, IP, GRE/VXLAN) will be physically contiguous and will be in the first MDL of the packet.

Protocol and filter drivers don't ensure that the total UDP payload length is an exact multiple of the reduced **MSS** value when **UdpSegmentation.SubMssFinalSegmentSupported** is set in the [**NDIS_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) capabilities. For this reason, miniport drivers and NICs with **SubMssFinalSegmentSupported** must update the tunnel (outer) IP header. NICs must generate as many full-sized segments as possible based on the reduced **MSS** value in the [**NDIS_UDP_SEGMENTATION_OFFLOAD_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/nbluso/ns-nbluso-ndis_udp_segmentation_offload_net_buffer_list_info).**Transmit** OOB information. Only one sub-**MSS** segment may be generated per LSOv2 send.

Miniport drivers must:

- Compute the checksum for the tunnel (outer) IP header.
- Increment the IP identification (IP ID) value of the tunnel (outer) IP header for every packet. The first packet must use the IP ID in the original tunnel (outer) IP header.
- Increment the IP ID of the transport (inner) IP header for every packet. The first packet must use the IP ID in the original transport (inner) IP header.
- Compute the checksum for the UDP header and the transport (inner) IP header.
- Ensure that the complete headers, including the encapsulation tunnel (outer) headers are added to every generated packet.

## Related articles

[UDP Segmentation Offload (USO)](udp-segmentation-offload-uso-.md)
