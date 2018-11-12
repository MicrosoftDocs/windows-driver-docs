---
title: Handling an Interface Object Set Request
description: Handling an Interface Object Set Request
ms.assetid: aed27b0b-fff5-4e9f-b368-526a8bf79c59
keywords:
- NDIS network interfaces WDK , set requests
- network interfaces WDK , set requests
- OIDs WDK networking , network interfaces
- OID requests WDK networking
- set requests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling an Interface Object Set Request


To set the data that is associated with an interface object, NDIS calls an interface provider's [**ProviderSetObject**](https://msdn.microsoft.com/library/windows/hardware/ff570403) function. This function returns NDIS\_STATUS\_SUCCESS if it successfully changed the data or an NDIS\_STATUS\_*Xxx* error code otherwise.

For a list of interface provider-specific OID requests, see [NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545). For a list of OIDs that NDIS uses with providers, miniport adapters, and filter modules to support network interface objects, see [NDIS Network Interface to OID Mapping](mapping-of-ndis-network-interfaces-to-ndis-oids.md).

The handle at the *ProviderIfContext* parameter of [**ProviderSetObject**](https://msdn.microsoft.com/library/windows/hardware/ff570403) identifies the context area that the interface provider passed to NDIS when it called the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function to register the interface. The *ObjectId* parameter specifies the OID for the object that is being set. The *InputBufferLength* and *pInputBuffer* parameters provide the length of the input buffer and a pointer to the input buffer, respectively.

 

 





