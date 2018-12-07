---
title: Supporting Ejectable Devices
description: Supporting Ejectable Devices
ms.assetid: 7820bb71-7218-4c5f-af2b-f41e1b5f696d
keywords:
- PnP WDK KMDF , ejectable devices
- Plug and Play WDK KMDF , ejectable devices
- power management WDK KMDF , ejectable devices
- docking stations WDK KMDF
- bus drivers WDK KMDF
- ejecting devices WDK KMDF
- ejection relations WDK KMDF
- removing ejectable devices
- listing ejectable devices WDK KMDF
- locking ejectable devices WDK KMDF
- portable devices WDK KMDF
- mobile devices WDK , KMDF
- removable devices WDK KMDF
- mobile devices WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Ejectable Devices


*Ejectable devices* are devices that can be inserted into a docking station and ejected from the docking station. Typically, an ejectable device's bus power must be disabled before the device can be removed.

If a device is ejectable, the bus driver for the device's bus must set the **EjectSupported** member in the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551257) structure.

When a bus driver determines that one of its enumerated child devices is about to be ejected, it calls either [**WdfPdoRequestEject**](https://msdn.microsoft.com/library/windows/hardware/ff548817) or [**WdfChildListRequestChildEject**](https://msdn.microsoft.com/library/windows/hardware/ff545641). For example, the bus driver might detect that a user has pressed an eject button.

When a driver calls [**WdfChildListRequestChildEject**](https://msdn.microsoft.com/library/windows/hardware/ff545641) or [**WdfPdoRequestEject**](https://msdn.microsoft.com/library/windows/hardware/ff548817), the PnP manager uses the [orderly removal](a-user-unplugs-a-device.md#orderly-removal) scenario to inform the device's drivers that the device is being removed. After the framework has called the [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function in the bus driver for the device's bus, the framework calls the bus driver's [*EvtDeviceEject*](https://msdn.microsoft.com/library/windows/hardware/ff540863) callback function, which performs any operations that are necessary to physically eject the device.

If ejecting your device causes additional devices to also be ejected, your bus driver can maintain a list of *ejection relations*. When a user removes your device, the PnP manager informs the drivers of devices in the list that their devices are also being removed. To maintain a list of ejection relations, a bus driver can use the [**WdfPdoAddEjectionRelationsPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548770), [**WdfPdoRemoveEjectionRelationsPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548814), and [**WdfPdoClearEjectionRelationsDevices**](https://msdn.microsoft.com/library/windows/hardware/ff548771) methods.

If a device can be locked in its docking station, the bus driver must set the **LockSupported** member in the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551257) structure. The bus driver must also provide an [*EvtDeviceSetLock*](https://msdn.microsoft.com/library/windows/hardware/ff540909) callback function, which locks the device to disable ejection or unlocks the device to enable ejection.

 

 





