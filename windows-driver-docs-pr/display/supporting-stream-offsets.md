---
title: Supporting Stream Offsets
description: Supporting Stream Offsets
ms.assetid: 2c2ca906-8685-47f5-a2ca-855394b9674f
keywords:
- stream offsets WDK DirectX 9.0
- vertex stream offsets WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Stream Offsets


## <span id="ddk_supporting_stream_offsets_gg"></span><span id="DDK_SUPPORTING_STREAM_OFFSETS_GG"></span>


A DirectX 9.0 version driver must support letting applications store vertex data of multiple vertex formats in a single vertex data stream. Applications notify the driver of where vertex data of a particular format is located in the vertex data stream by supplying the *stream offset*, in bytes, to the beginning of that vertex data. To support stream offset, the driver must process the D3DDP2OP\_SETSTREAMSOURCE2 operation code in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. A [**D3DHAL\_DP2SETSTREAMSOURCE2**](https://msdn.microsoft.com/library/windows/hardware/ff545801) structure, which follows the operation code in the [command stream](command-stream.md), is used to specify the stream and the offset to where vertex data is located.

 

 





