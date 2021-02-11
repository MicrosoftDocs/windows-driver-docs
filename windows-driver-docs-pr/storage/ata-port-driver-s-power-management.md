---
title: ATA Port Driver's Power Management
description: ATA Port Driver's Power Management
keywords:
- ATA Port drivers WDK , power management
- power management WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Port Driver's Power Management


## <span id="ddk_ata_port_drivers_power_management_kg"></span><span id="DDK_ATA_PORT_DRIVERS_POWER_MANAGEMENT_KG"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.


The ATA port driver enables the miniport driver to change the power state on an individual LUN or an individual channel. To change the power state of a LUN, the ATA port driver sends an IRB with a function value of IRB\_FUNCTION\_POWER\_CHANGE to the device driver. The **PowerChange** member of the IRB indicates the current and target power states. To change the power state of the whole channel, the port driver calls the [**IdeHwControl**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_control) miniport driver routine.

The miniport driver can begin a power state transition by calling [**AtaPortRequestPowerStateChange**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportrequestpowerstatechange). A miniport driver might call this routine after, for example, a hot plug of an IDE device.

Doing idle detection from a miniport driver is strongly discouraged.

