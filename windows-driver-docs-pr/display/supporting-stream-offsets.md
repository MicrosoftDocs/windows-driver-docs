---
title: Supporting Stream Offsets
description: Supporting Stream Offsets
ms.assetid: 2c2ca906-8685-47f5-a2ca-855394b9674f
keywords:
- stream offsets WDK DirectX 9.0
- vertex stream offsets WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Stream Offsets


## <span id="ddk_supporting_stream_offsets_gg"></span><span id="DDK_SUPPORTING_STREAM_OFFSETS_GG"></span>


A DirectX 9.0 version driver must support letting applications store vertex data of multiple vertex formats in a single vertex data stream. Applications notify the driver of where vertex data of a particular format is located in the vertex data stream by supplying the *stream offset*, in bytes, to the beginning of that vertex data. To support stream offset, the driver must process the D3DDP2OP\_SETSTREAMSOURCE2 operation code in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. A [**D3DHAL\_DP2SETSTREAMSOURCE2**](https://msdn.microsoft.com/library/windows/hardware/ff545801) structure, which follows the operation code in the [command stream](command-stream.md), is used to specify the stream and the offset to where vertex data is located.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Stream%20Offsets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




