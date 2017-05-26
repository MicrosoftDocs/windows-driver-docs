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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Starting the Device of the Video Miniport Driver


## <span id="ddk_starting_the_device_of_the_video_miniport_driver_gg"></span><span id="DDK_STARTING_THE_DEVICE_OF_THE_VIDEO_MINIPORT_DRIVER_GG"></span>


The PnP manager sends an IRP code (see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710)) to the video port driver requesting that the graphics adapter be started. The video port driver's dispatch routine calls the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine in response to this IRP code. Details for some of *HwVidFindAdapter*'s tasks are discussed in the following topics:

[Setting up Video Adapter Access Ranges](setting-up-video-adapter-access-ranges.md)

[Setting Hardware Information in the Registry](setting-hardware-information-in-the-registry.md)

[Changing State on the Adapter](changing-state-on-the-adapter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Starting%20the%20Device%20of%20the%20Video%20Miniport%20Driver%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




