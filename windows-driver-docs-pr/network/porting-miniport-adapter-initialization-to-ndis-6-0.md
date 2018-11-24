---
title: Porting Miniport Adapter Initialization to NDIS 6.0
description: Porting Miniport Adapter Initialization to NDIS 6.0
ms.assetid: 3917cf4f-809a-4acc-9655-7115b02436cf
keywords:
- adapters WDK networking , initializing
- miniport adapters WDK networking , initializing
- porting miniport drivers WDK networking , adapters
- initializing miniport adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Adapter Initialization to NDIS 6.0





As with NDIS 5.*x*, NDIS 6.0 miniport drivers can support multiple miniport adapters. A miniport adapter is the logical entity within NDIS that manages a physical or virtual device (also known as a physical or virtual adapter). To initialize a miniport adapter, NDIS 5.*x* calls the miniport driver's [**MiniportInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff550472) function. In NDIS 6.0, the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function replaces *MiniportInitialize*. The following topics provide information about porting miniport adapter initialization to NDIS 6.0:

[Updating the MiniportInitialize Function for NDIS 6.0](updating-the-miniportinitialize-function-for-ndis-6-0.md)

[Setting the NDIS 6.0 Miniport Adapter Attributes](setting-the-ndis-6-0-miniport-adapter-attributes.md)

[Reading the Registry in an NDIS 6.0 Miniport Driver](reading-the-registry-in-an-ndis-6-0-miniport-driver.md)

[Allocating Memory in an NDIS 6.0 Miniport Driver](allocating-memory-in-an-ndis-6-0-miniport-driver.md)

[Updating Bus-Specific Configuration Space Access for NDIS 6.0](updating-bus-specific-configuration-space-access-for-ndis-6-0.md)

 

 





