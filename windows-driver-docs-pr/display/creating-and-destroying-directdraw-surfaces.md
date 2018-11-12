---
title: Creating and Destroying DirectDraw Surfaces
description: Creating and Destroying DirectDraw Surfaces
ms.assetid: d5557897-1810-448e-a2a8-aba96643b19c
keywords:
- drawing surfaces WDK DirectDraw , creating
- DirectDraw surfaces WDK Windows 2000 display , creating
- surfaces WDK DirectDraw , creating
- drawing surfaces WDK DirectDraw , destroying
- DirectDraw surfaces WDK Windows 2000 display , destroying
- surfaces WDK DirectDraw , destroying
- destroying surfaces WDK DirectDraw
- DdCanCreateSurface
- DdCreateSurface
- D3dCreateSurfaceEx
- DdDestroySurface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Destroying DirectDraw Surfaces


## <span id="ddk_creating_and_destroying_directdraw_surfaces_gg"></span><span id="DDK_CREATING_AND_DESTROYING_DIRECTDRAW_SURFACES_GG"></span>


Direct Draw surfaces are created in a four-stage process. These stages are:

1.  [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213). The runtime calls the driver's *DdCanCreateSurface* to see if the driver allows the creation of a surface of this type, size, and format. The driver can return a failure code that is propagated to the application.

2.  [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263). The driver creates the surface, potentially allocating memory for the contents of the surface. Complex surfaces can be created all at once, with one call to *DdCreateSurface*. Thus, the driver may be required to create many surfaces in one call.

3.  Memory allocation. The DirectDraw runtime allocates memory for any surface that is not allocated by the driver in response to the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) call. This process is covered in more detail in the following sections.

4.  [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840). This function associates a handle with the surface in question for later use in the DirectX[**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) token stream. The driver also creates its own copy of the surface structure maintained by DirectDraw at this time. For more information about **D3dCreateSurfaceEx**, see the DirectX Driver Development Kit (DDK) documentation.

**Note**   A DirectDraw driver must never directly allocate user-mode memory for a surface (for example, by calling the [**EngAllocUserMem**](https://msdn.microsoft.com/library/windows/hardware/ff564178) function). Instead, the driver can have the DirectDraw runtime allocate user-mode memory for a surface.
If the driver allocates the memory directly, a subsequent request to change the video mode by a process other than the one that created the surface, could cause an operating system crash or memory leaks. To have the DirectDraw runtime allocate user-mode memory, the driver should return the DDHAL\_PLEASEALLOC\_USERMEM value from its [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) function. For more information, see the Remarks section on the *DdCreateSurface* reference page.

 

Surfaces are destroyed by a single call to the driver's [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) entry point only if the driver allocated or was involved in allocating the memory for the surface during surface creation. If the DirectDraw runtime allocated the memory and the driver was not involved, the runtime does not call *DdDestroySurface*.

Surfaces persist only as long as the mode in which they are created persists. Where there is a mode change, all the surfaces under the driver's control are destroyed, as far as the driver is concerned. There are also other events that can cause all surfaces to be destroyed in this way. It is not necessary for the driver to determine the cause of a [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) call.

 

 





