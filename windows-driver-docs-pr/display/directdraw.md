---
title: DirectDraw for XDDM
description: DirectDraw for XDDM
keywords:
- DirectDraw WDK WDDM
- WDDM driver model WDK , DirectDraw
- display driver model WDK Windows 2000 , DirectDraw
- header files WDK DirectDraw
- DirectDraw WDK WDDM , header files
- drawing WDK DirectDraw
- drawing WDK DirectDraw , header files
- graphics WDK WDDM
ms.date: 07/19/2024
---

# DirectDraw for XDDM

This section describes the DirectDraw interface,  architecture, and implementation guidelines for the legacy Windows 2000 display driver model (XDDM).

Driver writers who are creating DirectDraw drivers for XDDM should use the following header files:

* *ddrawint.h* contains the basic types, constants, and structures for DirectDraw drivers.

* *ddraw.h* contains the basic types, constants, and structures used by both applications and drivers.

* *dvp.h* is used when the driver supports the DirectDraw video port extensions (VPE).

* *dxmini.h* is used when the video miniport driver includes support for kernel-mode video transport, the DxApi interface (functions specified by the DXAPI_INTERFACE structure).

* *ddkmapi.h* is used by video capture drivers to access the DxApi function. DirectDraw, in turn, calls upon the DxApi interface.

* *dmemmgr.h* is used when the driver wants to perform its own memory management instead of relying on the DirectDraw runtime.

* *ddkernel.h* is used when the driver includes kernel-mode support.

* *dx95type.h* allows driver writers to easily port existing Windows 98/Me drivers to Windows 2000 and later. This header file maps names that are different on the two platforms.

For more information about DirectDraw, see the [Windows SDK](/windows/win32/directdraw/directdraw).
