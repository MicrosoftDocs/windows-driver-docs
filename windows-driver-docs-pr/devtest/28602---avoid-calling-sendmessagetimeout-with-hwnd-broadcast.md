---
title: C28602
description: Warning C28602 Avoid calling SendMessageTimeout with HWND\_BROADCAST.
ms.assetid: 511df04e-97dc-43a2-9c48-ea1ffe62b813
---

# C28602


warning C28602: Avoid calling SendMessageTimeout with HWND\_BROADCAST

The Code Analysis tool reports this warning when applications use **SendMessageTimeout**, even when the application requests a time-out period for the thread of only 10 seconds. The function does not return until each window has timed out. The application could actually be blocked for the length of time it takes each window to respond. This is because it is not possible to control the response time of every other **HWND** on the system.

To fix this, consider use **PostMessage** instead,so that it is not a blocking call. Alternatively, avoid the use of **HWND\_BROADCAST** to direct the message to a particular window.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28602%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




