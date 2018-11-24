---
title: Extended Surface Capability Flags
description: Extended Surface Capability Flags
ms.assetid: 197d899e-57ab-40f8-9c09-440c2dc6197c
keywords:
- drawing extended surface capabilities WDK DirectDraw , flags
- DirectDraw extended surface capabilities WDK Windows 2000 display , flags
- extended surface capabilities WDK DirectDraw , flags
- flags WDK DirectDraw extended surface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Surface Capability Flags


## <span id="ddk_extended_surface_capability_flags_gg"></span><span id="DDK_EXTENDED_SURFACE_CAPABILITY_FLAGS_GG"></span>


The extended surface capabilities added to the latest versions of DirectDraw are made visible to the driver when the application sets the appropriate flags in the **dwCaps2** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure.

Applications can only set the DDSCAPS2\_HARDWAREDEINTERLACE flag in conjunction with the DDSCAPS\_OVERLAY flag. If a driver sees this flag set at **CreateSurface** time, it means that DirectDraw expects that the driver will do whatever is necessary to match the hardware video port frame rate with the device frame rate.

The DDSCAPS2\_HINTDYNAMIC, DDSCAPS2\_HINTSTATIC, and DDSCAPS2\_OPAQUE flags are hints set by the application at **CreateSurface** time that inform the driver what the application plans to do with the surface. The DDSCAPS2\_HINTDYNAMIC flag means that the application will update the surface frequently. The DDSCAPS2\_HINTSTATIC flag means that the application will update the surface rarely, but still requires access. This means the driver must be able to allow locks on the surface, which may involve some hidden decompression and compression steps. The DDSCAPS2\_OPAQUE flag means that the application will never lock, blt, or update the surface for the rest of that surface's lifetime. The driver is free to compress or reorder the surface without having to ever decompress it.

**Note**   The driver does not need to set these flags to enable them. DirectDraw merely passes these bits to the driver when [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) is called.

 

Driver writers might want to use the extended heap restriction features (described in [Extended Heap Restrictions](extended-heap-restrictions.md)) of DirectDraw to automatically place DDSCAPS2\_OPAQUE textures in optimized heaps. This is entirely up to the driver developer.

The DDSCAPS2\_HINTDYNAMIC, DDSCAPS2\_HINTSTATIC, and DDSCAPS2\_OPAQUE flags are described in more detail in the Microsoft DirectX Driver Development Kit (DDK) documentation.

The DDSCAPS2\_TEXTUREMANAGE flag is not relevant to drivers. This flag informs the DirectX runtime that it is responsible for moving the surface from a backing surface to display memory, as appropriate, to enable accelerated 3D texturing.

 

 





