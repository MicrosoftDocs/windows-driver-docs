---
title: FVF (Flexible Vertex Format)
description: FVF (Flexible Vertex Format)
ms.assetid: 206f4275-bcb8-4e8e-9c11-c6fb5d9c561d
keywords:
- vertex format WDK Direct3D
- flexible vertex format WDK Direct3D
- FVF WDK Direct3D
- Direct3D WDK Windows 2000 display , flexible vertex format
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FVF (Flexible Vertex Format)


## <span id="ddk_fvf_gg"></span><span id="DDK_FVF_GG"></span>


The driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback receives vertex data in a flexible vertex format (FVF). Because the vertex format is flexible, there is no comprehensive data structure defined for this data. Drivers must implement full FVF functionality.

There is an FVF update for Microsoft DirectX 7.0 that includes 1D, 3D, and 4D textures in addition to the usual 2D textures. For more information about this update, see [FVF Update](fvf-update.md). See the *Perm3* sample driver and DirectX SDK documentation for more information about these topics.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

 

 

 





