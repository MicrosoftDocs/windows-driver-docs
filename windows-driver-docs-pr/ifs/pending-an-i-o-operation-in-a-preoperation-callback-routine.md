---
title: Pending an I/O Operation in a Preoperation Callback Routine
description: Pending an I/O Operation in a Preoperation Callback Routine
keywords:
- preoperation callback routines WDK file system minifilter , pending operations
- pending I/O operations in callback routines WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pending an I/O Operation in a Preoperation Callback Routine


## <span id="ddk_pending_an_io_operation_in_a_preoperation_callback_routine_if"></span><span id="DDK_PENDING_AN_IO_OPERATION_IN_A_PREOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**preoperation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) can pend an I/O operation by posting the operation to a system work queue and returning FLT\_PREOP\_PENDING. Returning this status value indicates that the minifilter driver is retaining control of the I/O operation until it calls [**FltCompletePendedPreOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpreoperation) to resume processing for the I/O operation.

A minifilter driver's preoperation callback routine pends an I/O operation by performing the following steps:

1.  Posting the I/O operation to a system work queue by calling a routine such as [**FltQueueDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuedeferredioworkitem).

2.  Returning FLT\_PREOP\_PENDING.

A minifilter driver that must pend all (or most) incoming I/O operations should not use routines such as **FltQueueDeferredIoWorkItem** to pend operations, because calling this routine can cause the system work queues to be flooded. Instead, such a minifilter driver should use a cancel-safe queue. For more information about using cancel-safe queues, see [*FltCbdqInitialize*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqinitialize).

Note that the call to **FltQueueDeferredIoWorkItem** will fail if any of the following conditions are true:

-   The operation is not an IRP-based I/O operation.

-   The operation is a paging I/O operation.

-   The **TopLevelIrp** field of the current thread is not **NULL**. (For more information about how to find the value of this field, see [**IoGetTopLevelIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogettoplevelirp).)

-   The target instance for the I/O operation is being torn down.

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_PENDING, it must return **NULL** in the *CompletionContext* output parameter.

A minifilter driver can return FLT\_PREOP\_PENDING only for IRP-based I/O operations. To determine whether an operation is an IRP-based I/O operation, use the [**FLT\_IS\_IRP\_OPERATION**](/previous-versions/ff544654(v=vs.85)) macro.

The work routine that dequeues and processes the I/O operation must call **FltCompletePendedPreOperation** to resume processing for the operation.

 

