---
title: DirectDraw and GDI
description: DirectDraw and GDI
ms.assetid: 22106821-dac1-4c99-bf2c-c051b5a8893a
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

<span id="DrvDeriveSurface"></span><span id="drvderivesurface"></span><span id="DRVDERIVESURFACE"></span>[**DrvDeriveSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556188)  
A driver-implemented function that wraps a GDI driver surface around a DirectDraw driver surface, allowing any GDI drawing to DirectDraw video memory or AGP surfaces to be hardware accelerated (rather than being drawn in software via the [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) engine). Typically, if the driver already supports off-screen device bitmaps, this function should require only a few additional lines of code.

[**DrvDeriveSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556188) improves the performance of DirectDraw applications that also use GDI, and it also eliminates cursor flicker when a software cursor is used with DirectDraw or Direct3D applications.

<span id="HeapVidMemAllocAligned_and_VidMemFree"></span><span id="heapvidmemallocaligned_and_vidmemfree"></span><span id="HEAPVIDMEMALLOCALIGNED_AND_VIDMEMFREE"></span>[**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267) and [**VidMemFree**](https://msdn.microsoft.com/library/windows/hardware/ff570554)  
Driver-called functions that use the DirectDraw [*heap manager*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-heap-manager) for all [*off-screen memory*](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-off-screen-memory) management. [**DrvCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556185) should call [**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267) to request DirectDraw to allocate space for GDI bitmaps; [**DrvDeleteDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556187) should call [**VidMemFree**](https://msdn.microsoft.com/library/windows/hardware/ff570554) to free this allocation.

DirectDraw has priority over the graphics DDI portion of the driver for off-screen memory allocation. The driver should hook the DirectDraw [*DdFreeDriverMemory*](https://msdn.microsoft.com/library/windows/hardware/ff549360) callback, which allows the driver to remove GDI surfaces from off-screen memory to make space for higher priority DirectDraw surface allocations.

Both [**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267) and [**VidMemFree**](https://msdn.microsoft.com/library/windows/hardware/ff570554) are declared in *dmemmgr.h*, which ships with the Windows Driver Kit (WDK). A driver might have to define \_\_NTDDKCOMP\_\_ before including this header file.

 

 





