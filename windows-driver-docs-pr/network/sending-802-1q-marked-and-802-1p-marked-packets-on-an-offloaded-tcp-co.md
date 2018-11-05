---
title: Sending marked packets on an offloaded TCP connection
description: Sending 802.1Q-Marked and 802.1p-Marked Packets on an Offloaded TCP Connection
ms.assetid: 4c16d5af-33e2-4cce-b9e8-d2b60afa0986
keywords:
- 802.1Q and 802.1p information WDK TCP chimney offload , sending marked packets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending 802.1Q-Marked and 802.1p-Marked Packets on an Offloaded TCP Connection


\[The TCP chimney offload feature is deprecated and should not be used.\]




When processing a send packet on an offloaded TCP connection, an offload target uses the values of the **VlanId** and **UserPriority** members to determine whether an IEEE 802.3ac packet header, referred to as a [tag header](https://msdn.microsoft.com/library/windows/hardware/ff564233), should be included. The IEEE 802.3ac header contains a VLAN identifier value, a priority value, and a bit called CFI, which is always set to zero.

An offload target uses the following algorithm to determine whether to insert an 802.3ac header into a packet and what VLAN identifier and priority values to supply in the header:

-   If the neighbor **VlanId** is zero:
    -   If the value of **UserPriority** for the TCP connection is zero, the offload target does not insert a tag header into the packet.
    -   If the value of **UserPriority** for the TCP connection is nonzero, the offload target inserts a tag header into the packet. In this tag header, the offload target specifies a VLAN identifier of zero and a priority value that is equal to the value of **UserPriority** for the TCP connection.

<!-- -->

-   If the neighbor **VlanId** is nonzero, the offload target inserts a tag header into the packet. In this tag header, the offload target specifies a VLAN identifier that is equal to the neighbor **VlanId** and a priority value that is equal to the value of **UserPriority** for the TCP connection.

 

 





