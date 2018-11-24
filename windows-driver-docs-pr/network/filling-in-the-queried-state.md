---
title: Filling In the Queried State
description: Filling In the Queried State
ms.assetid: 33289a37-cbbb-4c73-8849-05d206d7d24d
keywords:
- querying offloaded TCP chimney state, queried state referencing
- queried TCP chimney state referencing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filling In the Queried State


\[The TCP chimney offload feature is deprecated and should not be used.\]




The offload target queries the state that is identified by the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structures in the state tree. An NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure references state to be queried if its **MiniportOffloadContext** member points to a memory location that contains a non-NULL PVOID value. (For more information about the **MiniportOffloadContext** member, see [Storing and Referencing Offloaded State](storing-and-referencing-offloaded-state.md).) This PVOID value references the miniport offload context that contains the state to be queried.

An NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure that references state to be queried is immediately followed in memory by an [offload state structure](offload-state-structures.md). The offload target writes the queried state into the offload state structure.

 

 





