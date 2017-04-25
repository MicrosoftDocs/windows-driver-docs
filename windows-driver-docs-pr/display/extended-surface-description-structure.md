---
title: Extended Surface Description Structure
description: Extended Surface Description Structure
ms.assetid: 51936b15-590c-4113-a393-1a8306c24e7f
keywords:
- drawing extended surface capabilities WDK DirectDraw , description structure
- DirectDraw extended surface capabilities WDK Windows 2000 display , description structure
- extended surface capabilities WDK DirectDraw , description structure
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extended Surface Description Structure


## <span id="ddk_extended_surface_description_structure_gg"></span><span id="DDK_EXTENDED_SURFACE_DESCRIPTION_STRUCTURE_GG"></span>


The extended DirectDraw surface description structure, [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340), is identical to the [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) structure, except that the pointer to the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure at the end of the structure has been replaced with a pointer to a [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure.

The data blocks for the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) and [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213) driver calls each contain a pointer to a DDSURFACEDESC structure. Beginning with DirectX 6.0, these pointers might actually point to a DDSURFACEDESC2 structure, even though the pointers remain typed as LPDDSURFACEDESC. If a driver chooses, it can examine the **dwSize** member of the [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) pointer, and thereby decide if the pointer actually points to a [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure. If your driver must run on pre-DirectX 6.0 installations, it must make this check.

If the size returned is sizeof(DDSURFACEDESC2), the driver can then examine the **dwCaps2**, **dwCaps3**, and **dwCaps4** members of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Surface%20Description%20Structure%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




