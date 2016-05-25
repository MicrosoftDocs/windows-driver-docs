---
title: Access to Scatter/Gather Lists in the ATA Port I/O Model
author: windows-driver-content
description: Access to Scatter/Gather Lists in the ATA Port I/O Model
ms.assetid: 56221602-9588-47f2-acd9-a11bd5ce02d9
keywords: ["ATA Port drivers WDK , scatter/gather list", "scatter/gather list WDK ATA Port driver"]
---

# Access to Scatter/Gather Lists in the ATA Port I/O Model


## <span id="ddk_access_to_scatter_gather_lists_in_the_ata_port_i_o_model_kg"></span><span id="DDK_ACCESS_TO_SCATTER_GATHER_LISTS_IN_THE_ATA_PORT_I_O_MODEL_KG"></span>


The [ATA Port I/O Model](ata-port-i-o-model.md), such as the [Storport I/O Model](storport-i-o-model.md), provides its miniport drivers that have direct access to the system's scatter/gather list structure. This direct access reduces the number of calls that the miniport driver must make to port driver support routines to build its private scatter/gather list.

On the other hand, the SCSI port I/O model forces a miniport driver to manually discover and build its own scatter/gather list through repeated calls to the [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) routine.

ATA port miniport drivers can directly access the system's scatter/gather list by using the [**AtaPortGetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff550164) routine. The scatter/gather list that **AtaPortGetScatterGatherList** returns is valid only until the IRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **AtaPortGetScatterGatherList** returns.

The miniport driver's [**IdeHwBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557462) routine should translate the scatter/gather list, if it is necessary.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Access%20to%20Scatter/Gather%20Lists%20in%20the%20ATA%20Port%20I/O%20Model%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


