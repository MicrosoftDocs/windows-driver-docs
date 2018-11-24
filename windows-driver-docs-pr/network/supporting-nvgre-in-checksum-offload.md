---
title: Supporting NVGRE in Checksum Offload
description: This section describes supporting NVGRE in checksum offload
ms.assetid: 933EE18B-917A-40BC-87AA-0F463615A082
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NVGRE in Checksum Offload


NDIS 6.30 (Windows Server 2012) introduces [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md). NDIS miniport, protocol, and filter drivers and NICs that offload checksum tasks should do so in a way that supports NVGRE.

**Note**  This page assumes that you are familiar with the information in [Offloading Checksum Tasks](offloading-checksum-tasks.md).

 

If [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**IsEncapsulatedPacket** is **TRUE** and the **TcpIpChecksumNetBufferListInfo** out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header.

The **IsIPv4** and **IsIPv6** flags in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877) structure indicate the IP header version of the tunnel (outer) IP header. The NIC must parse the transport (inner) IP header to determine that header's IP version. Because mixed-mode packets are allowed (see [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/jj991956)), the NIC must not assume that the inner and outer IP headers will have the same IP header version.

NICs and miniport drivers may use the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values provided in the [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957) structure. The NIC or miniport driver may perform any needed header checks on the tunnel (outer) IP header or subsequent headers to validate these offsets.

Note that when [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**IsEncapsulatedPacket** is TRUE, the existing header offset fields, [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882).**LsoV2Transmit**.**TcpHeaderOffset** and [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877).**Transmit**.**TcpHeaderOffset**, will not have correct values and must not be used by the NIC or driver.

Miniport drivers must handle the case where [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**InnerFrameOffset** may be in a different scatter-gather list than the beginning of the packet. The protocol driver will guarantee that all the prepended encapsulation headers (ETH, IP, GRE) will be physically contiguous and will be in the first MDL of the packet.

## Checksum Validation


Checksum validation for NVGRE is largely the same as it would be otherwise.

If a miniport receives an [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request and succeeds it for **NDIS\_ENCAPSULATION\_TYPE\_GRE\_MAC** (see [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)), the NIC must perform checksum validation on the tunnel (outer) IP header, transport (inner) IP header, and TCP or UDP header.

For encapsulated packets that have an IPv4 tunnel (outer) header and an IPv4 transport (inner) header, a miniport driver should set the **IpChecksumSucceeded** flag in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877) structure only if both IP header checksum validations succeeded. For encapsulated packets that have both a tunnel (outer) IPv4 header and a transport (inner) IPv4 header, the miniport driver should set the **IpChecksumFailed** flag if either of the IP header checksum validations failed.

 

 





