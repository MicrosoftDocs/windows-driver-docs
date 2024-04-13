---
title: Handling an Interface Object Set Request
description: Handling an Interface Object Set Request
keywords:
- NDIS network interfaces WDK , set requests
- network interfaces WDK , set requests
- OIDs WDK networking , network interfaces
- OID requests WDK networking
- set requests WDK networking
ms.date: 04/20/2017
---

# Handling an Interface Object Set Request


To set the data that is associated with an interface object, NDIS calls an interface provider's [**ProviderSetObject**](/windows-hardware/drivers/ddi/ndis/nc-ndis-if_set_object) function. This function returns NDIS\_STATUS\_SUCCESS if it successfully changed the data or an NDIS\_STATUS\_*Xxx* error code otherwise.

For a list of interface provider-specific OID requests, see [NDIS Network Interface OIDs](./ndis-network-interface-oids.md). For a list of OIDs that NDIS uses with providers, miniport adapters, and filter modules to support network interface objects, see [NDIS Network Interface to OID Mapping](mapping-of-ndis-network-interfaces-to-ndis-oids.md).

The handle at the *ProviderIfContext* parameter of [**ProviderSetObject**](/windows-hardware/drivers/ddi/ndis/nc-ndis-if_set_object) identifies the context area that the interface provider passed to NDIS when it called the [**NdisIfRegisterInterface**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterinterface) function to register the interface. The *ObjectId* parameter specifies the OID for the object that is being set. The *InputBufferLength* and *pInputBuffer* parameters provide the length of the input buffer and a pointer to the input buffer, respectively.

 

