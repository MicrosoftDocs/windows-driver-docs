---
title: ATA Port I/O Model
description: ATA Port I/O Model
ms.assetid: 6feaf2c4-63b2-4ab2-9d4d-7259406be652
keywords:
- ATA Port drivers WDK , I/O
- I/O WDK ATA Port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Port I/O Model


## <span id="ddk_ata_port_i_o_model_kg"></span><span id="DDK_ATA_PORT_I_O_MODEL_KG"></span>

**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.



The ATA port driver, just as the Storport driver, uses a push model of I/O. This means that the driver forwards I/O requests asynchronously to its miniport driver, up to a maximum number of overlapping packets, without waiting for the miniport driver to request input. In the push model, the port driver controls the flow of the I/O requests and pushes requests down to the miniport driver.

On the other hand, the SCSI port driver uses a pull model of I/O. In a pull model of I/O, the SCSI port driver forwards I/O requests to its miniport driver synchronously and waits for the miniport driver to request new input before it sends the next I/O request. Additionally, the miniport driver controls the flow of I/O requests and pulls the requests down from the port driver.

For more information about the I/O model of the Storport driver, see [Storport I/O Model](storport-i-o-model.md).

For more information about the I/O model of the SCSI port driver, see [SCSI Port I/O Model](scsi-port-i-o-model.md).

 

 


