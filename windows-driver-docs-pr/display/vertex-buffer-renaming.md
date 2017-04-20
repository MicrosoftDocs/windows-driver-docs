---
title: Vertex Buffer Renaming
description: Vertex Buffer Renaming
ms.assetid: b76552b4-77a9-43f4-984b-10de92dffa83
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, renaming
- vertex buffers WDK DirectX 8.0 , renaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vertex Buffer Renaming


## <span id="ddk_vertex_buffer_renaming_gg"></span><span id="DDK_VERTEX_BUFFER_RENAMING_GG"></span>


To improve parallelism between the driver and the runtime, Direct3D supports the concept of vertex buffer "renaming". Essentially, this is a double buffering scheme for vertex buffers. In certain circumstances a driver can, when passed a vertex buffer through a DDI call, modify the video memory pointer of the vertex buffer. In this way, the driver can continue to process the contents of the vertex buffer, while, at the same time, the application can lock and fill the vertex buffer. As far as the application is concerned it is using the same vertex buffer. The fact that the memory pointed to by that vertex buffer has been modified is hidden by the runtime and driver.

Although previous versions of DirectX supported vertex buffer renaming there have been certain changes with DirectX 8.0. In previous versions of Direct3D, renaming was primarily accomplished via the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) DDI entry point. Flags specified in [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) would specify whether the driver could swap the vertex or command buffer and if so, what the required sizes of the buffers would be. However, in DirectX 8.0, vertex buffer swapping is not accomplished through *D3dDrawPrimitives2* (although calls through legacy interfaces still exploit this mechanism) but rather through the *LockExecuteBuffer* ([*LockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff568216)) DDI entry point.

DirectX 8.0 defines a new lock flag, D3DLOCK\_DISCARD, that, when passed to the driver, indicates that the caller does not require the existing contents of the driver and hence they can be discarded before returning the pointer to the vertex buffer data. Hence, when the driver receives a vertex buffer lock call with the D3DLOCK\_DISCARD flag set, it can choose to rename the vertex buffer by setting the **fpVidMem** to a new value.

Note that the D3DLOCK\_DISCARD flag will not be passed to the driver by the initial retail release of Windows 2000. The flag will be passed on Windows 2000 Service Pack 1 (SP1) and all subsequent versions of Windows 2000.

In DirectX 7.0, vertex buffer renaming could also be accomplished via *LockExecuteBuffer* using the flag DDLOCK\_DISCARDCONTENTS. However, the synchronization between runtime and driver on the original release of DirectX 7.0 prevents this mechanism from working correctly. However, the version of DirectX 7.0 released with DirectX 8.0 corrects this problem and vertex buffer renaming at lock time are functional through DirectX 7.0 interfaces.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20Buffer%20Renaming%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




