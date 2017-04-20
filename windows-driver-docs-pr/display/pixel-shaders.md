---
title: Pixel Shaders
description: Pixel Shaders
ms.assetid: a44c5ee8-e9a7-4f9a-9547-e0c5ae49b82c
keywords:
- pixel shaders WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pixel Shaders


## <span id="ddk_pixel_shaders_gg"></span><span id="DDK_PIXEL_SHADERS_GG"></span>


All drivers that support the DirectX 8.0 DDI may support the new DP2 token D3DDP2OP\_SETPIXELSHADER if programmable pixel shaders are supported in hardware.

D3DDP2OP\_SETPIXELSHADER can be used to notify the driver of the handle of the current programmable pixel shader to use. A pixel shader handle refers to a programmable pixel shader handle previously created by means of the D3DDP2OP\_CREATEPIXELSHADER DP2 token.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Pixel%20Shaders%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




