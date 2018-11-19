---
title: Extended Surface Description Structure
description: Extended Surface Description Structure
ms.assetid: 51936b15-590c-4113-a393-1a8306c24e7f
keywords:
- drawing extended surface capabilities WDK DirectDraw , description structure
- DirectDraw extended surface capabilities WDK Windows 2000 display , description structure
- extended surface capabilities WDK DirectDraw , description structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Surface Description Structure


## <span id="ddk_extended_surface_description_structure_gg"></span><span id="DDK_EXTENDED_SURFACE_DESCRIPTION_STRUCTURE_GG"></span>


The extended DirectDraw surface description structure, [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340), is identical to the [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) structure, except that the pointer to the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure at the end of the structure has been replaced with a pointer to a [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure.

The data blocks for the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) and [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213) driver calls each contain a pointer to a DDSURFACEDESC structure. Beginning with DirectX 6.0, these pointers might actually point to a DDSURFACEDESC2 structure, even though the pointers remain typed as LPDDSURFACEDESC. If a driver chooses, it can examine the **dwSize** member of the [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) pointer, and thereby decide if the pointer actually points to a [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure. If your driver must run on pre-DirectX 6.0 installations, it must make this check.

If the size returned is sizeof(DDSURFACEDESC2), the driver can then examine the **dwCaps2**, **dwCaps3**, and **dwCaps4** members of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure.

 

 





