---
title: Introduction
description: Introduction
ms.assetid: 0AEFA19D-C270-4777-8C08-E6056FBB6BC5
ms.date: 12/15/2019
ms.topic: article
---

# Storage driver design guide

Storage drivers include [class](introduction-to-storage-class-drivers.md), [port](storage-port-drivers.md), [miniport](storage-miniport-drivers.md), and [filter](storage-filter-drivers.md) drivers. Typically, a device vendor will implement a miniport driver for a specific adapter or adapter type. Although not common, a new storage class can be defined and a new class driver developed for it. Storage classes in Windows include the Disk, CDROM, USB storage, and encrypted drive classes. Storage driver development is usually limited to writing a miniport driver to work with the [StorPort](storport-driver-overview.md) port driver.

Other types of storage drivers are secure [silo](overview.md) drivers and Device Specific Modules (_DSM) for multipath I/O. For storage management, [WMI](./storage-wmi-classes.md) providers are developed as a control interface to a driver.

The storage driver design guide includes the following sections:

* [Roadmap for Developing Windows Storage Drivers](roadmap-for-developing-storage-drivers.md)
* [Roadmap for Developing Storport Miniport Drivers](roadmap-for-developing-storport-miniport-drivers.md)  
* [Storage Drivers](storage-drivers.md)  
* [Storage Class Drivers](introduction-to-storage-class-drivers.md)  
* [Storage Port Drivers](storage-port-drivers.md)  
* [Storage Miniport Drivers](storage-miniport-drivers.md)  
* [Storage Virtual Miniport Drivers](overview-of-storage-virtual-miniport-drivers.md)  
* [Storage Filter Drivers](storage-filter-drivers.md)  
* [Crash Dump Filter Drivers](crash-dump-filter-drivers.md)  
* [Storage Silo Drivers](overview.md)  
* [CD-ROM Drivers](cd-rom-drivers.md)  
* [Tape Drivers](tape-drivers-overview.md)  
* [Changer Drivers](changer-drivers.md)  
* [Storage Scenarios](offloaded-data-transfer.md)  

## Samples

Studying samples is a practical way to see how working storage drivers are developed. [Sample storage drivers](https://github.com/Microsoft/Windows-driver-samples) are available on GitHub.

## Driver Verification for StorPort

Using code analysis tools during driver development and testing helps to catch performance problems and defects in a storage driver. The [Static Driver Verifier (SDV)](../devtest/static-driver-verifier.md) tool is available to discover defects in storage driver code. Included with SDV are compliance [rules](../devtest/declaring-functions-by-using-function-role-types-for-storport-drivers.md) for verifying proper usage of StorPort routines by miniport drivers.