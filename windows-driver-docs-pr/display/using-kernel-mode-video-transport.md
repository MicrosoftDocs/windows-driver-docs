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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Kernel-Mode Video Transport


## <span id="ddk_using_kernel_mode_video_transport_gg"></span><span id="DDK_USING_KERNEL_MODE_VIDEO_TRANSPORT_GG"></span>


Kernel-mode video transport functionality is accessed by the [video capture driver](https://msdn.microsoft.com/library/windows/hardware/ff568699) linking with *dxapi.lib*, which allows it to later call *dxapi.sys*. This functionality is available only when DirectDraw is loaded.

A video capture driver (for a hardware decoder) uses the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function supplied with kernel-mode DirectDraw to access the DxApi interface callback functions. The **DxApi** function is a single entry point that accepts a function identifier, an input buffer and size, and an output buffer and size. The behavior of this function and the size and format of the input and output buffers depend on the specified function identifier. The **DxApi** function and its function identifiers are defined in *ddkmapi.h*.

DirectShow or another client accesses the DxApi interface callback functions supplied by the video miniport driver through DirectDraw. The DxApi interface callback functions are defined in *dxmini.h*.

To use the kernel-mode video transport interface, the video capture driver must first receive user-mode handles for each DirectDraw object, surface, and VPE object that it needs to use. For the capture and MPEG models, these handles are passed down using their existing APIs. If a driver requires this functionality but is not a stream-class driver, a user-mode component can retrieve the handles using the [IDirectDrawKernel](https://msdn.microsoft.com/library/windows/hardware/ff567398) and [IDirectDrawSurfaceKernel](https://msdn.microsoft.com/library/windows/hardware/ff567409) COM interfaces and pass them down to the driver. The COM interfaces and their methods are identified in *ddkernel.h*.

 

 





