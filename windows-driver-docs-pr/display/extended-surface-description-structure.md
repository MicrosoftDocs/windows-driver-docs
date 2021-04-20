---
title: Extended Surface Description Structure
description: Extended Surface Description Structure
keywords:
- drawing extended surface capabilities WDK DirectDraw , description structure
- DirectDraw extended surface capabilities WDK Windows 2000 display , description structure
- extended surface capabilities WDK DirectDraw , description structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Surface Description Structure


## <span id="ddk_extended_surface_description_structure_gg"></span><span id="DDK_EXTENDED_SURFACE_DESCRIPTION_STRUCTURE_GG"></span>


The extended DirectDraw surface description structure, [**DDSURFACEDESC2**](/previous-versions/windows/hardware/drivers/ff550340(v=vs.85)), is identical to the [**DDSURFACEDESC**](/previous-versions/windows/hardware/drivers/ff550339(v=vs.85)) structure, except that the pointer to the [**DDSCAPS**](/previous-versions/windows/hardware/drivers/ff550286(v=vs.85)) structure at the end of the structure has been replaced with a pointer to a [**DDSCAPS2**](/previous-versions/windows/hardware/drivers/ff550292(v=vs.85)) structure.

The data blocks for the [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)) and [*DdCanCreateSurface*](/previous-versions/windows/hardware/drivers/ff549213(v=vs.85)) driver calls each contain a pointer to a DDSURFACEDESC structure. Beginning with DirectX 6.0, these pointers might actually point to a DDSURFACEDESC2 structure, even though the pointers remain typed as LPDDSURFACEDESC. If a driver chooses, it can examine the **dwSize** member of the [**DDSURFACEDESC**](/previous-versions/windows/hardware/drivers/ff550339(v=vs.85)) pointer, and thereby decide if the pointer actually points to a [**DDSURFACEDESC2**](/previous-versions/windows/hardware/drivers/ff550340(v=vs.85)) structure. If your driver must run on pre-DirectX 6.0 installations, it must make this check.

If the size returned is sizeof(DDSURFACEDESC2), the driver can then examine the **dwCaps2**, **dwCaps3**, and **dwCaps4** members of the [**DDSCAPS2**](/previous-versions/windows/hardware/drivers/ff550292(v=vs.85)) structure.

 

