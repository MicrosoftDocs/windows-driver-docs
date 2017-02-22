---
title: High Order Surface Render States
description: High Order Surface Render States
ms.assetid: c664e0b8-8b96-4f66-bb9c-b87c5d5e7a05
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , high order surfaces, render states", "high order surfaces WDK DirectX 8.0 , render states", "render states WDK DirectX 8.0", "render states WDK DirectX 8.0 , high order surfaces"]
---

# High Order Surface Render States


## <span id="ddk_high_order_surface_render_states_gg"></span><span id="DDK_HIGH_ORDER_SURFACE_RENDER_STATES_GG"></span>


There are three render states that are used with high order surfaces. These render states are described below.

### <span id="d3drs_patchedgestyle"></span><span id="D3DRS_PATCHEDGESTYLE"></span>D3DRS\_PATCHEDGESTYLE

This render state is used to control whether patch edges use discrete or continuous tessellation. See the DirectX 8.0 SDK documentation for more details.

### <span id="d3drs_patchsegments"></span><span id="D3DRS_PATCHSEGMENTS"></span>D3DRS\_PATCHSEGMENTS

This render state gives the number of segments to be used for each edge of the patch. If an explicit number of segments is specified in the DP2 token those segments should override the value of this render state. For more details, see the DirectX 8.0 SDK documentation.

### <span id="d3drs_deletertpatch"></span><span id="D3DRS_DELETERTPATCH"></span> D3DRS\_DELETERTPATCH

This render state notifies the driver that a patch is to be deleted. For more information, see [**D3DRENDERSTATETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff549036).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20High%20Order%20Surface%20Render%20States%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




