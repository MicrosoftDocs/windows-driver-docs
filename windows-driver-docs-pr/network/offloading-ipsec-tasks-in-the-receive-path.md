---
title: Offloading IPsec Tasks in the Receive Path
description: Offloading IPsec Tasks in the Receive Path
ms.assetid: d1dff4fa-7354-4c8c-8591-223c6b524619
keywords:
- ESP-protected packets WDK IPsec offload , receive path offload
- AH-protected packets WDK IPsec offload , receive path offload
- receive path offload WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offloading IPsec Tasks in the Receive Path

\[The IPsec Task Offload feature is deprecated and should not be used.\]




When a NIC performs Internet protocol security (IPsec) processing on a receive packet, it decrypts the packet if the packet contains an ESP payload and calculates the AH or ESP encryption checksums (or both) for the packet. Before indicating the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the packet up to the TCP/IP transport, the miniport driver calls the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with an *\_Id* of **IPsecOffloadV1NetBufferListInfo** to obtain the [**NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565801) structure that is associated with a packet.

The miniport driver sets the **CryptoDone** flag in the NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO structure to indicate that the NIC performed IPsec checking on at least one IPsec payload in the receive packet. If a NIC performed IPsec checking on both the tunnel and transport portions of a receive packet, the miniport driver also sets the **NextCryptoDone** flag in the NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO structure. The miniport driver sets **NextCryptoDone** only if a packet has both tunnel and transport IPsec payloads. Otherwise, the miniport driver sets **NextCryptoDone** to zero. To indicate the results of the IPsec checks, the miniport driver must also supply a value for the **CryptoStatus** member in the NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO structure. If the NIC detects a checksum failure or a decryption failure, the miniport driver must indicate a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the receive packet in whatever form it is and specify the appropriate **CryptoStatus** value.

Note that, if the miniport driver is not decrypting an incoming packet, it clears both the **CryptoDone** and the **NextCryptoDone** flags. The miniport driver does this for all receive packets that it does not decrypt, regardless of whether the packet is AH-protected or ESP-protected. The miniport driver sets **CryptoStatus** to CRYPTO\_SUCCESS for all packets that it does not decrypt.

After the miniport driver indicates the NET\_BUFFER\_LIST structure to the TCP/IP transport, the transport examines the results of the IPsec checks that the NIC performed, checks the sequence numbers for the packet, and determines what to do with a packet that fails the checksum or sequencing tests.

 

 





