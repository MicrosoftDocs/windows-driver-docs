---
title: Handling a GUID_TARGET_DEVICE_REMOVE_COMPLETE Event
description: Handling a GUID_TARGET_DEVICE_REMOVE_COMPLETE Event
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "GUID_TARGET_DEVICE_REMOVE_COMPLETE"]
ms.date: 06/16/2017
---

# Handling a GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE Event





Before the PnP manager sends an [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) IRP to the drivers for a device, the PnP manager calls any kernel-mode notification callback routines that registered for **EventCategoryTargetDeviceChange** on the device. The PnP manager specifies a *NotificationStructure*.**Event** of GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE.

When handling a GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE event, a notification callback routine should:

-   Remove notification registration on the device.

    The device has been removed, so the driver calls [**IoUnregisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregisterplugplaynotification) to remove the notification registration.

    The device may still be physically present on the machine, but all device objects have been deleted and the device is not available for use.

-   Perform surprise-remove processing if the driver did not receive a previous query-remove notification.

    If a device is surprise-removed, the PnP manager sends registered drivers a remove-complete notification without a prior query-remove notification. In this case a driver has to perform any necessary cleanup, such as closing any handles to the device and removing any outstanding references to the file object.

 

