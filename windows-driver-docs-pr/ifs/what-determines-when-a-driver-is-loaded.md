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
ms.date: 10/16/2019
ms.localizationpriority: medium
---

# What Determines When a Driver Is Loaded

> [!NOTE]
> For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Before exploring when and how file system drivers are loaded during the system boot sequence, it is necessary to understand driver start types and load order groups.

## Driver Start Types

A kernel-mode driver's *start type* specifies whether the driver is to be loaded during or after system startup. There are five possible start types:

- SERVICE_BOOT_START (0x00000000)  
  Indicates a driver started by the operating system (OS) loader. File system filter drivers commonly use this start type or SERVICE_DEMAND_START. On Microsoft Windows XP and later systems, filters must use this start type in order to take advantage of the new [file system filter load order groups](load-order-groups-for-file-system-filter-drivers.md).

- SERVICE_SYSTEM_START (0x00000001)  
  Indicates a driver started during OS initialization. This start type is used by the file system recognizer. Except for the file systems listed below under "SERVICE_DISABLED," file systems (including network file system components) commonly use this start type or SERVICE_DEMAND_START. This start type is also used by device drivers for PnP devices that are enumerated during system initialization but not required to load the system.

- SERVICE_AUTO_START (0x00000002)  
  Indicates a driver started by the Service Control Manager during system startup. Rarely used.

- SERVICE_DEMAND_START (0x00000003)  
  Indicates a driver started on demand, either by the PnP Manager (for device drivers) or by the Service Control Manager (for file systems and file system filter drivers).

- SERVICE_DISABLED (0x00000004)  
  Indicates a driver that is not started by the OS loader, Service Control Manager, or PnP Manager. Used by file systems that are loaded by a file system recognizer (except when they are the boot file system) or (in the case of EFS) by another file system. Such file systems include CDFS, EFS, FastFat, NTFS, and UDFS. Also used to temporarily disable a driver during debugging.

## Specifying Start Type

A driver writer can specify the start type for a driver at installation time in either of the following ways:

- By specifying the desired start type for the **StartType** entry in the *service-install-section* referred to by an [**AddService**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addservice-directive) directive in the driver's INF file. This method is described in ServiceInstall Section.

- By passing the desired start type for the *dwStartType* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

## Driver Load Order Groups

Within the SERVICE_BOOT_START and SERVICE_SYSTEM_START start types, the relative order in which drivers are loaded is specified by each driver's *load order group*.

Drivers whose start type is SERVICE_BOOT_START are called *boot (or boot-start) drivers*. On Microsoft Windows 2000 and earlier systems, most filters that are boot drivers belong to the "filter" group. On Microsoft Windows XP and later systems, filters that are boot drivers generally belong to one of the new FSFilter load order groups. These load order groups are described in detail in [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md).

Driver whose start type is SERVICE_SYSTEM_START are also loaded in the order of the load order groups to which they belong. However, no system-start driver is loaded until after all boot drivers have been loaded.

> [!NOTE]
> Load order groups are ignored for drivers whose start type is SERVICE_AUTO_START, SERVICE_DEMAND_START, or SERVICE_DISABLED.

A complete, ordered list of load order groups can be found under the **ServiceGroupOrder** subkey of the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control** registry key.

The same load group ordering is used for SERVICE_BOOT_START and SERVICE_SYSTEM_START drivers. However, all SERVICE_BOOT_START drivers are loaded and started before any SERVICE_SYSTEM_START drivers are loaded.

## Specifying Load Order Group

A driver writer can specify the load order group for a driver at installation time in either of the following ways:

- By specifying the desired load order group for the **LoadOrderGroup** entry in the *service-install-section* referred to by an **AddService** directive in the driver's INF file. This method is described in ServiceInstall Section.

- By passing the desired start type for the *lpLoadOrderGroup* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

For more general information about driver load order and load order groups, see [Specifying Driver Load Order](https://docs.microsoft.com/windows-hardware/drivers/install/specifying-driver-load-order).
