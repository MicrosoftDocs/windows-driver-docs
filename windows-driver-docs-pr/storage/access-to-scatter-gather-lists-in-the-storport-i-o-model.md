---
title: Access to Scatter/Gather Lists in the Storport I/O Model
description: Access to Scatter/Gather Lists in the Storport I/O Model
ms.assetid: db05ac58-3317-44b2-9550-e4520537955f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access to Scatter/Gather Lists in the Storport I/O Model


## <span id="ddk_access_to_scatter_gather_lists_in_the_storport_i_o_model_kg"></span><span id="DDK_ACCESS_TO_SCATTER_GATHER_LISTS_IN_THE_STORPORT_I_O_MODEL_KG"></span>


The SCSI Port driver has complete access to a set of scatter/gather list structures that define the memory ranges and physical addresses of an SRB. However, miniport drivers that work with the SCSI Port driver do not. The SCSI Port I/O model forces a miniport driver to manually discover and build its own scatter/gather list through repeated calls to the [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) routine.

The Storport I/O model provides its miniport drivers with direct access to the system's scatter/gather list structure, reducing the number of calls that the miniport driver has to make to port driver support routines to build its private scatter/gather list.

The scatter/gather list that [**StorPortGetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff567097) returns is valid only until the SRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **StorPortGetScatterGatherList** returns.

The miniport driver should perform any necessary translation of the scatter/gather list supplied by Storport to a miniport driver-specific format in the miniport driver's [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) routine.

 

 




