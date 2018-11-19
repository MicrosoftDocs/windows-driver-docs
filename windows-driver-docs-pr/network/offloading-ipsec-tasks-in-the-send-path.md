---
title: Offloading IPsec Tasks in the Send Path
description: Offloading IPsec Tasks in the Send Path
ms.assetid: b95878e0-0aee-43cb-a64c-b5d8e07cb1b4
keywords:
- ESP-protected packets WDK IPsec offload , send path offload
- AH-protected packets WDK IPsec offload , send path offload
- send path offload WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offloading IPsec Tasks in the Send Path

\[The IPsec Task Offload feature is deprecated and should not be used.\]




Before the TCP/IP transport passes to the miniport driver a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for a packet on which a NIC will perform Internet protocol security (IPsec) tasks, it updates the IPsec information that is associated with the NET\_BUFFER\_LIST structure. The TCP/IP transport specifies this information in an [**NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565801) structure, which is part of the NET\_BUFFER\_LIST information (out-of-band data) that is associated with the NET\_BUFFER\_LIST structure.

The TCP/IP transport supplies *OffloadHandle*, which specifies the handle to the outbound SA for the transport (end-to-end connection) portion of the send packet. If the packet will be transmitted through a tunnel, the TCP/IP transport also supplies *NextOffloadHandle*, which specifies the handle to the outbound SA for the tunnel portion of the send packet.

After a miniport driver receives the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure in its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) or [**MiniportCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559365) function, it can call the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with an *\_Id* of **IPsecOffloadV1NetBufferListInfo** to obtain the NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO structure that is associated with the NET\_BUFFER\_LIST structure.

When the NIC performs IPsec processing on a send packet, it calculates the AH or ESP encryption checksums (or both) for the packet and, if the packet contains an ESP payload, encrypts the packet. The TCP/IP transport has already framed the packet, padded it (if necessary), and assigned it a sequence number and SPI.

 

 





