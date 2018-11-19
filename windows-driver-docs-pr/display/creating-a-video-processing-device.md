---
title: Creating a Video Processing Device
description: Creating a Video Processing Device
ms.assetid: 3bedf0bf-360a-4dad-a7dd-ee73a0f1fc31
keywords:
- video processing WDK DirectX VA , creating devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Video Processing Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateVideoProcessDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540729) function to create a device for processing a video stream. When the Direct3D runtime is finished with the device, it calls the user-mode display driver's [**DestroyVideoProcessDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552814) function.

 

 





