---
title: Porting OID Requests for CoNDIS 6.0 Miniport Drivers
description: Porting OID Requests for CoNDIS 6.0 Miniport Drivers
ms.assetid: f432f149-f066-41ac-b9f9-2dd849da6395
keywords:
- porting OID requests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting OID Requests for CoNDIS 6.0 Miniport Drivers





In CoNDIS 6.0, the [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function replaces the NDIS 5.x [**MiniportCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549413) function, and the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaces the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

NDIS calls a miniport driver's *MiniportCoOidRequest* function to send an OID request to a CoNDIS miniport driver. In contrast with *MiniportCoRequest*, which NDIS can call only at IRQL = DISPATCH\_LEVEL, NDIS can call *MiniportCoOidRequest* at IRQL &lt;= DISPATCH\_LEVEL.

CoNDIS 6.0 miniport drivers should provide a [*MiniportCancelOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559339) function, which NDIS calls to cancel an OID request. For NDIS 6.0 miniport drivers, NDIS does not reset the miniport adapter to cancel OID requests.

If *MiniportCoOidRequest* returns NDIS\_STATUS\_PENDING, the miniport driver must subsequently call the [**NdisMCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563568) function to complete the request.

The [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure differs from [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) in that NDIS\_OID\_REQUEST can specify a time-out and a request identifier.

For more information about handling OID requests in a CoNDIS miniport driver, see [CoNDIS Miniport Driver OID Requests](condis-miniport-driver-oid-requests.md).

 

 





