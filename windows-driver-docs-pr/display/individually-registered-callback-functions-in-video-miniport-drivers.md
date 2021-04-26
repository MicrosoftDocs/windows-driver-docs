---
title: Registering Callback Functions in Video Miniport Drivers
description: Individually Registered Callback Functions in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , callback functions
- callback functions WDK video miniport
- individually registered callback functions WDK video miniport
- registered callback functions WDK video miniport
- temporary registration WDK video miniport
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Registering Callback Functions in Video Miniport Drivers

In certain instances, communication between the vendor-supplied video miniport driver and the system-supplied video port driver proceeds as follows:

1. The video miniport driver calls a function in the video port driver.

2. Before the video port driver function completes, it calls back into the video miniport driver for assistance.

When the video miniport driver calls the video port driver function, it passes a pointer to the callback function. For example, when the video miniport driver calls [**VideoPortStartDma**](/windows-hardware/drivers/ddi/video/nf-video-videoportstartdma), it passes a pointer to an *HwVidExecuteDma* callback function (implemented by the video miniport driver).

When the video miniport driver passes the address of a callback function to a video port driver function, it *registers* the callback function with the video port driver. The registration is temporary in the sense that the video port driver does not permanently store the callback function pointer. Rather, the video port driver holds the function pointer only during the execution of the function that calls back. This kind of temporary registration is in contrast to the permanent registration of many video miniport driver functions. For example, the video miniport driver registers a set of functions during **DriverEntry**, and the video port driver stores those function pointers permanently in the device extension.

In some instances, it makes sense for the video miniport driver to implement several functions, each of which can serve as the callback function for a particular video port driver function. For example, the video miniport driver might implement several variations of the *HwVidQueryDeviceCallback* function and pass the variation of choice in a particular call to [**VideoPortGetDeviceData**](/windows-hardware/drivers/ddi/video/nf-video-videoportgetdevicedata).

For a list of callback functions that can be implemented by the video miniport driver, see [**VIDEO_HW_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data).
