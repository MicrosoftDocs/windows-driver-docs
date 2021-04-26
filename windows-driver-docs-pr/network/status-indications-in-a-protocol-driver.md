---
title: Status Indications in a Protocol Driver
description: Status Indications in a Protocol Driver
keywords:
- protocol drivers WDK networking , status indications
- NDIS protocol drivers WDK , status indications
- status indications WDK networking , protocol drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Status Indications in a Protocol Driver





There are two different interfaces for status indications in a protocol driver. An NDIS protocol driver with a connectionless lower edge is required to supply a [**ProtocolStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex) function. NDIS calls *ProtocolStatusEx* when an underlying connectionless miniport driver calls [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to report a change in its hardware status. NDIS calls *ProtocolStatusEx* when the status change begins. For more information about status indications in connectionless protocol drivers, see [Handling Status Indications in a Protocol Driver](handling-status-indications-in-a-protocol-driver.md).

A connection-oriented protocol driver must supply a [**ProtocolCoStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_status_ex) function. NDIS calls *ProtocolCoStatusEx* when an underlying connection-oriented miniport driver calls [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex) to report a change in its hardware status. NDIS calls *ProtocolCoStatusEx* when the status change begins. For more information about status indications in connection-oriented protocol drivers, see [Connection-Oriented Operations](connection-oriented-operations-performed-by-clients.md)

For a complete list of the possible status indications, see [Status Indications](/windows-hardware/drivers/ddi/_netvista/).

 

