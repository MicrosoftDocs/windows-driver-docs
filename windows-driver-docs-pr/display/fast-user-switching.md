---
title: Fast User Switching
description: Fast User Switching
ms.assetid: 79e13d56-f71f-4a7d-9069-de4821d29d94
keywords:
- display driver model WDK Windows 2000 , Fast User Switching
- Windows 2000 display driver model WDK , Fast User Switching
- video miniport drivers WDK Windows 2000 , Fast User Switching
- Fast User Switching WDK Windows 2000 display
- multiple virtual display drivers WDK Windows 2000 display
- virtual display drivers WDK Windows 2000 display
- display drivers WDK Windows 2000 , Fast User Switching
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Fast User Switching


## <span id="ddk_fast_user_switching_gg"></span><span id="DDK_FAST_USER_SWITCHING_GG"></span>


Fast User Switching, a feature of Windows XP and later, enables multiple users to be logged onto the same machine. A particular user's desktop and any running applications persist from that user's logon session to his or her next.

Fast User Switching works by allowing multiple virtual display drivers to run at the same time. (Each virtual display driver is associated with a particular PDEV.) The video miniport driver, however, exists as a single instance. When one of the virtual display drivers calls a video miniport driver callback, serious problems ensue if the miniport driver attempts to access a passed-in memory address in the context of the display driver when that display driver instance is no longer the active kernel thread. A tenet of the display driver/video miniport driver architecture is that information should flow in one direction only: from the display driver to the video miniport driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Fast%20User%20Switching%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




