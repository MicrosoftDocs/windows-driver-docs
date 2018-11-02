---
title: Rasterizer Update
description: Rasterizer Update
ms.assetid: 0b7db462-2b04-42e1-baa0-ec9070741c1d
keywords:
- rasterizers WDK Direct3D
- production rasterizers WDK Direct3D
- reference rasterizers WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rasterizer Update


## <span id="ddk_rasterizer_update_gg"></span><span id="DDK_RASTERIZER_UPDATE_GG"></span>


The reference rasterizer has been extracted into a separate DLL to enable additional WHQL tests to be added asynchronously of normal DirectX ship cycles (quarterly is typical). It has been updated to support any of the rasterizer-level operations added to the API either in the core or as extensions that require guaranteed consistency of implementation.

The production rasterizer may not be updated to support these techniques, because environment mapping at the vertex level is likely to be faster than at the pixel level when running in software.

This rasterizer is likely to be upgraded in terms of performance on key cases that are identified.

 

 





