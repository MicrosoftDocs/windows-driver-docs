---
title: VGA-Compatible Miniport Driver's HwVidStartIO
description: VGA-Compatible Miniport Driver's HwVidStartIO
ms.assetid: e5a81f87-b220-4497-aed3-8c4d08504340
keywords:
- video miniport drivers WDK Windows 2000 , VGA, HwVidStartIO
- VGA WDK video miniport , HwVidStartIO
- HwVidStartIO
- non-VGA-compatible video miniport drivers WDK
- SVGA WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VGA-Compatible Miniport Driver's HwVidStartIO


## <span id="ddk_vga_compatible_miniport_driver_s_hwvidstartio_gg"></span><span id="DDK_VGA_COMPATIBLE_MINIPORT_DRIVER_S_HWVIDSTARTIO_GG"></span>


When the user switches a full-screen MS-DOS application back to running in a window, a VGA-compatible miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function is sent a [*VRP*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-) with the I/O control code IOCTL\_VIDEO\_SAVE\_HARDWARE\_STATE. The miniport driver must store the state of the adapter in case the user switches the application to full-screen mode again.

Note that the miniport driver's *SvgaHwIoPortXxx* function might have buffered a sequence of application **IN**s and/or **OUT**s, as described in [Validating Instructions in SvgaHwIoPortXxx](validating-instructions-in-svgahwioportxxx.md), when its *HwVidStartIO* function is called to save the adapter state. In these circumstances, the miniport driver should save the current state, including the buffered instructions, so that the *SvgaHwIoPortXxx* functions can resume validation operations exactly where they left off if the user switches the application to full-screen mode again.

When the miniport driver completes a save operation, the port driver automatically disables the current IOPM for [*VDM*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdm)s and the miniport driver's *SvgaHwIoPortXxx* functions. The video port driver restores the IOPM automatically if the application is switched to full-screen mode again. It also resumes calling the miniport driver's *SvgaHwIoPortXxx* function, after it calls the miniport driver's *HwVidStartIO* function with the IOCTL\_VIDEO\_RESTORE\_HARDWARE\_STATE request.

 

 





