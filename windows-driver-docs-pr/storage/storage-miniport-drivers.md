---
title: Introduction to Storage Miniport Drivers
description: Storage Miniport Drivers
keywords:
- storage miniport drivers WDK
- miniport drivers WDK storage
- storage drivers WDK , miniport drivers
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to Storage Miniport Drivers

A vendor-supplied storage miniport driver works together with a system-supplied storage port driver to support a vendor's storage device on Windows. Communication between these modules happens as follows:

- A miniport calls a set of storage port driver-supplied support routines

- A miniport implements a standard set of routines for its storage port driver to call, some that are required and some that are optional

The miniport driver routines called by the SCSI port driver, the Storport driver, and the ATA port driver are very similar to one another.

The following table lists the types of storage miniport drivers and their associated system-supplied port driver support library:

| Miniport Driver | Port Driver |
| --------------- | ----------- |
| [Storport Miniport Drivers](storport-miniport-drivers.md) | [Storport Driver](storport-driver-overview.md) (*Storport.sys*), available in Windows Server 2003 and later versions of the operating system (recommended) |
| [SCSI Miniport Drivers](scsi-miniport-drivers.md) | [SCSI Port Driver](scsi-port-driver-overview.md) (*Scsiport.sys*) |
| [ATA Miniport Drivers](ata-miniport-drivers.md) | [ATA Port Driver](ata-port-driver-overview.md) (*Ataport.sys*), available in Windows Vista and later versions of the operating system |
| [IDE Controller Minidrivers](requirements-for-vendor-supplied-ide-controller-minidrivers.md) | See [IDE Port Driver](ide-port-driver.md) |

The best practice for storage miniport drivers is to avoid calling operating system routines other than the support routines provided by the appropriate port driver support. For example, storage miniport drivers should not call [**KeQuerySystemTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime). Instead, miniport drivers should call routines like [**ScsiPortQuerySystemTime**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportquerysystemtime) or [**StorPortQuerySystemTime**](/windows-hardware/drivers/ddi/storport/nf-storport-storportquerysystemtime). Storage miniport drivers should not call [**MmGetPhysicalAddress**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmgetphysicaladdress). Instead, miniport drivers should call routines like [**ScsiPortGetPhysicalAddress**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetphysicaladdress) and [**StorPortGetPhysicalAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetphysicaladdress).

Do not use [Hardware Abstraction Layer Routines](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) in miniport drivers.
