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


In Windows XP SP1 and later, a video miniport driver can implement and register [**HwVidBugcheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff567324), a function that the system calls when [**Bug Check 0xEA (THREAD\_STUCK\_IN\_DEVICE\_DRIVER)**](https://msdn.microsoft.com/library/windows/hardware/ff560350) occurs. *HwVidBugcheckCallback* can append its own data to a dump file that driver developers can use to diagnose problems in their drivers.

For information about registering *HwVidBugcheckCallback*, see the following topics:

[Individually Registered Video Miniport Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff567672)

[**VideoPortRegisterBugcheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff570353)

 

 





