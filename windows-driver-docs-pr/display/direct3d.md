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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm* ) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 DDK, which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

Reference pages for Direct3D DDI functions, structures, and enumerations can be found in [Direct3D Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff552853), [Direct3D Driver Structures](https://msdn.microsoft.com/library/windows/hardware/ff552858), and [Direct3D Driver Enumerations](https://msdn.microsoft.com/library/windows/hardware/ff552850).

The primary reference for SDK-related aspects of the Direct3D interface is the Microsoft Windows SDK documentation. *Computer Graphics: Principles and Practice* by Foley, van Dam, Feiner, and Hughes, which was published by Addison-Wesley, is a useful general graphics reference.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




