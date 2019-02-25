---
title: Registering as an Interface Provider
description: Registering as an Interface Provider
ms.assetid: 7eb4b86d-077a-48de-94b6-11906e847569
keywords:
- NDIS network interfaces WDK , interface providers
- network interfaces WDK , interface providers
- interface providers WDk network interface
- registering interface providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering as an Interface Provider





An NDIS interface provider is a software component that provides and manages information for NDIS network interfaces. For example, protocol drivers, MUX intermediate drivers, and NDIS are interface providers. (NDIS provides a proxy interface provider for miniport drivers and filter drivers. However, miniport drivers and filter drivers can also be interface providers.) Each interface provider calls the [**NdisIfRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff562716) function to register as a network interface provider.

If the call to **NdisIfRegisterProvider** succeeds, **NdisIfRegisterProvider** returns a handle at the address that the *pNdisProviderHandle* parameter specifies. The caller uses this handle in subsequent calls (for example, to register interfaces). The *ProviderCharacteristics* parameter points to an [**NDIS\_IF\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565728) structure that contains the provider's entry points to handle OID query and set requests. NDIS\_IF\_PROVIDER\_CHARACTERISTICS includes the following query and set functions:

-   [**ProviderQueryObject**](https://msdn.microsoft.com/library/windows/hardware/ff570399)

-   [**ProviderSetObject**](https://msdn.microsoft.com/library/windows/hardware/ff570403)

For more information about interface provider query and set handlers, see [Handling OID Query and Set Requests in an NDIS Interface Provider](handling-oid-query-and-set-requests-in-an-ndis-interface-provider.md).

NDIS drivers can call the [**NdisIfDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff562703) function to deregister as a network interface provider. For example, NDIS drivers should deregister as a interface providers when they are unloaded. An interface provider must ensure that it does not have any interfaces registered before it calls **NdisIfDeregisterProvider**. The provider must not use the provider handle that it passed at the *NdisProviderHandle* parameter of **NdisIfDeregisterProvider** after it calls **NdisIfDeregisterProvider**.

 

 





