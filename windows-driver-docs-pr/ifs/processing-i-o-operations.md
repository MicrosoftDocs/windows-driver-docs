---
title: Processing I/O Operations
description: Processing I/O Operations
keywords:
- filter manager WDK file system minifilter , processing I/O operations
- preoperation callback routines WDK file system minifilter , filter manager
- postoperation callback routines WDK file system minifilter , filter manager
- opportunistic lock WDK file system minifilter
- locking WDK file system minifilter
ms.date: 05/29/2024
ms.topic: concept-article
---

# Processing I/O Operations

*FltMgr* simplifies processing I/O operations for minifilter drivers. A legacy filter driver must correctly pass all I/O requests to the next-lower driver and correctly handle pending requests, synchronization, and I/O completion regardless of whether it does any work related to the request. In contrast, a minifilter driver registers only for the I/O operations it must handle.

For a given I/O operation, *FltMgr* calls only minifilter drivers that register a [**preoperation callback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) routine for that operation. *FltMgr* also handles certain IRP maintenance tasks on behalf of the minifilter driver, such as copying parameters to the next stack location and propagating the IRP **PendingReturned** flag.

In its preoperation callback routine, a minifilter driver:

* Does whatever processing is needed for the I/O operation.
* Indicates what should be done to the IRP by returning the appropriate value from its preoperation callback routine.

For example, to forward an IRP to the next-lower driver without a completion routine, the minifilter driver returns FLT_PREOP_SUCCESS_NO_CALLBACK. To do the same with a completion routine (the minifilter driver's postoperation callback routine for the I/O operation), the minifilter driver returns FLT_PREOP_SUCCESS_WITH_CALLBACK.

In its preoperation callback routine, the minifilter driver can queue the operation to a worker thread if needed by calling [**FltQueueDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuedeferredioworkitem). After doing so, the minifilter driver returns FLT_PREOP_PENDING from its preoperation callback routine to indicate that the I/O operation is pending. The minifilter driver is responsible for completing or resuming processing of the request. To resume processing, the minifilter driver calls [**FltCompletePendedPreOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpreoperation) from the worker thread.

If the minifilter driver needs to maintain its own per-instance cancel-safe queue of outstanding I/O operations to be processed, it can set up such a queue by making the following calls:

* Calling [*FltCbdqInitialize*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqinitialize) in its *InstanceSetupCallback* routine.
* Calling [*FltCbdqInsertIo*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqinsertio) in its preoperation callback routine as needed to insert I/O operations into the queue.

*FltMgr* calls a minifilter driver's [**postoperation callback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) routine for an I/O operation when lower filter drivers (legacy filters and minifilter drivers) finish completion processing.

In its postoperation callback routine, the minifilter driver can call [**FltDoCompletionProcessingWhenSafe**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdocompletionprocessingwhensafe) to ensure that completion processing is performed at a safe IRQL. Or it can queue the completion processing of the operation to a worker thread if needed by calling [**FltQueueDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuedeferredioworkitem). After doing so, the minifilter driver returns FLT_POSTOP_MORE_PROCESSING_REQUIRED from its postoperation callback routine to halt *FltMgr*'s completion processing for the I/O operation. To resume completion processing, the minifilter driver calls [**FltCompletePendedPostOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpostoperation) from the worker thread.

*FltMgr* provides support for queuing of "generic" work items - work items that are associated with a minifilter driver or minifilter driver instance rather than an I/O operation. A minifilter driver can insert a work item into a system work queue by calling [**FltQueueGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuegenericworkitem). This routine is similar to routines such as [**ExQueueWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exqueueworkitem); for example, work items (allocated by calling [**FltAllocateGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocategenericworkitem)) can be reused. However, **FltQueueGenericWorkItem** is safer for minifilter drivers to use, because *FltMgr* doesn't allow the minifilter driver or minifilter driver instance to unload while outstanding work items are still being processed.

*FltMgr* also provides support for opportunistic lock (oplock) operations. For oplock operations, a minifilter driver can use such filter manager routines as [**FltInitializeOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitializeoplock) and [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl), which are equivalent to the **FsRtlInitializeOplock** and **FsRtlOplockFsctrl** routines that are used by file systems and legacy filter drivers.

## Filter Manager routines for processing I/O operations

*FltMgr* provides the following support routines for pending I/O in [**preoperation**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) and [**postoperation**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) callback routines:

* [**FltCompletePendedPostOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpostoperation)
* [**FltCompletePendedPreOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpreoperation)
* [**FltDoCompletionProcessingWhenSafe**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdocompletionprocessingwhensafe)

The following routines are used for queuing work items in preoperation and postoperation callback routines:

* [**FltAllocateDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatedeferredioworkitem)
* [**FltAllocateGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocategenericworkitem)
* [**FltFreeDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreedeferredioworkitem)
* [**FltFreeGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreegenericworkitem)
* [**FltQueueDeferredIoWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuedeferredioworkitem)
* [**FltQueueGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuegenericworkitem)

The following routines provide cancel-safe queue support:

* [*FltCbdqDisable*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqdisable)
* [*FltCbdqEnable*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqenable)
* [*FltCbdqInitialize*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqinitialize)
* [*FltCbdqInsertIo*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqinsertio)
* [*FltCbdqRemoveIo*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqremoveio)
* [*FltCbdqRemoveNextIo*](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcbdqremovenextio)

The following routines provide oplock support:

* [**FltInitializeOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitializeoplock)
* [**FltUninitializeOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuninitializeoplock)

* [**FltCheckOplockEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcheckoplockex)
* [**FltCheckOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcheckoplock)

* [**FltCurrentOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcurrentoplock)
* [**FltCurrentOplockH**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcurrentoplockh)
* [**FltCurrentBatchOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcurrentbatchoplock)

* [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl)
* [**FltOplockFsctrlEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrlex)

* [**FltOplockIsFastIoPossible**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockisfastiopossible)
* [**FltOplockIsSharedRequest**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockissharedrequest)
* [**FltOplockKeysEqual**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockkeysequal)

* [**FltOplockBreakToNone**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockbreaktonone)
* [**FltOplockBreakToNoneEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockbreaktononeex)
* [**FltOplockBreakH**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockbreakh)

## Minifilter callback routines for processing I/O operations

The following callback routines are stored in the [**FLT_OPERATION_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_operation_registration) structure for each type of I/O operation that the minifilter driver handles:

| Callback Routine Name | Callback Routine Type |
| --------------------- | --------------------- |
| *PreOperation*        | [**PFLT_PRE_OPERATION_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) |
| *PostOperation*       | [**PFLT_POST_OPERATION_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) |
