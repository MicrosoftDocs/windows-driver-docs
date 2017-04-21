---
title: Rendering to Multiple Targets Simultaneously
description: Rendering to Multiple Targets Simultaneously
ms.assetid: 72c56ea6-d5da-420a-91f4-c7fa09daf67e
keywords:
- rendering multiple targets WDK DirectX 9.0
- multiple render targets WDK DirectX 9.0
- simultaneous render targets WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rendering to Multiple Targets Simultaneously


## <span id="ddk_rendering_to_multiple_targets_simultaneously_gg"></span><span id="DDK_RENDERING_TO_MULTIPLE_TARGETS_SIMULTANEOUSLY_GG"></span>


A DirectX 9.0 version driver can render to multiple targets simultaneously if the driver indicates that its device supports multiple render targets. To indicate the number of render targets that the device supports, the driver sets this number in the **NumSimultaneousRTs** member of the D3DCAPS9 structure. The driver must set this number to 1, if only rendering to a single target is supported. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

Render targets in a multiple render target group must have identical dimensions but can have different surface formats.

The driver receives the D3DDP2OP\_SETRENDERTARGET2 operation code if an application requests to set the color buffer for one of the render targets in the multiple group.

If the DirectX 9.0 driver supports rendering to multiple targets simultaneously, it must support certain features and can support extended features. The following topics describe these required and optional features:

[Required Features for Multiple Render Targets](required-features-for-multiple-render-targets.md)

[Optional Features for Multiple Render Targets](optional-features-for-multiple-render-targets.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Rendering%20to%20Multiple%20Targets%20Simultaneously%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




