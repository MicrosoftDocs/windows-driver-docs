---
title: Synchronizing Update Operations
description: Synchronizing Update Operations
ms.assetid: 175ca97a-99b9-46ff-aa6a-51eb531310cd
keywords:
- updating offloaded TCP chimney state, synchronizing operations
- synchronization WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Update Operations


\[The TCP chimney offload feature is deprecated and should not be used.\]




The host stack synchronizes update operations as follows:

-   The host stack never attempts to update a state object that is in the process of being offloaded.

-   The host stack never attempts to update a state object that is in the process of being updated. At any given time, only one update operation can be in progress for any given state object. However, multiple update operations can be in progress, if these operations are each updating different objects.

-   The host stack never attempts to update an invalidated state object.

 

 





