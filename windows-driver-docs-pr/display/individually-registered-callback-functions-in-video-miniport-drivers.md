---
title: Individually Registered Callback Functions in Video Miniport Drivers
description: Individually Registered Callback Functions in Video Miniport Drivers
ms.assetid: 18469b9b-aca4-4225-97d0-8cafe64b8e1f
keywords:
- video miniport drivers WDK Windows 2000 , callback functions
- callback functions WDK video miniport
- individually registered callback functions WDK video miniport
- registered callback functions WDK video miniport
- temporary registration WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Individually Registered Callback Functions in Video Miniport Drivers


## <span id="ddk_individually_registered_callback_functions_in_video_miniport_drive"></span><span id="DDK_INDIVIDUALLY_REGISTERED_CALLBACK_FUNCTIONS_IN_VIDEO_MINIPORT_DRIVE"></span>


In certain instances, communication between the vendor-supplied video miniport driver and the system-supplied video port driver proceeds as follows:

1.  The video miniport driver calls a function in the video port driver.

2.  Before the video port driver function completes, it calls back into the video miniport driver for assistance.

When the video miniport driver calls the video port driver function, it passes a pointer to the callback function. For example, when the video miniport driver calls [**VideoPortStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570369), it passes a pointer to an *HwVidExecuteDma* callback function (implemented by the video miniport driver).

When the video miniport driver passes the address of a callback function to a video port driver function, it *registers* the callback function with the video port driver. The registration is temporary in the sense that the video port driver does not permanently store the callback function pointer. Rather, the video port driver holds the function pointer only during the execution of the function that calls back. This kind of temporary registration is in contrast to the permanent registration of many video miniport driver functions. For example, the video miniport driver registers a set of functions during **DriverEntry**, and the video port driver stores those function pointers permanently in the device extension.

In some instances, it makes sense for the video miniport driver to implement several functions, each of which can serve as the callback function for a particular video port driver function. For example, the video miniport driver might implement several variations of the *HwVidQueryDeviceCallback* function and pass the variation of choice in a particular call to [**VideoPortGetDeviceData**](https://msdn.microsoft.com/library/windows/hardware/ff570311).

For a list of callback functions that can be implemented by the video miniport driver and For information about how those callback functions are registered, see [Individually Registered Video Miniport Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff567672).

 

 





