---
title: Packet Coalescing Receive Filters
description: Packet Coalescing Receive Filters
ms.assetid: B5C17A9D-A495-4A3D-B53E-B10F53C732D4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Packet Coalescing Receive Filters


Starting with NDIS 6.30, [NDIS receive filters](https://msdn.microsoft.com/library/windows/hardware/hh205393) have been extended to support packet coalescing. Each receive filter for packet coalescing defines the following:

-   A set of fields within the various protocol headers of a packet, such as the destination address of a media access control (MAC) header or destination port of a User Datagram Protocol (UDP) header.

-   The maximum time that a packet that matches a coalescing receive filter is coalesced by the network adapter. The adapter uses this value to set an expiration value on a hardware timer on the adapter. As soon as the timer expires, the adapter must interrupt the host so the miniport driver can process the coalesced packets.

    **Note**  As soon as the first packet that matches a receive filter is coalesced and the timer is started, the network adapter must coalesce additional packets that match receive filters without resetting and restarting the timer.

     

Overlying drivers, such as protocol and filter drivers, download the packet coalescing receive filters to the miniport driver by issuing object identifier (OID) set requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). For more information, see [Setting Packet Coalescing Receive Filters](setting-packet-coalescing-receive-filters.md).

Overlying drivers can also query the packet coalescing receive filters downloaded to the miniport driver. Overlying drivers do this by issuing OID method requests of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787) to the miniport driver. For more information, see [Querying Packet Coalescing Receive Filters](querying-packet-coalescing-receive-filters.md).

 

 





