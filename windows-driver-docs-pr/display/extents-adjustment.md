---
title: Extents Adjustment
description: Extents Adjustment
ms.assetid: b3562744-375a-4d6f-be09-e28314282faa
keywords:
- Direct3D WDK Windows 2000 display , extents adjustment
- extents adjustment WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extents Adjustment


## <span id="ddk_extents_adjustment_gg"></span><span id="DDK_EXTENTS_ADJUSTMENT_GG"></span>


Some hardware uses an anti-aliasing kernel that influences pixels outside the extents rectangle defined by the screen-space vertices. Applications that use the extents rectangle in the D3DCLIPSTATUS structure (defined in *d3dtypes.h*) for dirty rectangle processing might experience rendering artifacts because the extents rectangle does not cover the pixels modified by the hardware.

Direct3D addresses this problem by enabling hardware drivers to request that the extents rectangle be adjusted outward by a specified number of pixels in the **dvExtentsAdjust** member of the [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753) structure. This member is filled in response to the GUID\_D3DExtendedCaps GUID in [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404). The extents rectangle is clipped to the extents of the render target surface for the device. The default is zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extents%20Adjustment%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




