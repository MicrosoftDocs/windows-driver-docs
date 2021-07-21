---
title: Supporting Stream Offsets
description: Supporting Stream Offsets
keywords:
- stream offsets WDK DirectX 9.0
- vertex stream offsets WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Stream Offsets


## <span id="ddk_supporting_stream_offsets_gg"></span><span id="DDK_SUPPORTING_STREAM_OFFSETS_GG"></span>


A DirectX 9.0 version driver must support letting applications store vertex data of multiple vertex formats in a single vertex data stream. Applications notify the driver of where vertex data of a particular format is located in the vertex data stream by supplying the *stream offset*, in bytes, to the beginning of that vertex data. To support stream offset, the driver must process the D3DDP2OP\_SETSTREAMSOURCE2 operation code in its [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function. A [**D3DHAL\_DP2SETSTREAMSOURCE2**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2setstreamsource2) structure, which follows the operation code in the [command stream](command-stream.md), is used to specify the stream and the offset to where vertex data is located.

 

