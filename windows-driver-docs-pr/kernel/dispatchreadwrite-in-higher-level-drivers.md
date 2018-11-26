---
title: DispatchReadWrite in Higher-Level Drivers
description: DispatchReadWrite in Higher-Level Drivers
ms.assetid: d8406115-c62e-4362-8d2c-77d0414c4104
keywords: ["DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchReadWrite in Higher-Level Drivers





Except for file system drivers, a higher-level driver usually does not have any internal driver queues for IRPs. Such a driver's [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine can pass IRPs with valid parameters on to lower drivers, possibly after setting up its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

However, a SCSI class driver's *DispatchReadWrite* routine is responsible for splitting up large transfer requests, if necessary, before it sends an IRP with the major function code [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) to the SCSI port/miniport driver pair. For more information, see [Storage Class Driver's SplitTransferRequest Routine](https://msdn.microsoft.com/library/windows/hardware/ff566965).

If a higher-level driver allocates one or more IRPs, which it sets up for the next-lower driver in its *DispatchReadWrite* routine, to request some number of partial transfers, the *DispatchReadWrite* routine must call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) with each driver-allocated IRP. The driver must register its *IoCompletion* routine to track how much data is transferred in each partial-transfer operation so that the *IoCompletion* routine can release all driver-allocated IRPs and, eventually, complete the original request.

If the underlying driver controls a removable-media device, any IRPs allocated by the higher-level driver must have a thread context. To set up a thread context, the allocating driver must set the **Irp-&gt;Tail.Overlay**.Thread in each newly allocated IRP from the same value in the incoming transfer IRP. For more information, see [Supporting Removable Media](supporting-removable-media.md).

If the underlying device driver returns an IRP for a partial transfer with an error, the *IoCompletion* routine can either retry the partial-transfer request or complete the original IRP with its I/O status block set with the returned error, after freeing any IRPs and memory the higher-level driver has allocated.

If a higher-level driver's *DispatchReadWrite* routine allocates memory for partial-transfer operations and its allocation will be accessed by the driver's *IoCompletion* routine (or by the underlying device driver), the *DispatchReadWrite* routine must allocate that memory from nonpaged pool.

 

 




