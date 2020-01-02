---
title: ATA Port's Interface with the Storage Class Driver
description: ATA Port's Interface with the Storage Class Driver
ms.assetid: 6b22bbb1-f14e-48d9-a00c-c7eae79a078f
keywords:
- ATA Port drivers WDK , storage class drivers
- storage class drivers WDK , ATA Port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Port's Interface with the Storage Class Driver

> [!NOTE]
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://docs.microsoft.com/windows-hardware/drivers/storage/storport-driver-overview) and [Storport miniport](https://docs.microsoft.com/windows-hardware/drivers/storage/storport-miniport-drivers) driver models.

The ATA port driver, SCSI port driver, and Storport driver all use SRBs to communicate with higher-level drivers, such as storage class drivers. For more information about the interface between storage class and storage port drivers, see [SCSI Port's Interface with the Storage Class Driver](scsi-port-s-srb-interface-with-the-storage-class-driver.md).
