---
title: Setting Multiple Render Targets and Depth Stencils
description: Setting Multiple Render Targets and Depth Stencils
ms.assetid: 98acd448-0b65-4a3a-9e95-8e753729a7d7
keywords:
- render targets WDK DirectX 9.0 , multiple
- multiple render targets WDK DirectX 9.0
- depth stencils WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Multiple Render Targets and Depth Stencils


## <span id="ddk_setting_multiple_render_targets_and_depth_stencils_gg"></span><span id="DDK_SETTING_MULTIPLE_RENDER_TARGETS_AND_DEPTH_STENCILS_GG"></span>


A DirectX 9.0 version driver must process D3DDP2OP\_SETRENDERTARGET2 and D3DDP2OP\_SETDEPTHSTENCIL operation codes in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function even if it does not support [rendering to multiple targets simultaneously](rendering-to-multiple-targets-simultaneously.md). [**D3DHAL\_DP2SETRENDERTARGET2**](https://msdn.microsoft.com/library/windows/hardware/ff545785) and [**D3DHAL\_DP2SETDEPTHSTENCIL**](https://msdn.microsoft.com/library/windows/hardware/ff545724) structures respectively follow these codes in the [command stream](command-stream.md).

 

 





