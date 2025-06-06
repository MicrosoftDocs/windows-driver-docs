---
title: Storport Driver
description: Storport Driver
keywords:
- storage port drivers WDK , Storport driver
- Storport drivers WDK
- Storport drivers WDK , about Storport drivers
ms.date: 04/24/2025
---

# Storport Driver

Storport (*storport.sys*) is a system-supplied storage port driver that's especially suitable for use with high-performance buses, such as NVMe over fibre channel (FC) or FC buses and RAID adapters.

There are several advantages to using Storport rather than the older SCSI Port driver:

- Improved performance, both in terms of throughput and the system resources that are used.

- Improved miniport driver interface that addresses the needs of high-end storage vendors such as host-based RAID and fibre channel vendors.

All vendors are encouraged to use Storport where possible, rather than the SCSI Port driver. Certain restrictions apply, however. For example, Storport can't be used with adapters or devices that don't support Plug and Play. All DMA devices must have bus-mastering DMA capability, because Storport doesn't support programmed I/O or subordinate-mode DMA. Other restrictions apply in regard to tagged queuing, autorequest sense, WMI support, the sort of SCSI inquiry data that devices must report, and booting directly from an adapter's ROM BIOS. For a detailed list of restrictions on the use of the Storport driver, see [Requirements for Using Storport with an Adapter](requirements-for-using-storport-with-an-adapter.md).

To better use the investment that vendors made in SCSI Port miniport drivers, Storport follows the SCSI Port-miniport driver architecture with few modifications. Changes to the SCSI Port driver interface were made in areas where new algorithms were able to produce measurable speed increases, or where it was necessary to add support for high-speed buses.
