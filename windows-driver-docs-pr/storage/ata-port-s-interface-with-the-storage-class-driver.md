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


## <span id="ddk_ata_ports_interface_with_the_storage_class_driver_kg"></span><span id="DDK_ATA_PORTS_INTERFACE_WITH_THE_STORAGE_CLASS_DRIVER_KG"></span>

**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.



The ATA port driver, SCSI port driver, and Storport driver all use SRBs to communicate with higher-level drivers, such as storage class drivers. For more information about the interface between storage class and storage port drivers, see [SCSI Port's Interface with the Storage Class Driver](scsi-port-s-interface-with-the-storage-class-driver.md).

 

 


