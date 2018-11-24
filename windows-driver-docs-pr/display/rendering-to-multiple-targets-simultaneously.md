---
title: Rendering to Multiple Targets Simultaneously
description: Rendering to Multiple Targets Simultaneously
ms.assetid: 72c56ea6-d5da-420a-91f4-c7fa09daf67e
keywords:
- rendering multiple targets WDK DirectX 9.0
- multiple render targets WDK DirectX 9.0
- simultaneous render targets WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rendering to Multiple Targets Simultaneously


## <span id="ddk_rendering_to_multiple_targets_simultaneously_gg"></span><span id="DDK_RENDERING_TO_MULTIPLE_TARGETS_SIMULTANEOUSLY_GG"></span>


A DirectX 9.0 version driver can render to multiple targets simultaneously if the driver indicates that its device supports multiple render targets. To indicate the number of render targets that the device supports, the driver sets this number in the **NumSimultaneousRTs** member of the D3DCAPS9 structure. The driver must set this number to 1, if only rendering to a single target is supported. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

Render targets in a multiple render target group must have identical dimensions but can have different surface formats.

The driver receives the D3DDP2OP\_SETRENDERTARGET2 operation code if an application requests to set the color buffer for one of the render targets in the multiple group.

If the DirectX 9.0 driver supports rendering to multiple targets simultaneously, it must support certain features and can support extended features. The following topics describe these required and optional features:

[Required Features for Multiple Render Targets](required-features-for-multiple-render-targets.md)

[Optional Features for Multiple Render Targets](optional-features-for-multiple-render-targets.md)

 

 





