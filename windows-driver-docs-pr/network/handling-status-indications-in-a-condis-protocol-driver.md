---
title: Handling Status Indications in a CoNDIS Protocol Driver
description: Handling Status Indications in a CoNDIS Protocol Driver
keywords:
- protocol drivers WDK networking , CoNDIS
- NDIS protocol drivers WDK , CoNDIS
ms.date: 03/02/2023
---

# Handling Status Indications in a CoNDIS Protocol Driver





Protocol drivers must supply a [**ProtocolCoStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_status_ex) function that NDIS calls when an underlying driver reports status.

NDIS calls a protocol driver's *ProtocolCoStatusEx* function after an underlying driver calls a status indication function (for example, [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex)). For more information about indicating status from a miniport driver, see [CoNDIS Miniport Driver Status Indications](condis-miniport-driver-status-indications.md).

If the status indication is associated with an OID request, the underlying driver can set the **DestinationHandle** and **RequestId** members of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure that contains the status information so that NDIS can provide the status indication to a specific protocol binding. For more information about OID requests, see [CoNDIS Protocol Driver OID Requests](condis-protocol-driver-oid-requests.md).

 

