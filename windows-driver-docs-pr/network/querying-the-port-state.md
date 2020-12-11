---
title: Querying the Port State
description: Querying the Port State
keywords:
- port states WDK NDIS
- querying NDIS port states
- ports WDK NDIS , OID requests
- NDIS ports WDK , OID requests
- OID requests WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the Port State





Overlying drivers can issue an [OID\_GEN\_PORT\_STATE](./oid-gen-port-state.md) OID query request to get the current state of the port that is specified in the **PortNumber** member of an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. NDIS handles this OID, and miniport drivers do not receive this OID query. NDIS receives port state information in the [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structure.

The OID\_GEN\_PORT\_STATE OID is supported in NDIS 6.0 and later versions.

Overlying drivers should avoid using OID\_GEN\_PORT\_STATE when possible and should instead rely on the [**NDIS\_STATUS\_PORT\_STATE**](./ndis-status-port-state.md) status indication. For more information about port-related status indications, see [Handling NDIS Ports Status Indications](handling-ndis-ports-status-indications.md).

If the OID\_GEN\_PORT\_STATE query succeeds, NDIS returns the port state information in an [**NDIS\_PORT\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_state) structure.

 

