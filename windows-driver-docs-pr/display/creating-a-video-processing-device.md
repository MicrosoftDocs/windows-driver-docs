---
title: Creating a Video Processing Device
description: Creating a Video Processing Device
keywords:
- video processing WDK DirectX VA , creating devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Video Processing Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateVideoProcessDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createvideoprocessdevice) function to create a device for processing a video stream. When the Direct3D runtime is finished with the device, it calls the user-mode display driver's [**DestroyVideoProcessDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_destroyvideoprocessdevice) function.

 

