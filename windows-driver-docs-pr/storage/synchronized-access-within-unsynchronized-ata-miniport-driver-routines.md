---
title: Synchronized Access within ATA Miniport Driver Routines
description: Synchronized Access within Unsynchronized ATA Miniport Driver Routines
ms.assetid: ed047579-9f22-4725-a4b0-3c44b8db89ef
keywords:
- ATA Port drivers WDK , synchronization
- synchronization WDK ATA Port driver
- unsynchronized processing WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronized Access within ATA Miniport Driver Routines


## <span id="ddk_synchronized_access_within_unsynchronized_ata_miniport_driver_rout"></span><span id="DDK_SYNCHRONIZED_ACCESS_WITHIN_UNSYNCHRONIZED_ATA_MINIPORT_DRIVER_ROUT"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.


Even when an ATA miniport driver does unsynchronized processing of I/O requests in its [**IdeHwBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557462) routine, it can synchronize access to critical system structures by calling [**AtaPortRequestSynchronizedRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550223). This routine resembles the [**StorPortSynchronizeAccess**](https://msdn.microsoft.com/library/windows/hardware/ff567511) routine that is provided in the Storport I/O model. For more information about how Storport miniport drivers manage synchronized access of critical data structures, see [Synchronized Access within Unsynchronized Miniport Driver Routines](synchronized-access-within-unsynchronized-miniport-driver-routines.md).

When an ATA miniport driver calls **AtaPortRequestSynchronizedRoutine**, it must supply a pointer to a callback routine. The callback routine processes the part of the I/O request that must be synchronized with the interrupt handler. For better performance, write your driver to spend as little time as possible to execute the callback routine.

 

 


