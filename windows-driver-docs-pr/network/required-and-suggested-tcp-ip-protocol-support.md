---
title: Required and Suggested TCP/IP Protocol Support
description: Required and Suggested TCP/IP Protocol Support
ms.assetid: ffc0d131-18f1-4a20-ad78-bbfe7c02a052
keywords:
- RFC compliance WDK TCP chimney offload
- IETF RFC compliance WDK TCP chimney offload
- task-offload engine NIC WDK TCP chimney offload
- TOE NIC WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required and Suggested TCP/IP Protocol Support


\[The TCP chimney offload feature is deprecated and should not be used.\]

Like the host TCP/IP stack, a TOE NIC's TCP/IP stack must conform to the requirements of applicable IETF standard RFCs:

-   The TOE NIC's TCP/IP stack must conform to the following transport layer RFCs: 793, 813, 1122, 1191, 1323, 2012, 2581, and 2988. The vendor should review RFC 2525 to determine whether the TOE NIC's TCP/IP stack suffers from any common TCP implementation flaws.

-   The TCP/IP stack of a TOE NIC that supports IPv4 must conform to the following IPv4 network layer RFCs: 791, 894, 1042, and 1122.

-   The TCP/IP stack of a TOE NIC that supports IPv6 must conform to the following IPv6 network layer RFCs: 1752, 1981, 2374, 2460, 2461, 2675, 2711, 3122, and 3513.

In particular, a TOE NIC must:

-   Follow the TCP connection state diagram and perform state transitions, as specified in the RFC 793 sections 3.2, 3.4, and 3.5.

-   Do no window probing and respond to it correctly, as specified in the RFC 793 section 3.7.

-   Implement delayed acknowledgment (ACK), as specified in RFC 813 and RFC 1122 section 4.2.3.2.

-   Implement slow start, fast retransmit, and congestion avoidance algorithms, as specified in RFC 1122 sections 4.2.2.15 and 4.2.2.21 and updated in RFC 2581.

-   Implement half-closed, as specified in RFC 793 sections 3.5 and RFC 1122 section 4.2.2.13.

-   Not implement reassembly of IP datagrams, as specified in RFC 791 section 3.2 and RFC 1122 section 3.3.2.

-   Implement the Nagle algorithm in data communication, as specified in RFC 1122 section 4.2.3.4.

-   Implement retransmission queues, as specified in RFC 1122 section 4.2.2.15.

-   Implement algorithms for computing retransmission time-out, as specified in RFC 1122 section 4.2.3.1 and updated in RFC 2988.

-   Be capable of queuing out-of-order TCP segments, as specified in RFC 793 Section 3.9 and RFC 1122 Section 4.2.2.20.

-   Implement Protection Against Wrapping Sequence numbers (PAWS), as specified in RFC 1323 section 4.

-   Support TCP timestamps and windows scaling, as specified in RFC 1323.

-   Set the Don't Fragment (DF) bit in the IPv4 header when sending IPv4 datagrams.

-   Deliver Internet Control Message Protocol (ICMP) messages for path maximum transmission unit (MTU) support to the host stack for processing.

-   If it supports configurable medium access control (MAC) addresses, set the remote MAC address, as updated by the host TCP stack. (For more information about setting the MAC address, see the description of the **DlSourceAddress** member of the [**NEIGHBOR\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff568324) structure). See RFCs 792, 826, 1256, and 2461 for a description of how destination MAC addresses can change after the host TCP stack receives Address Resolution Protocol (ARP), Neighbor Advertisement, Router Advertisement, and Redirect messages.

-   If it uses the PCI bus, support 64-bit addresses. 64-bit data support is not required.

A TOE NIC can optionally support the selective acknowledgment (SACK) option for both transmit and receive operations. If the NIC does not support the SACK option, it must be able to ignore the SACK option in a TCP segment and process the rest of the segment normally.

 

 





