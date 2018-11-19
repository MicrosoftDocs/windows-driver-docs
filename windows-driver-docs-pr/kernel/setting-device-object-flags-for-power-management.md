---
title: Setting Device Object Flags for Power Management
description: Setting Device Object Flags for Power Management
ms.assetid: 58d1a3a2-c8ea-446c-b1d6-ed00411d1d75
keywords: ["DO_POWER_PAGABLE", "DO_POWER_INRUSH", "device object flags WDK power management", "object flags WDK power management", "flags WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting Device Object Flags for Power Management





In its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, each driver creates a device object (filter device object (DO), functional device object (FDO), or physical device object (PDO)) and sets the DO\_*XXX* flags in the device object to describe the device attributes and driver configuration. The following device object flags pertain to power management.

| Flag               | Description                                                                                                                                                                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DO\_POWER\_INRUSH  | Indicates that the current drawn by the device surges when the device is first turned on. This surge or "inrush" lasts for a short period, after which the current drawn by the device falls to a lower operating level.                                                                                   |
| DO\_POWER\_PAGABLE | Indicates that the driver is pageable. Starting with Windows 2000, drivers that can be paged must set the DO\_POWER\_PAGABLE flag. The power manager calls such drivers at IRQL = PASSIVE\_LEVEL. For more information about pageable drivers, see [Making Drivers Pageable](making-drivers-pageable.md). |

 

The device object flags are typically set by the bus driver when it creates the PDO for the device. However, some function drivers might need to alter the values of these flags as part of their *AddDevice* routines. Starting with Windows Vista, the operating system does not require that all device objects within a device stack have the same power-related flags set. However, in Windows Server 2003, Windows XP, and Windows 2000, all the device objects in a device stack should have the same power-related flags set.

Starting with Windows 2000, drivers of devices that are in the paging path must not set the DO\_POWER\_PAGABLE flag. A driver is in the "paging path" if it participates in I/O operations on the paging file. Drivers that do not set this flag must be callable at IRQL = DISPATCH\_LEVEL. For more information, see [Constraints on Dispatch Routines](https://msdn.microsoft.com/library/windows/hardware/ff539309).

In general, drivers should not alter the bus driver's value for the DO\_POWER\_PAGABLE flag, and a driver must never set this flag if a lower-level driver has cleared it. When handling transitions involving [PnP paging requests](https://msdn.microsoft.com/library/windows/hardware/ff554992) (typically in response to an [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) request), a storage driver must carefully sequence its setting and clearing of the flag.

Drivers for devices that require an inrush of power at start-up must set the DO\_POWER\_INRUSH flag in the device object before clearing the DO\_DEVICE\_INITIALIZING flag. Only one driver in the device stack, typically the bus driver (PDO), needs to set the DO\_POWER\_INRUSH flag for the device. The flag notifies the power manager that such devices must be powered up one at a time, in sequence with other such devices, to avoid overloading the power supply. The power manager ensures that only one power inrush IRP is active anywhere in the system at any given time.

Starting with Windows Vista, drivers can set both the DO\_POWER\_PAGABLE flag and the DO\_POWER\_INRUSH flag. In Windows Server 2003, Windows XP, and Windows 2000, drivers cannot set both the DO\_POWER\_PAGABLE flag and the DO\_POWER\_INRUSH flag.

 

 




