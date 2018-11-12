---
title: Protocol Offloads for NDIS Power Management
description: Protocol Offloads for NDIS Power Management
ms.assetid: 191aa59d-1772-4824-ad15-e813f2e154e0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Offloads for NDIS Power Management





NDIS 6.20 and later versions of NDIS support protocol offloads for NDIS power management. For example, NDIS can offload the handling of Address Resolution Protocol (ARP) requests to a network adapter. Some applications use periodic ARP request packets to discover and ensure the presence of a host on the network. These applications send the ARP requests even when there is no current need to send data to the host. Such ARP requests wake up the host and waste power when there is nothing for the host to do.

**Note**   In Windows 7, the power management offload functionality is enabled only when all protocol and filter drivers that are bound to the miniport adapter support NDIS 6.20 and later versions. In Windows 8, the power management offload functionality is enabled if the miniport adapter supports it, regardless of the protocol and filter driver versions.

 

**Note**  If an incoming packet matches both an offloaded protocol and a pattern (for example, because of a configuration error), the network adapter responds to the packet and wakes up the computer.

 

To minimize spurious wake ups, NDIS protocol drivers attempt to offload the response to commonly used network requests to the hardware. Some network protocols require the host to periodically advertise certain information. When a network adapter responds to ARP requests, or takes over protocol specific periodic advertisements without waking up the system for processing these requests, many spurious wake-up events can be avoided.

There are three types of low power protocol offloads:

-   IPv4 ARP

-   IPv6 Neighbor Solicitation (NS)

-   IEEE 802.11 robust secure network (RSN) 4-way and 2-way handshake

NDIS allows multiple protocol drivers to offload different protocols to a network adapter. To ensure that the correct set of protocols is offloaded when the number of requested protocol offloads is higher than the number that the network adapter can support, protocol drivers assign a priority to each protocol offload. When NDIS cannot add a new high-priority protocol offload because the network adapter is out of resources, NDIS might delete the lower priority offloads.

For more information about managing protocol offloads, see [Adding and Deleting Low Power Protocol Offloads](adding-and-deleting-low-power-protocol-offloads.md).

 

 





