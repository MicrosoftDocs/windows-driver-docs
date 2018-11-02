---
title: Reasons for Updating Offloaded State Objects
description: Reasons for Updating Offloaded State Objects
ms.assetid: 5c2a6330-a6dd-49c0-817b-68b4ae6628bc
keywords:
- updating offloaded TCP chimney state, about updating offloaded state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reasons for Updating Offloaded State Objects


\[The TCP chimney offload feature is deprecated and should not be used.\]




The host stack updates offloaded state objects if:

-   The values of cached variables in one or more [offload state objects](offload-state-objects.md) have changed.

-   Offloaded path state objects must be linked to a new neighbor state object.

Note that the host stack updates only path-to-neighbor links. It never updates TCP connection-to-path links.

 

 





