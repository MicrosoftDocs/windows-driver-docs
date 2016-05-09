---
title: Storage Class Driver's RetryRequest Routine
description: Storage Class Driver's RetryRequest Routine
ms.assetid: de1eea7d-88db-444c-a9f7-462ad4a5df27
keywords: ["RetryRequest", "retrying requests WDK storage", "errors WDK storage"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20RetryRequest%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




