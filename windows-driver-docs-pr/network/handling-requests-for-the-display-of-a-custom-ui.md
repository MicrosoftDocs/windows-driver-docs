---
title: Handling Requests for the Display of a Custom UI
description: Handling Requests for the Display of a Custom UI
ms.assetid: 77c67469-ac59-449a-87d9-8535527059cb
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , custom UI display requests
- custom UI WDK Native 802.11 IHV UI Extensions DLL
- custom UI WDK Native 802.11 IHV UI Extensions DLL , about custom UI display requests
- displaying custom UI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Requests for the Display of a Custom UI


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section discusses how the Native 802.11 IHV UI Extensions DLL can display a custom user interface (UI) through one of the following:

-   A request from the Native 802.11 IHV Extensions DLL. For example, the Native 802.11 IHV Extensions DLL might request a custom UI for user notification of a wireless LAN (WLAN) event.

-   A query, made by the operating system, to determine whether the Native 802.11 IHV UI Extensions DLL has a custom UI that can be displayed.

This section has the following topics:

[Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md)

[Querying for the Display of a Custom UI](querying-for-the-display-of-a-custom-ui.md)

[Displaying Custom UI Pages within a Balloon Notification](displaying-custom-ui-pages-within-a-balloon-notification.md)

[Displaying Custom UI Pages within the Network Connection Wizard](displaying-custom-ui-pages-within-the-network-connection-wizard.md)

[Accessing Profile and Context Data](accessing-profile-and-context-data.md)

For more information about the Native 802.11 IHV Extensions DLL, see [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614).

 

 





