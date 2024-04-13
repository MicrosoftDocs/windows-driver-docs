---
title: Handling Status Indications in a Protocol Driver
description: Handling Status Indications in a Protocol Driver
ms.date: 04/20/2017
---

# Handling Status Indications in a Protocol Driver





Protocol drivers must supply a [**ProtocolStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex) function that NDIS calls when an underlying driver reports status.

NDIS calls a protocol driver's *ProtocolStatusEx* function, after an underlying driver calls a status indication function ([**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus) or [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus)). For more information about indicating status from a miniport driver, see [Adapter Status Indications](miniport-adapter-status-indications.md).

For more information about indicating status from a filter driver, see [Filter Module Status Indications](filter-module-status-indications.md).

If the status indication is associated with an OID request, the underlying driver can set the **DestinationHandle** and **RequestId** members so that NDIS can provide the status indication to a specific protocol binding. For more information about OID requests, see [Protocol Driver OID Requests](protocol-driver-oid-requests.md).

 

