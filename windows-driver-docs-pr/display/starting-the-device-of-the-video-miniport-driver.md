---
title: Starting the Device of the Video Miniport Driver
description: Starting the Device of the Video Miniport Driver
ms.assetid: e51a9483-eb12-4f7c-943f-075e670e97b1
keywords:
- video miniport drivers WDK Windows 2000 , starting devices
- starting device of video miniport driver
- device startups WDK video miniport
- video miniport drivers WDK Windows 2000 , initializing
- initializing video miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting the Device of the Video Miniport Driver


## <span id="ddk_starting_the_device_of_the_video_miniport_driver_gg"></span><span id="DDK_STARTING_THE_DEVICE_OF_THE_VIDEO_MINIPORT_DRIVER_GG"></span>


The PnP manager sends an IRP code (see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710)) to the video port driver requesting that the graphics adapter be started. The video port driver's dispatch routine calls the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine in response to this IRP code. Details for some of *HwVidFindAdapter*'s tasks are discussed in the following topics:

[Setting up Video Adapter Access Ranges](setting-up-video-adapter-access-ranges.md)

[Setting Hardware Information in the Registry](setting-hardware-information-in-the-registry.md)

[Changing State on the Adapter](changing-state-on-the-adapter.md)

 

 





