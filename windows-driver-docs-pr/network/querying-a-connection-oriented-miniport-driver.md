---
title: Querying a Connection-Oriented Miniport Driver
description: Querying a Connection-Oriented Miniport Driver
keywords:
- connection-oriented drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying a Connection-Oriented Miniport Driver





To query information objects that a connection-oriented miniport driver maintains, a bound protocol calls [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) and passes an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure that specifies the object (OID) that is being queried and that provides a buffer into which NDIS eventually writes the requested information. The call to **NdisCoOidRequest** causes NDIS to call the miniport driver's [*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function, which returns the requested information to NDIS. *MiniportCoOidRequest* can complete synchronously or asynchronously with a call to [**NdisCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequestcomplete).

NDIS can also call a miniport driver's [*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function on its own behalf—for example, after the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function has returned NDIS\_STATUS\_SUCCESS—to query the miniport driver's capabilities, status, or statistics. The following diagram illustrates querying a connection-oriented miniport driver.

![diagram illustrating querying a connection-oriented miniport driver.](images/fig5-3.png)

A connection-oriented miniport driver must be able to provide information about a global basis for all virtual connections (VCs) for a particular NIC and also on a per-VC basis. For example, if a non-**NULL** *NdisVcHandle* is supplied to [*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) for a query of [OID\_GEN\_CO\_RCV\_CRC\_ERROR](./oid-gen-co-rcv-crc-error.md), the miniport driver returns the number of CRC errors that were encountered in all receives on the specified VC. For the same request with a **NULL** *NdisVcHandle*, the miniport driver returns the total number of CRC errors that are encountered for all incoming receives through a NIC.

The following list contains the set of mandatory general operational OIDs for connection-oriented miniport drivers:

[OID\_GEN\_CO\_SUPPORTED\_LIST](./oid-gen-co-supported-list.md)

[OID\_GEN\_CO\_HARDWARE\_STATUS](./oid-gen-co-hardware-status.md)

[OID\_GEN\_CO\_MEDIA\_SUPPORTED](./oid-gen-co-media-supported.md)

[OID\_GEN\_CO\_MEDIA\_IN\_USE](./oid-gen-co-media-in-use.md)

[OID\_GEN\_CO\_LINK\_SPEED](./oid-gen-co-link-speed.md)

[OID\_GEN\_CO\_VENDOR\_ID](./oid-gen-co-vendor-id.md)

[OID\_GEN\_CO\_VENDOR\_DESCRIPTION](./oid-gen-co-vendor-description.md)

[OID\_GEN\_CO\_VENDOR\_DRIVER\_VERSION](./oid-gen-co-vendor-driver-version.md)

[OID\_GEN\_CO\_DRIVER\_VERSION](./oid-gen-co-driver-version.md)

[OID\_GEN\_CO\_MAC\_OPTIONS](./oid-gen-co-mac-options.md)

[OID\_GEN\_CO\_MEDIA\_CONNECT\_STATUS](./oid-gen-co-media-connect-status.md)

[OID\_GEN\_CO\_MINIMUM\_LINK\_SPEED](./oid-gen-co-minimum-link-speed.md)

The miniport driver's [*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function must be prepared to respond to queries or sets, as appropriate, to any of the preceding OIDs.

When [*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) is called with OID\_GEN\_CO\_MAC\_OPTIONS, it must return a bitmask that specifies the optional operations that the miniport driver performs. The set of flags includes:

-   NDIS\_MAC\_OPTION\_NO\_LOOPBACK. If this flag is set, the miniport driver does not loopback a packet that is passed to [**MiniportCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_send_net_buffer_lists) that is directed to a receiver on the same computer and that the miniport driver expects NDIS to perform the loopback. If NDIS performs the loopback of a packet, the packet is not passed down to the miniport driver. A miniport driver always sets this flag unless a NIC performs hardware loopbacks.

-   NDIS\_MAC\_ETOX\_INDICATION. If this flag is set, the miniport driver indicates that a send is complete only after the NIC transmits the packet.

A miniport driver must never use the NDIS\_MAC\_OPTION\_RESERVED flag, which is reserved for NDIS internal use.

[*MiniportCoOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) will also be queried with a media-specific OID to determine the NIC's current address.

For more information, see [OIDs for Connection-Oriented Call Managers and Clients](./oids-for-connection-oriented-call-managers-and-clients.md) and [General Objects](/previous-versions/windows/hardware/network/ff546510(v=vs.85)).

 

