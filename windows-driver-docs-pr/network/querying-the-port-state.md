---
title: Querying the Port State
description: Querying the Port State
ms.assetid: 3659d99b-1bbd-453c-8a56-b968d1748c1f
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





Overlying drivers can issue an [OID\_GEN\_PORT\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569624) OID query request to get the current state of the port that is specified in the **PortNumber** member of an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. NDIS handles this OID, and miniport drivers do not receive this OID query. NDIS receives port state information in the [**NDIS\_PORT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566791) structure.

The OID\_GEN\_PORT\_STATE OID is supported in NDIS 6.0 and later versions.

Overlying drivers should avoid using OID\_GEN\_PORT\_STATE when possible and should instead rely on the [**NDIS\_STATUS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567415) status indication. For more information about port-related status indications, see [Handling NDIS Ports Status Indications](handling-ndis-ports-status-indications.md).

If the OID\_GEN\_PORT\_STATE query succeeds, NDIS returns the port state information in an [**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800) structure.

 

 





