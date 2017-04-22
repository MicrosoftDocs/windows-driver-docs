---
title: Setting Scissor Rectangle
description: Setting Scissor Rectangle
ms.assetid: e85b4987-26b7-4005-b8eb-81ca36a9a777
keywords:
- scissor rectangle WDK DirectX 9.0
- rectangular clipping region WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Scissor Rectangle


## <span id="ddk_setting_scissor_rectangle_gg"></span><span id="DDK_SETTING_SCISSOR_RECTANGLE_GG"></span>


A DirectX 9.0 version driver must support setting a rectangular clipping region, that is, a scissor rectangle. After this scissor rectangle is set, rendering is restricted to just the portion of the render target that is specified by the scissor rectangle. To set a scissor rectangle, the driver must process the D3DDP2OP\_SETSCISSORRECT operation code in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. A RECT structure that specifies the rectangular clipping region follows the operation code in the [command stream](command-stream.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20Scissor%20Rectangle%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




