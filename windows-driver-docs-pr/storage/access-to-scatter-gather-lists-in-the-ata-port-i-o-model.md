---
title: Access to Scatter/Gather Lists in the ATA Port I/O Model
description: Access to Scatter/Gather Lists in the ATA Port I/O Model
keywords:
- ATA Port drivers WDK , scatter/gather list
- scatter/gather list WDK ATA Port driver
ms.date: 04/20/2017
---

# Access to Scatter/Gather Lists in the ATA Port I/O Model


## <span id="ddk_access_to_scatter_gather_lists_in_the_ata_port_i_o_model_kg"></span><span id="DDK_ACCESS_TO_SCATTER_GATHER_LISTS_IN_THE_ATA_PORT_I_O_MODEL_KG"></span>

**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.



The [ATA Port I/O Model](ata-port-i-o-model.md), such as the [Storport I/O Model](storport-i-o-model.md), provides its miniport drivers that have direct access to the system's scatter/gather list structure. This direct access reduces the number of calls that the miniport driver must make to port driver support routines to build its private scatter/gather list.

On the other hand, the SCSI port I/O model forces a miniport driver to manually discover and build its own scatter/gather list through repeated calls to the [**ScsiPortGetPhysicalAddress**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetphysicaladdress) routine.

ATA port miniport drivers can directly access the system's scatter/gather list by using the [**AtaPortGetScatterGatherList**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportgetscattergatherlist) routine. The scatter/gather list that **AtaPortGetScatterGatherList** returns is valid only until the IRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **AtaPortGetScatterGatherList** returns.

The miniport driver's [**IdeHwBuildIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_buildio) routine should translate the scatter/gather list, if it is necessary.

