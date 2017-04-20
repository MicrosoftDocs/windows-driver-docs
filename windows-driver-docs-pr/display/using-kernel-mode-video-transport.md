---
title: Using Kernel-Mode Video Transport
description: Using Kernel-Mode Video Transport
ms.assetid: 0be84371-f7d5-42bb-b164-80fcf1b58d95
keywords:
- drawing kernel-mode video transport WDK DirectDraw , about kernel-mode video transport
- DirectDraw kernel-mode video transport WDK Windows 2000 display , about kernel-mode video transport
- kernel-mode video transport WDK DirectDraw , about kernel-mode video transport
- video transport kernel-mode WDK DirectDraw , about kernel-mode video transport
- video capture WDK video transport kernel-mode
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Kernel-Mode Video Transport


## <span id="ddk_using_kernel_mode_video_transport_gg"></span><span id="DDK_USING_KERNEL_MODE_VIDEO_TRANSPORT_GG"></span>


Kernel-mode video transport functionality is accessed by the [video capture driver](https://msdn.microsoft.com/library/windows/hardware/ff568699) linking with *dxapi.lib*, which allows it to later call *dxapi.sys*. This functionality is available only when DirectDraw is loaded.

A video capture driver (for a hardware decoder) uses the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function supplied with kernel-mode DirectDraw to access the DxApi interface callback functions. The **DxApi** function is a single entry point that accepts a function identifier, an input buffer and size, and an output buffer and size. The behavior of this function and the size and format of the input and output buffers depend on the specified function identifier. The **DxApi** function and its function identifiers are defined in *ddkmapi.h*.

DirectShow or another client accesses the DxApi interface callback functions supplied by the video miniport driver through DirectDraw. The DxApi interface callback functions are defined in *dxmini.h*.

To use the kernel-mode video transport interface, the video capture driver must first receive user-mode handles for each DirectDraw object, surface, and VPE object that it needs to use. For the capture and MPEG models, these handles are passed down using their existing APIs. If a driver requires this functionality but is not a stream-class driver, a user-mode component can retrieve the handles using the [IDirectDrawKernel](https://msdn.microsoft.com/library/windows/hardware/ff567398) and [IDirectDrawSurfaceKernel](https://msdn.microsoft.com/library/windows/hardware/ff567409) COM interfaces and pass them down to the driver. The COM interfaces and their methods are identified in *ddkernel.h*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Kernel-Mode%20Video%20Transport%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




