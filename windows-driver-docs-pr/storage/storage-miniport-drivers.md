---
title: Storage Miniport Drivers
description: Storage Miniport Drivers
ms.assetid: 374d8370-02a9-43ab-ab47-27fa9f4051ea
keywords:
- storage miniport drivers WDK
- miniport drivers WDK storage
- storage drivers WDK , miniport drivers
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# Storage Miniport Drivers

This section contains the following topics:

[SCSI Miniport Drivers](scsi-miniport-drivers.md)

[Storport Miniport Drivers](storport-miniport-drivers.md)

[IDE Controller Minidrivers](ide-controller-minidrivers.md)

[ATA Miniport Drivers](ata-miniport-drivers.md)

The best practice for storage miniport drivers is to avoid calling operating system routines other than the support routines provided by the appropriate port driver support. For example, storage miniport drivers should not call [**KeQuerySystemTime**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequerysystemtime). Instead, miniport drivers should call routines like [**ScsiPortQuerySystemTime**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/nf-srb-scsiportquerysystemtime) or [**StorPortQuerySystemTime**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportquerysystemtime). Storage miniport drivers should not call [**MmGetPhysicalAddress**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-mmgetphysicaladdress). Instead, miniport drivers should call routines like [**ScsiPortGetPhysicalAddress**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/nf-srb-scsiportgetphysicaladdress) and [**StorPortGetPhysicalAddress**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetphysicaladdress).

Do not use [Hardware Abstraction Layer Routines](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) in miniport drivers.

The following list indicates the system-supplied port driver support library that each type of storage miniport driver should use:

| Miniport Driver | Port Driver |
| --------------- | ----------- |
| Storport miniport drivers  | [Storport Driver](storport-driver.md) (*Storport.sys*), available in Windows Server 2003 and later versions of the operating system (recommended) |
| SCSI Port miniport drivers | [SCSI Port Driver](scsi-port-driver.md) (*Scsiport.sys*) |
| ATA Port miniport drivers  | [ATA Port Driver](ata-port-driver.md) (*Ataport.sys*), available in Windows Vista and later versions of the operating system |
| IDE miniport drivers       | See [IDE Port Driver](ide-port-driver.md) |
