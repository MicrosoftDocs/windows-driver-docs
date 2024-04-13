---
title: Enumerating Ports
description: Enumerating Ports
keywords:
- enumerating NDIS ports WDK NDIS
- ports WDK NDIS , OID requests
- NDIS ports WDK , OID requests
- OID requests WDK NDIS ports
ms.date: 04/20/2017
---

# Enumerating Ports





NDIS protocol drivers and filter drivers can use an [OID\_GEN\_ENUMERATE\_PORTS](./oid-gen-enumerate-ports.md) OID query request to determine the characteristics of the active NDIS ports that are associated with an underlying miniport adapter. NDIS handles this OID, and miniport drivers do not receive this OID query.

If the query succeeds, NDIS provides the results of the query in an [**NDIS\_PORT\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_array) structure. The **NumberOfPorts** member of NDIS\_PORT\_ARRAY contains the number of active ports that are associated with the miniport adapter. The **Ports** member of NDIS\_PORT\_ARRAY contains a list of pointers to [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structures. Each NDIS\_PORT\_CHARACTERISTICS structure defines the characteristics of a single port.

 

