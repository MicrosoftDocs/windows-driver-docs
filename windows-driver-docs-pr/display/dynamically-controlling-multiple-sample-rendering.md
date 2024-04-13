---
title: Dynamically Controlling Multiple-Sample Rendering
description: Dynamically Controlling Multiple-Sample Rendering
keywords:
- multiple-sample rendering WDK DirectX 9.0 , dynamic control
- rendering multisamples WDK DirectX 9.0 , dynamic control
ms.date: 04/20/2017
---

# Dynamically Controlling Multiple-Sample Rendering


## <span id="ddk_dynamically_controlling_multiple_sample_rendering_gg"></span><span id="DDK_DYNAMICALLY_CONTROLLING_MULTIPLE_SAMPLE_RENDERING_GG"></span>


A DirectX 9.0 version driver can support the capability of alternately enabling and disabling multiple-sample rendering between the rendering of primitives. To report that the driver's device supports this capability, the driver sets the D3DPRASTERCAPS\_MULTISAMPLE\_TOGGLE capability bit in the **RasterCaps** member of the D3DCAPS9 structure. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

To toggle multiple-sample rendering on and off between begin-scene and end-scene states, the driver receives the D3DDP2OP\_RENDERSTATE operation code in the [command stream](command-stream.md) of its [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function. The driver processes the D3DRS\_MULTISAMPLEANTIALIAS render state from the **RenderState** member of the [**D3DHAL\_DP2RENDERSTATE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2renderstate) structure that is associated with this operation code. The driver determines whether to enable or disable multiple-sample rendering from the Boolean value in the **dwState** member of D3DHAL\_DP2RENDERSTATE. The value **TRUE** means to enable and **FALSE** means to disable.

If the D3DPRASTERCAPS\_MULTISAMPLE\_TOGGLE capability bit is set, the driver can receive the D3DRS\_MULTISAMPLEANTIALIAS render state between D3DRENDERSTATE\_SCENECAPTURE render states that specify **TRUE** for begin-scene information and **FALSE** for end-scene information.

 

