---
title: Filter Module OID Requests
description: Filter Module OID Requests
ms.assetid: 6de5ec1c-8e12-4f50-8708-ec136cafd9c2
keywords:
- filter modules WDK networking , OID requests
- filter drivers WDK networking , OID requests
- NDIS filter drivers WDK , OID requests
- OIDs WDK networking , filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module OID Requests





NDIS defines object identifier (OID) values to identify adapter parameters, which include operating parameters such as device characteristics, configurable settings and statistics. For more information about OIDs, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

Filter drivers can query or set the operating parameters of underlying drivers or filter the OID requests of overlying drivers.

NDIS also provides a [direct OID request interface for NDIS 6.1](direct-oid-request-interface-in-ndis-6-1.md) and later filter drivers. The *direct OID request path* supports OID requests that are queried or set frequently. For example, the IPsec offload version 2 (IPsecv2) interface provides the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID for direct OID requests. The direct OID request interface is optional for NDIS drivers.

For NDIS 6.81 and later filter drivers, NDIS provides a [Synchronous OID Request Interface](synchronous-oid-request-interface-in-ndis-6-80.md). The *Synchronous OID request path* supports OIDs that require synchronization or OIDs that should not be queued by filter drivers, such as [RSSv2](receive-side-scaling-version-2-rssv2-in-ndis-6-80.md) OIDs. The Synchronous OID Request Interface is optional for NDIS drivers but is required if the filter driver advertises support for RSSv2.

The following topics provide more information about filter driver OID requests:

[Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md)

[Generating OID Requests from an NDIS Filter Driver](generating-oid-requests-from-an-ndis-filter-driver.md)

[Filter Module Direct OID Requests](filter-module-direct-oid-requests.md)

[Filter Module Synchronous OID Requests](filter-module-synchronous-oid-requests.md)

 

 





