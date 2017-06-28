---
title: Handling Device Interface Change Events
author: windows-driver-content
description: Handling Device Interface Change Events
ms.assetid: 8966ca72-41d6-42bb-84a9-8f907a514338
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Device Interface Change Events


## <a href="" id="ddk-handling-device-interface-change-events-kg"></a>


When a driver or a user-mode component enables or disables a device interface instance, the PnP manager calls all notification callback routines that are registered for **EventCategoryDeviceInterfaceChange** events on the device interface class. To indicate the reason for the notification, the PnP manager sets the **Event** member of the callback routine's *NotificationStructure* parameter to GUID\_DEVICE\_INTERFACE\_ARRIVAL or GUID\_DEVICE\_INTERFACE\_REMOVAL.

When handling a GUID\_DEVICE\_INTERFACE\_ARRIVAL event, a notification callback routine should:

-   Perform driver-defined tasks for handling the new interface.

    Typically, a notification callback routine directly opens the device in the context of the callback. However, if opening the device can cause subsequent PnP events to occur (for example, the enumeration of child devices), the callback routine should instead queue a worker routine to open the device; otherwise, a deadlock can occur.

    A callback routine might enable an interface of its own in response to the availability of the new interface.

When handling a GUID\_DEVICE\_INTERFACE\_REMOVAL event, a notification callback routine should:

-   Undo whatever operations it performed when the interface was enabled.

When the device is removed, the driver should close the file handle that it opened during the GUID\_DEVICE\_INTERFACE\_ARRIVAL event callback. For an orderly device removal, the driver should close the file handle during the GUID\_TARGET\_DEVICE\_QUERY\_REMOVE event callback. For a surprise removal, the driver should close the file handle during the GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE event callback. Do not close the file handle during the GUID\_DEVICE\_INTERFACE\_REMOVAL event callback.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Device%20Interface%20Change%20Events%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


