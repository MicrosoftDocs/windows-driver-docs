---
title: Clipping Transformed Vertices
description: Clipping Transformed Vertices
ms.assetid: 33b03264-780e-4b05-a108-6d1a017e8c27
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , clipping transformed vertices
- pretransformed vertices WDK DirectX 8.0
- clipping WDK DirectX 8.0
- vertex clipping WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Clipping Transformed Vertices


## <span id="ddk_clipping_transformed_vertices_gg"></span><span id="DDK_CLIPPING_TRANSFORMED_VERTICES_GG"></span>


The Direct3D 8.0 runtime fully supports the clipping of pretransformed vertices through both the **DrawPrimitive** and **ProcessVertices** API calls. This clipping includes user defined clipping planes as well as Z and the X and Y viewport extents. However, the runtime does not guarantee the clipping of posttransformed vertices. Posttransformed vertex data is passed directly from the application to the driver by the runtime. This does not imply that a driver is required to fully clip posttransformed vertex data. A new capability flag D3DPMISCCAPS\_CLIPTLVERTS has been added for DirectX 8.0. If the driver sets this flag in the **PrimitiveMiscCaps** field of the D3DCAPS8 structure, the application can assume that the driver fully clips posttransformed vertex data to Z and the X and Y viewport extents. Clipping to user-defined clip planes is never supported for posttransformed data. If the driver does not set this flag, the application is required to performing clipping of the posttransformed data to the Z extents and to (at least) the guard band extents in X and Y.

It is important to note that the runtime does not validate that the application has correctly clipped posttransformed data. It is the driver's responsibility to ensure that a crash or hang does not occur if unclipped or incorrectly clipped data is passed when this flag is set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Clipping%20Transformed%20Vertices%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




