---
title: Load order groups and altitudes for filter drivers
description: Describes load order groups and altitudes for filter drivers
keywords:
- altitudes WDK file system minifilter
- altitudes WDK file system filter driver
- load order groups WDK file system
- start types WDK file system
- driver start types WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Load order groups and altitudes for filter drivers

## About load order groups and altitudes

Windows uses a dedicated set of *load order groups* for file system filter drivers and legacy filter drivers that are loaded at system startup.

Each load order group has a defined range of *altitudes*. Every filter driver must have a unique altitude identifier. The filter's altitude defines its position relative to other filter drivers in the I/O stack when it is loaded. The altitude is an infinite-precision string interpreted as a decimal number. A filter driver that has a low numerical altitude is loaded into the I/O stack below a filter driver that has a higher numerical value.

Altitude allocation is managed by Microsoft. To request an altitude for your filter driver, see [Filter Altitude Request](minifilter-altitude-request.md).

Altitude values for a filter driver are specified in the **Instance** definitions of the [**Strings** Section in the filter driver's INF file](creating-an-inf-file-for-a-minifilter-driver.md). Instance definitions can also be specified in calls to the [**InstanceSetupCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_instance_setup_callback) routine in the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure. Multiple instances and altitudes can be defined for a filter driver. These instance definitions apply across all volumes.

## Table of load order groups and altitude ranges

The following table lists the system-defined load order groups and altitude ranges for filter drivers. For each load order group, the Load order group column contains the value that should be specified for that group in the **LoadOrderGroup** entry in the [**ServiceInstall** Section of a filter's INF file](creating-an-inf-file-for-a-minifilter-driver.md). The Altitude range column contains the range of altitudes for a particular load order group.

Note that the load order groups and altitude ranges are listed as they appear on the stack, which is the reverse of the order in which they are loaded.

Load order group | Altitude range | Description |
| -------------- | -------------- | ----------- |
| Filter | 420000-429999 | This group is the same as the Filter load order group that was available on Windows 2000 and earlier. This group loads last and thus attaches furthest from the file system. |
| FSFilter Top | 400000-409999 | This group is provided for filter drivers that must attach above all other FSFilter types. |
| FSFilter Activity Monitor | 360000-389999 | This group includes filter drivers that observe and report on file I/O. |
| FSFilter Undelete | 340000-349999 | This group includes filters that recover deleted files. |
| FSFilter Anti-Virus | 320000-329999 | This group includes filter drivers that detect and disinfect viruses during file I/O. |
| FSFilter Replication | 300000-309999 | This group includes filter drivers that replicate file data to remote servers. |
| FSFilter Continuous Backup | 280000-289999 | This group includes filter drivers that replicate file data to backup media. |
| FSFilter Content Screener | 260000-269999 | This group includes filter drivers that prevent the creation of specific files or file content. |
| FSFilter Quota Management | 240000-249999 | This group includes filter drivers that provide enhanced file system quotas. |
| FSFilter System Recovery | 220000-229999 | This group includes filter drivers that perform operations to maintain operating system integrity, such as the System Restore (SR) filter. |
| FSFilter Cluster File System | 200000-209999 | This group includes filter drivers that are used in products that provide file server metadata across a network. |
| FSFilter HSM | 180000-189999 | This group includes filter drivers that perform hierarchical storage management. |
| FSFilter Imaging | 170000-175000 | This group includes ZIP-like filter drivers that provide a virtual namespace. |
| FSFilter Compression | 160000-169999 | This group includes filter drivers that perform file data compression. |
| FSFilter Encryption | 140000-149999 | This group includes filter drivers that encrypt and decrypt data during file I/O. |
| FSFilter Virtualization | 130000- 139999 | This group includes filter drivers that virtualize the file path, such as the Least Authorized User (LUA) filter driver added in Windows Vista. |
| FSFilter Physical Quota Management | 120000-129999 | This group includes filter drivers that manage quotas by using physical block counts. |
| FSFilter Open File | 100000-109999 | This group includes filter drivers that provide snapshots of already open files. |
| FSFilter Security Enhancer | 80000-89999 | This group includes filter drivers that apply lockdown and enhanced access control lists (ACLs). |
| FSFilter Copy Protection | 60000-69999 | This group includes filter drivers that check for out-of-band data on media. |
| FSFilter Bottom | 40000-49999 | This group is provided for filter drivers that must attach below all other FSFilter types. |
| FSFilter System | 20000-29999 | Reserved for internal use. |
| FSFilter Infrastructure | Reserved for internal use. This group loads first and thus attaches closest to the file system. |
