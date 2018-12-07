---
title: Handling a GUID_TARGET_DEVICE_REMOVE_CANCELLED Event
description: Handling a GUID_TARGET_DEVICE_REMOVE_CANCELLED Event
ms.assetid: 19fe012b-3ed0-4356-999b-79b1d08dfbd6
keywords: ["notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification", "GUID_TARGET_DEVICE_REMOVE_CANCELLED"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED Event





If an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) request fails, the PnP manager sends an [**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823) IRP to the drivers for the device. After the cancel-remove IRP completes successfully, the PnP manager calls any notification callback routines that registered for **EventCategoryTargetDeviceChange** on the device. The PnP manager specifies a *NotificationStructure*.**Event** of GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED.

When handling a GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED event, a notification callback routine should:

-   Reregister for target device notification.

    Because the driver closed the previous registration handle in response to the query-remove notification, the driver must open a new handle. The driver must:

    1.  Remove the old registration with [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398).

    2.  Open a new handle to the device.

    3.  Reregister for notification on the new handle with **IoRegisterPlugPlayNotification**.

 

 




