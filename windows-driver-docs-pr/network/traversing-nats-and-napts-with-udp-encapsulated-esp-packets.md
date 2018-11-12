---
title: Traversing NATs and NAPTs with UDP-Encapsulated ESP Packets
description: Traversing NATs and NAPTs with UDP-Encapsulated ESP Packets
ms.assetid: 9bfd6a7c-2c24-419e-b82d-ef6ef8fe1fa5
keywords:
- UDP-encapsulated ESP packets WDK IPsec offload , transversing NATs and NAPTs
- network address translators WDK IPsec offload
- network address port translators WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Traversing NATs and NAPTs with UDP-Encapsulated ESP Packets

\[The IPsec Task Offload feature is deprecated and should not be used.\]




Network address translators (NATs) and network address port translators (NAPTs) convert multiple private network addresses into one routeable IP public address and vice versa, thereby allowing many systems to share a single IP address. In this way, NATs and NAPTs help to alleviate the shortage of routeable IPv4 addresses.

However, NATs and NAPTs can cause problems with Internet protocol security (IPsec). Because NATs and NAPTs modify the IP header of a packet, they cause AH-protected packets to fail checksum validation. NAPTs, which modify TCP and UDP ports, cannot modify the ports in the encrypted TCP header of an ESP-protected packet.

UDP encapsulation solves this problem. In practice, UDP encapsulation is used only on ESP packets. A NAT or NAPT can modify the unencrypted IP and UDP headers of a UDP-encapsulated ESP packet without breaking ESP authentication and without being stymied by ESP encryption. For a detailed description of the UDP encapsulation of ESP packets, see [IPsec over NAT Justification for UDP Encapsulation](http://go.microsoft.com/fwlink/p/?linkid=9856).

Microsoft supports UDP encapsulation of ESP packets on port 4500. After IKE peers initiate negotiation on port 500, detect support for NAT-traversal, and detect a NAT or NAPT along the path, they can negotiate to "float" IKE and UDP-ESP traffic to port 4500. For more information about this negotiation, see [Negotiation of NAT-Traversal in the IKE](http://go.microsoft.com/fwlink/p/?linkid=9857).

Floating to port 4500 for NAT traversal provides the following benefits:

-   It bypasses "IPsec-aware" NATs or NAPTs that break UDP-ESP encapsulation on port 500.

-   It improves performance. The UDP encapsulation of ESP data packets is more efficient on port 4500 than on port 500. For more information, see [UDP-ESP Encapsulation Types](udp-esp-encapsulation-types.md).

To support UDP-ESP encapsulation, a miniport driver or the NIC (or both) must:

-   Be able to process ESP packets in the receive path, as described in [Offloading IPsec Tasks in the Receive Path](offloading-ipsec-tasks-in-the-receive-path.md).

-   Maintain a list of parser entries. A parser entry contains information that a NIC requires to parse incoming UDP-ESP packets on one or more security associations (SAs). For more information about parser entries, see [UDP-ESP SAs and Parser Entries](udp-esp-sas-and-parser-entries.md).

-   Maintain a list of SAs that the transport has offloaded to the NIC.

-   Support the following OIDs:
    -   [OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569809)
    -   [OID\_TCP\_TASK\_IPSEC\_DELETE\_UDPESP\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569811)

 

 





