---
title: Storage Class Driver's RetryRequest Routine
description: Storage Class Driver's RetryRequest Routine
ms.assetid: de1eea7d-88db-444c-a9f7-462ad4a5df27
keywords:
- RetryRequest
- retrying requests WDK storage
- errors WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's RetryRequest Routine


## <span id="ddk_storage_class_drivers_retryrequest_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_RETRYREQUEST_ROUTINE_KG"></span>


The underlying storage port driver is responsible for retrying requests if device errors occur that involve transmission of data on the bus, including bus-parity errors, selection time-outs, and target/controller-busy errors. If retry attempts fail, the storage port driver completes the request with an appropriate error and logs the I/O error, as well.

A storage class driver should never attempt to retry a request that the port driver has already failed due to any of the preceding errors.

A storage class driver is responsible for retrying requests that fail due to device-specific errors, target/controller errors other than target/controller-busy, bus resets, or request time-outs. In general, a *RetryRequest* routine can resubmit such an IRP to the next-lower driver and direct that the SRB be placed at the head of the port driver's LU-specific queue.

In particular, a *RetryRequest* routine should do the following:

1.  Ensure that a partial transfer request has the correct values set for the starting address and length.

2.  Zero the **SrbStatus** and **ScsiStatus** members of the SRB.

3.  Set up the **SrbFlags** member, as necessary for the device.

4.  Set up the I/O stack location for the port driver in the IRP as already described in [Storage Class Driver's Dispatch Routines](storage-class-driver-s-dispatch-routines.md) through [Storage Class Driver's SplitTransferRequest Routine](storage-class-driver-s-splittransferrequest-routine.md).

5.  Call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) for the IRP, because the driver's [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine must free the SRB before the IRP returns. The *IoCompletion* routine might also need to retry the request more than once, or to call the driver's *InterpretRequestSense* or *ReleaseQueue* routine.

6.  Pass the request on to the next-lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

 

 




