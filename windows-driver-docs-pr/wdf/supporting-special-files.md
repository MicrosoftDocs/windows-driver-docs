---
title: Supporting Special Files
description: Supporting Special Files
ms.assetid: 350e715f-be36-4999-99a2-6175d9763b3f
keywords:
- special files WDK KMDF
- paging files WDK KMDF
- dump files WDK KMDF
- hibernation files WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Special Files


*Special files* include paging files, dump files, and hibernation files. If the target device for your driver is a storage device that the system might use for these files, the driver must do the following:

-   Call [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) to enable or disable support for each type of special file. (Each driver's support for special files is disabled by default.)

    A bus driver that [enumerates child devices](enumerating-the-devices-on-a-bus.md) should also call [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) for each child device that can support special files.

-   Call [**WdfDeviceAddDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff545864), if one device is dependent on another device when supporting special files.

-   Optionally provide an [*EvtDeviceUsageNotification*](https://msdn.microsoft.com/library/windows/hardware/ff540915) or (starting in KMDF 1.11) [*EvtDeviceUsageNotificationEx*](https://msdn.microsoft.com/library/windows/hardware/hh406365) callback function, so the driver will be notified when a special file is created or removed.

If your driver calls [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) for a device, and if a special file is open on the device, the framework does not allow the PnP manager to remove or stop the device.

After a driver has called [**WdfDeviceAddDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff545864), it can call [**WdfDeviceRemoveDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff546829) to remove a device's dependency on another device.

 

 





