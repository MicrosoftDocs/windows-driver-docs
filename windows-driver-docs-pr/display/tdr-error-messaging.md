---
title: TDR Error Messaging
description: TDR Error Messaging
ms.assetid: 0a29c701-2257-478d-bf2d-ca4a7edecfd0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TDR Error Messaging


Throughout the TDR process (that is, the process of detecting and recovering from situations where a GPU stops operating), the desktop is unresponsive and thus unavailable to the end user. In the final stages of recovery, a brief screen flash can occur that is similar to the brief screen flash that occurs when the end user changes the screen resolution. After the operating system has successfully recovered the desktop, the following informational message appears to the end user.

![screen shot of a notification that the "display driver stopped responding and has recovered"](images/tdr-error.png)

The operating system also logs the preceding message in the Event Viewer application and collects diagnosis information in the form of a debug report. If the end user opted in to provide feedback, the operating system returns this debug report to Microsoft through the Online Crash Analysis (OCA) mechanism.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20TDR%20Error%20Messaging%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




