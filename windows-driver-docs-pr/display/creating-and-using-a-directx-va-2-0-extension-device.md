---
title: Creating and Using a DirectX VA 2.0 Extension Device
description: Creating and Using a DirectX VA 2.0 Extension Device
ms.assetid: 650a77a5-67c3-4b11-93c8-24232905eb43
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
- extension device WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Using a DirectX VA 2.0 Extension Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateExtensionDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540644) function to create an extension device for DirectX VA 2.0. When the Direct3D runtime is finished with the device, it calls the user-mode display driver's [**DestroyExtensionDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552774) function.

The Direct3D runtime calls the user-mode display driver's [**DecodeExtensionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff551811) function to decode video on a nonstandard decode device between a begin-frame and end-frame time period and on a specific render target surface. For a general discussion about decoding video, see [Decoding Video](decoding-video.md).

The Direct3D runtime calls the user-mode display driver's [**ExtensionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff565604) function to perform nonstandard DirectX VA 2.0 operations on an extension device.

 

 





