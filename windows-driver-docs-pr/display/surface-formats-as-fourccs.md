---
title: Surface Formats as FOURCCs
description: Surface Formats as FOURCCs
ms.assetid: 947b73c9-3f1d-485e-9966-815b40a06342
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , texture format lists
- texture format lists WDK DirectX 8.0
- DPIXELFORMAT
- surface formats WDK DirectX 8.0
- FOURCCs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Surface Formats as FOURCCs


## <span id="ddk_surface_formats_as_fourccs_gg"></span><span id="DDK_SURFACE_FORMATS_AS_FOURCCS_GG"></span>


Three of the new surface formats defined by DirectX 8.0, D3DFMT\_Q8W8V8U8, D3DFMT\_V16U16 and D3DFMT\_W11V11U10, are passed to the driver as [*FOURCCs*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc). This means the various bit depth and mask fields of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) data structure are not initialized and their values are undefined. Hence, a driver processing these three formats must not rely on the bit count or masks in the pixel format but must compute these as necessary. For example, when computing the pitch of a surface of one of these types the **dwRGBBitCount** field of the pixel format must not be used. All other formats other than YUV, DXT and IHV specific extension formats are mapped to the legacy DDPIXELFORMAT representation when passed to the driver and, therefore, have valid pixel formats and masks in the pixel format data structure.

 

 





