---
title: Querying or Setting Information
description: Querying or Setting Information
ms.assetid: 39bd9846-7c7e-4b93-8060-4da9c66ac591
keywords:
- querying connection-oriented information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying or Setting Information





CoNDIS protocol drivers and NDIS can send OID requests to underlying drivers. CoNDIS protocol drivers and miniport call managers (MCMs) can also send OID requests to other protocol drivers.

A connection-oriented client or call manager calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) to query or set information that is maintained by another protocol driver on a binding or by the underlying miniport driver.

Before it calls **NdisCoOidRequest**, a client or call manager allocates a buffer for its request and initializes an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. This structure specifies the type of request (query or set), identifies the information (OID) that is being queried or set, and points to buffers that are used for passing OID data.

If the connection-oriented client or call manager passes a valid *NdisAfHandle* (see [Address Families](address-families.md)), NDIS calls the [**ProtocolCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff570254) function of each protocol driver on the binding.

NDIS defines object identifier (OID) values to identify adapter parameters, including operating parameters such as device characteristics, configurable settings, and statistics. For more information about OIDs, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

This section includes the following topics:

[CoNDIS Miniport Driver OID Requests](condis-miniport-driver-oid-requests.md)

[CoNDIS Protocol Driver OID Requests](condis-protocol-driver-oid-requests.md)

[CoNDIS MCM OID Requests](condis-mcm-oid-requests.md)

 

 





