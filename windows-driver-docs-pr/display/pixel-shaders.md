---
title: Pixel Shaders
description: Pixel Shaders
ms.assetid: a44c5ee8-e9a7-4f9a-9547-e0c5ae49b82c
keywords:
- pixel shaders WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pixel Shaders


## <span id="ddk_pixel_shaders_gg"></span><span id="DDK_PIXEL_SHADERS_GG"></span>


All drivers that support the DirectX 8.0 DDI may support the new DP2 token D3DDP2OP\_SETPIXELSHADER if programmable pixel shaders are supported in hardware.

D3DDP2OP\_SETPIXELSHADER can be used to notify the driver of the handle of the current programmable pixel shader to use. A pixel shader handle refers to a programmable pixel shader handle previously created by means of the D3DDP2OP\_CREATEPIXELSHADER DP2 token.

 

 





