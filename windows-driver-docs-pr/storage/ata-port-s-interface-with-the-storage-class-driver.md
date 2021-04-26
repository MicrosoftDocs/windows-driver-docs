---
title: ATA Port's Interface with the Storage Class Driver
description: ATA Port's Interface with the Storage Class Driver
keywords:
- ATA Port drivers WDK , storage class drivers
- storage class drivers WDK , ATA Port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Port's Interface with the Storage Class Driver

> [!NOTE]
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.

The ATA port driver, SCSI port driver, and Storport driver all use SRBs to communicate with higher-level drivers, such as storage class drivers. For more information about the interface between storage class and storage port drivers, see [SCSI Port's Interface with the Storage Class Driver](scsi-port-s-srb-interface-with-the-storage-class-driver.md).
