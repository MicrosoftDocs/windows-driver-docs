---
title: Network Interface Information
description: Network Interface Information
ms.assetid: 4d8cd9c2-6f78-4c70-83bd-f36fffbf1c35
keywords:
- NDIS network interfaces WDK , information about
- network interfaces WDK , information about
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Interface Information





An interface provider supplies information about each registered interface by using the following data structures.

-   [**NET\_IF\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff568743)

-   [**NDIS\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff565736)

To register an interface, a provider passes a pointer to an initialized NET\_IF\_INFORMATION structure to the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function.

NDIS interface providers provide an [**NDIS\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff565736) structure in response to a query of the [OID\_GEN\_INTERFACE\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569589) OID.

NDIS can also query providers with other OIDs. For more information about NDIS provider OIDs, see [NDIS Network Interface to OID Mapping](mapping-of-ndis-network-interfaces-to-ndis-oids.md). For more information about handling OID requests in interface providers, see [Handling OID Query and Set Requests in an NDIS Interface Provider](handling-oid-query-and-set-requests-in-an-ndis-interface-provider.md).

 

 





