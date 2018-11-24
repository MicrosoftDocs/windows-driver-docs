---
title: Porting Intermediate Driver OID Request Handling to NDIS 6.0
description: Porting Intermediate Driver OID Request Handling to NDIS 6.0
ms.assetid: 715d0ae9-8a5a-487a-9eb0-8864184db1f0
keywords:
- porting intermediate drivers WDK networking , OID requests
- OID request porting WDK networking
- OIDs WDK networking , request operation porting
- object identifiers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Intermediate Driver OID Request Handling to NDIS 6.0





Like NDIS 5.*x* intermediate drivers, NDIS 6.0 intermediate drivers can originate or forward OID requests. NDIS 6.0 intermediate drivers can also cancel OID requests.

To forward a request down to the underlying drivers, an NDIS intermediate driver calls [**NdisAllocateCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff560706) to allocate a cloned [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. The driver calls the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function to send the request. When the request is complete, the driver must call the [**NdisFreeCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561845) function to free the NDIS\_OID\_REQUEST structure.

To cancel an OID request, call the [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) function.

For more information about OID request handling in the miniport upper edge of an intermediate driver, see [Porting Miniport Driver OID Request Handling to NDIS 6.0](porting-miniport-driver-oid-request-handling-to-ndis-6-0.md).

For more information about OID request handling in the protocol lower edge of an intermediate driver, see [Porting Protocol Driver OID Request Handling to NDIS 6.0](porting-protocol-driver-oid-request-handling-to-ndis-6-0.md).

 

 





