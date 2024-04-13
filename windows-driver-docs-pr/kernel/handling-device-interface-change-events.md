---
title: Handling Device Interface Change Events
description: Handling Device Interface Change Events
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP"]
ms.date: 06/16/2017
---

# Handling Device Interface Change Events

When a driver or a user-mode component enables or disables a device interface instance, the PnP manager calls all notification callback routines that are registered for **EventCategoryDeviceInterfaceChange** events on the device interface class. To indicate the reason for the notification, the PnP manager sets the **Event** member of the callback routine's *NotificationStructure* parameter to GUID\_DEVICE\_INTERFACE\_ARRIVAL or GUID\_DEVICE\_INTERFACE\_REMOVAL.

When handling a GUID\_DEVICE\_INTERFACE\_ARRIVAL event, a notification callback routine should:

-   Perform driver-defined tasks for handling the new interface.

    Typically, a notification callback routine directly opens the device in the context of the callback. However, if opening the device can cause subsequent PnP events to occur (for example, the enumeration of child devices), the callback routine should instead queue a worker routine to open the device; otherwise, a deadlock can occur.

    A callback routine might enable an interface of its own in response to the availability of the new interface.

When handling a GUID\_DEVICE\_INTERFACE\_REMOVAL event, a notification callback routine should:

-   Undo whatever operations it performed when the interface was enabled. Close any file handles that were opened in response to the interface arrival event.

In addition to **EventCategoryDeviceInterfaceChange**, the driver must also register for [**EventCategoryTargetDeviceChange**](using-pnp-target-device-change-notification.md), and close the file handle from the [**GUID\_TARGET\_DEVICE\_QUERY\_REMOVE**](handling-a-guid-target-device-query-remove-event.md) event callback. Keeping the file handle open will veto the removal process and cause the orderly removal to be canceled.
