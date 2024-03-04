---
title: DirectDraw Interfaces for Kernel-Mode Video Transport
description: DirectDraw Interfaces for Kernel-Mode Video Transport Support
keywords:
- kernel-mode video transport WDK DirectDraw , interfaces
- DirectX VPE support WDK DirectDraw , kernel-mode video transport
- drawing VPEs WDK DirectDraw , kernel-mode video transport
- DirectDraw VPEs WDK Windows 2000 display , kernel-mode video transport
- video port extensions WDK DirectDraw , kernel-mode video transport
- VPEs WDK DirectDraw , kernel-mode video transport
ms.date: 12/06/2018
---

# DirectDraw Interfaces for Kernel-Mode Video Transport Support

The kernel-mode video transport must keep track of surface information for each surface it uses, and for each VPE object. This information must be updated every time [*DdUpdateOverlay*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_updateoverlay) or [*DdVideoPortUpdate*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_update) is called for the surface or hardware video port. Before DirectDraw sends this information to the kernel-mode video transport, it calls one of two driver functions: [*DdSyncSurfaceData*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncsurface) or [*DdSyncVideoPortData*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_kernelcb_syncvideoport). These functions allow the driver to fill in or modify some of the structure information and to use four **dwDriverReserved**_N_ members of the [**DD\_SYNCSURFACEDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_syncsurfacedata) or three **dwDriverReserved**_N_ members of the [**DD\_SYNCVIDEOPORTDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_syncvideoportdata) structure for its own purposes. These driver functions are required for the kernel-mode video transport support to work correctly.

A good example of how a driver can use these **dwDriverReserved**_N_ members is to set a flag indicating which physical overlay an overlay surface is using if the hardware supports more than one physical overlay.

 
