---
title: Video Port Driver Support for Bug Check Callbacks
description: Video Port Driver Support for Bug Check Callbacks
ms.assetid: 181fd4f2-feed-4759-80a7-aec97b9094b3
keywords:
- video miniport drivers WDK Windows 2000 , bug check callbacks
- bug check callbacks WDK video miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Port Driver Support for Bug Check Callbacks


## <span id="ddk_video_port_driver_support_for_bug_check_callbacks_gg"></span><span id="DDK_VIDEO_PORT_DRIVER_SUPPORT_FOR_BUG_CHECK_CALLBACKS_GG"></span>


In Windows XP SP1 and later, a video miniport driver can implement and register [**HwVidBugcheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff567324), a function that the system calls when [**Bug Check 0xEA (THREAD\_STUCK\_IN\_DEVICE\_DRIVER)**](https://msdn.microsoft.com/library/windows/hardware/ff560350) occurs. *HwVidBugcheckCallback* can append its own data to a dump file that driver developers can use to diagnose problems in their drivers.

For information about registering *HwVidBugcheckCallback*, see the following topics:

[Individually Registered Video Miniport Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff567672)

[**VideoPortRegisterBugcheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff570353)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Port%20Driver%20Support%20for%20Bug%20Check%20Callbacks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




