---
title: Dynamic Vertex and Index Buffers
description: Dynamic Vertex and Index Buffers
ms.assetid: 81ee22c6-3f98-4767-a4cd-a7907ed8f8a2
keywords: ["dynamic vertex WDK DirectX 9.0", "index buffers WDK DirectX 9.0", "dynamic buffers WDK DirectX 9.0"]
---

# Dynamic Vertex and Index Buffers


## <span id="ddk_dynamic_vertex_and_index_buffers_gg"></span><span id="DDK_DYNAMIC_VERTEX_AND_INDEX_BUFFERS_GG"></span>


A dynamic vertex or index buffer is a resource that an application frequently locks and writes to. When a dynamic buffer is locked in a call to the driver's [*LockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff568216) function, the DDLOCK\_OKTOSWAP bit (also known as the D3DLOCK\_DISCARD bit) of the **dwFlags** member of the DD\_LOCKDATA structure can be set to indicate that the caller does not require the existing contents of the buffer. Therefore, the driver can discard the contents before returning the pointer to the buffer data. Because the caller does not require the existing contents, the driver can rename the buffer by setting the **fpVidMem** member of the DD\_SURFACE\_GLOBAL structure for the buffer to a new value. By renaming the buffer (that is, setting up multiple buffering), the driver avoids hardware stalling.

The DDLOCK\_OKTOSWAP bit can only be set to lock dynamic buffers and never to lock static buffers.

Note that drivers should store dynamic buffers in [AGP](agp-support.md) memory because if dynamic buffers are stored in local video memory and an application writes data into those buffers in a nonsequential manner, bus performance might be seriously affected.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Dynamic%20Vertex%20and%20Index%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




