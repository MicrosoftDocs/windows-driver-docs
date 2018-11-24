---
title: Creating an Offload Context Area
description: Creating an Offload Context Area
ms.assetid: 5509ba04-aaad-4934-bc11-49d5c795db59
keywords:
- state offloading process WDK TCP chimney offload , context area
- offloading state process WDK TCP chimney offload , context area
- context area WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an Offload Context Area


\[The TCP chimney offload feature is deprecated and should not be used.\]




For each [offload state object](offload-state-objects.md) that it offloads from a state tree, an offload target must allocate an offload context area in which to store the offloaded state object. This context area can be in host memory or NIC memory.

In addition to the offloaded state object, an offload context area must also contain the following:

-   The handle that is specified in the **NdisOffloadHandle** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that was originally associated with the state object

-   Any additional internal information that the offload target uses to keep track of the state object or associated resources

 

 





