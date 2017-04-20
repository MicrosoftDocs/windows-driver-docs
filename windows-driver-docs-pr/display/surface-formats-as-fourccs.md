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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Surface Formats as FOURCCs


## <span id="ddk_surface_formats_as_fourccs_gg"></span><span id="DDK_SURFACE_FORMATS_AS_FOURCCS_GG"></span>


Three of the new surface formats defined by DirectX 8.0, D3DFMT\_Q8W8V8U8, D3DFMT\_V16U16 and D3DFMT\_W11V11U10, are passed to the driver as [*FOURCCs*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc). This means the various bit depth and mask fields of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) data structure are not initialized and their values are undefined. Hence, a driver processing these three formats must not rely on the bit count or masks in the pixel format but must compute these as necessary. For example, when computing the pitch of a surface of one of these types the **dwRGBBitCount** field of the pixel format must not be used. All other formats other than YUV, DXT and IHV specific extension formats are mapped to the legacy DDPIXELFORMAT representation when passed to the driver and, therefore, have valid pixel formats and masks in the pixel format data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Surface%20Formats%20as%20FOURCCs%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




