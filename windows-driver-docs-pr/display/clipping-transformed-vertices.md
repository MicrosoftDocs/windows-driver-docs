---
title: Clipping Transformed Vertices
description: Clipping Transformed Vertices
ms.assetid: 33b03264-780e-4b05-a108-6d1a017e8c27
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , clipping transformed vertices
- pretransformed vertices WDK DirectX 8.0
- clipping WDK DirectX 8.0
- vertex clipping WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clipping Transformed Vertices


## <span id="ddk_clipping_transformed_vertices_gg"></span><span id="DDK_CLIPPING_TRANSFORMED_VERTICES_GG"></span>


The Direct3D 8.0 runtime fully supports the clipping of pretransformed vertices through both the **DrawPrimitive** and **ProcessVertices** API calls. This clipping includes user defined clipping planes as well as Z and the X and Y viewport extents. However, the runtime does not guarantee the clipping of posttransformed vertices. Posttransformed vertex data is passed directly from the application to the driver by the runtime. This does not imply that a driver is required to fully clip posttransformed vertex data. A new capability flag D3DPMISCCAPS\_CLIPTLVERTS has been added for DirectX 8.0. If the driver sets this flag in the **PrimitiveMiscCaps** field of the D3DCAPS8 structure, the application can assume that the driver fully clips posttransformed vertex data to Z and the X and Y viewport extents. Clipping to user-defined clip planes is never supported for posttransformed data. If the driver does not set this flag, the application is required to performing clipping of the posttransformed data to the Z extents and to (at least) the guard band extents in X and Y.

It is important to note that the runtime does not validate that the application has correctly clipped posttransformed data. It is the driver's responsibility to ensure that a crash or hang does not occur if unclipped or incorrectly clipped data is passed when this flag is set.

 

 





