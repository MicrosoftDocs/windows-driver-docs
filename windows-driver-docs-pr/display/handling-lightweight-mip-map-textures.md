---
title: Handling Lightweight MIP Map Textures
description: Handling Lightweight MIP Map Textures
keywords:
- MIP map textures WDK DirectX 9.0 , lightweight
- lightweight MIP-map textures WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Lightweight MIP Map Textures


## <span id="ddk_handling_lightweight_mip_map_textures_gg"></span><span id="DDK_HANDLING_LIGHTWEIGHT_MIP_MAP_TEXTURES_GG"></span>


Because the MIP sublevels of lightweight MIP-map textures are implicit and do not have corresponding DirectDraw surface structures ([**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local), [**DD\_SURFACE\_GLOBAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_global) and [**DD\_SURFACE\_MORE**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_more)), a DirectX 9.0 version driver can determine if a MIP-map texture is lightweight and thus avoid creating unnecessary driver surface structures to save memory. To determine if a MIP-map texture is lightweight, the driver verifies if the DDSCAPS3\_LIGHTWEIGHTMIPMAP bit in the **dwCaps3** member of the DDSCAPSEX ([**DDSCAPS2**](/previous-versions/windows/hardware/drivers/ff550292(v=vs.85))) structure for the texture surface is set.

Note that all MIP-map textures in DirectX 9.0 are lightweight by default.

The DirectX 9.0 version driver observes the following rules when handling lightweight and heavyweight MIP-map textures:

-   A DirectX 9.0 and later driver can receive a D3DDP2OP\_TEXBLT operation code in which the source MIP-map texture is heavyweight and the destination MIP-map texture is lightweight or vice versa. Of course, the driver can also receive a D3DDP2OP\_TEXBLT in which both source and destination MIP-map textures are lightweight.

-   Because a system memory lightweight MIP-map texture consumes only a single surface of memory, the entire MIP map is visible to the driver within the top-level surface. The driver is never required to perform a texture operation directly from a system memory lightweight MIP-map texture. Such a MIP-map texture can only be the source of a D3DDP2OP\_TEXBLT.

-   The following MIP-mapped textures must be heavyweight because locks and direct writes to video or [AGP](agp-support.md) memory corresponding to each sublevel are possible with such textures:

    -   Render target
    -   Depth stencil
    -   Dynamic
    -   Vendor formatted

    Therefore, a full surface data structure is required per sublevel.

-   Because a video or AGP memory lightweight MIP-map texture is never locked or referenced by other DDIs, such as [*DdBlt*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt), the driver determines the sublevel placement for such a MIP-map texture. Therefore, full surfaces (explicit **fpVidmem** members of the [**DD\_SURFACE\_GLOBAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_global) structure) for the sublevels of such a MIP-map texture are not required.

-   Driver-managed lightweight MIP-map textures are also restricted to a single surface and must use exactly the same layout that Direct3D uses with system memory lightweight MIP-map textures. Note that this has no adverse effect (other than implementation cost) because the corresponding resident (video and AGP) MIP-map textures can have their own implementation-specific layout.

 

