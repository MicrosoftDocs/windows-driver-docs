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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Privately Defined Display-Miniport Driver IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_privately_defined_display_miniport_driver_ioctl_video_xxx_requests"></span><span id="DDK_PRIVATELY_DEFINED_DISPLAY_MINIPORT_DRIVER_IOCTL_VIDEO_XXX_REQUESTS"></span>


A miniport driver can define one or more private I/O control codes for its corresponding display driver.

However, only a specific display-and-miniport driver pair can use privately defined I/O control codes. That is, a miniport driver designed to run under an existing display driver should not define private I/O control codes because the existing display driver cannot make new I/O control requests without being rewritten and, possibly, without breaking existing miniport drivers it already uses. An existing or generic display driver layered over many different models of adapters, such as SVGA adapters, also cannot rely on a privately defined I/O control code to have the same effects in every underlying miniport driver.

For more information about defining private I/O control codes, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Privately%20Defined%20Display-Miniport%20Driver%20IOCTL_VIDEO_XXX%20Requests%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




