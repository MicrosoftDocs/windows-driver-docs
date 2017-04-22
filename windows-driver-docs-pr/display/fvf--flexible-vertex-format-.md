---
title: FVF (Flexible Vertex Format)
description: FVF (Flexible Vertex Format)
ms.assetid: 206f4275-bcb8-4e8e-9c11-c6fb5d9c561d
keywords:
- vertex format WDK Direct3D
- flexible vertex format WDK Direct3D
- FVF WDK Direct3D
- Direct3D WDK Windows 2000 display , flexible vertex format
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FVF (Flexible Vertex Format)


## <span id="ddk_fvf_gg"></span><span id="DDK_FVF_GG"></span>


The driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback receives vertex data in a flexible vertex format (FVF). Because the vertex format is flexible, there is no comprehensive data structure defined for this data. Drivers must implement full FVF functionality.

There is an FVF update for Microsoft DirectX 7.0 that includes 1D, 3D, and 4D textures in addition to the usual 2D textures. For more information about this update, see [FVF Update](fvf-update.md). See the *Perm3* sample driver and DirectX SDK documentation for more information about these topics.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20FVF%20%28Flexible%20Vertex%20Format%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




