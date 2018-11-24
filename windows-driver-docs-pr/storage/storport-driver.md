---
title: Storport Driver
description: Storport Driver
ms.assetid: d5bda2f6-c4bb-4b90-a149-131785295687
keywords:
- storage port drivers WDK , Storport driver
- Storport drivers WDK
- Storport drivers WDK , about Storport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport Driver


## <span id="ddk_storport_driver_kg"></span><span id="DDK_STORPORT_DRIVER_KG"></span>


In addition to the SCSI Port driver, Microsoft Windows Server 2003 and later versions provide Storport (*storport.sys*), a storage port driver that is especially suitable for use with high-performance buses, such as fibre channel buses, and RAID adapters.

There are several advantages to using Storport rather than the SCSI Port driver:

-   Improved performance, both in terms of throughput and the system resources that are utilized.

-   Improved miniport driver interface that addresses the needs of high-end storage vendors, particularly host-based RAID and fibre channel vendors.

All vendors are encouraged to use Storport where possible, rather than the SCSI Port driver. Certain restrictions apply, however. Storport cannot be used with adapters or devices that do not support Plug and Play. All DMA devices must have bus-mastering DMA capability, because Storport does not support programmed I/O or subordinate-mode DMA. Other restrictions apply in regard to tagged queuing, autorequest sense, WMI support, the sort of SCSI inquiry data that devices must report, and booting directly from an adapter's ROM BIOS. For a detailed list of restrictions on the use of the Storport driver, see [Requirements for Using Storport with an Adapter](requirements-for-using-storport-with-an-adapter.md).

To better utilize the investment that vendors have made in SCSI Port miniport drivers, Storport follows the SCSI Port-miniport driver architecture with very few modifications. Changes to the SCSI Port driver interface were made in areas where new algorithms were able to produce measurable speed increases, or where it was necessary to add support for high-speed buses.

This section includes the following topics:

[Life Cycle of a Storport Driver](life-cycle-of-a-storport-driver.md)

[History of Storport](history-of-storport.md)

[Capabilities Provided by Storport](capabilities-provided-by-storport.md)

[Storport's Interface with the Storage Class Driver](storport-s-interface-with-the-storage-class-driver.md)

[Storport's Interface with Storport Miniport Drivers](storport-s-interface-with-storport-miniport-drivers.md)

[Storport I/O Model](storport-i-o-model.md)

[Storport Queue Management](storport-queue-management.md)

[Storport Event Log Extensions](storport-event-log-extensions.md)

[Storport Error Management](storport-error-management.md)

[Storport Idle Power Management](storport-idle-power-management.md)

[Making SCSI Port Miniport Drivers Work with Storport](making-scsi-port-miniport-drivers-work-with-storport.md)

 

 




