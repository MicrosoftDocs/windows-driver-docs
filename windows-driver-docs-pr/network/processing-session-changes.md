---
title: Processing Session Changes
description: Processing Session Changes
ms.assetid: 6684b27e-d2ba-4305-bbd2-27543c9ec0cf
keywords: ["user interaction WDK Native 802.11 IHV Extensions DLL", "session changes WDK Native 802.11 IHV Extensions DLL"]
---

# Processing Session Changes


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the user's session changes state, such as when the user logs in or out, the operating system notifies the IHV Extensions DLL about the session change by calling the [*Dot11ExtIhvProcessSessionChange*](https://msdn.microsoft.com/library/windows/hardware/ff547501) function. The operating system passes the reason for the session change to the *uEventType* parameter.

If the *uEventType* parameter is set to WTS\_SESSION\_LOGOFF, the user has logged off of the current session. In this situation, all pending user interface (UI) requests must be canceled internally by the IHV Extensions DLL, and the DLL must free any allocated resources for each pending UI request.

 

 





