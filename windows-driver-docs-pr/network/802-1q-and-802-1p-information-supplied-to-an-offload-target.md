---
title: 802.1Q and 802.1p Information Supplied to an Offload Target
description: 802.1Q and 802.1p Information Supplied to an Offload Target
ms.assetid: 74c979ce-c7cb-427d-a9c9-ca042cf4c583
keywords:
- 802.1Q and 802.1p information WDK TCP chimney offload , supplied to target
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 802.1Q and 802.1p Information Supplied to an Offload Target


\[The TCP chimney offload feature is deprecated and should not be used.\]




A filter driver, an intermediate driver, or NDIS can supply the following 802.1Q and 802.1p information to an offload target:

-   A VLAN identifier (802.1Q) for an offloaded neighbor state object. For more information about this identifier, see [**NEIGHBOR\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff568324).

-   A user priority (802.1p) value for an offloaded TCP connection state object. For more information about this value, see [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937).

In addition, if one or more VLAN identifiers have been configured for the network interface, the offload target's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function reads these identifiers from the registry. For more information about processing VLAN identifiers, see [Initializing, Setting, and Retrieving VLAN Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff548945).

 

 





