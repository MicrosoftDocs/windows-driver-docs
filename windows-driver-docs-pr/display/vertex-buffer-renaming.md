---
title: Vertex Buffer Renaming
description: Vertex Buffer Renaming
ms.assetid: b76552b4-77a9-43f4-984b-10de92dffa83
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, renaming
- vertex buffers WDK DirectX 8.0 , renaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vertex Buffer Renaming


## <span id="ddk_vertex_buffer_renaming_gg"></span><span id="DDK_VERTEX_BUFFER_RENAMING_GG"></span>


To improve parallelism between the driver and the runtime, Direct3D supports the concept of vertex buffer "renaming". Essentially, this is a double buffering scheme for vertex buffers. In certain circumstances a driver can, when passed a vertex buffer through a DDI call, modify the video memory pointer of the vertex buffer. In this way, the driver can continue to process the contents of the vertex buffer, while, at the same time, the application can lock and fill the vertex buffer. As far as the application is concerned it is using the same vertex buffer. The fact that the memory pointed to by that vertex buffer has been modified is hidden by the runtime and driver.

Although previous versions of DirectX supported vertex buffer renaming there have been certain changes with DirectX 8.0. In previous versions of Direct3D, renaming was primarily accomplished via the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) DDI entry point. Flags specified in [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) would specify whether the driver could swap the vertex or command buffer and if so, what the required sizes of the buffers would be. However, in DirectX 8.0, vertex buffer swapping is not accomplished through *D3dDrawPrimitives2* (although calls through legacy interfaces still exploit this mechanism) but rather through the *LockExecuteBuffer* ([*LockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff568216)) DDI entry point.

DirectX 8.0 defines a new lock flag, D3DLOCK\_DISCARD, that, when passed to the driver, indicates that the caller does not require the existing contents of the driver and hence they can be discarded before returning the pointer to the vertex buffer data. Hence, when the driver receives a vertex buffer lock call with the D3DLOCK\_DISCARD flag set, it can choose to rename the vertex buffer by setting the **fpVidMem** to a new value.

Note that the D3DLOCK\_DISCARD flag will not be passed to the driver by the initial retail release of Windows 2000. The flag will be passed on Windows 2000 Service Pack 1 (SP1) and all subsequent versions of Windows 2000.

In DirectX 7.0, vertex buffer renaming could also be accomplished via *LockExecuteBuffer* using the flag DDLOCK\_DISCARDCONTENTS. However, the synchronization between runtime and driver on the original release of DirectX 7.0 prevents this mechanism from working correctly. However, the version of DirectX 7.0 released with DirectX 8.0 corrects this problem and vertex buffer renaming at lock time are functional through DirectX 7.0 interfaces.

 

 





