---
title: Vertex Blending
description: Vertex Blending
ms.assetid: 58e740fb-01e4-4c8c-8e44-f0c358fd621a
keywords: ["lending WDK Direct3D", "vertex blending WDK Direct3D", "Direct3D WDK Windows 2000 display , vertex blending"]
---

# Vertex Blending


## <span id="ddk_vertex_blending_gg"></span><span id="DDK_VERTEX_BLENDING_GG"></span>


Vertex blending operations are supported for the latest Direct X release. Vertex blending works in this way: an object from modeling space is multiplied by a 4X4 world matrix, placing the model's origin in a particular world space relative to the origin of that world space. One part of the matrix does orientation and another part does the position. There can be up to three world matrices applied, allowing objects to be "bent" by blending the vertices with different weighting over the span of the object.

Next, the view matrix is applied, which effectively compresses the space relative to a particular viewpoint; much like a camera renders the real world onto a two-dimensional picture.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20Blending%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




