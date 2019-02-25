---
title: Command and Vertex Buffer Allocation
description: Command and Vertex Buffer Allocation
ms.assetid: 07666a6f-1d2e-4f30-bba8-a09b59225ecf
keywords:
- command buffers WDK Direct3D
- vertex buffers WDK Direct3D
- buffers WDK Direct3D
- allocating Direct3D buffers
- implicit vertex buffers WDK Direct3D
- explicit vertex buffers WDK Direct3D
- DDSCAPS2_VERTEXBUFFER
- DDSCAPS2_COMMANDBUFFER
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command and Vertex Buffer Allocation


## <span id="ddk_command_and_vertex_buffer_allocation_gg"></span><span id="DDK_COMMAND_AND_VERTEX_BUFFER_ALLOCATION_GG"></span>


There are three types of buffers used in Direct3D:

-   Implicit vertex buffers, which are created for internal use only; that is, applications are unaware of them. One implicit vertex buffer is always created after context creation and Direct3D stores vertex data in them.

-   Explicit vertex buffers, which are created only in response to an application request. Direct3D then stores vertex data in explicit vertex buffers.

-   Command buffers, which are created for internal use only; that is, applications are unaware of command buffers. Direct3D stores command data in command buffers.

Implicit vertex buffers are special vertex buffers used internally by Direct3D for batching. They are created during device initialization and can be multibuffered. They are always read/write so they should not be put in video memory (for Microsoft DirectX 6.0 and the later versions). This type of buffer is marked by the absence of both the DDSCAPS2\_VERTEXBUFFER and DDSCAPS2\_COMMANDBUFFER flags.

Explicit vertex buffers are created and controlled by the application. These cannot be multibuffered and cannot be put into local or nonlocal video memory unless the DDSCAPS\_WRITEONLY flag is set. Explicit vertex buffers are marked with DDSCAPS\_VERTEXBUFFER.

Command buffers are used by Direct3D to batch commands. They can be multibuffered and are used for all APIs except for TLVERTEX or unclipped execute-buffer API calls. This type of buffer is marked by the flag DDSCAPS2\_COMMANDBUFFER. They are always write-only, though no explicit flag is set and they never contain invalid instructions.

By default, the Direct3D runtime allocates all of these buffers. Implicit vertex buffers and command buffers are accessed through the surfaces with which they are associated. All buffers are passed to the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback.

### <span id="Driver-Allocated_Vertex_and_Command_Buffers"></span><span id="driver-allocated_vertex_and_command_buffers"></span><span id="DRIVER-ALLOCATED_VERTEX_AND_COMMAND_BUFFERS"></span>Driver-Allocated Vertex and Command Buffers

A Direct3D driver optionally performs the allocation of vertex and command buffers by supplying callback functions. To supply these callback functions, the Direct3D driver fills out a [**DD\_D3DBUFCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550557) structure and points the **lpD3DBufCallbacks** member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to it. DD\_HALINFO is returned by [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) in response to the initialization of the DirectDraw component of the driver. The callbacks reported in the DD\_D3DBUFCALLBACKS structure are:

-   [*CanCreateD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff539361)

-   [*CreateD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff540616)

-   [*DestroyD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff552754)

-   [*LockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff568216)

-   [*UnlockD3DBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff570106)

These functions are called in the same way as the *DdXxxSurface* callbacks (such as [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213)) and only when the DDSCAPS\_EXECUTEBUFFER flag is set. The buffer creation flags are DDSCAPS\_WRITEONLY, DDSCAPS2\_VERTEXBUFFER, and DDSCAPS2\_COMMANDBUFFER.

Drivers determine the type of buffer being requested by checking the **ddsCaps** member of the [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733) structure passed to the **CanCreateExecuteBuffer** and **CreateExecuteBuffer** callback for the following flags:

-   DDSCAPS\_VERTEXBUFFER indicates that the driver should allocate an explicit vertex buffer.

-   DDSCAPS\_COMMANDBUFFER indicates that the driver should allocate a command buffer.

-   If neither flag is set, the driver should allocate an implicit vertex buffer.

The driver internally allocates vertex and command buffers and cycles through these buffers. Direct3D fills a given pair while the hardware asynchronously renders from the other queued buffers. This is very useful with direct memory access (DMA).

Buffers in a multibuffering set can be in different memory types, that is, in system or video memory. When the driver is called to create the first buffer, it creates the set immediately and returns the first buffer in the set to Direct3D. The driver uses flags to specify the type of memory that it used to allocate each buffer in the set. The driver should return a new buffer in system memory for each call to [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) if the D3DHALDP2\_SWAPVERTEXBUFFER or D3DHALDP2\_SWAPCOMMANDBUFFER flag is set. If the returned buffer is in video memory, the corresponding D3DHALDP2\_VIDMEMVERTEXBUF or D3DHALDP2\_VIDMEMCOMMANDBUF flag should be set.

Occasionally, Direct3D requests the minimum size for the next buffer. If the size is too large, the driver should allocate the buffer in system memory (a backing surface). If the size is too small, the driver is permitted to provide a larger buffer. The driver should keep track of how many buffers and what memory types they are and clean up everything on exit.

 

 





