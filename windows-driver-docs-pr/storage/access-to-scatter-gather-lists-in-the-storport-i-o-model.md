---
title: Access to Scatter/Gather Lists in the Storport I/O Model
description: Access to Scatter/Gather Lists in the Storport I/O Model
ms.assetid: db05ac58-3317-44b2-9550-e4520537955f
---

# Access to Scatter/Gather Lists in the Storport I/O Model


## <span id="ddk_access_to_scatter_gather_lists_in_the_storport_i_o_model_kg"></span><span id="DDK_ACCESS_TO_SCATTER_GATHER_LISTS_IN_THE_STORPORT_I_O_MODEL_KG"></span>


The SCSI Port driver has complete access to a set of scatter/gather list structures that define the memory ranges and physical addresses of an SRB. However, miniport drivers that work with the SCSI Port driver do not. The SCSI Port I/O model forces a miniport driver to manually discover and build its own scatter/gather list through repeated calls to the [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) routine.

The Storport I/O model provides its miniport drivers with direct access to the system's scatter/gather list structure, reducing the number of calls that the miniport driver has to make to port driver support routines to build its private scatter/gather list.

The scatter/gather list that [**StorPortGetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff567097) returns is valid only until the SRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **StorPortGetScatterGatherList** returns.

The miniport driver should perform any necessary translation of the scatter/gather list supplied by Storport to a miniport driver-specific format in the miniport driver's [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Access%20to%20Scatter/Gather%20Lists%20in%20the%20Storport%20I/O%20Model%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




