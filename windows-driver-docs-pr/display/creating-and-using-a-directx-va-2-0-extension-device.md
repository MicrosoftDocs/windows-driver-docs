---
title: Creating and Using a DirectX VA 2.0 Extension Device
description: Creating and Using a DirectX VA 2.0 Extension Device
ms.assetid: 650a77a5-67c3-4b11-93c8-24232905eb43
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
- extension device WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating and Using a DirectX VA 2.0 Extension Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateExtensionDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540644) function to create an extension device for DirectX VA 2.0. When the Direct3D runtime is finished with the device, it calls the user-mode display driver's [**DestroyExtensionDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552774) function.

The Direct3D runtime calls the user-mode display driver's [**DecodeExtensionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff551811) function to decode video on a nonstandard decode device between a begin-frame and end-frame time period and on a specific render target surface. For a general discussion about decoding video, see [Decoding Video](decoding-video.md).

The Direct3D runtime calls the user-mode display driver's [**ExtensionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff565604) function to perform nonstandard DirectX VA 2.0 operations on an extension device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20and%20Using%20a%20DirectX%20VA%202.0%20Extension%20Device%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




