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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20PnP%20Target%20Device%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


