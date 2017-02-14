---
title: Complex Surfaces and Attachments
description: Complex Surfaces and Attachments
ms.assetid: fb75c534-b1ff-44d3-a8dc-dcf0f221b6ad
keywords: ["drawing surfaces WDK DirectDraw , complex", "DirectDraw surfaces WDK Windows 2000 display , complex", "surfaces WDK DirectDraw , complex", "complex surfaces WDK DirectDraw", "surfaces WDK DirectDraw , attachments", "drawing surfaces WDK DirectDraw , attachments", "DirectDraw surfaces WDK Windows 2000 display , attachments"]
---

# Complex Surfaces and Attachments


## <span id="ddk_complex_surfaces_and_attachments_gg"></span><span id="DDK_COMPLEX_SURFACES_AND_ATTACHMENTS_GG"></span>


Surfaces can be *complex*, which means that they are part of a larger collection of associated surfaces. Examples of complex surfaces include the front buffer and associated back buffers, the various levels of a MIP map, and the various faces of a cube map.

The DirectDraw runtime uses a concept known as *surface attachments* to manage the linking of different simple surfaces into complex surfaces. Surfaces can be attached implicitly, as when the application makes one call to **IDirectDraw7::CreateSurface** to build a flipping chain (front buffer and back buffers with a possible Z-buffer); or explicitly, as when the application associates a Z-buffer with a render target by calling **IDirectDrawSurface7::AddAttachedSurface**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Complex%20Surfaces%20and%20Attachments%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




