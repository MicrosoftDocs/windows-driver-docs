---
title: Direct3D DDI for XDDM
description: Direct3D DDI for Windows 2000 display driver model (XDDM)
keywords:
- Direct3D WDK Windows 2000 display
- Direct3D WDK Windows 2000 display , about Direct3D
- graphics WDK Windows 2000 display
- DDI WDK Direct3D
- header files WDK Direct3D
- Direct3D WDK Windows 2000 display , header files
- display driver model WDK Windows 2000 , Direct3D
- Windows 2000 display driver model WDK , Direct3D
ms.date: 07/19/2024
---

# Direct3D DDI for XDDM

This section describes the Direct3D DDI as it pertains to the legacy Windows 2000 display driver model (XDDM), and provides implementation guidelines for XDDM driver writers.

The Direct3D device driver interface (DDI) is a graphics interface that allows vendors to provide hardware acceleration for Direct3D. The interface is flexible, allowing vendors to provide Direct3D acceleration according to hardware capabilities. Driver writers implement the Direct3D DDI as an integral part of the display driver.

All XDDM Direct3D drivers for Windows 2000 and later must conform to the DirectX 7.0 or later Direct3D driver model. The DirectX 8.0 driver model is supported in Windows XP.

Driver writers who are creating XDDM Direct3D drivers for Windows 2000 and later should use the following header files:

* [*d3dhal.h*](/windows-hardware/drivers/ddi/d3dhal), which contains prototypes for callbacks that the driver implements and definitions for driver-level structures. The [**D3DHAL_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation) enumerated type is defined in this file. This header is included in *winddi.h*, which must be included in all Windows 2000 and later display drivers.

* [*d3d9types.h*](/windows-hardware/drivers/ddi/d3d9types), which contains Direct3D type definitions used by both applications and drivers. Except for D3DHAL_DP2OPERATION, all other Direct3D enumerated types are defined in this header.

* [*d3dcaps.h*](/windows-hardware/drivers/ddi/d3dcaps), which contains structures and definitions that describe capabilities of various aspects of Direct3D drivers.

* [*ddrawint.h*](/windows/win32/api/ddrawint/), which is included in *winddi.h*. This header is required to develop the DirectDraw portion of a display driver.

All of these header files are shipped with the Windows Driver Kit (WDK). Previous Driver Development Kits (DDKs) also provide sample code for a Direct3D driver in the *Perm3* video display directory.

The Windows Driver Kit (WDK) doesn't contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 DDK, which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

The primary reference for SDK-related aspects of the Direct3D interface is the Windows SDK documentation. *Computer Graphics: Principles and Practice* by Foley, van Dam, Feiner, and Hughes is a useful general graphics reference.
