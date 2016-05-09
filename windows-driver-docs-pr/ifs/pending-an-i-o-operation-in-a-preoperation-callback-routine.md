---
title: Pending an I/O Operation in a Preoperation Callback Routine
author: windows-driver-content
description: Pending an I/O Operation in a Preoperation Callback Routine
ms.assetid: 39b04911-c0d9-42ec-b93e-b440b12f9e41
keywords: ["preoperation callback routines WDK file system minifilter , pending operations", "pending I/O operations in callback routines WDK file system"]
---

# Pending an I/O Operation in a Preoperation Callback Routine


## <span id="ddk_pending_an_io_operation_in_a_preoperation_callback_routine_if"></span><span id="DDK_PENDING_AN_IO_OPERATION_IN_A_PREOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) can pend an I/O operation by posting the operation to a system work queue and returning FLT\_PREOP\_PENDING. Returning this status value indicates that the minifilter driver is retaining control of the I/O operation until it calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) to resume processing for the I/O operation.

A minifilter driver's preoperation callback routine pends an I/O operation by performing the following steps:

1.  Posting the I/O operation to a system work queue by calling a routine such as [**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449).

2.  Returning FLT\_PREOP\_PENDING.

A minifilter driver that must pend all (or most) incoming I/O operations should not use routines such as **FltQueueDeferredIoWorkItem** to pend operations, because calling this routine can cause the system work queues to be flooded. Instead, such a minifilter driver should use a cancel-safe queue. For more information about using cancel-safe queues, see [*FltCbdqInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff541802).

Note that the call to **FltQueueDeferredIoWorkItem** will fail if any of the following conditions are true:

-   The operation is not an IRP-based I/O operation.

-   The operation is a paging I/O operation.

-   The **TopLevelIrp** field of the current thread is not **NULL**. (For more information about how to find the value of this field, see [**IoGetTopLevelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548405).)

-   The target instance for the I/O operation is being torn down.

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_PENDING, it must return **NULL** in the *CompletionContext* output parameter.

A minifilter driver can return FLT\_PREOP\_PENDING only for IRP-based I/O operations. To determine whether an operation is an IRP-based I/O operation, use the [**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654) macro.

The work routine that dequeues and processes the I/O operation must call **FltCompletePendedPreOperation** to resume processing for the operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Pending%20an%20I/O%20Operation%20in%20a%20Preoperation%20Callback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


