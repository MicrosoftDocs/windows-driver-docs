---
title: Registering for Target Device Change Notification
description: Registering for Target Device Change Notification
ms.assetid: 5f7a9c44-c9a4-4ff8-a97d-ad2462b86af0
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "registering target device change notifications", "IoRegisterPlugPlayNotification"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Target Device Change Notification

A driver registers for notification of PnP target device change events by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

The following information applies to calling this routine for target device change notification:

-   Specify an *EventCategory* of **EventCategoryTargetDeviceChange**.

-   *EventCategoryData* must point to the file object for the device on which notification is requested.

    If the driver's callback routine requires access to the file object, the driver should take out a reference on the file object before calling **IoRegisterPlugPlayNotification**.

    If the driver's callback routine does not require access to the file object, the driver does not need to reference the object.

    After the file object is closed, the driver continues to receive notifications for the device until the driver removes its notification registration. This design allows the driver to receive notification of GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED events, for example.

-   Specify a driver-defined *Context* that the PnP manager will pass to the callback routine.

    A driver might use the *Context* parameter to maintain information about the current state of the file object (for example, has it been closed/deleted).

    A driver might also use the *Context* to store the path it used to originally open the device. A driver can use this path to reopen the device after a canceled remove operation. (See [Handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED Event](handling-a-guid-target-device-remove-cancelled-event.md) for more information.)

A driver removes a notification registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398) with the *NotificationEntry* returned by **IoRegisterPlugPlayNotification**. If the driver took out a reference on the file object when it registered for notification and that reference is still outstanding, the driver must release the reference after it removes the registration.

 

 




