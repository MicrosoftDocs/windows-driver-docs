---
title: Supporting Vertex Elements Sharing Offset in a Stream
description: Supporting Vertex Elements Sharing Offset in a Stream
ms.assetid: 52b2d891-15a1-4b82-aaf2-634f33202974
keywords:
- vertex shader declarations WDK DirectX 9.0 , sharing the offset in a stream
- shader declarations WDK DirectX 9.0 , sharing the offset in a stream
- vertex stream offsets WDK DirectX 9.0
- vertex stream offsets WDK DirectX 9.0 , vertex shader declarations
- stream offsets WDK DirectX 9.0
- stream offsets WDK DirectX 9.0 , vertex shader declarations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Vertex Elements Sharing Offset in a Stream


## <span id="ddk_supporting_vertex_elements_sharing_offset_in_a_stream_gg"></span><span id="DDK_SUPPORTING_VERTEX_ELEMENTS_SHARING_OFFSET_IN_A_STREAM_GG"></span>


A DirectX 9.0 version driver indicates that its device lets multiple vertex elements share the same offset in a stream by setting the D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET capability bit in the **DevCaps2** member of the D3DCAPS9 structure. A vertex shader declaration consists of an array of vertex elements. For more information, see [Separating Declarations and Code for Vertex Shaders](separating-declarations-and-code-for-vertex-shaders.md).

If a DirectX 9.0 driver for a device that supports pixel shader (PS) versions earlier than 3.0 sets D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET, the driver can handle most vertex declarations with elements that specify the D3DDECLUSAGE\_POSITIONT (0) usage type. This pre PS 3.0-driver converts vertex declarations with D3DDECLUSAGE\_POSITIONT (0) to valid flexible vertex format (FVF). However, this pre PS 3.0-driver cannot handle vertex declarations with elements that specify the D3DDECLUSAGE\_POSITIONT (0) usage type if the declarations have gaps in texture coordinates. For example, this pre PS 3.0-driver cannot handle the following vertex declaration:

```cpp
{0,0,D3DDECLTYPE_FLOAT4, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITIONT, 0}
{0,16,D3DDECLTYPE_FLOAT2, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_TEXCOORD, 0}
{0,24,D3DDECLTYPE_FLOAT2, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_TEXCOORD, 5}
```

Because there is a gap in the texture coordinates, this pre PS 3.0-driver cannot express the D3DDECLUSAGE\_TEXCOORD elements using FVF.

If a DirectX 9.0 driver for a device that supports pixel shader 3.0 and later sets D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET, the driver must handle all vertex declarations with elements that specify the D3DDECLUSAGE\_POSITIONT (0) usage type. This driver must let multiple vertex elements:

-   Share the same offset in a stream.

-   Be different types. Therefore, they can have different sizes.

-   Overlap arbitrarily. For example, one element can start at a location of a stream that is currently in the middle of another element.

 

 





