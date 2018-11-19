---
title: Storage Class Driver's IoCompletion Routines
description: Storage Class Driver's IoCompletion Routines
ms.assetid: 03cf50be-1b7d-4e5b-8ee5-bbdef860d893
keywords:
- IoCompletion
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's IoCompletion Routines


## <span id="ddk_storage_class_drivers_iocompletion_routines_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_IOCOMPLETION_ROUTINES_KG"></span>


A storage class driver must have one or more [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines, unless the driver synchronously waits on the completion of every IRP it sends to the port driver, retries requests as necessary, then releases memory for SRBs from within a dispatch or *BuildRequest* routine. Note that handling every IRP synchronously will degrade the class driver's performance. Furthermore, storage class drivers for devices that might hold the system page file must handle all transfer requests asynchronously and thus must have an *IoCompletion* routine for read/write requests.

As described in [Storage Class Driver's BuildRequest Routine](storage-class-driver-s-buildrequest-routine.md), storage class drivers are responsible for freeing the memory they allocate for SRBs, whether back to a lookaside list or to nonpaged pool. Like any other higher-level kernel-mode driver, they are also responsible for releasing any IRPs that they allocate, such as an IRP to split up a transfer request as described in [Storage Class Driver's SplitTransferRequest Routine](storage-class-driver-s-splittransferrequest-routine.md).

A class driver's *IoCompletion* routine is ultimately responsible for ensuring that the I/O status block is set and for completing the original IRP. Note that completing an IRP can include translating an error returned in the SRB's **ScsiStatus** member or **SenseInfoBuffer** member into an NTSTATUS-type value and/or logging an error, as described in [Completing IRPs in Dispatch Routines](https://msdn.microsoft.com/library/windows/hardware/ff542019).

When certain kinds of errors occur in processing a request, a storage port driver freezes its internal queue for the target logical unit (LU) and sets SRB\_STATUS\_QUEUE\_FROZEN on completion of the request. Consequently, class drivers usually have internal routines to change the status of the queue for their device I/O requests. For more information, see [Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md).

If the driver's *BuildRequest* routine requested that the port driver return request-sense information for a request, its *IoCompletion* routine either calls an internal *InterpretRequestSense* routine or implements the same functionality inline. For more information, see [Storage Class Driver's InterpretRequestSense Routine](storage-class-driver-s-interpretrequestsense-routine.md).

Storage class drivers are responsible for retrying requests that fail due to target controller errors, bus resets, or request time-outs. When the port driver returns a particular request with its **SrbStatus** set to indicate such an error, the class driver can call a *RetryRequest* routine from its *IoCompletion* routine or, possibly, from its *InterpretRequestSense* routine. For more information, see [Storage Class Driver's RetryRequest Routine](storage-class-driver-s-retryrequest-routine.md).

For general information about *IoCompletion* routines, see [Completing IRPs](https://msdn.microsoft.com/library/windows/hardware/ff542018).

 

 




