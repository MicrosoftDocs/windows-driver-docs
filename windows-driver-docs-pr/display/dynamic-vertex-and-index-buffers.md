---
title: Dynamic Vertex and Index Buffers
description: Dynamic Vertex and Index Buffers
ms.assetid: 81ee22c6-3f98-4767-a4cd-a7907ed8f8a2
keywords:
- dynamic vertex WDK DirectX 9.0
- index buffers WDK DirectX 9.0
- dynamic buffers WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Vertex and Index Buffers


## <span id="ddk_dynamic_vertex_and_index_buffers_gg"></span><span id="DDK_DYNAMIC_VERTEX_AND_INDEX_BUFFERS_GG"></span>


A dynamic vertex or index buffer is a resource that an application frequently locks and writes to. When a dynamic buffer is locked in a call to the driver's [*LockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff568216) function, the DDLOCK\_OKTOSWAP bit (also known as the D3DLOCK\_DISCARD bit) of the **dwFlags** member of the DD\_LOCKDATA structure can be set to indicate that the caller does not require the existing contents of the buffer. Therefore, the driver can discard the contents before returning the pointer to the buffer data. Because the caller does not require the existing contents, the driver can rename the buffer by setting the **fpVidMem** member of the DD\_SURFACE\_GLOBAL structure for the buffer to a new value. By renaming the buffer (that is, setting up multiple buffering), the driver avoids hardware stalling.

The DDLOCK\_OKTOSWAP bit can only be set to lock dynamic buffers and never to lock static buffers.

Note that drivers should store dynamic buffers in [AGP](agp-support.md) memory because if dynamic buffers are stored in local video memory and an application writes data into those buffers in a nonsequential manner, bus performance might be seriously affected.

 

 





