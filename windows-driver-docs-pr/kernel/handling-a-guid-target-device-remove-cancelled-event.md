---
title: Handling a GUID_TARGET_DEVICE_REMOVE_CANCELLED Event
author: windows-driver-content
description: Handling a GUID_TARGET_DEVICE_REMOVE_CANCELLED Event
ms.assetid: 19fe012b-3ed0-4356-999b-79b1d08dfbd6
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "GUID_TARGET_DEVICE_REMOVE_CANCELLED"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED Event


## <a href="" id="ddk-handling-a-guid-target-device-remove-cancelled-event-kg"></a>


If an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) request fails, the PnP manager sends an [**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823) IRP to the drivers for the device. After the cancel-remove IRP completes successfully, the PnP manager calls any notification callback routines that registered for **EventCategoryTargetDeviceChange** on the device. The PnP manager specifies a *NotificationStructure*.**Event** of GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED.

When handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED event, a notification callback routine should:

-   Reregister for target device notification.

    Because the driver closed the previous registration handle in response to the query-remove notification, the driver must open a new handle. The driver must:

    1.  Remove the old registration with [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398).

    2.  Open a new handle to the device.

    3.  Reregister for notification on the new handle with **IoRegisterPlugPlayNotification**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20GUID_TARGET_DEVICE_REMOVE_CANCELLED%20Event%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


