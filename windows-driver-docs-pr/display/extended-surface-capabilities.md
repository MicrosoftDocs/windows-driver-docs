---
title: Extended Surface Capabilities
description: Extended Surface Capabilities
ms.assetid: daa1a310-1cea-48ca-a373-a496b997424f
keywords: ["drawing extended surface capabilities WDK DirectDraw , about extended surface capabilities", "DirectDraw extended surface capabilities WDK Windows 2000 display , about extended surface capabilities", "extended surface capabilities WDK DirectDraw , about extended surface capabilities", "surfaces WDK DirectDraw , extended capabilities", "drawing extended surface capabilities WDK DirectDraw", "DirectDraw extended surface capabilities WDK Windows 2000 display", "extended surface capabilities WDK DirectDraw", "DDSCAPS2", "DD_MORESURFACECAPS"]
---

# Extended Surface Capabilities


## <span id="ddk_extended_surface_capabilities_gg"></span><span id="DDK_EXTENDED_SURFACE_CAPABILITIES_GG"></span>


Beginning with Microsoft DirectX 6.0, Microsoft DirectDraw contains surface capabilities beyond those found in previous versions. These extended capabilities require the addition of several new structures, specifically the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) and [**DD\_MORESURFACECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff551659) structures. The DDSCAPS2 structure contains the **dwCaps** member originally found in the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure, but also contains three new members: **dwCaps2**, **dwCaps3**, and **dwCaps4**. Only **dwCaps2** is used in DirectDraw for DirectX 6.0. The last three members of the **DDSCAPS2** structure are also identically arranged in the DDSCAPSEX structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Surface%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




