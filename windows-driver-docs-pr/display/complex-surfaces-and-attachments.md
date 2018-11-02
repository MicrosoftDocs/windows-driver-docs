---
title: Complex Surfaces and Attachments
description: Complex Surfaces and Attachments
ms.assetid: fb75c534-b1ff-44d3-a8dc-dcf0f221b6ad
keywords:
- drawing surfaces WDK DirectDraw , complex
- DirectDraw surfaces WDK Windows 2000 display , complex
- surfaces WDK DirectDraw , complex
- complex surfaces WDK DirectDraw
- surfaces WDK DirectDraw , attachments
- drawing surfaces WDK DirectDraw , attachments
- DirectDraw surfaces WDK Windows 2000 display , attachments
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Complex Surfaces and Attachments


## <span id="ddk_complex_surfaces_and_attachments_gg"></span><span id="DDK_COMPLEX_SURFACES_AND_ATTACHMENTS_GG"></span>


Surfaces can be *complex*, which means that they are part of a larger collection of associated surfaces. Examples of complex surfaces include the front buffer and associated back buffers, the various levels of a MIP map, and the various faces of a cube map.

The DirectDraw runtime uses a concept known as *surface attachments* to manage the linking of different simple surfaces into complex surfaces. Surfaces can be attached implicitly, as when the application makes one call to **IDirectDraw7::CreateSurface** to build a flipping chain (front buffer and back buffers with a possible Z-buffer); or explicitly, as when the application associates a Z-buffer with a render target by calling **IDirectDrawSurface7::AddAttachedSurface**.

 

 





