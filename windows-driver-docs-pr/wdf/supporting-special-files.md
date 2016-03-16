---
title: Supporting Special Files
description: Supporting Special Files
ms.assetid: 350e715f-be36-4999-99a2-6175d9763b3f
keywords: ["special files WDK KMDF", "paging files WDK KMDF", "dump files WDK KMDF", "hibernation files WDK KMDF"]
---

# Supporting Special Files


*Special files* include paging files, dump files, and hibernation files. If the target device for your driver is a storage device that the system might use for these files, the driver must do the following:

-   Call [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) to enable or disable support for each type of special file. (Each driver's support for special files is disabled by default.)

    A bus driver that [enumerates child devices](enumerating-the-devices-on-a-bus.md) should also call [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) for each child device that can support special files.

-   Call [**WdfDeviceAddDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff545864), if one device is dependent on another device when supporting special files.

-   Optionally provide an [*EvtDeviceUsageNotification*](https://msdn.microsoft.com/library/windows/hardware/ff540915) or (starting in KMDF 1.11) [*EvtDeviceUsageNotificationEx*](https://msdn.microsoft.com/library/windows/hardware/hh406365) callback function, so the driver will be notified when a special file is created or removed.

If your driver calls [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) for a device, and if a special file is open on the device, the framework does not allow the PnP manager to remove or stop the device.

After a driver has called [**WdfDeviceAddDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff545864), it can call [**WdfDeviceRemoveDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff546829) to remove a device's dependency on another device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Special%20Files%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




