---
title: Protocol Driver OID Requests
description: Protocol Driver OID Requests
ms.assetid: ab664e75-d17d-4664-8c37-91fd651d23c2
keywords:
- protocol drivers WDK networking , OID requests
- OIDs WDK networking , protocol drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver OID Requests





NDIS defines object identifier (OID) values to identify adapter parameters which include operating parameters such as device characteristics, configurable settings and statistics. For more information about OIDs, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

Protocol drivers can query or set the operating parameters of underlying drivers.

NDIS also provides a [direct OID request interface for NDIS 6.1](direct-oid-request-interface-in-ndis-6-1.md) and later protocol drivers. The *direct OID request path* supports OID requests that are queried or set frequently. For example, the IPsec offload version 2 (IPsecv2) interface provides the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID for direct OID requests. The direct OID request interface is optional for NDIS drivers.

The following topics provide more information about protocol driver OID requests:

[Generating OID Requests from an NDIS Protocol Driver](generating-oid-requests-from-an-ndis-protocol-driver.md)

[Protocol Driver Direct OID Requests](protocol-driver-direct-oid-requests.md)

[Protocol Driver Synchronous OID Requests](protocol-driver-synchronous-oid-requests.md)

 

 





