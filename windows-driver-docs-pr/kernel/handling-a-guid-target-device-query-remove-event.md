---
title: Handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE Event
author: windows-driver-content
description: Handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE Event
ms.assetid: f3e867c5-f7b8-40d2-a6cc-c5cb82e0b59b
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "GUID_TARGET_DEVICE_QUERY_REMOVE"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE Event


## <a href="" id="ddk-handling-a-guid-target-device-query-remove-event-kg"></a>


Before the PnP manager sends an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) IRP to the drivers for a device, it calls any notification callback routines that registered for **EventCategoryTargetDeviceChange** on the device. The PnP manager specifies a *NotificationStructure*.**Event** of GUID\_TARGET\_DEVICE\_QUERY\_REMOVE.

In response to such a notification, the callback routine determines whether the device can be removed without disrupting the system.

If the device should not be removed, the callback routine returns STATUS\_UNSUCCESSFUL. In response to this status, the PnP manager aborts query-remove processing and the device will not be removed.

If the device can be removed, the callback routine should perform any appropriate operations to prepare for device removal, such as closing any handles open on the device (if possible). If handles remain open on the device, the PnP manager cannot remove the device, and the PnP manager aborts query-remove processing.

When successfully handling a GUID\_TARGET\_DEVICE\_QUERY\_REMOVE event, a notification callback routine should:

-   Close any open handles to the device.

-   If the driver has an outstanding reference on the file object, dereference the file object.

-   Remain registered for future **EventCategoryTargetDeviceChange** notifications. This is important because the impending remove operation might be canceled.

Closing a handle to a device does not cancel a driver's registration for PnP target device change notification. The PnP manager can still call the driver's notification callback routine, but in such calls the file object in the *NotificationStructure* is not valid.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20GUID_TARGET_DEVICE_QUERY_REMOVE%20Event%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


