---
title: Supporting Ejectable Devices
description: Supporting Ejectable Devices
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 7820bb71-7218-4c5f-af2b-f41e1b5f696d
keywords: ["PnP WDK KMDF ejectable devices", "Plug and Play WDK KMDF ejectable devices", "power management WDK KMDF ejectable devices", "docking stations WDK KMDF", "bus drivers WDK KMDF", "ejecting devices WDK KMDF", "ejection relations WDK KMDF", "removing ejectable devices", "listing ejectable devices WDK KMDF", "locking ejectable devices WDK KMDF", "portable devices WDK KMDF", "mobile devices WDK KMDF", "removable devices WDK KMDF", "mobile devices WDK"]
---

# Supporting Ejectable Devices


*Ejectable devices* are devices that can be inserted into a docking station and ejected from the docking station. Typically, an ejectable device's bus power must be disabled before the device can be removed.

If a device is ejectable, the bus driver for the device's bus must set the **EjectSupported** member in the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551257) structure.

When a bus driver determines that one of its enumerated child devices is about to be ejected, it calls either [**WdfPdoRequestEject**](https://msdn.microsoft.com/library/windows/hardware/ff548817) or [**WdfChildListRequestChildEject**](https://msdn.microsoft.com/library/windows/hardware/ff545641). For example, the bus driver might detect that a user has pressed an eject button.

When a driver calls [**WdfChildListRequestChildEject**](https://msdn.microsoft.com/library/windows/hardware/ff545641) or [**WdfPdoRequestEject**](https://msdn.microsoft.com/library/windows/hardware/ff548817), the PnP manager uses the [orderly removal](a-user-unplugs-a-device.md#orderly-removal) scenario to inform the device's drivers that the device is being removed. After the framework has called the [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function in the bus driver for the device's bus, the framework calls the bus driver's [*EvtDeviceEject*](https://msdn.microsoft.com/library/windows/hardware/ff540863) callback function, which performs any operations that are necessary to physically eject the device.

If ejecting your device causes additional devices to also be ejected, your bus driver can maintain a list of *ejection relations*. When a user removes your device, the PnP manager informs the drivers of devices in the list that their devices are also being removed. To maintain a list of ejection relations, a bus driver can use the [**WdfPdoAddEjectionRelationsPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548770), [**WdfPdoRemoveEjectionRelationsPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548814), and [**WdfPdoClearEjectionRelationsDevices**](https://msdn.microsoft.com/library/windows/hardware/ff548771) methods.

If a device can be locked in its docking station, the bus driver must set the **LockSupported** member in the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551257) structure. The bus driver must also provide an [*EvtDeviceSetLock*](https://msdn.microsoft.com/library/windows/hardware/ff540909) callback function, which locks the device to disable ejection or unlocks the device to enable ejection.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Ejectable%20Devices%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




