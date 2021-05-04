---
title: Direct3D DDI
description: Direct3D DDI
keywords:
- Direct3D WDK Windows 2000 display
- Direct3D WDK Windows 2000 display , about Direct3D
- graphics WDK Windows 2000 display
- DDI WDK Direct3D
- header files WDK Direct3D
- Direct3D WDK Windows 2000 display , header files
- display driver model WDK Windows 2000 , Direct3D
- Windows 2000 display driver model WDK , Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D DDI

The Microsoft Direct3D device driver interface (DDI) is a graphics interface that allows vendors to provide hardware acceleration for Direct3D. The interface is flexible, allowing vendors to provide Direct3D acceleration according to hardware capabilities. Driver writers implement the Direct3D DDI as an integral part of the display driver.

This section describes the Direct3D DDI, and provides implementation guidelines for Direct3D driver writers. It is assumed that the reader is familiar with the Direct3D and Microsoft DirectDraw APIs, and that the reader has a firm grasp of the Windows 2000 display driver model, including the DirectDraw DDI.

All Direct3D drivers for Windows 2000 and later must conform to the Microsoft DirectX 7.0 or later Direct3D driver model. The DirectX 8.0 driver model is supported in Microsoft Windows XP.

Driver writers who are creating Microsoft Direct3D drivers for Microsoft Windows 2000 and later should use the following header files:

[*d3dhal.h*](/windows-hardware/drivers/ddi/d3dhal)  
Contains prototypes for callbacks that are implemented by the driver and definitions for driver-level structures. The [**D3DHAL_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation) enumerated type is defined in this file. This header is included in *winddi.h*, which must be included in all Windows 2000 and later display drivers.

[*d3d9types.h*](/windows-hardware/drivers/ddi/d3d9types)
Contains Direct3D type definitions used by both applications and drivers. Except for D3DHAL_DP2OPERATION, all other Direct3D enumerated types are defined in this header.

[*d3dcaps.h*](/windows-hardware/drivers/ddi/d3dcaps)
Contains structures and definitions that describe capabilities of various aspects of Direct3D drivers.

*ddrawint.h*  
This header file, which is included in *winddi.h*, is required to develop the Microsoft DirectDraw portion of a display driver.

All of these header files are shipped with the Windows Driver Kit (WDK). Previous Driver Development Kits (DDKs) also provide sample code for a Direct3D driver in the *Perm3* video display directory.

The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm* ) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 DDK, which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

The primary reference for SDK-related aspects of the Direct3D interface is the Microsoft Windows SDK documentation. *Computer Graphics: Principles and Practice* by Foley, van Dam, Feiner, and Hughes, which was published by Addison-Wesley, is a useful general graphics reference.
