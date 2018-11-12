---
title: Supporting NVGRE in Large Send Offload (LSO)
description: This section describes supporting NVGRE in Large Send Offload (LSO)
ms.assetid: 1EB1B8C2-85C1-4256-BE96-C8B9F1D222B6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NVGRE in Large Send Offload (LSO)


NDIS 6.30 (Windows Server 2012) introduces [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md). NDIS miniport, protocol, and filter drivers and NICs that perform large send offload (LSO) version 2 (LSOV2) should do so in a way that supports NVGRE.

**Note**  This page assumes that you are familiar with the information in [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md).

 

If [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**IsEncapsulatedPacket** is **TRUE** and the **TcpIpChecksumNetBufferListInfo** out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must perform LSOV2 offload on the NVGRE-formatted packet, with the following conditions:

-   Only the values in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882).**LsoV2Transmit** structure are valid. The NIC and miniport driver must not refer to the values in the **NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**.**LsoV1Transmit** structure.
-   The [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882).**LsoV2Transmit**.**TcpHeaderOffset** member does not have the correct offset value and must not be used by the NIC or miniport driver.

To support NVGRE in LSOV2, protocol and filter drivers must make the following changes:

-   Reduce the **MSS** value in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882).**LsoV2Transmit** structure to account for the new GRE header.
-   Send down a TCP payload length that may not be an exact multiple of the reduced **MSS** value.
-   Adjust the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values in the [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957) structure to account for the GRE header.

NICs and miniport drivers may use the **InnerFrameOffset**, **TransportIpHeaderRelativeOffset**, and **TcpHeaderRelativeOffset** values provided in the [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957) structure. The NIC or miniport driver may perform any needed header checks on the tunnel (outer) IP header or subsequent headers to validate these offsets.

Miniport drivers must handle the case where [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**InnerFrameOffset** may be in a different scatter-gather list than the beginning of the packet. The protocol driver will guarantee that all the prepended encapsulation headers (ETH, IP, GRE) will be physically contiguous and will be in the first MDL of the packet.

Protocol and filter drivers do not ensure that the total TCP payload length is an exact multiple of the reduced **MSS** value. For this reason, miniport drivers and NICs must update the tunnel (outer) IP header. NICs must generate as many full-sized segments as possible based on the reduced **MSS** value in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882).**LsoV2Transmit** OOB information. Only one sub-**MSS** segment may be generated per LSOv2 send.

Miniport drivers must do the following:

-   Compute the checksum for the tunnel (outer) IP header.
-   Increment the IP identification (IP ID) value of the tunnel (outer) IP header for every packet. The first packet must use the IP ID in the original tunnel (outer) IP header.
-   Increment the IP ID of the transport (inner) IP header for every packet. The first packet must use the IP ID in the original transport (inner) IP header.
-   Compute the checksum for the TCP header and the transport (inner) IP header.
-   Ensure that the complete headers, including the encapsulation tunnel (outer) headers are added to every generated packet.

## Related topics


[Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md)

 

 






