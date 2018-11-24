---
title: What Happens to File Systems During System Boot
description: What Happens to File Systems During System Boot
ms.assetid: f6ed556a-2353-4a0d-8db1-1fb5eac3c1ef
keywords:
- filter drivers WDK file system , boot process
- file system filter drivers WDK , boot process
- file system drivers WDK , boot process
- File System Recognizer WDK
- FsRec WDK
- filter drivers WDK file system , driver loading
- file system filter drivers WDK , driver loading
- driver loading WDK file system
- loading drivers WDK file system
- load order groups WDK file system
- reinitialization routines WDK file system
- boot drivers WDK file system
- boot-start drivers WDK file system
- global file system queues WDK file system
- file system queues WDK
- queues WDK file system
- FsRec
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What Happens to File Systems During System Boot


## <span id="ddk_what_happens_to_file_systems_during_system_boot_if"></span><span id="DDK_WHAT_HAPPENS_TO_FILE_SYSTEMS_DURING_SYSTEM_BOOT_IF"></span>


File systems are initialized during the system boot process; specifically, during I/O system initialization. The I/O Manager creates the global file system queue and initializes the file system and filter drivers that were loaded by the operating system (OS) loader and the PnP Manager.

Following is a summary of selected portions of the system boot process that are of interest to file system and filter driver developers.

1.  During system boot, the OS loader loads the boot file system, the RAW file system, and all drivers of type SERVICE\_BOOT\_START before the loader transfers control to the kernel. These drivers are in memory when the kernel gets control.

    Drivers are loaded in order of the load order groups to which they are assigned. Among file system filters, those that are assigned to one of the new file system filter driver load order groups are loaded before all other filter drivers. These load order groups are described in detail in [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md).

    Then all drivers in the "filter" load order group are loaded. Note that the "filter" group includes storage filter drivers as well as file system filter drivers, and it includes third-party as well as built-in filter drivers.

2.  The I/O Manager creates a global file system queue with four segments: one each for CD-ROM, disk, tape devices, and network file systems. Later, when each file system is registered, its control device objects are added to the appropriate segments of this queue. At this point, however, no file systems have yet been registered, so the queue is empty.

3.  The PnP Manager calls the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routines of the RAW file system and all SERVICE\_BOOT\_START drivers.

    If a SERVICE\_BOOT\_START driver is dependent on other drivers, those drivers are loaded and started as well.

    The PnP Manager starts the boot devices by calling the [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routines of the boot device drivers. If a boot device has child devices, those devices are enumerated. The child devices are also configured and started if their drivers are boot-start drivers. If a device's drivers are not all boot-start drivers, the PnP Manager creates a devnode for the device but does not start the device.

    At this point, all boot drivers are loaded and the boot devices are started.

4.  The PnP Manager traverses the PnP device tree, locating and loading the drivers that are associated with each devnode but not already running.

    (For more information about the PnP device tree, see [Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).) When each PnP device starts, the PnP Manager enumerates the children of the device, if any. The PnP Manager configures the child devices, loads their device drivers, and starts the devices.

    The PnP Manager loads each device's drivers *regardless* of the drivers' **StartType**, **LoadOrderGroup**, or **Dependencies** values.

    In this step, the PnP Manager only configures and starts devices that are PnP-enumerable. If a device is not PnP-enumerable, the PnP Manager ignores the device and does not enumerate its children, even if the child devices are PnP-enumerable.

5.  The PnP Manager loads and initializes drivers of type SERVICE\_SYSTEM\_START that are not yet loaded.

    The file system recognizer (FsRec) is loaded at this time. Note that, although it is in the "Boot File System" load order group, FsRec is not the boot file system. The actual boot file system − that is, the file system that mounted the boot volume − is loaded at the start of the boot process.

    Later in the SERVICE\_SYSTEM\_START phase, file systems in the "File System" load order group are loaded. This includes the Named Pipe File System (NPFS) and Mailslot File System (MSFS). It does not include media-based file systems, such as NTFS, FAT, CDFS, or UDFS.

    Network file systems, which are in the "Network" load order group, are also loaded during this phase.

6.  After all drivers that load at boot time have been initialized, the I/O Manager calls the reinitialization routines of any drivers that have them. A *reinitialization routine* is a callback routine that is registered by a boot driver that needs to be given additional processing time at this point in the boot process. Reinitialization routines are registered by calling [**IoRegisterBootDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549494) or [**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511).

7.  The Service Control Manager loads drivers of type SERVICE\_AUTO\_START that are not already loaded.

### <span id="ddk_file_system_recognizer_if"></span><span id="DDK_FILE_SYSTEM_RECOGNIZER_IF"></span>File System Recognizer

After system boot, the storage device drivers for all volumes attached to the system are loaded and started. However, not all built-in file systems are loaded, and not all file system volumes are mounted. The File System Recognizer (FsRec) performs these tasks as needed to process [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) requests.

FsRec is loaded in the SERVICE\_SYSTEM\_START phase of system startup. Note that, although it is in the "Boot File System" load order group, FsRec is not the boot file system. The actual boot file system − that is, the file system that mounted the boot volume − is loaded at the start of the boot process.

 

 




