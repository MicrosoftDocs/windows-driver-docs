---
title: Setting Device Object Flags for Power Management
author: windows-driver-content
description: Setting Device Object Flags for Power Management
MS-HAID:
- 'PwrMgmt\_e5d16e16-83d3-455b-984a-0315e30dae29.xml'
- 'kernel.setting\_device\_object\_flags\_for\_power\_management'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 58d1a3a2-c8ea-446c-b1d6-ed00411d1d75
keywords: ["DO_POWER_PAGABLE", "DO_POWER_INRUSH", "device object flags WDK power management", "object flags WDK power management", "flags WDK power management"]
---

# Setting Device Object Flags for Power Management


## <a href="" id="ddk-setting-device-object-flags-for-power-management-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Device%20Object%20Flags%20for%20Power%20Management%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


