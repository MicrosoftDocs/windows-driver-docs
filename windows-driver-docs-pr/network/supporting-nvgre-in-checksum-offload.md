---
title: Supporting NVGRE in Checksum Offload
description: This section describes supporting NVGRE in checksum offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NVGRE in Checksum Offload


NDIS 6.30 (Windows Server 2012) introduces [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md). NDIS miniport, protocol, and filter drivers and NICs that offload checksum tasks should do so in a way that supports NVGRE.

**Note**  This page assumes that you are familiar with the information in [Offloading Checksum Tasks](offloading-checksum-tasks.md).

 

If [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info).**IsEncapsulatedPacket** is **TRUE** and the **TcpIpChecksumNetBufferListInfo** out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header.

The **IsIPv4** and **IsIPv6** flags in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/nblchecksum/ns-nblchecksum-ndis_tcp_ip_checksum_net_buffer_list_info) structure indicate the IP header version of the tunnel (outer) IP header. The NIC must parse the transport (inner) IP header to determine that header's IP version. Because mixed-mode packets are allowed (see [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_encapsulated_packet_task_offload)), the NIC must not assume that the inner and outer IP headers will have the same IP header version.

NICs and miniport drivers may use the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values provided in the [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info) structure. The NIC or miniport driver may perform any needed header checks on the tunnel (outer) IP header or subsequent headers to validate these offsets.

Note that when [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info).**IsEncapsulatedPacket** is TRUE, the existing header offset fields, [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/nbllso/ns-nbllso-ndis_tcp_large_send_offload_net_buffer_list_info).**LsoV2Transmit**.**TcpHeaderOffset** and [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/nblchecksum/ns-nblchecksum-ndis_tcp_ip_checksum_net_buffer_list_info).**Transmit**.**TcpHeaderOffset**, will not have correct values and must not be used by the NIC or driver.

Miniport drivers must handle the case where [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_tcp_send_offloads_supplemental_net_buffer_list_info).**InnerFrameOffset** may be in a different scatter-gather list than the beginning of the packet. The protocol driver will guarantee that all the prepended encapsulation headers (ETH, IP, GRE) will be physically contiguous and will be in the first MDL of the packet.

## Checksum Validation


Checksum validation for NVGRE is largely the same as it would be otherwise.

If a miniport receives an [OID\_TCP\_OFFLOAD\_PARAMETERS](./oid-tcp-offload-parameters.md) OID request and succeeds it for **NDIS\_ENCAPSULATION\_TYPE\_GRE\_MAC** (see [**NDIS\_OFFLOAD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters)), the NIC must perform checksum validation on the tunnel (outer) IP header, transport (inner) IP header, and TCP or UDP header.

For encapsulated packets that have an IPv4 tunnel (outer) header and an IPv4 transport (inner) header, a miniport driver should set the **IpChecksumSucceeded** flag in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/nblchecksum/ns-nblchecksum-ndis_tcp_ip_checksum_net_buffer_list_info) structure only if both IP header checksum validations succeeded. For encapsulated packets that have both a tunnel (outer) IPv4 header and a transport (inner) IPv4 header, the miniport driver should set the **IpChecksumFailed** flag if either of the IP header checksum validations failed.

 

