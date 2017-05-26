---
title: Vertex Buffer Creation Handling on Windows 2000
description: Vertex Buffer Creation Handling on Windows 2000
ms.assetid: 4155a4c6-cbac-4a75-8ddf-5983fe5099c6
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, creation handling
- vertex buffers WDK DirectX 8.0 , creation handling on Windows 2000
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vertex Buffer Creation Handling on Windows 2000


## <span id="ddk_vertex_buffer_creation_handling_on_windows_2000_gg"></span><span id="DDK_VERTEX_BUFFER_CREATION_HANDLING_ON_WINDOWS_2000_GG"></span>


In DirectX 8.0, vertex (and index) buffers can be managed as textures were in DirectX 7.0. That is, a system memory copy of a vertex buffer is maintained at all times and a video memory copy is only allocated when that vertex buffer is actually required.

If the driver does not allocate a vertex buffer in video memory but, instead, requires the runtime to allocate the buffer in system memory, it should not return DDHAL\_DRIVER\_NOTHANDLED but rather should return DDHAL\_DRIVER\_HANDLED and indicate failure by setting a **ddRVal** of E\_FAIL. If the driver returns DDHAL\_DRIVER\_NOTHANDLED, the runtime attempts to allocate the surface from the video memory heaps returned by the driver. This may either fail and return an error to the application or result in the surface being allocated in local or nonlocal video memory (which is not the intention).

Therefore, if you wish the runtime to allocate a vertex buffer in system memory on your behalf, set **ddRVal** to E\_FAIL and return DDHAL\_DRIVER\_HANDLED.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20Buffer%20Creation%20Handling%20on%20Windows%202000%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




