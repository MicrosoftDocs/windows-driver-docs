---
title: Dynamically Controlling Multiple-Sample Rendering
description: Dynamically Controlling Multiple-Sample Rendering
ms.assetid: cd0bea22-29e8-40f7-987b-5c36765e5677
keywords:
- multiple-sample rendering WDK DirectX 9.0 , dynamic control
- rendering multisamples WDK DirectX 9.0 , dynamic control
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamically Controlling Multiple-Sample Rendering


## <span id="ddk_dynamically_controlling_multiple_sample_rendering_gg"></span><span id="DDK_DYNAMICALLY_CONTROLLING_MULTIPLE_SAMPLE_RENDERING_GG"></span>


A DirectX 9.0 version driver can support the capability of alternately enabling and disabling multiple-sample rendering between the rendering of primitives. To report that the driver's device supports this capability, the driver sets the D3DPRASTERCAPS\_MULTISAMPLE\_TOGGLE capability bit in the **RasterCaps** member of the D3DCAPS9 structure. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

To toggle multiple-sample rendering on and off between begin-scene and end-scene states, the driver receives the D3DDP2OP\_RENDERSTATE operation code in the [command stream](command-stream.md) of its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. The driver processes the D3DRS\_MULTISAMPLEANTIALIAS render state from the **RenderState** member of the [**D3DHAL\_DP2RENDERSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545705) structure that is associated with this operation code. The driver determines whether to enable or disable multiple-sample rendering from the Boolean value in the **dwState** member of D3DHAL\_DP2RENDERSTATE. The value **TRUE** means to enable and **FALSE** means to disable.

If the D3DPRASTERCAPS\_MULTISAMPLE\_TOGGLE capability bit is set, the driver can receive the D3DRS\_MULTISAMPLEANTIALIAS render state between D3DRENDERSTATE\_SCENECAPTURE render states that specify **TRUE** for begin-scene information and **FALSE** for end-scene information.

 

 





