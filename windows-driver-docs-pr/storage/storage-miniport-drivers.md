---
title: About Storage Miniport Drivers
description: Storage Miniport Drivers
keywords:
- storage miniport drivers WDK
- miniport drivers WDK storage
- storage drivers WDK , miniport drivers
ms.date: 03/16/2021
---

# About Storage Miniport Drivers

A vendor-supplied storage miniport driver [works together](communicating-with-a-storage-port-driver.md) with a system-supplied storage port driver to support a vendor's storage device on Windows.

The following table lists the types of storage miniport drivers and their associated system-supplied port driver support library:

| Miniport Driver | Port Driver |
| --------------- | ----------- |
| [Storport Miniport Drivers](storport-miniport-drivers.md) | [Storport Driver](storport-driver-overview.md) (*Storport.sys*), available in Windows Server 2003 and later versions of the operating system (recommended) |
| [SCSI Miniport Drivers](scsi-miniport-drivers.md) | [SCSI Port Driver](scsi-port-driver-overview.md) (*Scsiport.sys*) |
| [ATA Miniport Drivers](ata-miniport-drivers.md) | [ATA Port Driver](ata-port-driver-overview.md) (*Ataport.sys*), available in Windows Vista and later versions of the operating system |
| [IDE Controller Minidrivers](requirements-for-vendor-supplied-ide-controller-minidrivers.md) | See [IDE Port Driver](ide-port-driver.md) |
