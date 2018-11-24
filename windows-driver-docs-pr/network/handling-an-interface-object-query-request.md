---
title: Handling an Interface Object Query Request
description: Handling an Interface Object Query Request
ms.assetid: c4dc4d9e-52ea-477f-9bc8-cf04ccaa73b2
keywords:
- NDIS network interfaces WDK , query requests
- network interfaces WDK , query requests
- OIDs WDK networking , network interfaces
- OID requests WDK networking
- query requests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling an Interface Object Query Request





To obtain the current value that is associated with an interface object, NDIS calls an interface provider's [**ProviderQueryObject**](https://msdn.microsoft.com/library/windows/hardware/ff570399) function. This function returns NDIS\_STATUS\_SUCCESS if it successfully processes the query request or an NDIS\_STATUS\_*Xxx* error code otherwise.

For a list of interface provider-specific OID requests, see [NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545). For a list of OIDs that NDIS uses with providers, miniport adapters, and filter modules to support network interface objects, see [NDIS Network Interface to OID Mapping](mapping-of-ndis-network-interfaces-to-ndis-oids.md).

The handle at the *ProviderIfContext* parameter of [**ProviderQueryObject**](https://msdn.microsoft.com/library/windows/hardware/ff570399) identifies the context area that the interface provider passed to NDIS when it called the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function to register the interface. The *ObjectId* parameter specifies the OID for the object that is being queried. The *pOutputBufferLength* and *pOutputBuffer* parameters provide a pointer to the resulting length of the output buffer and a pointer to the output buffer, respectively.

 

 





