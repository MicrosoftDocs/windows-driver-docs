---
title: Exposing the Extended Surface Capabilities
description: Exposing the Extended Surface Capabilities
ms.assetid: 833171f0-e86a-46c9-9596-87b9b292c03c
keywords:
- drawing extended surface capabilities WDK DirectDraw , exposing
- DirectDraw extended surface capabilities WDK Windows 2000 display , exposing
- extended surface capabilities WDK DirectDraw , exposing
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Exposing the Extended Surface Capabilities


## <span id="ddk_exposing_the_extended_surface_capabilities_gg"></span><span id="DDK_EXPOSING_THE_EXTENDED_SURFACE_CAPABILITIES_GG"></span>


The [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure contains a [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) field which drivers fill in to indicate what types of surfaces they support. When these caps are reported to the application, a slightly different structure, DDCAPS, is returned. This DDCAPS structure is built from the driver's DDCORECAPS and other structures that are queried using the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) interface. For the latest version of DirectX, the application-visible DDCAPS contains a [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) member. This DDCAPS2 member is constructed from the DDSCAPS member in the DDCORECAPS structure, and the **ddsCapsMore** member of the [**DD\_MORESURFACECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff551659) structure.

The DD\_MORESURFACECAPS structure is queried from the driver at driver initialization time using the *DdGetDriverInfo* call. The appropriate GUID, as defined in *ddrawint.h*, is GUID\_DDMoreSurfaceCaps.

Responding to the GUID\_DDMoreSurfaceCaps query is entirely optional. It is intended to allow drivers to do two distinct things:

-   Expose extended surface capabilities that the driver can create in display memory.

-   Express to DirectDraw new heap restrictions for these extended surface capabilities.

The first item has been covered in the previous section and is fairly self-explanatory. The second item is more complex, and readers should be familiar with the significance of the **ddsCaps** and **ddsCapsAlt** members of the [**VIDEOMEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff570171) structure, described in [Memory Heap Allocation](memory-heap-allocation.md), before reading the next section.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Exposing%20the%20Extended%20Surface%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




