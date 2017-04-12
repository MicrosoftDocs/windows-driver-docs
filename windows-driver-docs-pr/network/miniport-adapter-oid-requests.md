---
title: Miniport Adapter OID Requests
description: Miniport Adapter OID Requests
ms.assetid: c3769b1e-c84a-499d-9f93-17a31441a477
keywords: ["OIDs WDK networking , miniport adapter requests", "miniport adapters WDK networking , OID requests", "adapters WDK networking , OID requests", "object identifiers WDK networking"]
---

# Miniport Adapter OID Requests


## <a href="" id="ddk-oid-requests-for-an-adapter-ng"></a>


NDIS defines object identifier (OID) values to identify miniport adapter parameters, which include operating parameters such as device characteristics, configurable settings and statistics. For more information about OIDs, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

NDIS also provides a [direct OID request interface for NDIS 6.1](direct-oid-request-interface-in-ndis-6-1.md) and later miniport drivers. The *direct OID request path* supports OID requests that are queried or set frequently. The direct OID request interface is optional for NDIS drivers.

The following topics provide more information about miniport driver OID requests:

[Handling OID Requests In a Miniport Adapter](handling-oid-requests-in-a-miniport-adapter.md)

[Miniport Adapter Direct OID Requests](miniport-adapter-direct-oid-requests.md)

 

 





