---
title: Sending Network Data with IPsec Offload Version 2
description: Sending Network Data with IPsec Offload Version 2
ms.assetid: d3580313-a98b-4150-b344-e3e395ce68e9
keywords:
- IPsecOV2 WDK TCP/IP transport , sending data
- sending data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Network Data with IPsec Offload Version 2

\[The IPsec Task Offload feature is deprecated and should not be used.\]




The TCP/IP transport provides IPsec Offload Version 2 (IPsecOV2) information for one or more SAs with the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID. Before the miniport driver returns a successful result for OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA, the miniport driver initializes an offload handle. The TCP/IP transport requests the miniport driver to offload the processing of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure by specifying IPsecOV2 information in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) and [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) structures, which are part of the **NET\_BUFFER\_LIST** out-of-band (OOB) information.

The TCP/IP transport supplies an offload handle in the **OffloadHandle** member of [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) that specifies the handle to the outbound security association (SA) for the transport (end-to-end connection) portion of the send packet.

The TCP/IP transport supplies the following header information in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) structure:

-   Header offsets for an AH header, ESP header, or both.

-   The next protocol value (identical to the one that is contained in the ESP trailer).

-   The pad length that is used for a combined large send offload (LSO) and IPsec offload.

Also, if the send packet will be transmitted through a tunnel, the TCP/IP transport supplies an [**NDIS\_IPSEC\_OFFLOAD\_V2\_TUNNEL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565843) structure. This structure specifies the offload handle to the outbound SA for the tunnel portion of the send packet. For more information about accessing OOB information, see [Accessing NET\_BUFFER\_LIST Information in IPsec Offload Version 2](accessing-net-buffer-list-information-in-ipsec-offload-version-2.md).

The miniport driver provided the offload handles in response to an OID set request of [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812). For more information about SAs, see [Managing Security Associations in IPsec Offload Version 2](managing-security-associations-in-ipsec-offload-version-2.md).

When a miniport driver handles a send request in the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function, the miniport driver:

-   Verifies that the hardware is configured to handle IPsec offload services. If the hardware is not configured to handle IPsec offload services, the miniport driver should handle the send request without providing the offload services.

-   Verifies the handles in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) and [**NDIS\_IPSEC\_OFFLOAD\_V2\_TUNNEL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565843) structures to determine if IPsec cryptographic processing is required. An offload handle value of zero indicates that no IPsec task offload should be performed for the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388). If the miniport driver cannot find the offloaded SA that corresponds to the specified offload handle, the send packet should fail with an **NDIS\_STATUS\_FAILURE** value.

-   Verifies the handles in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) structures to determine if segmentation offload should be performed for the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388).

-   Completes the required AH and ESP processing for all of the send packets in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388). When the NIC performs IPsec processing on a send packet, it performs the cryptographic operations on the packet data. The TCP/IP transport has already framed the packet, padded it (if necessary), and assigned it a sequence number and security parameters index (SPI). For a combined LSO and IPsec offload, the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) might have padding that will be discarded while the NIC segments the large packet. The amount of padding is specified in the **PadLength** member of the [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) structure. Segmented packets might require padding to support IPsec operations.

When a protocol driver transmits a packet that requests both LSO and IPsecOV2, it will not frame the ESP trailer. This is because the information in the ESP trailer, such as the padding length, will not be accurate for the last segment that was generated by the NIC.

 

 





