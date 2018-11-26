---
title: What Determines When a Driver Is Loaded
description: What Determines When a Driver Is Loaded
ms.assetid: fe0f27e4-84d4-483e-8b4e-69c39ae332de
keywords:
- filter drivers WDK file system , driver loading
- file system filter drivers WDK , driver loading
- driver loading WDK file system
- loading drivers WDK file system
- driver start types WDK file system
- start types WDK file system
- load order groups WDK file system
- SERVICE_BOOT_START
- SERVICE_SYSTEM_START
- SERVICE_AUTO_START
- SERVICE_DEMAND_START
- SERVICE_DISABLED
- boot drivers WDK file system
- boot-start drivers WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What Determines When a Driver Is Loaded


## <span id="ddk_what_determines_when_a_driver_is_loaded_if"></span><span id="DDK_WHAT_DETERMINES_WHEN_A_DRIVER_IS_LOADED_IF"></span>


Before exploring when and how file system drivers are loaded during the system boot sequence, it is necessary to understand driver start types and load order groups.

### <span id="ddk_driver_start_types_if"></span><span id="DDK_DRIVER_START_TYPES_IF"></span>Driver Start Types

A kernel-mode driver's *start type* specifies whether the driver is to be loaded during or after system startup. There are five possible start types:

<span id="SERVICE_BOOT_START__0x00000000_"></span><span id="service_boot_start__0x00000000_"></span><span id="SERVICE_BOOT_START__0X00000000_"></span>SERVICE\_BOOT\_START (0x00000000)  
Indicates a driver started by the operating system (OS) loader. File system filter drivers commonly use this start type or SERVICE\_DEMAND\_START. On Microsoft Windows XP and later systems, filters must use this start type in order to take advantage of the new [file system filter load order groups](load-order-groups-for-file-system-filter-drivers.md).

<span id="SERVICE_SYSTEM_START__0x00000001_"></span><span id="service_system_start__0x00000001_"></span><span id="SERVICE_SYSTEM_START__0X00000001_"></span>SERVICE\_SYSTEM\_START (0x00000001)  
Indicates a driver started during OS initialization. This start type is used by the file system recognizer. Except for the file systems listed below under "SERVICE\_DISABLED," file systems (including network file system components) commonly use this start type or SERVICE\_DEMAND\_START. This start type is also used by device drivers for PnP devices that are enumerated during system initialization but not required to load the system.

<span id="SERVICE_AUTO_START__0x00000002_"></span><span id="service_auto_start__0x00000002_"></span><span id="SERVICE_AUTO_START__0X00000002_"></span>SERVICE\_AUTO\_START (0x00000002)  
Indicates a driver started by the Service Control Manager during system startup. Rarely used.

<span id="SERVICE_DEMAND_START__0x00000003_"></span><span id="service_demand_start__0x00000003_"></span><span id="SERVICE_DEMAND_START__0X00000003_"></span>SERVICE\_DEMAND\_START (0x00000003)  
Indicates a driver started on demand, either by the PnP Manager (for device drivers) or by the Service Control Manager (for file systems and file system filter drivers).

<span id="SERVICE_DISABLED__0x00000004_"></span><span id="service_disabled__0x00000004_"></span><span id="SERVICE_DISABLED__0X00000004_"></span>SERVICE\_DISABLED (0x00000004)  
Indicates a driver that is not started by the OS loader, Service Control Manager, or PnP Manager. Used by file systems that are loaded by a file system recognizer (except when they are the boot file system) or (in the case of EFS) by another file system. Such file systems include CDFS, EFS, FastFat, NTFS, and UDFS. Also used to temporarily disable a driver during debugging.

### <span id="ddk_specifying_start_type_if"></span><span id="DDK_SPECIFYING_START_TYPE_IF"></span>Specifying Start Type

A driver writer can specify the start type for a driver at installation time in either of the following ways:

-   By specifying the desired start type for the **StartType** entry in the *service-install-section* referred to by an [**AddService**](https://msdn.microsoft.com/library/windows/hardware/ff546326) directive in the driver's INF file. This method is described in ServiceInstall Section.

-   By passing the desired start type for the *dwStartType* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

### <span id="ddk_driver_load_order_groups_if"></span><span id="DDK_DRIVER_LOAD_ORDER_GROUPS_IF"></span>Driver Load Order Groups

Within the SERVICE\_BOOT\_START and SERVICE\_SYSTEM\_START start types, the relative order in which drivers are loaded is specified by each driver's *load order group*.

Drivers whose start type is SERVICE\_BOOT\_START are called *boot (or boot-start) drivers*. On Microsoft Windows 2000 and earlier systems, most filters that are boot drivers belong to the "filter" group. On Microsoft Windows XP and later systems, filters that are boot drivers generally belong to one of the new FSFilter load order groups. These load order groups are described in detail in [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md).

Driver whose start type is SERVICE\_SYSTEM\_START are also loaded in the order of the load order groups to which they belong. However, no system-start driver is loaded until after all boot drivers have been loaded.

**Note**   Load order groups are ignored for drivers whose start type is SERVICE\_AUTO\_START, SERVICE\_DEMAND\_START, or SERVICE\_DISABLED.

 

A complete, ordered list of load order groups can be found under the **ServiceGroupOrder** subkey of the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**

The same load group ordering is used for SERVICE\_BOOT\_START and SERVICE\_SYSTEM\_START drivers. However, all SERVICE\_BOOT\_START drivers are loaded and started before any SERVICE\_SYSTEM\_START drivers are loaded.

### <span id="ddk_specifying_load_order_group_if"></span><span id="DDK_SPECIFYING_LOAD_ORDER_GROUP_IF"></span>Specifying Load Order Group

A driver writer can specify the load order group for a driver at installation time in either of the following ways:

-   By specifying the desired load order group for the **LoadOrderGroup** entry in the *service-install-section* referred to by an **AddService** directive in the driver's INF file. This method is described in ServiceInstall Section.

-   By passing the desired start type for the *lpLoadOrderGroup* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

For more general information about driver load order and load order groups, see [Specifying Driver Load Order](https://msdn.microsoft.com/library/windows/hardware/ff552319).

 

 




