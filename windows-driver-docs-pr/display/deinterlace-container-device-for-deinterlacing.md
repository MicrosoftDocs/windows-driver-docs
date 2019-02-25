---
title: Deinterlace Container Device for Deinterlacing
description: Deinterlace Container Device for Deinterlacing
ms.assetid: e14db243-46e5-4ab3-b134-8aadfa99e614
keywords:
- deinterlace container device WDK DirectX VA
- container device WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deinterlace Container Device for Deinterlacing


## <span id="ddk_deinterlace_container_device_for_deinterlacing_gg"></span><span id="DDK_DEINTERLACE_CONTAINER_DEVICE_FOR_DEINTERLACING_GG"></span>


The [sample functions for deinterlacing](sample-functions-for-deinterlacing.md) can only be used in the context of a DirectX VA device, so it is necessary to first define and create a deinterlace container device.

If a driver supports accelerated decoding of compressed video, when initiated by the VMR, the driver also creates two more DirectX VA devices: one to perform the video decoding work and one to perform deinterlacing operations.

**Note**   The deinterlace container device is a software construct only and does not represent any functional hardware contained on a device.

 

 

 





