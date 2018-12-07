---
title: OID Request Operations in a Protocol Driver
description: OID Request Operations in a Protocol Driver
ms.assetid: 767252a2-98de-4df2-89dc-ee48b2c7ca9d
keywords:
- protocol drivers WDK networking , OID requests
- NDIS protocol drivers WDK , OID requests
- OID requests WDK networking
- OIDs WDK networking , protocol drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OID Request Operations in a Protocol Driver





There are two different interfaces for OID request operations in a protocol driver. NDIS protocol drivers with a connectionless lower edge call the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function to initiate an OID request. An NDIS protocol driver with a connectionless lower edge must supply a [**ProtocolOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570264) function. NDIS calls *ProtocolOidRequestComplete* when the underlying drivers complete a pending OID request. For more information about OID requests in connectionless protocol drivers, see [Protocol Driver OID Requests](protocol-driver-oid-requests.md).

Connection-oriented NDIS (CoNDIS) protocol drivers call the [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function to initiate an OID request. A CoNDIS protocol driver must supply a [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255) function. NDIS calls *ProtocolOidRequestComplete* when the underlying drivers complete a pending OID request. For more information OID requests in connection-oriented protocol drivers, see [Connection-Oriented Operations](connection-oriented-operations.md).

For more information about OIDs, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

 

 





