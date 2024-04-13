---
title: Unsynchronized HwStorBuildIo Routine
description: Unsynchronized HwStorBuildIo Routine
ms.date: 04/20/2017
---

# Unsynchronized HwStorBuildIo Routine


## <span id="ddk_unsynchronized_hwstorbuildio_routine_kg"></span><span id="DDK_UNSYNCHRONIZED_HWSTORBUILDIO_ROUTINE_KG"></span>


In the SCSI Port-miniport driver I/O model, the miniport driver's [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, [**HwScsiStartIo**](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)), should transmit SCSI request blocks (SRBs) to the hardware as quickly as possible. This is essential, because work done in the miniport driver's *StartIo* routine is accomplished while interrupts are disabled and at IRQL = DISPATCH\_LEVEL. Unfortunately, this model is not well suited to drivers of some high-performance host bus adapters (HBAs), because the miniport drivers for these HBAs must do a significant amount of processing when I/O is initiated. If the miniport driver does this processing in its *StartIo* routine, it degrades system performance.

The Storport I/O model supports the [**HwStorBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio) routine in an effort to remove some of the processing burden from the miniport driver's *StartIo* routine, [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio). In the Storport I/O model, the system calls *HwStorBuildIo* just prior to calling the miniport driver's *HwStorStartIo* routine and does as much processing as possible there. This strategy avoids contention for CPU cycles and for access to critical system structures, such as the device extension, because *HwStorBuildIo* executes at a lower IRQL and holds no synchronization locks.

The *HwStorBuildIo* routine should translate the SRB to a more convenient data structure, build scatter/gather lists, and do other per-SRB processing. Because no locks are held during the execution of the *HwStorBuildIo* routine, the miniport driver should access no data other than that in the SRB and the SRB extension. If access to other structures is required for part of the processing, that part should still be performed in the *HwStartIo* routine.

To achieve maximum performance, the *HwStorBuildIo* routine should be used in conjunction with the full-duplex mode.

 

