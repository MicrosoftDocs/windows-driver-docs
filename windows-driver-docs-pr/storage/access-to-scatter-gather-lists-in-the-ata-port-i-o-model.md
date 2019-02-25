---
title: Access to Scatter/Gather Lists in the ATA Port I/O Model
description: Access to Scatter/Gather Lists in the ATA Port I/O Model
ms.assetid: 56221602-9588-47f2-acd9-a11bd5ce02d9
keywords:
- ATA Port drivers WDK , scatter/gather list
- scatter/gather list WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access to Scatter/Gather Lists in the ATA Port I/O Model


## <span id="ddk_access_to_scatter_gather_lists_in_the_ata_port_i_o_model_kg"></span><span id="DDK_ACCESS_TO_SCATTER_GATHER_LISTS_IN_THE_ATA_PORT_I_O_MODEL_KG"></span>

**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.



The [ATA Port I/O Model](ata-port-i-o-model.md), such as the [Storport I/O Model](storport-i-o-model.md), provides its miniport drivers that have direct access to the system's scatter/gather list structure. This direct access reduces the number of calls that the miniport driver must make to port driver support routines to build its private scatter/gather list.

On the other hand, the SCSI port I/O model forces a miniport driver to manually discover and build its own scatter/gather list through repeated calls to the [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) routine.

ATA port miniport drivers can directly access the system's scatter/gather list by using the [**AtaPortGetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff550164) routine. The scatter/gather list that **AtaPortGetScatterGatherList** returns is valid only until the IRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **AtaPortGetScatterGatherList** returns.

The miniport driver's [**IdeHwBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557462) routine should translate the scatter/gather list, if it is necessary.

 

 


