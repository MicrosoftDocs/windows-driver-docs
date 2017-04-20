---
title: FIX Coordinates
description: FIX Coordinates
ms.assetid: dfa5c61f-9464-4c63-998e-7fee21cfd278
keywords:
- surface negotiation WDK GDI , FIX coordinates
- fractional coordinates WDK GDI
- FIX coordinates WDK GDI
- Bezier curves WDK GDI
- lines WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FIX Coordinates


## <span id="ddk_fix_coordinates_gg"></span><span id="DDK_FIX_COORDINATES_GG"></span>


Graphics DDIs use fractional coordinates that can specify a location on the device surface within one-sixteenth of a pixel. (On vector devices, the fractional coordinates are sixteen times more accurate than the device resolution.) The fractional coordinates are represented as 32-bit numbers in signed 28.4 bit FIX notation. In this notation, the highest-order 28 bits represent the integer part of the coordinate, and the lowest 4 bits represent the fractional part. For example, 0x0000003C equals +3.7500, and 0xFFFFFFE8 equals -1.5000.

FIX coordinates represent control points for lines and Bezier curves. For certain objects, such as rectangular clip regions, GDI uses signed 32-bit integers to represent coordinates. Because coordinates are 28-bit quantities, the highest 5 bits of an integer coordinate are either all cleared or all set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20FIX%20Coordinates%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




