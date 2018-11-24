---
title: Privately Defined Display-Miniport Driver IOCTL_VIDEO_XXX Requests
description: Privately Defined Display-Miniport Driver IOCTL_VIDEO_XXX Requests
ms.assetid: 45d8c9bc-993c-4fd3-949d-dfb30bb685d7
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- privately-defined IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
- I/O WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Privately Defined Display-Miniport Driver IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_privately_defined_display_miniport_driver_ioctl_video_xxx_requests"></span><span id="DDK_PRIVATELY_DEFINED_DISPLAY_MINIPORT_DRIVER_IOCTL_VIDEO_XXX_REQUESTS"></span>


A miniport driver can define one or more private I/O control codes for its corresponding display driver.

However, only a specific display-and-miniport driver pair can use privately defined I/O control codes. That is, a miniport driver designed to run under an existing display driver should not define private I/O control codes because the existing display driver cannot make new I/O control requests without being rewritten and, possibly, without breaking existing miniport drivers it already uses. An existing or generic display driver layered over many different models of adapters, such as SVGA adapters, also cannot rely on a privately defined I/O control code to have the same effects in every underlying miniport driver.

For more information about defining private I/O control codes, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406).

 

 





