---
title: Processing UDP-Encapsulated ESP Packets
description: Processing UDP-Encapsulated ESP Packets
keywords:
- UDP-encapsulated ESP packets WDK IPsec offload , processing
ms.date: 04/20/2017
---

# Processing UDP-Encapsulated ESP Packets

\[The IPsec Task Offload feature is deprecated and should not be used.\]




When a NIC receives a UDP-encapsulated packet on port 4500, it checks whether the packet is an IKE (control) packet or an ESP (data) packet. For a description of the UDP encapsulation types for IKE and ESP packets, see [UDP-ESP Encapsulation Types](udp-esp-encapsulation-types.md).

-   If the packet is an IKE packet, the NIC passes the packet to the miniport driver without further IPsec-related processing.

-   If the packet is an ESP packet, the NIC checks whether the packet's inbound SA (or SAs in the case of a transport-over-tunnel packet) is currently offloaded to the NIC.
    -   If the inbound SAs are not currently offloaded to the NIC, the NIC passes the packet to the miniport driver without further IPsec-related processing.
    -   If the inbound SAs are currently offloaded to the NIC, the NIC parses the packet by using the encapsulation type specified by the parser entry that is associated with the SAs. The NIC then processes the ESP payloads in the packet, as described in [Offloading IPsec Tasks in the Receive Path](offloading-ipsec-tasks-in-the-receive-path.md).

If the incoming ESP packet is a UDP-encapsulated transport-over-tunnel packet, as described in [UDP-ESP Encapsulation Types](udp-esp-encapsulation-types.md), the NIC first decrypts the ESP payload of tunnel-mode portion of the packet, which is not UDP-encapsulated. Then the NIC processes the UDP-encapsulated tunnel-mode portion of the packet.

 

 





