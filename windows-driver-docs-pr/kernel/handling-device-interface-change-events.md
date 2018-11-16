---
title: Handling Device Interface Change Events
description: Handling Device Interface Change Events
ms.assetid: 8966ca72-41d6-42bb-84a9-8f907a514338
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Device Interface Change Events





When a driver or a user-mode component enables or disables a device interface instance, the PnP manager calls all notification callback routines that are registered for **EventCategoryDeviceInterfaceChange** events on the device interface class. To indicate the reason for the notification, the PnP manager sets the **Event** member of the callback routine's *NotificationStructure* parameter to GUID\_DEVICE\_INTERFACE\_ARRIVAL or GUID\_DEVICE\_INTERFACE\_REMOVAL.

When handling a GUID\_DEVICE\_INTERFACE\_ARRIVAL event, a notification callback routine should:

-   Perform driver-defined tasks for handling the new interface.

    Typically, a notification callback routine directly opens the device in the context of the callback. However, if opening the device can cause subsequent PnP events to occur (for example, the enumeration of child devices), the callback routine should instead queue a worker routine to open the device; otherwise, a deadlock can occur.

    A callback routine might enable an interface of its own in response to the availability of the new interface.

When handling a GUID\_DEVICE\_INTERFACE\_REMOVAL event, a notification callback routine should:

-   Undo whatever operations it performed when the interface was enabled.

When the device is removed, the driver should close the file handle that it opened during the GUID\_DEVICE\_INTERFACE\_ARRIVAL event callback. For an orderly device removal, the driver should close the file handle during the GUID\_TARGET\_DEVICE\_QUERY\_REMOVE event callback. For a surprise removal, the driver should close the file handle during the GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE event callback. Do not close the file handle during the GUID\_DEVICE\_INTERFACE\_REMOVAL event callback.

 

 




