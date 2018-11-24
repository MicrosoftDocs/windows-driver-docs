---
title: Direct3D DDI
description: Direct3D DDI
ms.assetid: 5b6f7c06-7f54-4fc4-9b94-5fb425b5b3c8
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


## <span id="ddk_direct3d_gg"></span><span id="DDK_DIRECT3D_GG"></span>


The Microsoft Direct3D device driver interface (DDI) is a graphics interface that allows vendors to provide hardware acceleration for Direct3D. The interface is flexible, allowing vendors to provide Direct3D acceleration according to hardware capabilities. Driver writers implement the Direct3D DDI as an integral part of the display driver.

This section describes the Direct3D DDI, and provides implementation guidelines for Direct3D driver writers. It is assumed that the reader is familiar with the Direct3D and Microsoft DirectDraw APIs, and that the reader has a firm grasp of the Windows 2000 display driver model, including the DirectDraw DDI.

All Direct3D drivers for Windows 2000 and later must conform to the Microsoft DirectX 7.0 or later Direct3D driver model. The DirectX 8.0 driver model is supported in Microsoft Windows XP.

Driver writers who are creating Microsoft Direct3D drivers for Microsoft Windows 2000 and later should use the following header files:

<span id="D3DNTHAL.H"></span>*d3dnthal.h*  
Contains prototypes for callbacks that are implemented by the driver and definitions for driver-level structures. The [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678) enumerated type is defined in this file. This header is included in *winddi.h*, which must be included in all Windows 2000 and later display drivers.

<span id="D3DTYPES.H"></span>*d3dtypes.h*  
Contains Direct3D type definitions used by both applications and drivers. Except for D3DHAL\_DP2OPERATION, all other Direct3D enumerated types are defined in this header.

<span id="D3DCAPS.H"></span>*d3dcaps.h*  
Contains structures and definitions that describe capabilities of various aspects of Direct3D drivers.

<span id="DX95TYPE.H"></span>*dx95type.h*  
Allows driver developers to write driver code that is portable between Windows 2000 and later and Windows 98/Me.

<span id="DDRAWINT.H"></span>*ddrawint.h*  
This header file, which is included in *winddi.h*, is required to develop the Microsoft DirectDraw portion of a display driver.

All of these header files are shipped with the Windows Driver Kit (WDK). Previous Driver Development Kits (DDKs) also provide sample code for a Direct3D driver in the *Perm3* video display directory.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm* ) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 DDK, which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

 

Reference pages for Direct3D DDI functions, structures, and enumerations can be found in [Direct3D Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff552853), [Direct3D Driver Structures](https://msdn.microsoft.com/library/windows/hardware/ff552858), and [Direct3D Driver Enumerations](https://msdn.microsoft.com/library/windows/hardware/ff552850).

The primary reference for SDK-related aspects of the Direct3D interface is the Microsoft Windows SDK documentation. *Computer Graphics: Principles and Practice* by Foley, van Dam, Feiner, and Hughes, which was published by Addison-Wesley, is a useful general graphics reference.

 

 





