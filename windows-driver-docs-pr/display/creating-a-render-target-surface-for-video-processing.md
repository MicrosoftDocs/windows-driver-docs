---
title: Creating a Render Target Surface for Video Processing
description: Creating a Render Target Surface for Video Processing
ms.assetid: f18b348d-837a-4e1b-b91a-40593661bd56
keywords: ["video processing WDK DirectX VA , render target surfaces", "render target surfaces WDK DirectX VA"]
---

# Creating a Render Target Surface for Video Processing


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function to create render target surfaces for video processing. The user-mode display driver determines that it should create a render target surface for video processing from the presence of the **VideoProcessRenderTarget** bit-field flag in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter of **CreateResource** points to. The user-mode display driver can use this render target for video processing but not necessarily for 3-D. The user-mode display driver can perform video processing on regular RGB 3-D render target surfaces. However, the user-mode display driver can often output to YUV formats that the 3-D hardware cannot support as a render target.

The following are the only surface types that the driver should support as valid render targets for video processing:

-   RGB or YUV surfaces that are created with the **VideoProcessRenderTarget** bit-field flag.

-   RGB surfaces that are created with the **RenderTarget** bit-field flag.

-   RGB textures that are created with the **RenderTarget** and **Texture** bit-field flags.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20a%20Render%20Target%20Surface%20for%20Video%20Processing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




