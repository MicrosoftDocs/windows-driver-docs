---
title: Returning the Completion Status of an Update Offload Operation
description: Returning the Completion Status of an Update Offload Operation
ms.assetid: ca305816-8723-4643-9f23-0b2e939e4b78
keywords:
- updating offloaded TCP chimney state, completion status
- completion status of updates WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning the Completion Status of an Update Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Before calling the [**NdisMUpdateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563694) function, the offload target must write either of the following NDIS\_STATUS values to the **Status** member of each [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure in the state tree:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The offload target successfully updated the state object variables, successfully updated path-to-neighbor links, or successfully updated both.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The update operation did not succeed. The host stack will terminate the offload of the state objects that could not be updated.

 

 





