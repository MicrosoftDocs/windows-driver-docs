---
title: Receiving Network Data with IPsec Offload Version 2
description: Receiving Network Data with IPsec Offload Version 2
ms.assetid: c09ce374-6dd6-4d16-914b-5576304d4440
keywords:
- IPsecOV2 WDK TCP/IP transport , receiving data
- receiving data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Network Data with IPsec Offload Version 2

\[The IPsec Task Offload feature is deprecated and should not be used.\]




A NIC performs IPsec offload version 2 (IPsecOV2) processing on a receive packet as specified in a security association (SA) that was offloaded from the transport.

The miniport driver sets the IPsecOV2 out-of-band (OOB) information before indicating the received data to overlying drivers. For more information about accessing OOB information, see [Accessing NET\_BUFFER\_LIST Information in IPsec Offload Version 2](accessing-net-buffer-list-information-in-ipsec-offload-version-2.md).

**Note**  A miniport driver should indicate all received packets to overlying drivers even if an error occurs while processing the IPsec data in the NIC. The driver must indicate packets with errors to enable the driver stack to monitor and troubleshoot the network traffic.

 

Before the miniport driver indicates the received data packet up the driver stack, the miniport driver:

-   Verifies that the hardware is configured to handle IPsec offload tasks. If not, the miniport driver does a receive indication with no additional IPsec offload processing.

-   Looks at the security parameters index (SPI) to determine if a matching offloaded SA exists. The miniport driver confirms the destination address on the packet is same as the one specified in offloaded SA. If there is no matching SA, the NIC indicates the received data without setting the IPsecOV2 OOB information.

-   Verifies that it can process the packet based on the capabilities that the miniport driver reported to the transport or it makes a receive indication without further IPsec processing. For example, the packet might have IP options where the NIC does not support IPsec offload processing for such packets and the miniport driver does the IPsec processing.

-   Sets the **CryptoDone** flag in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) structure to indicate that a NIC performed IPsec checking on at least one IPsec payload in the received packet.

-   Sets the **NextCryptoDone** flag in the NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO structure to indicate that a NIC performed IPsec checking on both the tunnel and transport portions of a receive packet. The miniport driver sets this flag only if a packet has both tunnel and transport payloads; otherwise, this flag should be zero.

-   Sets the correct **CryptoStatus** value of the NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO structure to indicate the results of the IPsec checks.

If the NIC did not perform offload processing on an incoming packet, the miniport driver clears both the **CryptoDone** and the **NextCryptoDone** flags. The miniport driver clears these flags for all receive packets where a NIC does not decrypt, regardless of whether the packet is AH-protected or ESP-protected.

A miniport driver can set **SaDeleteReq**, in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) structure for a receive [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388). The TCP/IP transport subsequently issues [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569813) once to delete the inbound SA that the packet was received over and once again to delete the outbound SA that corresponds to the deleted inbound SA. For more information about adding and deleting SAs, see [Managing Security Associations in IPsec Offload Version 2](managing-security-associations-in-ipsec-offload-version-2.md).

After the miniport driver indicates the NET\_BUFFER\_LIST structure to the TCP/IP transport, the TCP/IP transport examines the results of the IPsec checks that the NIC performed on the packet, checks the sequence numbers for the packet, and determines what to do with a packet that fails the checksum or sequencing tests.

 

 





