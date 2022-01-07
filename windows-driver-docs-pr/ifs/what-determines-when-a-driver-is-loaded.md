---
title: File system filter load order
description: Describes concepts related to loading a file system filter driver
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
ms.date: 08/31/2020
---

# File system filter load order

The Windows operating system loads file system filter drivers based on:

- The driver's start type, where each start type represents phases of booting a system.
- The load order groups for file system filter drivers that are loaded at system startup. The concept of load order groups is required by file system filter drivers for interoperability with legacy file system filter drivers. Note that a "minifilter" filter driver can be loaded at any time.

Before exploring when and how file system filter drivers are loaded during the system boot sequence, it is necessary to understand driver start types and load order groups.

## Driver start types

A kernel-mode driver's *start type* specifies whether the driver is to be loaded during or after system startup. There are five possible start types:

| Start Type | Description |
| ---------- | ----------- |
| SERVICE_BOOT_START (0x00000000) | Indicates a driver started by the operating system (OS) loader. File system filter drivers commonly use this start type or SERVICE_DEMAND_START. Legacy file system filters must use this start type; see [file system filter load order groups](load-order-groups-for-file-system-filter-drivers.md) for more information. |
| SERVICE_SYSTEM_START (0x00000001) | Indicates a driver started during OS initialization. This start type is used by the file system recognizer. Except for the file systems listed below under "SERVICE_DISABLED," file systems (including network file system components) commonly use this start type or SERVICE_DEMAND_START. This start type is also used by device drivers for PnP devices that are enumerated during system initialization but not required to load the system. |
| SERVICE_AUTO_START (0x00000002) | Indicates a driver started by the Service Control Manager during system startup. Rarely used. |
| SERVICE_DEMAND_START (0x00000003) | Indicates a driver started on demand, either by the PnP Manager (for device drivers) or by the Service Control Manager (for file systems and file system filter drivers). |
| SERVICE_DISABLED (0x00000004) | Indicates a driver that is not started by the OS loader, Service Control Manager, or PnP Manager. Used by file systems that are loaded by a file system recognizer (except when they are the boot file system) or (in the case of EFS) by another file system. Such file systems include CDFS, EFS, FastFat, NTFS, and UDFS. Also used to temporarily disable a driver during debugging.

All drivers that specify a start type of SERVICE_BOOT_START will be loaded before drivers with a start type of SERVICE_SYSTEM_START or SERVICE_AUTO_START. Within each start type category, the load order group determines when file system filter drivers (and legacy filter drivers) will be loaded.

## Specifying start type

A driver writer can specify the start type for a driver at installation time in either of the following ways:

- By specifying the desired start type for the **StartType** entry in the *service-install-section* referred to by an [**AddService**](../install/inf-addservice-directive.md) directive in the driver's INF file. This method is described in the **ServiceInstall** Section of [Creating an INF file for a filter driver](creating-an-inf-file-for-a-minifilter-driver.md).

- By passing the desired start type for the *dwStartType* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

## Driver load order groups

Within the SERVICE_BOOT_START and SERVICE_SYSTEM_START start types, the relative order in which drivers are loaded is specified by each driver's *load order group*.

Drivers whose start type is SERVICE_BOOT_START are called *boot (or boot-start) drivers*. On Microsoft Windows 2000 and earlier systems, most filters that are boot drivers belong to the "filter" group. On Microsoft Windows XP and later systems, filters that are boot drivers generally belong to one of the FSFilter load order groups. These load order groups are described in detail in [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md).

Driver whose start type is SERVICE_SYSTEM_START are also loaded in the order of the load order groups to which they belong. However, no system-start driver is loaded until after all boot drivers have been loaded.

> [!NOTE]
> Load order groups are ignored for drivers whose start type is SERVICE_AUTO_START, SERVICE_DEMAND_START, or SERVICE_DISABLED.

A complete, ordered list of load order groups can be found under the **ServiceGroupOrder** subkey of the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control** registry key.

The same load group ordering is used for SERVICE_BOOT_START and SERVICE_SYSTEM_START drivers. However, all SERVICE_BOOT_START drivers are loaded and started before any SERVICE_SYSTEM_START drivers are loaded.

## Specifying load order group

A driver writer can specify the load order group for a driver at installation time in either of the following ways:

- By specifying the desired load order group for the **LoadOrderGroup** entry in the *service-install-section* referred to by an **AddService** directive in the driver's INF file. This method is described in **ServiceInstall** Section of [Creating an INF file for a filter driver](creating-an-inf-file-for-a-minifilter-driver.md).

- By passing the desired start type for the *lpLoadOrderGroup* parameter when calling **CreateService** or **ChangeServiceConfig** from a user-mode installation program. This method is described in the reference entries for **CreateService** and **ChangeServiceConfig** in the Microsoft Windows SDK documentation.

For more general information about driver load order and load order groups, see [Specifying Driver Load Order](../install/specifying-driver-load-order.md).

## Rules for loading a filter driver

The following rules about start type and load order groups determine when a filter driver will be loaded:

- A filter driver that specifies a particular start type and load order group is loaded at the same time as other file system filter drivers and legacy filter drivers in that start type and load order group.
- Within each load order group, file system filter drivers and legacy drivers are generally loaded in random order. This normally results in drivers being loaded based on the order in which the driver was installed.
- If a file system filter driver or legacy filter driver does not specify a load order group, it is loaded after all the other drivers of the same start type that do specify a load order group.
