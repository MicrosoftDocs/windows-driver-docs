---
title: D3dCreateSurfaceEx and MIP Maps
description: D3dCreateSurfaceEx and MIP Maps
ms.assetid: d0f4ee41-7622-4153-877c-17c88f8147a9
keywords: ["MIP map surfaces WDK Direct3D", "context WDK Direct3D , D3dCreateSurfaceEx", "D3dCreateSurfaceEx"]
---

# D3dCreateSurfaceEx and MIP Maps


## <span id="ddk_d3dcreatesurfaceex_and_mip_maps_gg"></span><span id="DDK_D3DCREATESURFACEEX_AND_MIP_MAPS_GG"></span>


Each level in a MIP map is associated with a different handle value. These handles might not be consecutive, however. The Direct3D DDI is designed so that only the top-level surface's handle is passed as an argument in the **IDirect3DDevice7::SetTexture** API method (described in the Direct3D SDK documentation), and then the current level-of-detail is specified by a texture stage state (D3DTSS\_MAXMIPLEVEL). The most natural way to work with MIP maps is to build one driver-side structure that represents the entire MIP map.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3dCreateSurfaceEx%20and%20MIP%20Maps%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




