---
title: Unsynchronized IdeHwBuildIo Routine
description: Unsynchronized IdeHwBuildIo Routine
keywords:
- ATA Port drivers WDK , synchronization
- synchronization WDK ATA Port driver
- AtaHwBuildIo
- unsynchronized processing WDK ATA Port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unsynchronized IdeHwBuildIo Routine


## <span id="ddk_unsynchronized_atahwbuildio_routine_kg"></span><span id="DDK_UNSYNCHRONIZED_ATAHWBUILDIO_ROUTINE_KG"></span>


**NOTE** The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.


The ATA port driver raises the IRQL of the processor to DISPATCH\_LEVEL or above before it calls the ATA miniport driver's start I/O routine, [**IdeHwStartIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_startio). The ATA port driver raises the IRQL of the processor to mask out interrupts and to guarantee that the start I/O routine and the interrupt handler synchronize access to critical operating system structures. To reduce the time that the miniport driver spends in the start I/O routine at an IRQL &gt;= DISPATCH\_LEVEL, the miniport driver provides the [**IdeHwBuildIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_buildio) routine. The ATA port driver calls *IdeHwBuildIo* at IRQL &lt;= DISPATCH\_LEVEL, so that the miniport driver can preprocess as much of the I/O request as possible at the lower IRQL and avoid monopolizing control of the processor.

The Storport I/O model uses a similar technique to minimize the time that is spent in its start I/O routine. For more information about how the Storport driver uses [**HwStorBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio), see the [Unsynchronized HwStorBuildIo Routine](unsynchronized-hwstorbuildio-routine.md).

All processing of an I/O request that requires access to critical system structures, such as the device extension, should be done within the [**IdeHwStartIo**](/windows-hardware/drivers/ddi/irb/nc-irb-ide_hw_startio) routine.

