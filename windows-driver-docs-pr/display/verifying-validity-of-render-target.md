---
title: Verifying Validity of Render Target
description: Verifying Validity of Render Target
ms.assetid: 316ecd58-996a-4277-b2dc-4424c96d8a56
keywords:
- render targets WDK DirectX 9.0 , verifying validity
- validating render targets WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Verifying Validity of Render Target


## <span id="ddk_verifying_validity_of_render_target_gg"></span><span id="DDK_VERIFYING_VALIDITY_OF_RENDER_TARGET_GG"></span>


A DirectX 9.0 version driver must verify whether its internal render target is valid before using the render target because the DirectX 9.0 runtime permits applications to set render targets to **NULL**. In contrast, DirectX 8.1 and earlier runtimes guarantee that render targets are always valid for a Direct3D context.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Verifying%20Validity%20of%20Render%20Target%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




