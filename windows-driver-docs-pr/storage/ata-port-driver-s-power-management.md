---
title: ATA Port Driver's Power Management
description: ATA Port Driver's Power Management
ms.assetid: 01c37fed-3b5b-4dd9-bdbd-5c5499a2ddcf
keywords: ["ATA Port drivers WDK , power management", "power management WDK ATA Port driver"]
---

# ATA Port Driver's Power Management


## <span id="ddk_ata_port_drivers_power_management_kg"></span><span id="DDK_ATA_PORT_DRIVERS_POWER_MANAGEMENT_KG"></span>


The ATA port driver enables the miniport driver to change the power state on an individual LUN or an individual channel. To change the power state of a LUN, the ATA port driver sends an IRB with a function value of IRB\_FUNCTION\_POWER\_CHANGE to the device driver. The **PowerChange** member of the IRB indicates the current and target power states. To change the power state of the whole channel, the port driver calls the [**IdeHwControl**](https://msdn.microsoft.com/library/windows/hardware/ff557465) miniport driver routine.

The miniport driver can begin a power state transition by calling [**AtaPortRequestPowerStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff550220). A miniport driver might call this routine after, for example, a hot plug of an IDE device.

Doing idle detection from a miniport driver is strongly discouraged.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ATA%20Port%20Driver's%20Power%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




