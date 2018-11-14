---
title: Guard Band Clipping
description: Guard Band Clipping
ms.assetid: bd4ebd97-c948-4219-95a5-f7c6ca45f792
keywords:
- Direct3D WDK Windows 2000 display , guard band clipping
- guard band clipping WDK Direct3D
- clipping WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guard Band Clipping


## <span id="ddk_guard_band_clipping_gg"></span><span id="DDK_GUARD_BAND_CLIPPING_GG"></span>


The driver signals that it supports guard band clipping when it fields the GUID\_D3DExtendedCaps GUID in [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404). A guard band is a rectangle that is potentially larger than the viewport (and even the render target), to which vertices can be clipped automatically by the driver. The Microsoft Direct3D clipping code clips to this rectangle instead of to the viewport. By allowing the driver to specify potentially large guard band rectangles, the need to generate new vertices due to clipping is reduced. One example is a hardware device that can correctly render as long as screen x and y coordinates fall in the range -2048 through 2047.

Guard band clipping is also beneficial for anti-aliasing hardware, because the filter area can extend outside the rendering surface extent. This reduces filtering errors that can be introduced if primitives are geometrically clipped to this extent.

To do the correct clipping, the driver is passed the viewport information. This specifies the actual viewport that the application requires the geometry to be clipped to. Driver writers who do not want to implement guard band clipping can ignore this information. It is recommended that drivers do not use this data to implement clipping through scissors or masking operations because these are likely to be slower than letting Direct3D do the clipping.

 

 





