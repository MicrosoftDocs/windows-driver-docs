---
title: OID Request Operations in a Protocol Driver
description: OID Request Operations in a Protocol Driver
keywords:
- protocol drivers WDK networking , OID requests
- NDIS protocol drivers WDK , OID requests
- OID requests WDK networking
- OIDs WDK networking , protocol drivers
ms.date: 04/20/2017
---

# OID Request Operations in a Protocol Driver





There are two different interfaces for OID request operations in a protocol driver. NDIS protocol drivers with a connectionless lower edge call the [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) function to initiate an OID request. An NDIS protocol driver with a connectionless lower edge must supply a [**ProtocolOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_oid_request_complete) function. NDIS calls *ProtocolOidRequestComplete* when the underlying drivers complete a pending OID request. For more information about OID requests in connectionless protocol drivers, see [Protocol Driver OID Requests](protocol-driver-oid-requests.md).

Connection-oriented NDIS (CoNDIS) protocol drivers call the [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) function to initiate an OID request. A CoNDIS protocol driver must supply a [**ProtocolCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete) function. NDIS calls *ProtocolOidRequestComplete* when the underlying drivers complete a pending OID request. For more information OID requests in connection-oriented protocol drivers, see [Connection-Oriented Operations](connection-oriented-operations-performed-by-clients.md).

For more information about OIDs, see [NDIS OIDs](/windows-hardware/drivers/ddi/_netvista/).

 

