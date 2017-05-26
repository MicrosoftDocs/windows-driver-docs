---
title: Vertex and Pixel Fogging
description: Vertex and Pixel Fogging
ms.assetid: 4cdba82f-0cfe-4416-951c-59b577c7f30e
keywords:
- pixel fogging WDK Direct3D
- vertex fog WDK Direct3D
- fogging WDK Direct3D
- linear fog WDK Direct3D
- exponential fog WDK Direct3D
- exponential squared fog WDK Direct3D
- monochromatic lighting WDK Direct3D
- color fog calculations WDK Direct3D
- blending fog factor WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vertex and Pixel Fogging


## <span id="ddk_vertex_and_pixel_fogging_gg"></span><span id="DDK_VERTEX_AND_PIXEL_FOGGING_GG"></span>


Fog has three main profile types: linear, exponential, and exponential squared. There are also two main implementation methods: vertex fog (also known as iterated or local fog) and pixel fog (also known as table or global fog).

In monochromatic (ramp) lighting mode, fog can work properly only when the fog color is black. (If there is no lighting, any fog color works because fog is rendered as black.) Fog can be considered a measure of visibility -- the lower the fog value, the greater the fog effect and the less visible the object.

The fog blending factor **f** is used in all fog calculations. It stands for the proportion of fog color versus object color. The final color is determined by the following formula:

**Color = f \* objColor + (1.0 - f) \* fogColor**

Therefore, a fog blending factor of 0.0 is full fog color and a fog blending factor of 1.0 is full object color. Typically, **f** decreases with distance.

As the following figure shows, linear fog density increases in a linear fashion as the distance increases.

![diagram illustrating linear fog](images/d3dfig23.png)

This linear increase differs from exponential fog where the fog density increases exponentially. A linear fog profile might be set up as follows: the D3DRENDERSTATE\_FOGSTART render state is set to ZFront and *f* = 1.0; the D3DRENDERSTATE\_FOGEND render state is set to ZBack and *f* = 0.0. The D3DRENDERSTATE\_FOGDENSITY render state is ignored.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20and%20Pixel%20Fogging%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




