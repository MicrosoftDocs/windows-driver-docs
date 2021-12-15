---
title: Creating and Using a DirectX VA 2.0 Extension Device
description: Creating and Using a DirectX VA 2.0 Extension Device
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
- extension device WDK DirectX VA
ms.date: 04/20/2017
---

# Creating and Using a DirectX VA 2.0 Extension Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateExtensionDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createextensiondevice) function to create an extension device for DirectX VA 2.0. When the Direct3D runtime is finished with the device, it calls the user-mode display driver's [**DestroyExtensionDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_destroyextensiondevice) function.

The Direct3D runtime calls the user-mode display driver's [**DecodeExtensionExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeextensionexecute) function to decode video on a nonstandard decode device between a begin-frame and end-frame time period and on a specific render target surface. For a general discussion about decoding video, see [Decoding Video](decoding-video.md).

The Direct3D runtime calls the user-mode display driver's [**ExtensionExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_extensionexecute) function to perform nonstandard DirectX VA 2.0 operations on an extension device.

 

