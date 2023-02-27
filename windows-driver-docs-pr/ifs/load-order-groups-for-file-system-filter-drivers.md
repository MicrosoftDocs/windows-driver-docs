---
title: Load order groups for legacy FS filter drivers
description: Load order groups for legacy FS filter drivers
keywords:
- filter drivers WDK file system , driver loading
- file system filter drivers WDK , driver loading
- driver loading WDK file system
- loading drivers WDK file system
- load order groups WDK file system
ms.date: 02/23/2023
---

# Load order groups for legacy file system filter drivers

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Microsoft Windows XP and later operating systems provide a dedicated set of load order groups for legacy file system filter drivers that the OS loads at startup time. On operating systems before Windows XP, filter drivers could use only the "filter" and "file system" load order groups.

A filter can attach only to the top of an existing file system driver stack and can't attach in the middle of a stack. As a result, load order groups are important to file system filter drivers, because the earlier a filter driver loads, the lower it can attach on the file system driver stack.

The following rules about load order groups determine when a file system filter driver is loaded:

- A filter driver that specifies a particular load order group is loaded at the same time as other filter drivers in that group.

- Within each load order group, filter drivers are loaded in random order.

- A filter driver that doesn't specify a load order group is loaded after all other drivers of the same start type that do specify a load order group.

The following table lists the system-defined load order groups for file system filter drivers. For each load order group, the Load Order Group column contains the value that should be specified for that group in the **LoadOrderGroup** entry in the [**Version section**](../install/inf-version-section.md) of a filter's INF file.

The load order groups are listed as they appear on the stack, which is the reverse of the order in which they're loaded.

| Load order group | Description |
| ---------------- | ----------- |
| Filter                       | This group is the same as the "filter" load order group that was available on Windows 2000 and earlier. This group loads last and thus attaches furthest from the file system. |
| FSFilter Top                 | This group is provided for filter drivers that must attach above all other FSFilter types. |
| FSFilter Activity Monitor    | This group includes filter drivers that observe and report on file I/O. |
| FSFilter Undelete            | This group includes filter drivers that recover deleted files. |
| FSFilter Anti-Virus          | This group includes filters that detect and disinfect viruses during file I/O. |
| FSFilter Replication         | This group includes filter drivers that replicate file data to remote servers. |
| FSFilter Continuous Backup   | This group includes filter drivers that replicate file data to backup media. |
| FSFilter Content Screener    | This group includes filter drivers that prevent the creation of specific files or file content. |
| FSFilter Quota Management    | This group includes filter drivers that provide enhanced file system quotas. |
| FSFilter System Recovery     | This group includes filter drivers that perform operations to maintain operating system integrity, such as the System Restore (SR) filter. |
| FSFilter Cluster File System | This group includes filter drivers that are used in products that provide file server metadata across a network. |
| FSFilter HSM                 | This group includes filter drivers that perform hierarchical storage management. |
| FSFilter Imaging             | This group includes ZIP-like filter drivers that provide a virtual namespace. This load group is available on Windows Vista and later versions of the operating system. |
| FSFilter Compression         | This group includes filter drivers that perform file data compression. |
| FSFilter Encryption          | This group includes filter drivers that encrypt and decrypt data during file I/O. |
| FSFilter Virtualization      | This group includes filter drivers that virtualize the file path, such as the Least Authorized User (LUA) filter driver added in Windows Vista. This load group is available on Windows Vista and later versions of the operating system. |
| FSFilter Physical Quota Management | This group includes filter drivers that manage quotas by using physical block counts. |
| FSFilter Open File           | This group includes filter drivers that provide snapshots of already open files. |
| FSFilter Security Enhancer   | This group includes filter drivers that apply lockdown and enhanced access control lists (ACLs). |
| FSFilter Copy Protection     | This group includes filter drivers that check for out-of-band data on media. |
| FSFilter Bottom              | This group is provided for filter drivers that must attach below all other FSFilter types. |
| FSFilter System              | Reserved for internal use. This group includes the HSM and SIS filter drivers. |
| FSFilter Infrastructure      | Reserved for internal use. This group loads first and thus attaches closest to the file system. |
