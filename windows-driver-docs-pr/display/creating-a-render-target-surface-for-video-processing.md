---
title: Creating a Render Target Surface for Video Processing
description: Creating a Render Target Surface for Video Processing
keywords:
- video processing WDK DirectX VA , render target surfaces
- render target surfaces WDK DirectX VA
ms.date: 04/20/2017
---

# Creating a Render Target Surface for Video Processing


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function to create render target surfaces for video processing. The user-mode display driver determines that it should create a render target surface for video processing from the presence of the **VideoProcessRenderTarget** bit-field flag in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure that the *pResource* parameter of **CreateResource** points to. The user-mode display driver can use this render target for video processing but not necessarily for 3-D. The user-mode display driver can perform video processing on regular RGB 3-D render target surfaces. However, the user-mode display driver can often output to YUV formats that the 3-D hardware cannot support as a render target.

The following are the only surface types that the driver should support as valid render targets for video processing:

-   RGB or YUV surfaces that are created with the **VideoProcessRenderTarget** bit-field flag.

-   RGB surfaces that are created with the **RenderTarget** bit-field flag.

-   RGB textures that are created with the **RenderTarget** and **Texture** bit-field flags.

 

