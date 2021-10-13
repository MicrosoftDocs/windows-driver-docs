---
title: Managing PDEVs
description: Managing PDEVs
keywords:
- PDEV WDK DirectDraw
- drawing WDK DirectDraw , PDEV
- DirectDraw WDK Windows 2000 display , PDEV
- disabled PDEV WDK DirectDraw
- enabled PDEV WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing PDEVs


## <span id="ddk_managing_pdevs_gg"></span><span id="DDK_MANAGING_PDEVS_GG"></span>


**This topic applies only to Windows 2000 and later.**

The number of threads that call into a display driver is dependent on the number of existing PDEVs on a device. Each device has a maximum of one enabled PDEV per adapter output and an unlimited number of disabled PDEVs. A PDEV is disabled or enabled by calling the driver's [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) function. When a display driver manages a mix of disabled and enabled PDEVs, the operating system permits a single thread to call a driver function with an enabled PDEV while simultaneously permitting multiple threads to call driver functions with disabled PDEVs. For example, [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt) could be running on the enabled PDEV while another disabled PDEV is being destroyed by [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface). Even if a single display driver manages multiple enabled PDEVs, (for example, in a multiple monitor scenario), the operating system still only lets a single thread call into driver code with any of those enabled PDEVs.

If the display driver must manage any global resources and hardware states that are shared between PDEVs, the display driver must also handle any necessary synchronization. The display driver is mapped into session space, so each session has its own set of global variables. Therefore, you must not use a display driver global variable to hold a synchronization object such as a mutex. Instead, store the mutex in the device extension of the video miniport driver, which is mapped into global space not session space. You can initialize the mutex in the video miniport driver's [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) function. Then, the display driver's [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function can obtain a pointer to the mutex by sending a custom IOCTL to the video miniport driver. Display driver threads that belong to different sessions will have separate copies of the pointer, but all of those copies will point to the same mutex object.

The display driver is not allowed to directly call the kernel routines that acquire and release a mutex, so the display driver must rely on the video miniport driver to perform those tasks. The video miniport driver could implement a function that acquires and releases the mutex, and the display driver could obtain a pointer to that function in the same custom IOCTL that it uses to obtain a pointer to the mutex itself.

Only the following limited number of driver functions can be called with a disabled PDEV:

-   [*DdMapMemory*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mapmemory) (for unmapping memory only)

-   [**DrvDisableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvdisabledirectdraw)

-   [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) (for system memory only)

-   [**D3dDestroyDDLocal**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_destroyddlocal)

-   [**D3dContextCreate**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextcreatecb)

-   [**D3dContextDestroy**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb)

-   [*DdDestroySurface*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_destroysurface)

-   [*DdLock*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_lock)

-   [*DdUnlock*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_unlock)

-   [*DestroyD3DBuffer*](/previous-versions/windows/hardware/drivers/ff552754(v=vs.85))

-   [*LockD3DBuffer*](/previous-versions/windows/hardware/drivers/ff568216(v=vs.85))

-   [*UnlockD3DBuffer*](/previous-versions/windows/hardware/drivers/ff570106(v=vs.85))

-   [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode)

-   [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev)

-   [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface)

-   [**DrvResetPDEV**](/windows/win32/api/winddi/nf-winddi-drvresetpdev)

 

