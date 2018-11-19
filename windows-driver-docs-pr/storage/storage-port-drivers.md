---
title: Storage Port Drivers
description: Storage Port Drivers
ms.assetid: 5ff4916c-7d1f-4b61-a332-6ed89df9db56
keywords:
- storage port drivers WDK
- storage port drivers WDK , about storage port drivers
- port drivers WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Port Drivers


## <span id="ddk_storage_port_drivers_kg"></span><span id="DDK_STORAGE_PORT_DRIVERS_KG"></span>


Microsoft Windows contains three system-supplied storage port drivers:

-   [SCSI Port Driver](scsi-port-driver.md) (*Scsiport.sys*)

-   [Storport Driver](storport-driver.md) (*Storport.sys*), available in Windows Server 2003 and later versions of the operating system

-   [ATA Port Driver](ata-port-driver.md) (*Ataport.sys*), available in Windows Vista and later versions of the operating system

The Storport driver is a more efficient, higher performance driver than SCSI Port. Therefore you should develop miniport drivers that work with the Storport driver whenever possible. It is particularly important to use Storport with high performance devices, such as host-based RAID and fibre channel adapters. Storport cannot be used with adapters or devices that do not support Plug and Play (PnP) or that must use system DMA. For a detailed list of restrictions on the use of the Storport driver, see [Requirements for Using Storport with an Adapter](requirements-for-using-storport-with-an-adapter.md).

The ATA port driver shields an ATA miniport driver from the SCSI-based protocol that the port driver uses to communicate with higher-level drivers, such as storage class drivers. For instance, miniport drivers that are attached to either SCSI port or Storport must provide SCSI sense data to the port driver. This is not necessary for an ATA miniport driver. The ATA port driver collects the necessary data from the ATA miniport driver by using ATA commands, organizes the data so that it conforms to a SCSI sense data format, and passes the data on to higher-level drivers as though it were SCSI sense data. The ATA port driver also converts each [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) that it receives from higher-level drivers into an ATA-based equivalent called an [**IDE\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559140).

Each port driver communicates with a set of vendor-supplied storage miniport drivers and supplies a set of support routines for the miniport drivers to call. Support routines supplied by the SCSI Port driver are described in [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375). Support routines supplied by the Storport driver are described in [Storport Driver Support Routines](https://msdn.microsoft.com/library/windows/hardware/ff567548). Support routines supplied by the ATA port driver are described in [ATA Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff551343).

Each port driver communicates with its miniport drivers by calling a standard set of routines that every storage miniport driver must implement. The miniport driver routines called by the SCSI port driver, the Storport driver, and the ATA port driver are very similar to one another. Descriptions of these routines can be found in [SCSI Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff565312), [Storport Driver Miniport Routines](https://msdn.microsoft.com/library/windows/hardware/ff567543), and [ATA Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff551318), respectively.

If you want your storage device to be supported on client Windows products, or on server products earlier than Windows Server 2003, you must supply a SCSI Port miniport driver.

If you want your storage device to be supported on Windows Server 2003 and later versions of the server product family, you can provide either a SCSI Port miniport driver or a Storport miniport driver. If you wish to install an ATA storage device in Windows Vista and later versions of the operating system, you must provide an ATA port miniport driver.

The sections that follow describe the SCSI Port, Storport, and ATA port drivers and how they differ.

 

 




