---
title: Handling a GUID_TARGET_DEVICE_QUERY_REMOVE Event
description: Handling a GUID_TARGET_DEVICE_QUERY_REMOVE Event
ms.assetid: f3e867c5-f7b8-40d2-a6cc-c5cb82e0b59b
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "GUID_TARGET_DEVICE_QUERY_REMOVE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE Event





Before the PnP manager sends an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) IRP to the drivers for a device, it calls any notification callback routines that registered for **EventCategoryTargetDeviceChange** on the device. The PnP manager specifies a *NotificationStructure*.**Event** of GUID\_TARGET\_DEVICE\_QUERY\_REMOVE.

In response to such a notification, the callback routine determines whether the device can be removed without disrupting the system.

If the device should not be removed, the callback routine returns STATUS\_UNSUCCESSFUL. In response to this status, the PnP manager aborts query-remove processing and the device will not be removed.

If the device can be removed, the callback routine should perform any appropriate operations to prepare for device removal, such as closing any handles open on the device (if possible). If handles remain open on the device, the PnP manager cannot remove the device, and the PnP manager aborts query-remove processing.

When successfully handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE event, a notification callback routine should:

-   Close any open handles to the device.

-   If the driver has an outstanding reference on the file object, dereference the file object.

-   Remain registered for future **EventCategoryTargetDeviceChange** notifications. This is important because the impending remove operation might be canceled.

Closing a handle to a device does not cancel a driver's registration for PnP target device change notification. The PnP manager can still call the driver's notification callback routine, but in such calls the file object in the *NotificationStructure* is not valid.

 

 




