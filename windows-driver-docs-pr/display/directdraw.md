---
title: DirectDraw
description: DirectDraw
ms.assetid: b7f1194e-0f5e-444e-a71c-6a4a836547d9
keywords:
- DirectDraw WDK Windows 2000 display
- Windows 2000 display driver model WDK , DirectDraw
- display driver model WDK Windows 2000 , DirectDraw
- header files WDK DirectDraw
- DirectDraw WDK Windows 2000 display , header files
- drawing WDK DirectDraw
- drawing WDK DirectDraw , header files
- graphics WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectDraw


## <span id="ddk_directdraw_gg"></span><span id="DDK_DIRECTDRAW_GG"></span>


This section describes the Microsoft DirectDraw interface and architecture, and provides implementation guidelines for DirectDraw driver writers. The guidelines are written for Microsoft Windows 2000 and later. The reader should be familiar with the DirectDraw APIs, and have a firm grasp of the Windows 2000 display driver model.

Driver writers who are creating Microsoft DirectDraw drivers for Microsoft Windows 2000 and later should use the following header files:

-   *ddrawint.h* contains the basic types, constants, and structures for DirectDraw drivers.

-   *ddraw.h* contains the basic types, constants, and structures used by both applications and drivers.

-   *dvp.h* is used when the driver supports the DirectDraw video port extensions (VPE).

-   *dxmini.h* is used when the video miniport driver includes support for kernel-mode video transport, the DxApi interface (functions specified by the [**DXAPI\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff557395) structure).

-   *ddkmapi.h* is used by video capture drivers to access the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function. DirectDraw, in turn, calls upon the DxApi interface.

-   *dmemmgr.h* is used when the driver wants to perform its own memory management instead of relying on the DirectDraw runtime.

-   *ddkernel.h* is used when the driver includes kernel-mode support.

-   *dx95type.h* allows driver writers to easily port existing Windows 98/Me drivers to Windows 2000 and later. This header file maps names that are different on the two platforms.

The *ddraw.h* header file is shipped with the Windows SDK; all other header files are included with the Windows Driver Kit (WDK). The Windows Driver Development Kit (DDK) also contains sample code for a DirectDraw driver in the *p3samp* video display directory.

Reference pages for DirectDraw driver functions, callbacks, and structures can be found in [DirectDraw Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff553825) and [DirectDraw Driver Structures](https://msdn.microsoft.com/library/windows/hardware/ff553831).

For more information about DirectDraw, see the Windows SDK. DirectDraw driver writers can send questions and comments by email to <em>directx@microsoft.com</em>.

 

 





