---
title: ATA Port Driver's Reset Mechanism
description: ATA Port Driver's Reset Mechanism
ms.assetid: adc27819-d1ae-4b97-8109-5d742c0595d3
keywords:
- ATA Port drivers WDK , reset mechanism
- reset mechanism WDK ATA Port driver
- LUN resets WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Port Driver's Reset Mechanism


## <span id="ddk_ata_port_drivers_reset_mechanism_kg"></span><span id="DDK_ATA_PORT_DRIVERS_RESET_MECHANISM_KG"></span>

**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.



The ATA port driver supports a two-tier reset mechanism that resembles, in some respects, the reset mechanism of the Storport driver. For more information about the Storport reset mechanism, see [Multi-Tier Reset in Storport](multi-tier-reset-in-storport.md).

Like the Storport driver, and unlike the SCSI port driver, the ATA port driver avoids resetting the entire bus wherever possible. The ATA port driver first tries to reset an individual LUN by using an IRB with a function value of IRB\_FUNCTION\_LUN\_RESET. If the reset fails, the ATA port driver resets the entire bus.

For example, suppose the ATA port driver issues an IRB to reset a LUN after one of the LUN's uncompleted requests times out. In response to this LUN reset, the miniport driver performs a device reset operation, if the hardware supports it, and completes all the outstanding requests on the LUN including the reset IRB. The reset IRB is not timed. Therefore no additional requests will be issued to the LUN if the miniport driver does not complete the reset IRB.

If the miniport driver fails the reset IRB (that is, completes the reset IRB with any status other than IRB\_STATUS\_SUCCESS), the ATA port driver calls the miniport driver's [**IdeHwReset**](https://msdn.microsoft.com/library/windows/hardware/ff558998) routine to reset the whole channel. The miniport driver must then complete all the outstanding requests for that channel and perform the necessary operations on the hardware to reset the devices that are attached to that channel.

The ATA port driver does not support target resets for devices that have multiple LUNs.

 

 


