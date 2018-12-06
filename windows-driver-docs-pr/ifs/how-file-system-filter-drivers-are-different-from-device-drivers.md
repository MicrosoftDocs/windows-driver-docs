---
title: How File System Filter Drivers Are Different from Device Drivers
description: How File System Filter Drivers Are Different from Device Drivers
ms.assetid: 64a59564-a4d7-4174-82d3-60bd1a30b2d8
keywords:
- filter drivers WDK file system , vs. device drivers
- file system filter drivers WDK , vs. device drivers
- device drivers WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How File System Filter Drivers Are Different from Device Drivers


## <span id="ddk_how_file_system_filter_drivers_are_different_from_device_drivers_i"></span><span id="DDK_HOW_FILE_SYSTEM_FILTER_DRIVERS_ARE_DIFFERENT_FROM_DEVICE_DRIVERS_I"></span>


The following subsections describe some of the differences between file system filter drivers and device drivers.

### <span id="No_Power_Management"></span><span id="no_power_management"></span><span id="NO_POWER_MANAGEMENT"></span>No Power Management

Because file system filter drivers are not device drivers and thus do not control hardware devices directly, they do not receive [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests. Instead, power IRPs are sent directly to the storage device stack. In rare circumstances, however, file system filter drivers might interfere with power management. For this reason, file system filter drivers should not register dispatch routines for IRP\_MJ\_POWER in the **DriverEntry** routine, and they should not call [PoXxx](https://msdn.microsoft.com/library/windows/hardware/ff559835) routines.

### <span id="No_WDM"></span><span id="no_wdm"></span><span id="NO_WDM"></span>No WDM

File system filter drivers cannot be Windows Driver Model (WDM) drivers. The Microsoft [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) is only for device drivers. For more information about file system driver development in Windows Me, Windows 98, and Windows 95, see the Windows Me Driver Development Kit (DDK).

### <span id="No_AddDevice_or_StartIo"></span><span id="no_adddevice_or_startio"></span><span id="NO_ADDDEVICE_OR_STARTIO"></span>No AddDevice or StartIo

Because file system filter drivers are not device drivers and thus do not control hardware devices directly, they should not have [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) or [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routines.

### <span id="Different_Device_Objects_Created"></span><span id="different_device_objects_created"></span><span id="DIFFERENT_DEVICE_OBJECTS_CREATED"></span>Different Device Objects Created

Although file system filter drivers and device drivers both create device objects, they differ in the number and kinds of device objects that they create.

Device drivers create physical and functional device objects to represent devices. The Plug and Play (PnP) Manager builds and maintains a global device tree that contains all device objects that are created by device drivers. The device objects that file system filter drivers create are not contained in this device tree.

File system filter drivers do not create physical or functional device objects. Instead, they create control device objects and filter device objects. The *control device object* represents the filter driver to the system and to user-mode applications. The *filter device object* performs the actual work of filtering a specific file system or volume. A file system filter driver normally creates one control device object and one or more filter device objects.

### <span id="Other_Differences"></span><span id="other_differences"></span><span id="OTHER_DIFFERENCES"></span>Other Differences

Because file system filter drivers are not device drivers, they do not perform [direct memory access (DMA)](https://msdn.microsoft.com/library/windows/hardware/ff565374).

Unlike device filter drivers, which can attach above or below a target device's function driver, file system filter drivers can attach only above a target file system driver. Thus, in device-driver terms, a file system filter driver can be only an upper filter, never a lower filter.

 

 




