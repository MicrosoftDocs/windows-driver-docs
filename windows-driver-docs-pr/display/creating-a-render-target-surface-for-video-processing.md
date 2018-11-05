---
title: Creating a Render Target Surface for Video Processing
description: Creating a Render Target Surface for Video Processing
ms.assetid: f18b348d-837a-4e1b-b91a-40593661bd56
keywords:
- video processing WDK DirectX VA , render target surfaces
- render target surfaces WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Render Target Surface for Video Processing


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function to create render target surfaces for video processing. The user-mode display driver determines that it should create a render target surface for video processing from the presence of the **VideoProcessRenderTarget** bit-field flag in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter of **CreateResource** points to. The user-mode display driver can use this render target for video processing but not necessarily for 3-D. The user-mode display driver can perform video processing on regular RGB 3-D render target surfaces. However, the user-mode display driver can often output to YUV formats that the 3-D hardware cannot support as a render target.

The following are the only surface types that the driver should support as valid render targets for video processing:

-   RGB or YUV surfaces that are created with the **VideoProcessRenderTarget** bit-field flag.

-   RGB surfaces that are created with the **RenderTarget** bit-field flag.

-   RGB textures that are created with the **RenderTarget** and **Texture** bit-field flags.

 

 





