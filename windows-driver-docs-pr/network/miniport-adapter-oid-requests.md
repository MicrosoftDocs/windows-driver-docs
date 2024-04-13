---
title: Miniport Adapter OID Requests
description: Miniport Adapter OID Requests
keywords:
- OIDs WDK networking , miniport adapter requests
- miniport adapters WDK networking , OID requests
- adapters WDK networking , OID requests
- object identifiers WDK networking
ms.date: 04/20/2017
---

# Miniport Adapter OID Requests





NDIS defines object identifier (OID) values to identify miniport adapter parameters, which include operating parameters such as device characteristics, configurable settings and statistics. For more information about OIDs, see [NDIS OIDs](/windows-hardware/drivers/ddi/_netvista/).

For NDIS 6.1 and later miniport drivers, NDIS provides a [Direct OID Request Interface](direct-oid-request-interface-in-ndis-6-1.md). The *Direct OID request path* supports OID requests that are queried or set frequently. The Direct OID Request Interface is optional for NDIS drivers.

For NDIS 6.80 and later miniport drivers, NDIS provides a [Synchronous OID Request Interface](synchronous-oid-request-interface-in-ndis-6-80.md). The *Synchronous OID request path* supports OIDs that require synchronization or OIDs that should not be queued by filter drivers, such as [RSSv2](receive-side-scaling-version-2-rssv2-in-ndis-6-80.md) OIDs. The Synchronous OID Request Interface is optional for NDIS drivers but is required if the miniport driver advertises support for RSSv2.

The following topics provide more information about miniport driver OID requests:

[Handling OID Requests In a Miniport Adapter](handling-oid-requests-in-a-miniport-adapter.md)

[Miniport Adapter OID Request Serialization](miniport-adapter-oid-request-serialization.md)

[Miniport Adapter Direct OID Requests](miniport-adapter-direct-oid-requests.md)

[Miniport Adapter Synchronous OID Requests](miniport-adapter-synchronous-oid-requests.md)
