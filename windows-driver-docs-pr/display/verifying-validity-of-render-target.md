---
title: Verifying Validity of Render Target
description: Verifying Validity of Render Target
ms.assetid: 316ecd58-996a-4277-b2dc-4424c96d8a56
keywords:
- render targets WDK DirectX 9.0 , verifying validity
- validating render targets WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying Validity of Render Target


## <span id="ddk_verifying_validity_of_render_target_gg"></span><span id="DDK_VERIFYING_VALIDITY_OF_RENDER_TARGET_GG"></span>


A DirectX 9.0 version driver must verify whether its internal render target is valid before using the render target because the DirectX 9.0 runtime permits applications to set render targets to **NULL**. In contrast, DirectX 8.1 and earlier runtimes guarantee that render targets are always valid for a Direct3D context.

 

 





