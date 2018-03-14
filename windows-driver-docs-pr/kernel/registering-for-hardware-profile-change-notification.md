---
title: Registering for Hardware Profile Change Notification
author: windows-driver-content
description: Registering for Hardware Profile Change Notification
ms.assetid: 3aaa09f7-ac63-4b56-917a-74cf344f6dd3
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "registering hardware profile change notifications", "machine hardware profile change notifications WDK PnP", "IoRegisterPlugPlayNotification"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering for Hardware Profile Change Notification


## <a href="" id="ddk-registering-for-hardware-profile-change-notification-kg"></a>


A driver registers for notification of hardware profile changes by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

The following information applies to calling this routine for hardware profile change notification:

-   Specify an *EventCategory* of **EventCategoryHardwareProfileChange**.

-   *EventCategoryData* must be **NULL**.

-   Specify a driver-defined *Context*, if appropriate, that the PnP manager will pass to the callback routine.

A driver removes notification registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398) with the *NotificationEntry* returned by **IoRegisterPlugPlayNotification**.

 

 




