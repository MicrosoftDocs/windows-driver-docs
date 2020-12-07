---
title: Introduction to Storage Port Drivers
description: Storage Port Drivers
keywords:
- storage port drivers WDK
- storage port drivers WDK , about storage port drivers
- port drivers WDK storage
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to Storage Port Drivers

Microsoft Windows contains three system-supplied storage port drivers:

- [Storport Driver](storport-driver-overview.md) (*Storport.sys*), available in Windows Server 2003 and later versions of the operating system (recommended)

- [SCSI Port Driver](scsi-port-driver-overview.md) (*Scsiport.sys*)

- [ATA Port Driver](ata-port-driver-overview.md) (*Ataport.sys*), available in Windows Vista and later versions of the operating system

The Storport driver is a more efficient, higher performance driver than SCSI Port. Therefore you should develop miniport drivers that work with the Storport driver whenever possible. It is particularly important to use Storport with high performance devices, such as host-based RAID and fibre channel adapters. Storport cannot be used with adapters or devices that do not support Plug and Play (PnP) or that must use system DMA. For a detailed list of restrictions on the use of the Storport driver, see [Requirements for Using Storport with an Adapter](requirements-for-using-storport-with-an-adapter.md).

The ATA port driver shields an ATA miniport driver from the SCSI-based protocol that the port driver uses to communicate with higher-level drivers, such as storage class drivers. For instance, miniport drivers that are attached to either SCSI port or Storport must provide SCSI sense data to the port driver. This is not necessary for an ATA miniport driver. The ATA port driver collects the necessary data from the ATA miniport driver by using ATA commands, organizes the data so that it conforms to a SCSI sense data format, and passes the data on to higher-level drivers as though it were SCSI sense data. The ATA port driver also converts each [SCSI_REQUEST_BLOCK](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block) that it receives from higher-level drivers into an ATA-based equivalent called an [IDE_REQUEST_BLOCK](/windows-hardware/drivers/ddi/irb/ns-irb-_ide_request_block).

Each port driver communicates with a set of vendor-supplied storage miniport drivers and supplies a set of support routines for the miniport drivers to call. Each port driver communicates with its miniport drivers by calling a standard set of routines that every storage miniport driver must implement. The miniport driver routines called by the SCSI port driver, the Storport driver, and the ATA port driver are very similar to one another. Lists of port driver support routines and miniport driver routines can be found in the following sections:

| Port Driver | Support Routines | Miniport Driver Routines |
| ----------- | ---------------- | ------------------------ |
| Storport driver | [Storport Driver Support Routines](storport-driver-support-routines.md) | [Storport Driver Miniport Routines](storport-miniport-driver-routines.md) |
| SCSI Port driver | [SCSI Port Driver Support Routines](scsi-port-driver-support-routines.md) | [SCSI Miniport Driver Routines](scsi-miniport-driver-routines.md) |
| ATA port driver | [ATA Port Driver Support Routines](ata-miniport-drivers.md) | [ATA Miniport Driver Routines](ata-miniport-drivers.md) |

If you want your storage device to be supported on client Windows products, or on server products earlier than Windows Server 2003, you must supply a SCSI Port miniport driver.

If you want your storage device to be supported on Windows Server 2003 and later versions of the server product family, you can provide either a Storport miniport driver or a SCSI miniport driver. If you wish to install an ATA storage device in Windows Vista and later versions of the operating system, you must provide an ATA port miniport driver.

The sections that follow describe the Storport, SCSI Port, and ATA port drivers and how they differ.
