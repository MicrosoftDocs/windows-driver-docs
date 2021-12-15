---
title: Extended Surface Capabilities
description: Extended Surface Capabilities
keywords:
- drawing extended surface capabilities WDK DirectDraw , about extended surface capabilities
- DirectDraw extended surface capabilities WDK Windows 2000 display , about extended surface capabilities
- extended surface capabilities WDK DirectDraw , about extended surface capabilities
- surfaces WDK DirectDraw , extended capabilities
- drawing extended surface capabilities WDK DirectDraw
- DirectDraw extended surface capabilities WDK Windows 2000 display
- extended surface capabilities WDK DirectDraw
- DDSCAPS2
- DD_MORESURFACECAPS
ms.date: 04/20/2017
---

# Extended Surface Capabilities


## <span id="ddk_extended_surface_capabilities_gg"></span><span id="DDK_EXTENDED_SURFACE_CAPABILITIES_GG"></span>


Beginning with Microsoft DirectX 6.0, Microsoft DirectDraw contains surface capabilities beyond those found in previous versions. These extended capabilities require the addition of several new structures, specifically the [**DDSCAPS2**](/previous-versions/windows/hardware/drivers/ff550292(v=vs.85)) and [**DD\_MORESURFACECAPS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_moresurfacecaps) structures. The DDSCAPS2 structure contains the **dwCaps** member originally found in the [**DDSCAPS**](/previous-versions/windows/hardware/drivers/ff550286(v=vs.85)) structure, but also contains three new members: **dwCaps2**, **dwCaps3**, and **dwCaps4**. Only **dwCaps2** is used in DirectDraw for DirectX 6.0. The last three members of the **DDSCAPS2** structure are also identically arranged in the DDSCAPSEX structure.

 

