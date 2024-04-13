---
title: NDIS 6.20 Updates to NDIS 6.1 Features
description: NDIS 6.20 Updates to NDIS 6.1 Features
keywords:
- NDIS 6.20 WDK , updates to NDIS 6.1 features
ms.date: 03/02/2023
---

# NDIS 6.20 Updates to NDIS 6.1 Features





NDIS 6.1 added the following interfaces to NDIS 6.0:

[Header-Data Split](header-data-split-in-ndis-6-1.md)

[Direct OID Requests](direct-oid-request-interface-in-ndis-6-1.md)

[IPsec Task Offload Version 2](ipsec-task-offload-version-2-in-ndis-6-1.md)

[NetDMA 1.1 and 2.0](netdma-updates-in-ndis-6-1.md)

For more information about NDIS 6.1, see [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md).

NDIS 6.1 also includes updates to support MSI-X dynamic configuration for receive side scaling (RSS). For more information about NDIS 6.1 changes in RSS, see [NDIS MSI-X](ndis-msi-x.md). RSS is updated in NDIS 6.20 to provide support for more than 64 processors.

The [direct OID request interface](direct-oid-request-interface-in-ndis-6-1.md) is optional for NDIS 6.1 drivers but it is mandatory for NDIS 6.20 miniport drivers.

After NDIS 6.20 [IPsec task offload version 1](background-reading-on-ipsec.md) will not be supported. All drivers that support IPsec task offload should be updated to support [IPsec task offload version 2](./introduction-to-ipsec-offload-version-2.md).

NetDMA 1.1 and 2.0 were introduced with NDIS 6.1. NetDMA 2.1 is introduced with NDIS 6.20 to provide support for more than 64 processors.

 

