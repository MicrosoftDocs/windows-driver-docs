---
title: DirectDraw Interfaces for Kernel-Mode Video Transport Support
description: DirectDraw Interfaces for Kernel-Mode Video Transport Support
ms.assetid: 8012f6b0-3b55-438f-8146-4f62e6bafad3
keywords:
- kernel-mode video transport WDK DirectDraw , interfaces
- DirectX VPE support WDK DirectDraw , kernel-mode video transport
- drawing VPEs WDK DirectDraw , kernel-mode video transport
- DirectDraw VPEs WDK Windows 2000 display , kernel-mode video transport
- video port extensions WDK DirectDraw , kernel-mode video transport
- VPEs WDK DirectDraw , kernel-mode video transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectDraw Interfaces for Kernel-Mode Video Transport Support


## <span id="ddk_directdraw_interfaces_for_kernel_mode_video_transport_support_gg"></span><span id="DDK_DIRECTDRAW_INTERFACES_FOR_KERNEL_MODE_VIDEO_TRANSPORT_SUPPORT_GG"></span>


The kernel-mode video transport must keep track of surface information for each surface it uses, and for each VPE object. This information must be updated every time [*DdUpdateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff550369) or [*DdVideoPortUpdate*](https://msdn.microsoft.com/library/windows/hardware/ff550450) is called for the surface or hardware video port. Before DirectDraw sends this information to the kernel-mode video transport, it calls one of two driver functions: [*DdSyncSurfaceData*](https://msdn.microsoft.com/library/windows/hardware/ff550345) or [*DdSyncVideoPortData*](https://msdn.microsoft.com/library/windows/hardware/ff550350). These functions allow the driver to fill in or modify some of the structure information and to use four **dwDriverReserved***N* members of the [**DD\_SYNCSURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551739) or three **dwDriverReserved***N* members of the [**DD\_SYNCVIDEOPORTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551740) structure for its own purposes. These driver functions are required for the kernel-mode video transport support to work correctly.

A good example of how a driver can use these **dwDriverReserved***N* members is to set a flag indicating which physical overlay an overlay surface is using if the hardware supports more than one physical overlay.

 

 





