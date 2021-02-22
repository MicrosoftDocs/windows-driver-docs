---
title: Querying 64-Bit Statistics OIDs
description: Querying 64-Bit Statistics OIDs
keywords:
- statistics OIDs WDK networking
- 64-bit statistics OIDs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying 64-Bit Statistics OIDs


All miniport drivers that are 1 Gigabyte per second (Gbps) and faster must support 64-bit counters for certain statistics OIDs. All 100 Megabytes per second (Mbps) and faster miniport drivers should support 64-bit counters for such OIDs. For more information about statistics OIDs for connectionless miniport drivers, see [General Statistics](./ndis-general-statistics-oids.md). For more information about such OIDs for connection-oriented miniport drivers, see [General Statistics for Connection-Oriented Miniport Drivers](./general-statistics-oids-for-connection-oriented-miniport-drivers.md).

A requester that queries a statistics OID sets NDIS\_OID\_REQUEST **InformationBufferLength** to 4 (bytes) to indicate a 32-bit statistics request or to 8 (bytes) to indicate a 64-bit statistics request. In its response, the miniport driver sets NDIS\_OID\_REQUEST **BytesNeeded** to the size of the statistics value that the miniport driver supports (4 for 32-bits or 8 for 64-bits). The miniport driver sets NDIS\_OID\_REQUEST **BytesWritten** to the smaller of the **InformationBufferLength** value and the size of statistics that the miniport driver supports.

The following sections describe how a miniport driver that supports 64-bit statistics OIDs responds to queries of such OIDs.

### <a href="" id="-64-bit-query-of-a-64-bit-value"></a>64-bit query of a 64-bit value

NDIS\_OID\_REQUEST **InformationBufferLength** is greater than or equal to 8.

The miniport driver:

-   Returns the 64-bit value in the information buffer.

-   Sets NDIS\_OID\_REQUEST **BytesWritten** to 8.

-   Returns NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) or [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function.

### <a href="" id="-32-bit-query-of-a-64-bit-value"></a>32-bit query of a 64-bit value

NDIS\_OID\_REQUEST **InformationBufferLength** is greater to or equal to 4 and less than 8.

The miniport driver:

-   Returns, in the information buffer, the lower 32 bits of the 64-bit value.

-   Sets NDIS\_OID\_REQUEST **BytesWritten** to 4.

-   Sets NDIS\_OID\_REQUEST **BytesNeeded** to 8.

-   Returns NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) or [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function.

### Invalid-length query of a 64-bit value

NDIS\_OID\_REQUEST **InformationBufferLength** is less than 4.

The miniport driver:

-   Does not return any value in the information buffer.

-   Sets NDIS\_OID\_REQUEST **BytesWritten** to 0.

-   Sets NDIS\_OID\_REQUEST **BytesNeeded** to 8.

-   Returns NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) or [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function.

 

