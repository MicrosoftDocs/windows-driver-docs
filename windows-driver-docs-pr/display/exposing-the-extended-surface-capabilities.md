---
title: Exposing the Extended Surface Capabilities
description: Exposing the Extended Surface Capabilities
ms.assetid: 833171f0-e86a-46c9-9596-87b9b292c03c
keywords:
- drawing extended surface capabilities WDK DirectDraw , exposing
- DirectDraw extended surface capabilities WDK Windows 2000 display , exposing
- extended surface capabilities WDK DirectDraw , exposing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exposing the Extended Surface Capabilities


## <span id="ddk_exposing_the_extended_surface_capabilities_gg"></span><span id="DDK_EXPOSING_THE_EXTENDED_SURFACE_CAPABILITIES_GG"></span>


The [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure contains a [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) field which drivers fill in to indicate what types of surfaces they support. When these caps are reported to the application, a slightly different structure, DDCAPS, is returned. This DDCAPS structure is built from the driver's DDCORECAPS and other structures that are queried using the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) interface. For the latest version of DirectX, the application-visible DDCAPS contains a [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) member. This DDCAPS2 member is constructed from the DDSCAPS member in the DDCORECAPS structure, and the **ddsCapsMore** member of the [**DD\_MORESURFACECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff551659) structure.

The DD\_MORESURFACECAPS structure is queried from the driver at driver initialization time using the *DdGetDriverInfo* call. The appropriate GUID, as defined in *ddrawint.h*, is GUID\_DDMoreSurfaceCaps.

Responding to the GUID\_DDMoreSurfaceCaps query is entirely optional. It is intended to allow drivers to do two distinct things:

-   Expose extended surface capabilities that the driver can create in display memory.

-   Express to DirectDraw new heap restrictions for these extended surface capabilities.

The first item has been covered in the previous section and is fairly self-explanatory. The second item is more complex, and readers should be familiar with the significance of the **ddsCaps** and **ddsCapsAlt** members of the [**VIDEOMEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff570171) structure, described in [Memory Heap Allocation](memory-heap-allocation.md), before reading the next section.

 

 





