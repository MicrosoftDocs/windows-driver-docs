---
title: C28602
description: Warning C28602 Avoid calling SendMessageTimeout with HWND_BROADCAST.
ms.assetid: 511df04e-97dc-43a2-9c48-ea1ffe62b813
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28602


warning C28602: Avoid calling SendMessageTimeout with HWND\_BROADCAST

The Code Analysis tool reports this warning when applications use **SendMessageTimeout**, even when the application requests a time-out period for the thread of only 10 seconds. The function does not return until each window has timed out. The application could actually be blocked for the length of time it takes each window to respond. This is because it is not possible to control the response time of every other **HWND** on the system.

To fix this, consider use **PostMessage** instead,so that it is not a blocking call. Alternatively, avoid the use of **HWND\_BROADCAST** to direct the message to a particular window.

 

 





