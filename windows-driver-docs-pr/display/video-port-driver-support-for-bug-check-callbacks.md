---
title: Video Port Driver Support for Bug Check Callbacks
description: Video Port Driver Support for Bug Check Callbacks
ms.assetid: 181fd4f2-feed-4759-80a7-aec97b9094b3
keywords:
- video miniport drivers WDK Windows 2000 , bug check callbacks
- bug check callbacks WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Port Driver Support for Bug Check Callbacks


## <span id="ddk_video_port_driver_support_for_bug_check_callbacks_gg"></span><span id="DDK_VIDEO_PORT_DRIVER_SUPPORT_FOR_BUG_CHECK_CALLBACKS_GG"></span>


In Windows XP SP1 and later, a video miniport driver can implement and register [**HwVidBugcheckCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nc-video-pvideo_bugcheck_callback), a function that the system calls when [**Bug Check 0xEA (THREAD\_STUCK\_IN\_DEVICE\_DRIVER)**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xea--thread-stuck-in-device-driver) occurs. *HwVidBugcheckCallback* can append its own data to a dump file that driver developers can use to diagnose problems in their drivers.

For information about registering *HwVidBugcheckCallback*, see the following topics:

[Individually Registered Video Miniport Driver Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

[**VideoPortRegisterBugcheckCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nf-video-videoportregisterbugcheckcallback)

 

 





