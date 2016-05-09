---
title: Unsynchronized HwStorBuildIo Routine
description: Unsynchronized HwStorBuildIo Routine
ms.assetid: 6b18e3ff-30dd-414b-99b5-4bb914660a67
---

# Unsynchronized HwStorBuildIo Routine


## <span id="ddk_unsynchronized_hwstorbuildio_routine_kg"></span><span id="DDK_UNSYNCHRONIZED_HWSTORBUILDIO_ROUTINE_KG"></span>


In the SCSI Port-miniport driver I/O model, the miniport driver's [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323), should transmit SCSI request blocks (SRBs) to the hardware as quickly as possible. This is essential, because work done in the miniport driver's *StartIo* routine is accomplished while interrupts are disabled and at IRQL = DISPATCH\_LEVEL. Unfortunately, this model is not well suited to drivers of some high-performance host bus adapters (HBAs), because the miniport drivers for these HBAs must do a significant amount of processing when I/O is initiated. If the miniport driver does this processing in its *StartIo* routine, it degrades system performance.

The Storport I/O model supports the [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) routine in an effort to remove some of the processing burden from the miniport driver's *StartIo* routine, [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423). In the Storport I/O model, the system calls *HwStorBuildIo* just prior to calling the miniport driver's *HwStorStartIo* routine and does as much processing as possible there. This strategy avoids contention for CPU cycles and for access to critical system structures, such as the device extension, because *HwStorBuildIo* executes at a lower IRQL and holds no synchronization locks.

The *HwStorBuildIo* routine should translate the SRB to a more convenient data structure, build scatter/gather lists, and do other per-SRB processing. Because no locks are held during the execution of the *HwStorBuildIo* routine, the miniport driver should access no data other than that in the SRB and the SRB extension. If access to other structures is required for part of the processing, that part should still be performed in the *HwStartIo* routine.

To achieve maximum performance, the *HwStorBuildIo* routine should be used in conjunction with the full-duplex mode.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Unsynchronized%20HwStorBuildIo%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




