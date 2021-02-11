---
title: Video Port Driver Support for Bug Check Callbacks
description: Video Port Driver Support for Bug Check Callbacks
keywords:
- video miniport drivers WDK Windows 2000 , bug check callbacks
- bug check callbacks WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Port Driver Support for Bug Check Callbacks

In Windows XP SP1 and later, a video miniport driver can implement and register [**HwVidBugcheckCallback**](/windows-hardware/drivers/ddi/video/nc-video-pvideo_bugcheck_callback), a function that the system calls when [**Bug Check 0xEA (THREAD\_STUCK\_IN\_DEVICE\_DRIVER)**](../debugger/bug-check-0xea--thread-stuck-in-device-driver.md) occurs. *HwVidBugcheckCallback* can append its own data to a dump file that driver developers can use to diagnose problems in their drivers.

For information about registering *HwVidBugcheckCallback*, see [**VideoPortRegisterBugcheckCallback**](/windows-hardware/drivers/ddi/video/nf-video-videoportregisterbugcheckcallback).
