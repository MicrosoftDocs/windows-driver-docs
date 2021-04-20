---
title: Synchronization in the ATA Port I/O Model
description: Synchronization in the ATA Port I/O Model
keywords:
- ATA Port drivers WDK , synchronization
- synchronization WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronization in the ATA Port I/O Model


## <span id="ddk_synchronization_in_the_ata_port_i_o_model_kg"></span><span id="DDK_SYNCHRONIZATION_IN_THE_ATA_PORT_I_O_MODEL_KG"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.


The ATA port driver can be configured to synchronize access to critical data structures, such as the device extension, by ATA miniport driver routines. It is especially important that accesses by the interrupt handler are synchronized with accesses by other miniport driver routines, because these accesses might occur within different thread contexts.

The ATA port driver can operate in either of two synchronization modes. In one mode the miniport driver is synchronized with the interrupt service routine. In the other mode it is not synchronized. An ATA miniport driver can specify the synchronization mode by setting the **SyncWithIsr** member of the [**IDE\_CHANNEL\_CONFIGURATION**](/windows-hardware/drivers/ddi/irb/ns-irb-_ide_channel_configuration) structure. If the miniport driver sets **SyncWithIsr** to **TRUE**, the ATA port driver raises the IRQL to DIRQL before it calls any of the following miniport driver routines: [**IdeHwInitialize**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_initialize), [**IdeHwStartIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_startio), or [**IdeHwReset**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_reset). The following table indicates how the value assigned to **SyncWithIsr** affects the IRQL at which the ATA port driver calls ATA miniport driver routines.

**Miniport driver routines in channel interface**

**IRQL**

**SyncWithIsr = TRUE**

**SyncWithIsr = FALSE**

***AtaChannelInitRoutine***

PASSIVE\_LEVEL

PASSIVE\_LEVEL

***IdeHwControl***

(with parameter ControlAction = StartChannel)

PASSIVE\_LEVEL

PASSIVE\_LEVEL

***IdeHwControl***

(with parameter ControlAction = StopChannel)

PASSIVE\_LEVEL

PASSIVE\_LEVEL

***IdeHwControl***

(with parameter ControlAction = PowerUpChannel)

&lt;= DISPATCH\_LEVEL

&lt;= DISPATCH\_LEVEL

***IdeHwControl***

(with parameter ControlAction = PowerDownChannel)

&lt;= DISPATCH\_LEVEL

&lt;= DISPATCH\_LEVEL

***IdeHwBuildIo***

&lt;= DISPATCH\_LEVEL

&lt;= DISPATCH\_LEVEL

Worker Routine (callback)

DISPATCH\_LEVEL

DISPATCH\_LEVEL

***IdeHwInitialize***

DIRQL

DISPATCH\_LEVEL

***IdeHwStartIo***

DIRQL

DISPATCH\_LEVEL

***IdeHwReset***

DIRQL

DISPATCH\_LEVEL

Synchronization Routine (callback routine specified by [**AtaPortRequestSynchronizedRoutine**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportrequestsynchronizedroutine))

DIRQL

DIRQL

***IdeHwInterrupt***

DIRQL

DIRQL

 

Even when **SyncWithIsr** is set to **FALSE**, the miniport driver can synchronize a callback routine with the interrupt handler by calling [**AtaPortRequestSynchronizedRoutine**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportrequestsynchronizedroutine) and passing it a pointer to the callback routine.

Synchronization is on a per channel basis. Therefore, on a synchronized channel, no two miniport driver routines will execute at the same time, but routines running on separate synchronized channels can execute concurrently.

