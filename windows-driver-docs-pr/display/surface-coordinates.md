---
title: Surface Coordinates
description: Surface Coordinates
ms.assetid: 1f59f135-530a-475a-92b6-f3995aa0c1bb
keywords:
- surface negotiation WDK GDI , surface coordinates
- surface coordinates WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Surface Coordinates


## <span id="ddk_surface_coordinates_gg"></span><span id="DDK_SURFACE_COORDINATES_GG"></span>


A device surface is a subset of an array of 2²⁸ by 2²⁸ pixels. These pixels are addressed by pairs of 28-bit signed numbers, the upper-leftmost pixel of the device surface is given the coordinates (0,0). The device surface lies in the lower right quadrant of this coordinate space, where both coordinates are nonnegative.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Surface%20Coordinates%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




