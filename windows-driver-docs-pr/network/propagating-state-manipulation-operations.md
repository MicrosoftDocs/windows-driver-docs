---
title: Propagating State-Manipulation Operations
description: Propagating State-Manipulation Operations
ms.assetid: 3a7395b0-0cd0-4623-8251-e9857fab7f0d
keywords:
- intermediate drivers WDK TCP chimney offload , propagating state-manipulation operations
- propagating TCP chimney state-manipulation operations
- state-manipulation operations WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Propagating State-Manipulation Operations


\[The TCP chimney offload feature is deprecated and should not be used.\]

This section describes how an intermediate driver propagates a state-manipulation operation that was initiated by the host stack and the completion of such an operation by an underlying offload target.

State-manipulation operations include:

-   Initiating the offload of a state object.

-   Invalidating an offloaded state object.

-   Querying an offloaded state object.

-   Updating an offloaded state object.

-   Terminating the offload of a state object.

This section includes:

-   [Propagating a State-Manipulation Operation](propagating-a-state-manipulation-operation.md)

-   [Propagating the Completion of a State-Manipulation Operation](propagating-the-completion-of-a-state-manipulation-operation.md)

-   [Comparison of Offload Block List Types](comparison-of-offload-block-list-types.md)

-   [Reusing an NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST Structure](reusing-an-ndis-miniport-offload-block-list-structure.md)

-   [Reusing an NDIS\_PROTOCOL\_OFFLOAD\_BLOCK\_LIST Structure](reusing-an-ndis-miniport-offload-block-list-structure.md)

 

 





