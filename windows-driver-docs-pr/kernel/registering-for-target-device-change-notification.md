---
title: Registering for Target Device Change Notification
author: windows-driver-content
description: Registering for Target Device Change Notification
ms.assetid: 5f7a9c44-c9a4-4ff8-a97d-ad2462b86af0
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "registering target device change notifications", "IoRegisterPlugPlayNotification"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering for Target Device Change Notification


## <a href="" id="ddk-registering-for-target-device-change-notification-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Target%20Device%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


