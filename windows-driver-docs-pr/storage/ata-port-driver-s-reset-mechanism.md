---
title: ATA Port Driver's Reset Mechanism
description: ATA Port Driver's Reset Mechanism
ms.assetid: adc27819-d1ae-4b97-8109-5d742c0595d3
keywords: ["ATA Port drivers WDK , reset mechanism", "reset mechanism WDK ATA Port driver", "LUN resets WDK ATA Port driver"]
---

# ATA Port Driver's Reset Mechanism


## <span id="ddk_ata_port_drivers_reset_mechanism_kg"></span><span id="DDK_ATA_PORT_DRIVERS_RESET_MECHANISM_KG"></span>


The ATA port driver supports a two-tier reset mechanism that resembles, in some respects, the reset mechanism of the Storport driver. For more information about the Storport reset mechanism, see [Multi-Tier Reset in Storport](multi-tier-reset-in-storport.md).

Like the Storport driver, and unlike the SCSI port driver, the ATA port driver avoids resetting the entire bus wherever possible. The ATA port driver first tries to reset an individual LUN by using an IRB with a function value of IRB\_FUNCTION\_LUN\_RESET. If the reset fails, the ATA port driver resets the entire bus.

For example, suppose the ATA port driver issues an IRB to reset a LUN after one of the LUN's uncompleted requests times out. In response to this LUN reset, the miniport driver performs a device reset operation, if the hardware supports it, and completes all the outstanding requests on the LUN including the reset IRB. The reset IRB is not timed. Therefore no additional requests will be issued to the LUN if the miniport driver does not complete the reset IRB.

If the miniport driver fails the reset IRB (that is, completes the reset IRB with any status other than IRB\_STATUS\_SUCCESS), the ATA port driver calls the miniport driver's [**IdeHwReset**](https://msdn.microsoft.com/library/windows/hardware/ff558998) routine to reset the whole channel. The miniport driver must then complete all the outstanding requests for that channel and perform the necessary operations on the hardware to reset the devices that are attached to that channel.

The ATA port driver does not support target resets for devices that have multiple LUNs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ATA%20Port%20Driver's%20Reset%20Mechanism%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




