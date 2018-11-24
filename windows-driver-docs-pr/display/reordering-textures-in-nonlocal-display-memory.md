---
title: Reordering Textures In Nonlocal Display Memory
description: Reordering Textures In Nonlocal Display Memory
ms.assetid: b4b4c478-7034-4ff9-8cb2-f86baffd89f7
keywords:
- display memory WDK DirectDraw , reordering textures
- nonlocal display memory WDK DirectDraw , reordering textures
- AGP WDK DirectDraw , reordering textures
- drawing AGP support WDK DirectDraw , reordering textures
- DirectDraw AGP support WDK Windows 2000 display , reordering textures
- memory WDK DirectDraw AGP , reordering textures
- reordering textures WDK DirectDraw
- DDCAPS2_SYSTONONLOCAL_AS_SYSTOLOCAL
- textures WDK DirectDraw , reordering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reordering Textures In Nonlocal Display Memory


## <span id="ddk_reordering_textures_in_nonlocal_display_memory_gg"></span><span id="DDK_REORDERING_TEXTURES_IN_NONLOCAL_DISPLAY_MEMORY_GG"></span>


There are special cases where the driver writer might want to reorder textures in AGP memory to allow more efficient texture management. The DDCAPS2\_SYSTONONLOCAL\_AS\_SYSTOLOCAL flag signals that the driver can support blts from backing surfaces (system memory copy of a surface) to nonlocal video memory using all the same caps that were specified for backing surface memory to local video memory blts.

The DDCAPS2\_SYSTONONLOCAL\_AS\_SYSTOLOCAL flag is valid only if the DDCAPS2\_NONLOCALVIDMEMCAPS flag is set. If DDCAPS2\_SYSTONONLOCAL\_AS\_SYSTOLOCAL is set, then the DDCAPS\_CANBLTSYSMEM flag must be set by the driver and all the associated backing surface blt caps must be correct. DDCAPS2\_SYSTONONLOCAL\_AS\_SYSTOLOCAL signifies that the backing surface to video memory DDCAPS blt caps also apply to backing surface to nonlocal video memory blts. For example, the **dwSVBCaps**, **dwSVBCKeyCaps**, **dwSVBFXCaps**, and **dwSVBRops** members of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure are assumed to be filled in correctly. Any blt from a backing surface to nonlocal memory that matches these caps bits is passed to the driver.

**Note**   This feature is intended to enable the driver itself to do efficient reordering of textures. This is *not* meant to imply that hardware can write into AGP memory. Hardware writing directly into AGP memory is not currently supported.

 

 

 





