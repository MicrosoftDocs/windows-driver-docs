---
title: Vertex Buffer Creation Handling on Windows 2000
description: Vertex Buffer Creation Handling on Windows 2000
ms.assetid: 4155a4c6-cbac-4a75-8ddf-5983fe5099c6
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, creation handling
- vertex buffers WDK DirectX 8.0 , creation handling on Windows 2000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vertex Buffer Creation Handling on Windows 2000


## <span id="ddk_vertex_buffer_creation_handling_on_windows_2000_gg"></span><span id="DDK_VERTEX_BUFFER_CREATION_HANDLING_ON_WINDOWS_2000_GG"></span>


In DirectX 8.0, vertex (and index) buffers can be managed as textures were in DirectX 7.0. That is, a system memory copy of a vertex buffer is maintained at all times and a video memory copy is only allocated when that vertex buffer is actually required.

If the driver does not allocate a vertex buffer in video memory but, instead, requires the runtime to allocate the buffer in system memory, it should not return DDHAL\_DRIVER\_NOTHANDLED but rather should return DDHAL\_DRIVER\_HANDLED and indicate failure by setting a **ddRVal** of E\_FAIL. If the driver returns DDHAL\_DRIVER\_NOTHANDLED, the runtime attempts to allocate the surface from the video memory heaps returned by the driver. This may either fail and return an error to the application or result in the surface being allocated in local or nonlocal video memory (which is not the intention).

Therefore, if you wish the runtime to allocate a vertex buffer in system memory on your behalf, set **ddRVal** to E\_FAIL and return DDHAL\_DRIVER\_HANDLED.

 

 





