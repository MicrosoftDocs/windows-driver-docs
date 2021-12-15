---
title: Handling OID Query and Set Requests in an NDIS Interface Provider
description: Handling OID Query and Set Requests in an NDIS Interface Provider
keywords:
- NDIS network interfaces WDK , interface providers
- network interfaces WDK , interface providers
- interface providers WDk network interface
ms.date: 04/20/2017
---

# Handling OID Query and Set Requests in an NDIS Interface Provider





The NDISIF interface defines several interface parameters (including statistical counters) that can be queried or set which correspond to information in RFC 2863. NDIS accesses these interface parameters through entry points that the interface provider defines when it calls the [**NdisIfRegisterProvider**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterprovider) function. For more information about registering as an interface provider, see [Registering as an Interface Provider](registering-as-an-interface-provider.md).

Interface parameters are identified by object identifiers (OIDs). Some OIDs are specific to interface providers.

The following topics describe how to handle query and set requests for interface parameters:

[Handling an Interface Object Query Request](handling-an-interface-object-query-request.md)

[Handling an Interface Object Set Request](handling-an-interface-object-set-request.md)

 

