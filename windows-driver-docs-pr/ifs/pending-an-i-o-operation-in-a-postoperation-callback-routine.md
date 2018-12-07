---
title: Pending an I/O Operation in a Postoperation Callback Routine
description: Pending an I/O Operation in a Postoperation Callback Routine
ms.assetid: 126e13fb-51f6-4dcc-aa13-850921b3c752
keywords:
- postoperation callback routines WDK file system minifilter , pending operations
- pending I/O operations in callback routines WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pending an I/O Operation in a Postoperation Callback Routine


## <span id="ddk_pending_an_io_operation_in_a_postoperation_callback_routine_if"></span><span id="DDK_PENDING_AN_IO_OPERATION_IN_A_POSTOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) can pend an I/O operation by performing the following steps:

1.  Calling [**FltAllocateDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff541720) to allocate a work item for the I/O operation.

2.  Calling [**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449) to post the I/O operation to a system work queue.

3.  Returning FLT\_POSTOP\_MORE\_PROCESSING\_REQUIRED.

Note that the call to **FltQueueDeferredIoWorkItem** will fail if any of the following conditions are true:

-   The operation is not an IRP-based I/O operation.

-   The operation is a paging I/O operation.

-   The **TopLevelIrp** field of the current thread is not **NULL**. (For more information about how to find the value of this field, see [**IoGetTopLevelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548405).)

-   The target instance for the I/O operation is being torn down. (The filter manager indicates this situation by setting the FLTFL\_POST\_OPERATION\_DRAINING flag in the *Flags* input parameter to the postoperation callback routine.)

Minifilter drivers must be prepared to handle this failure. If your minifilter driver cannot handle such failures, you should consider using the technique that is described in [Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md) instead of pending the I/O operation.

After the minifilter driver's postoperation callback routine returns FLT\_POSTOP\_MORE\_PROCESSING\_REQUIRED, the filter manager will not perform any further completion processing for the I/O operation until the minifilter driver's work routine calls [**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897) to return control of the operation to the filter manager. The filter manager will not perform any further processing in this situation even if the work routine sets a failure NTSTATUS value in the **IoStatus.Status** field of the callback data structure for the operation.

The work routine that dequeues and performs completion processing for the I/O operation must call **FltCompletePendedPostOperation** to return control of the operation to the filter manager.

 

 




