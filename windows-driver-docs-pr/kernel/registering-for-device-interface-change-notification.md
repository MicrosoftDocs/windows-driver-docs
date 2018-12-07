---
title: Registering for Device Interface Change Notification
description: Registering for Device Interface Change Notification
ms.assetid: 680e4c5c-dac6-41b1-b754-aee782145ed0
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP", "registering device interface change notifications", "IoRegisterPlugPlayNotification"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Device Interface Change Notification





A driver registers for notification of device interface arrival and removal events by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

The following information applies to calling this routine for device interface change notification:

-   Specify an *EventCategory* of **EventCategoryDeviceInterfaceChange**.

-   *EventCategoryData* must point to the GUID for a device interface class.

    The GUID for a interface class is typically defined in a header file with the structures, constants, and so forth, for the interface.

-   Specify an *EventCategoryFlags* of PNPNOTIFY\_DEVICE\_INTERFACE\_INCLUDE\_EXISTING\_INTERFACES.

    This flag directs the PnP manager to register the *CallbackRoutine* for future device interface arrivals and departures of the specified class and to call the *CallbackRoutine* immediately for any relevant device interfaces that are already active.

    A driver can call [**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186) to get a list of existing interfaces of a specific class and then register its callback routine without this flag, but using the flag is easier and avoids a potential timing issue.

-   Specify a driver-defined *Context*, if appropriate, that the PnP manager will pass to the callback routine.

A driver that opens a handle to a device in response to a device interface arrival notification should register for **EventCategoryTargetDeviceChange** events on the device. (See [Using PnP Target Device Change Notification](using-pnp-target-device-change-notification.md).)

A driver cancels notification registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398) with the *NotificationEntry* returned by **IoRegisterPlugPlayNotification**.

 

 




