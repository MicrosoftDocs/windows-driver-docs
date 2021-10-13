---
title: Packet Coalescing Receive Filters
description: Packet Coalescing Receive Filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Packet Coalescing Receive Filters


Starting with NDIS 6.30, [NDIS receive filters](/windows-hardware/drivers/ddi/_netvista/) have been extended to support packet coalescing. Each receive filter for packet coalescing defines the following:

-   A set of fields within the various protocol headers of a packet, such as the destination address of a media access control (MAC) header or destination port of a User Datagram Protocol (UDP) header.

-   The maximum time that a packet that matches a coalescing receive filter is coalesced by the network adapter. The adapter uses this value to set an expiration value on a hardware timer on the adapter. As soon as the timer expires, the adapter must interrupt the host so the miniport driver can process the coalesced packets.

    **Note**  As soon as the first packet that matches a receive filter is coalesced and the timer is started, the network adapter must coalesce additional packets that match receive filters without resetting and restarting the timer.

     

Overlying drivers, such as protocol and filter drivers, download the packet coalescing receive filters to the miniport driver by issuing object identifier (OID) set requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md). For more information, see [Setting Packet Coalescing Receive Filters](specifying-a-packet-coalescing-receive-filter.md).

Overlying drivers can also query the packet coalescing receive filters downloaded to the miniport driver. Overlying drivers do this by issuing OID method requests of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) to the miniport driver. For more information, see [Querying Packet Coalescing Receive Filters](querying-packet-coalescing-receive-filters.md).

 

