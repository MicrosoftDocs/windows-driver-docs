---
title: Overview of Packet Coalescing
description: Overview of Packet Coalescing
ms.date: 04/20/2017
---

# Overview of Packet Coalescing


Certain IP version 4 (IPv4) and IP version 6 (IPv6) network protocols involve the transmission of packets to broadcast or multicast addresses. These packets are received by multiple hosts in the IPv4/IPv6 subnet. In most cases, the host that receives these packets does not do anything with these packets. Therefore, the reception of these unwanted multicast or broadcast packets causes unnecessary processing and power consumption to occur within the receiving host.

For example, host A sends a multicast Link-local Multicast Name Resolution (LLMNR) request on an IPv6 subnet to resolve host B's name. Except for host A, this LLMNR request is received by all hosts on the subnet. Except for host B, the TCP/IP protocol stack that runs on the other hosts inspects the packet and determines that the packet is not intended for it. Therefore, the protocol stack rejects the packet and calls [**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists) to return the packet to the miniport driver.

Starting with NDIS 6.30, network adapters can support NDIS packet coalescing. By reducing the number of receive interrupts through the coalescing of random broadcast or multicast packets, the processing overhead and power consumption is significantly reduced on the system.

Packet coalescing involves the following steps:

1.  Overlying drivers, such as the TCP/IP protocol stack, define NDIS receive filters that are used to screen broadcast and multicast packets. The overlying drivers download these filters to the underlying miniport driver that supports packet coalescing. Once downloaded, the miniport driver configures the network adapter with the packet coalescing receive filters.

    For more information about these filters, see [Packet Coalescing Receive Filters](packet-coalescing-receive-filters.md).

2.  Received packets that match receive filters are cached, or *coalesced*, on the network adapter. The adapter does not generate a receive interrupt for coalesced packets. Instead, the adapter interrupts the host when another hardware event occurs.

    When this interrupt is generated, the adapter must indicate a receive event with the interrupt. This allows the network adapter to process coalesced packets that were received by the network adapter.

    For example, the network adapter that supports packet coalescing can generate a receive interrupt when one of the following events occur:

    -   The expiration of a hardware timer whose expiration time is set to a maximum coalescing delay value of the matching receive filter.

    -   The available space within the hardware coalescing buffer reaches an adapter-specified low-water mark.

    -   A packet is received that does not match a coalescing filter.

    -   Another interrupt event, such as a send completion event, has occurred.

    For more information about this process, see [Handling Packet Coalescing Receive Filters](handling-packet-coalescing-receive-filters.md).

The following points apply to the support of packet coalescing by NDIS:

-   NDIS supports packet coalescing for packets received on the default NDIS port (port 0) assigned to the physical network adapter. NDIS does not support packet coalescing on NDIS ports that are assigned to virtual network adapters. For more information, see [NDIS Ports](overview-of-ndis-ports.md).

-   NDIS supports packet coalescing for packets received on the default receive queue of the network adapter. This receive queue has an identifier of NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.
