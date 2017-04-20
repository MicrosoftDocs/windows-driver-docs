---
title: Sending Notifications
description: Sending Notifications
ms.assetid: 55e0f41c-e042-4170-bedd-160b6c457365
keywords:
- notifications WDK Native 802.11 IHV Extensions DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sending Notifications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The IHV Extensions DLL calls the [**Dot11ExtSendNotification**](https://msdn.microsoft.com/library/windows/hardware/ff547560) function to send notifications to any service or application that has registered for the notification. In order to receive the notification, the service or application must register with the Auto Configuration Manager (ACM) by calling the **WlanRegisterNotification** function. For more information about this function, refer to the Microsoft Windows SDK documentation.

**Note**  The service or application must register for notifications with a source value of L2\_NOTIFICATION\_SOURCE\_WLAN\_IHV in order to receive notifications through calls to the [**Dot11ExtSendNotification**](https://msdn.microsoft.com/library/windows/hardware/ff547560) function.

 

When calling [**Dot11ExtSendNotification**](https://msdn.microsoft.com/library/windows/hardware/ff547560), the IHV Extensions DLL passes a pointer to a [**L2\_NOTIFICATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557044) structure to the *pNotificationData* parameter. The L2\_NOTIFICATION\_DATA defines the type of the notification and can provide additional data about the notification to the IHV Extensions DLL.

 

 





