---
title: Introduction
description: Introduction
ms.assetid: 0AEFA19D-C270-4777-8C08-E6056FBB6BC5
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Storage driver design guide


Storage drivers include [class](storage-class-drivers.md), [port](storage-port-drivers.md), [miniport](storage-miniport-drivers.md), and [filter](storage-filter-drivers.md) drivers. Typically, a device vendor will implement a miniport driver for a specific adapter or adapter type. Although not common, a new storage class can be defined and a new class driver developed for it. Storage classes in Windows include the Disk, CDROM, USB storage, and encrypted drive classes. Storage driver development is usually limited to writing a miniport driver to work with the [StorPort](storport-driver.md) port driver.

Other types of storage drivers are secure [silo](storage-silo-drivers.md) drivers and Device Specific Modules (DSM) for multipath I/O. For storage management, [WMI](https://docs.microsoft.com/windows-hardware/drivers/storage/storage-wmi-classes) providers are developed as a control interface to a driver.

## <span id="Storage_Driver_WDK_Resources"></span><span id="storage_driver_wdk_resources"></span><span id="STORAGE_DRIVER_WDK_RESOURCES"></span>Overview
This design guide includes the following sections:
* [Roadmap for Developing Windows Storage Drivers](roadmap-for-developing-storage-drivers.md)  
* [Roadmap for Developing Storport Miniport Drivers](roadmap-for-developing-storport-miniport-drivers.md)  
* [Storage Drivers](storage-drivers.md)  
* [Storage Class Drivers](storage-class-drivers.md)  
* [Storage Port Drivers](storage-port-drivers.md)  
* [Storage Miniport Drivers](storage-miniport-drivers.md)  
* [Storage Virtual Miniport Drivers](storage-virtual-miniport-drivers.md)  
* [Storage Filter Drivers](storage-filter-drivers.md)  
* [Crash Dump Filter Drivers](crash-dump-filter-drivers.md)  
* [Storage Silo Drivers](storage-silo-drivers.md)  
* [CD-ROM Drivers](cd-rom-drivers.md)  
* [Tape Drivers](tape-drivers.md)  
* [Changer Drivers](changer-drivers.md)  
* [Storage Scenarios](storage-scenarios.md)  

## Samples
Studying samples is a practical way to see how working storage drivers are developed. [Sample storage drivers](https://github.com/Microsoft/Windows-driver-samples) are available on GitHub.

## <span id="Driver_Verification_for_StorPort"></span><span id="driver_verification_for_storport"></span><span id="DRIVER_VERIFICATION_FOR_STORPORT"></span>Driver Verification for StorPort


Using code analysis tools during driver development and testing helps to catch performance problems and defects in a storage driver. The [Static Driver Verifier (SDV)](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier) tool is available to discover defects in storage driver code. Included with SDV are compliance [rules](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) for verifying proper usage of StorPort routines by miniport drivers.

Tests for storage hardware certification are found in the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Test for storage devices are found in the [Devices.Storage](https://docs.microsoft.com/previous-versions/windows/hardware/hck/jj125097(v=vs.85)) category of the HCK.

 

 




