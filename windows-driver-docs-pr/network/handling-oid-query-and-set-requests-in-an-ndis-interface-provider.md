---
title: Handling OID Query and Set Requests in an NDIS Interface Provider
description: Handling OID Query and Set Requests in an NDIS Interface Provider
ms.assetid: 9ce51fc8-426f-4d36-8ee7-0a93b7b8439c
keywords:
- NDIS network interfaces WDK , interface providers
- network interfaces WDK , interface providers
- interface providers WDk network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID Query and Set Requests in an NDIS Interface Provider





The NDISIF interface defines several interface parameters (including statistical counters) that can be queried or set which correspond to information in RFC 2863. NDIS accesses these interface parameters through entry points that the interface provider defines when it calls the [**NdisIfRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff562716) function. For more information about registering as an interface provider, see [Registering as an Interface Provider](registering-as-an-interface-provider.md).

Interface parameters are identified by object identifiers (OIDs). Some OIDs are specific to interface providers.

The following topics describe how to handle query and set requests for interface parameters:

[Handling an Interface Object Query Request](handling-an-interface-object-query-request.md)

[Handling an Interface Object Set Request](handling-an-interface-object-set-request.md)

 

 





