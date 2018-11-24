---
title: Synchronization in the ATA Port I/O Model
description: Synchronization in the ATA Port I/O Model
ms.assetid: 91b95588-8cf7-4833-84c2-a991fd066fb2
keywords:
- ATA Port drivers WDK , synchronization
- synchronization WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronization in the ATA Port I/O Model


## <span id="ddk_synchronization_in_the_ata_port_i_o_model_kg"></span><span id="DDK_SYNCHRONIZATION_IN_THE_ATA_PORT_I_O_MODEL_KG"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.


The ATA port driver can be configured to synchronize access to critical data structures, such as the device extension, by ATA miniport driver routines. It is especially important that accesses by the interrupt handler are synchronized with accesses by other miniport driver routines, because these accesses might occur within different thread contexts.

The ATA port driver can operate in either of two synchronization modes. In one mode the miniport driver is synchronized with the interrupt service routine. In the other mode it is not synchronized. An ATA miniport driver can specify the synchronization mode by setting the **SyncWithIsr** member of the [**IDE\_CHANNEL\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff559029) structure. If the miniport driver sets **SyncWithIsr** to **TRUE**, the ATA port driver raises the IRQL to DIRQL before it calls any of the following miniport driver routines: [**IdeHwInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557467), [**IdeHwStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff559003), or [**IdeHwReset**](https://msdn.microsoft.com/library/windows/hardware/ff558998). The following table indicates how the value assigned to **SyncWithIsr** affects the IRQL at which the ATA port driver calls ATA miniport driver routines.

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

Synchronization Routine (callback routine specified by [**AtaPortRequestSynchronizedRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550223))

DIRQL

DIRQL

***IdeHwInterrupt***

DIRQL

DIRQL

 

Even when **SyncWithIsr** is set to **FALSE**, the miniport driver can synchronize a callback routine with the interrupt handler by calling [**AtaPortRequestSynchronizedRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550223) and passing it a pointer to the callback routine.

Synchronization is on a per channel basis. Therefore, on a synchronized channel, no two miniport driver routines will execute at the same time, but routines running on separate synchronized channels can execute concurrently.

 

 


