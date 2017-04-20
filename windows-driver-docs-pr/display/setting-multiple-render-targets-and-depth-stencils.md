---
title: Setting Multiple Render Targets and Depth Stencils
description: Setting Multiple Render Targets and Depth Stencils
ms.assetid: 98acd448-0b65-4a3a-9e95-8e753729a7d7
keywords:
- render targets WDK DirectX 9.0 , multiple
- multiple render targets WDK DirectX 9.0
- depth stencils WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Multiple Render Targets and Depth Stencils


## <span id="ddk_setting_multiple_render_targets_and_depth_stencils_gg"></span><span id="DDK_SETTING_MULTIPLE_RENDER_TARGETS_AND_DEPTH_STENCILS_GG"></span>


A DirectX 9.0 version driver must process D3DDP2OP\_SETRENDERTARGET2 and D3DDP2OP\_SETDEPTHSTENCIL operation codes in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function even if it does not support [rendering to multiple targets simultaneously](rendering-to-multiple-targets-simultaneously.md). [**D3DHAL\_DP2SETRENDERTARGET2**](https://msdn.microsoft.com/library/windows/hardware/ff545785) and [**D3DHAL\_DP2SETDEPTHSTENCIL**](https://msdn.microsoft.com/library/windows/hardware/ff545724) structures respectively follow these codes in the [command stream](command-stream.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20Multiple%20Render%20Targets%20and%20Depth%20Stencils%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




