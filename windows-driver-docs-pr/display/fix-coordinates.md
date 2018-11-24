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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FIX Coordinates


## <span id="ddk_fix_coordinates_gg"></span><span id="DDK_FIX_COORDINATES_GG"></span>


Graphics DDIs use fractional coordinates that can specify a location on the device surface within one-sixteenth of a pixel. (On vector devices, the fractional coordinates are sixteen times more accurate than the device resolution.) The fractional coordinates are represented as 32-bit numbers in signed 28.4 bit FIX notation. In this notation, the highest-order 28 bits represent the integer part of the coordinate, and the lowest 4 bits represent the fractional part. For example, 0x0000003C equals +3.7500, and 0xFFFFFFE8 equals -1.5000.

FIX coordinates represent control points for lines and Bezier curves. For certain objects, such as rectangular clip regions, GDI uses signed 32-bit integers to represent coordinates. Because coordinates are 28-bit quantities, the highest 5 bits of an integer coordinate are either all cleared or all set.

 

 





