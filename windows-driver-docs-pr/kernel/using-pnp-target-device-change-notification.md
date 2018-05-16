---
title: Using PnP Target Device Change Notification
author: windows-driver-content
description: Using PnP Target Device Change Notification
ms.assetid: a56bda5c-e398-442d-bc90-2e63f8f7e6bf
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using PnP Target Device Change Notification


## <a href="" id="ddk-using-pnp-target-device-change-notification-kg"></a>


A driver registers for **EventCategoryTargetDeviceChange** notification on a device so the driver can be notified when the device is about to be removed. For example, if a driver opens a handle to a device, the driver should register for **EventCategoryTargetDeviceChange** notification on the device so the driver can close its handle when the PnP manager needs to remove the device.

Drivers can also use **EventCategoryTargetDeviceChange** notification for custom notification. (See [Using PnP Custom Notification](using-pnp-custom-notification.md).)

The following subsections discuss how to register for target device change notification and how to handle target device change events in a PnP notification callback routine:

[Registering for Target Device Change Notification](registering-for-target-device-change-notification.md)

[Handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE Event](handling-a-guid-target-device-query-remove-event.md)

[Handling a GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE Event](handling-a-guid-target-device-remove-complete-event.md)

[Handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED Event](handling-a-guid-target-device-remove-cancelled-event.md)

 

 




