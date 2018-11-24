---
title: Porting Miniport Driver OID Request Handling to NDIS 6.0
description: Porting Miniport Driver OID Request Handling to NDIS 6.0
ms.assetid: f84ec462-d149-47f6-ab46-c38941843bda
keywords:
- NDIS miniport drivers WDK networking , OID requests
- miniport drivers WDK networking , OID requests
- OID request porting WDK networking
- OIDs WDK networking , request operation porting
- object identifiers WDK networking
- porting miniport drivers WD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver OID Request Handling to NDIS 6.0





In NDIS 6.0, the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function replaces the NDIS 5.x [**MiniportQueryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550490) and [**MiniportSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550530) functions. Also, the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaces the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

NDIS calls a miniport driver's *MiniportOidRequest* function to send an OID request to the driver. As is the case with NDIS 5.x miniport drivers, NDIS serializes OID requests so it does not call *MiniportOidRequest* until any pending request is complete. In contrast with *MiniportQueryInformation* and *MiniportSetInformation*, which NDIS can call only at IRQL = DISPATCH\_LEVEL, NDIS can call the *MiniportOidRequest* function at IRQL &lt;= DISPATCH\_LEVEL.

NDIS 6.0 miniport drivers should provide a [*MiniportCancelOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559339) function. NDIS calls *MiniportCancelOidRequest* to cancel an OID request. For NDIS 6.0 miniport drivers, NDIS does not reset the miniport adapter to cancel OID requests.

If the *MiniportOidRequest* function returns NDIS\_STATUS\_PENDING, the miniport driver must subsequently call the [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) function to complete the request.

The NDIS\_OID\_REQUEST structure differs from [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) in that it can specify a time-out and a request ID.

For more information about handling OID requests in a miniport driver, see [OID Requests for an Adapter](miniport-adapter-oid-requests.md).

 

 





