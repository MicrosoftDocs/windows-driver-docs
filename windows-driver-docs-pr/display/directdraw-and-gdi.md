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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectDraw%20and%20GDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




