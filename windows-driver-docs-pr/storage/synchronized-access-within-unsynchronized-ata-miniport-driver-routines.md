---
title: Synchronized Access within ATA Miniport Driver Routines
description: Synchronized Access within Unsynchronized ATA Miniport Driver Routines
keywords:
- ATA Port drivers WDK , synchronization
- synchronization WDK ATA Port driver
- unsynchronized processing WDK ATA Port driver
ms.date: 04/20/2017
---

# Synchronized Access within ATA Miniport Driver Routines


## <span id="ddk_synchronized_access_within_unsynchronized_ata_miniport_driver_rout"></span><span id="DDK_SYNCHRONIZED_ACCESS_WITHIN_UNSYNCHRONIZED_ATA_MINIPORT_DRIVER_ROUT"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.


Even when an ATA miniport driver does unsynchronized processing of I/O requests in its [**IdeHwBuildIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_buildio) routine, it can synchronize access to critical system structures by calling [**AtaPortRequestSynchronizedRoutine**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportrequestsynchronizedroutine). This routine resembles the [**StorPortSynchronizeAccess**](/windows-hardware/drivers/ddi/storport/nf-storport-storportsynchronizeaccess) routine that is provided in the Storport I/O model. For more information about how Storport miniport drivers manage synchronized access of critical data structures, see [Synchronized Access within Unsynchronized Miniport Driver Routines](synchronized-access-within-unsynchronized-miniport-driver-routines.md).

When an ATA miniport driver calls **AtaPortRequestSynchronizedRoutine**, it must supply a pointer to a callback routine. The callback routine processes the part of the I/O request that must be synchronized with the interrupt handler. For better performance, write your driver to spend as little time as possible to execute the callback routine.

