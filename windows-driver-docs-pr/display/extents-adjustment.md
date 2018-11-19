---
title: Extents Adjustment
description: Extents Adjustment
ms.assetid: b3562744-375a-4d6f-be09-e28314282faa
keywords:
- Direct3D WDK Windows 2000 display , extents adjustment
- extents adjustment WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extents Adjustment


## <span id="ddk_extents_adjustment_gg"></span><span id="DDK_EXTENTS_ADJUSTMENT_GG"></span>


Some hardware uses an anti-aliasing kernel that influences pixels outside the extents rectangle defined by the screen-space vertices. Applications that use the extents rectangle in the D3DCLIPSTATUS structure (defined in *d3dtypes.h*) for dirty rectangle processing might experience rendering artifacts because the extents rectangle does not cover the pixels modified by the hardware.

Direct3D addresses this problem by enabling hardware drivers to request that the extents rectangle be adjusted outward by a specified number of pixels in the **dvExtentsAdjust** member of the [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753) structure. This member is filled in response to the GUID\_D3DExtendedCaps GUID in [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404). The extents rectangle is clipped to the extents of the render target surface for the device. The default is zero.

 

 





