---
title: Stream Zero
description: Stream Zero
ms.assetid: d6f0a625-c594-45b6-a229-b9c8a5275002
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
- stream zero WDK DirectX 8.0
- vertex stream zero WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stream Zero


## <span id="ddk_stream_zero_gg"></span><span id="DDK_STREAM_ZERO_GG"></span>


Vertex stream zero is treated differently from the other streams because it is the only stream supported by earlier versions of Direct3D. Vertex buffers that have a flexible vertex format (FVF), where the FVF field is nonzero, can only be bound to stream zero. However, this does not imply that the vertex buffer bound to stream zero always has a flexible vertex format.

Stream zero is also the implied vertex source when one of the special, fixed-function vertex shaders is the current vertex shader handle.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Stream%20Zero%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




