---
title: Deinterlace Container Device for Deinterlacing
description: Deinterlace Container Device for Deinterlacing
ms.assetid: e14db243-46e5-4ab3-b134-8aadfa99e614
keywords:
- deinterlace container device WDK DirectX VA
- container device WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deinterlace Container Device for Deinterlacing


## <span id="ddk_deinterlace_container_device_for_deinterlacing_gg"></span><span id="DDK_DEINTERLACE_CONTAINER_DEVICE_FOR_DEINTERLACING_GG"></span>


The [sample functions for deinterlacing](sample-functions-for-deinterlacing.md) can only be used in the context of a DirectX VA device, so it is necessary to first define and create a deinterlace container device.

If a driver supports accelerated decoding of compressed video, when initiated by the VMR, the driver also creates two more DirectX VA devices: one to perform the video decoding work and one to perform deinterlacing operations.

**Note**   The deinterlace container device is a software construct only and does not represent any functional hardware contained on a device.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deinterlace%20Container%20Device%20for%20Deinterlacing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




