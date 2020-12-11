---
title: DirectDraw and GDI
description: DirectDraw and GDI
keywords:
- display drivers WDK Windows 2000 , DirectDraw
- DirectDraw WDK Windows 2000 display , GDI
- GDI DirectDraw support WDK Windows 2000 display
- display drivers WDK Windows 2000 , graphics
- graphics WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectDraw and GDI


## <span id="ddk_directdraw_and_gdi_gg"></span><span id="DDK_DIRECTDRAW_AND_GDI_GG"></span>


GDI automatically enables DirectDraw when the display driver is initialized. To provide better interaction between DirectDraw and the graphics DDI portion of the driver, a driver that also supports the DirectDraw DDI can implement or call the following functions:

<span id="DrvDeriveSurface"></span><span id="drvderivesurface"></span><span id="DRVDERIVESURFACE"></span>[**DrvDeriveSurface**](/windows/win32/api/winddi/nf-winddi-drvderivesurface)  
A driver-implemented function that wraps a GDI driver surface around a DirectDraw driver surface, allowing any GDI drawing to DirectDraw video memory or AGP surfaces to be hardware accelerated (rather than being drawn in software via the *DIB* engine). Typically, if the driver already supports off-screen device bitmaps, this function should require only a few additional lines of code.

[**DrvDeriveSurface**](/windows/win32/api/winddi/nf-winddi-drvderivesurface) improves the performance of DirectDraw applications that also use GDI, and it also eliminates cursor flicker when a software cursor is used with DirectDraw or Direct3D applications.

<span id="HeapVidMemAllocAligned_and_VidMemFree"></span><span id="heapvidmemallocaligned_and_vidmemfree"></span><span id="HEAPVIDMEMALLOCALIGNED_AND_VIDMEMFREE"></span>[**HeapVidMemAllocAligned**](/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned) and [**VidMemFree**](/windows/win32/api/dmemmgr/nf-dmemmgr-vidmemfree)  

Driver-called functions that use the DirectDraw *heap manager* for all [*off-screen memory*](video-present-network-terminology.md#off_screen_memory) management. [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) should call [**HeapVidMemAllocAligned**](/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned) to request DirectDraw to allocate space for GDI bitmaps; [**DrvDeleteDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvdeletedevicebitmap) should call [**VidMemFree**](/windows/win32/api/dmemmgr/nf-dmemmgr-vidmemfree) to free this allocation.

DirectDraw has priority over the graphics DDI portion of the driver for off-screen memory allocation. The driver should hook the DirectDraw [*DdFreeDriverMemory*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_freedrivermemory) callback, which allows the driver to remove GDI surfaces from off-screen memory to make space for higher priority DirectDraw surface allocations.

Both [**HeapVidMemAllocAligned**](/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned) and [**VidMemFree**](/windows/win32/api/dmemmgr/nf-dmemmgr-vidmemfree) are declared in *dmemmgr.h*, which ships with the Windows Driver Kit (WDK). A driver might have to define \_\_NTDDKCOMP\_\_ before including this header file.

 

