---
title: Enumerating Ports
description: Enumerating Ports
ms.assetid: b38c5556-5124-45ea-af2f-4a4cd9313cc7
keywords:
- enumerating NDIS ports WDK NDIS
- ports WDK NDIS , OID requests
- NDIS ports WDK , OID requests
- OID requests WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Ports





NDIS protocol drivers and filter drivers can use an [OID\_GEN\_ENUMERATE\_PORTS](https://msdn.microsoft.com/library/windows/hardware/ff569583) OID query request to determine the characteristics of the active NDIS ports that are associated with an underlying miniport adapter. NDIS handles this OID, and miniport drivers do not receive this OID query.

If the query succeeds, NDIS provides the results of the query in an [**NDIS\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff566786) structure. The **NumberOfPorts** member of NDIS\_PORT\_ARRAY contains the number of active ports that are associated with the miniport adapter. The **Ports** member of NDIS\_PORT\_ARRAY contains a list of pointers to [**NDIS\_PORT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566791) structures. Each NDIS\_PORT\_CHARACTERISTICS structure defines the characteristics of a single port.

 

 





