---
title: Connection-Oriented Timing Features
description: Connection-Oriented Timing Features
keywords:
- connection-oriented NDIS WDK , timing features
- CoNDIS WDK networking , timing features
- timing features WDK CoNDIS
- clocks
- local clocks WDK CoNDIS
ms.date: 04/20/2017
---

# Connection-Oriented Timing Features





Connection-oriented NDIS supports using a NIC's local time for scheduling the transmission of packets and for time-stamping send and receive packets.

**Note**  These connection-oriented timing features are optional. These features are not supported by all CoNDIS NICs.

 

A connection-oriented protocol driver can call [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) to query the local timing capabilities of a connection-oriented miniport driver or an MCM driver with [OID\_GEN\_CO\_GET\_TIME\_CAPS](./oid-gen-co-get-time-caps.md). In response to such a query, the miniport driver or MCM driver returns information about:

-   Whether there is a readable clock on the NIC.

-   Whether the NIC derives its time from the network connection.

-   The precision of the local clock.

-   Whether the NIC can timestamp received packets with its local time.

-   Whether the NIC can schedule a send packet for transmission according to its local time.

-   Whether the NIC can timestamp transmitted packets with its local time.

To obtain a NIC's local time, a connection-oriented protocol can call **NdisCoOidRequest** to query a connection-oriented miniport driver or MCM driver with [OID\_GEN\_CO\_GET\_NETCARD\_TIME](./oid-gen-co-get-netcard-time.md). The connection-oriented miniport driver or MCM driver synchronously returns its local time, which the connection-oriented protocol can then use to schedule the transmission of packets.

Timing information for a send or receive packet is contained in the packet's out-of-band (OOB) data. For more information, see [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list).

 

