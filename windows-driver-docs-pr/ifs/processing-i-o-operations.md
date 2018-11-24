---
title: Processing I/O Operations
description: Processing I/O Operations
ms.assetid: 750fa89b-dbdf-45ff-bfa5-83c717d2d7bb
keywords:
- filter manager WDK file system minifilter , processing I/O operations
- preoperation callback routines WDK file system minifilter , filter manager
- postoperation callback routines WDK file system minifilter , filter manager
- opportunistic lock WDK file system minifilter
- locking WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing I/O Operations


The filter manager simplifies processing I/O operations for minifilter drivers. Unlike a legacy filter driver, which must correctly pass all I/O requests to the next-lower driver and correctly handle pending requests, synchronization, and I/O completion whether the legacy filter driver does any work related to the request, a minifilter driver registers only for the I/O operations it must handle.

For a given I/O operation, the filter manager calls only minifilter drivers that have registered a [**preoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551109) routine for that operation. The filter manager also handles certain IRP maintenance tasks on behalf of the minifilter driver, such as copying parameters to the next stack location and propagating the IRP **PendingReturned** flag.

In its preoperation callback routine, a minifilter driver does whatever processing is needed for the I/O operation and indicates what should be done to the IRP by returning the appropriate value from its preoperation callback routine. For example, to forward an IRP to the next-lower driver without a completion routine, the minifilter driver returns FLT\_PREOP\_SUCCESS\_NO\_CALLBACK; to do the same with a completion routine (the minifilter driver's postoperation callback routine for the I/O operation), the minifilter driver returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK.

In its preoperation callback routine, the minifilter driver can queue the operation to a worker thread if needed by calling [**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449). After doing so, the minifilter driver returns FLT\_PREOP\_PENDING from its preoperation callback routine to indicate that the I/O operation is pending, and the minifilter driver is responsible for completing or resuming processing of the request. To resume processing, the minifilter driver calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) from the worker thread.

If the minifilter driver needs to maintain its own per-instance cancel-safe queue of outstanding I/O operations to be processed, it can set up such a queue by calling [*FltCbdqInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff541802) in its *InstanceSetupCallback* routine and calling [*FltCbdqInsertIo*](https://msdn.microsoft.com/library/windows/hardware/ff541815) in its preoperation callback routine as needed to insert I/O operations into the queue.

The filter manager calls a minifilter driver's [**postoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551107) routine for an I/O operation when lower filter drivers (legacy filters and minifilter drivers) have finished completion processing.

In its postoperation callback routine, the minifilter driver can call [**FltDoCompletionProcessingWhenSafe**](https://msdn.microsoft.com/library/windows/hardware/ff542047) to ensure that completion processing is performed at safe IRQL. Or it can queue the completion processing of the operation to a worker thread if needed by calling [**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449). After doing so, the minifilter driver returns FLT\_POSTOP\_MORE\_PROCESSING\_REQUIRED from its postoperation callback routine to halt the filter manager's completion processing for the I/O operation. To resume completion processing, the minifilter driver calls [**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897) from the worker thread.

The filter manager provides support for queuing of "generic" work items - work items that are associated with a minifilter driver or minifilter driver instance rather than an I/O operation. A minifilter driver can insert a work item into a system work queue by calling [**FltQueueGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543452). This routine is similar to routines such as [**ExQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff540216); for example, work items (allocated by calling [**FltAllocateGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff541749)) can be reused. However, **FltQueueGenericWorkItem** is safer for minifilter drivers to use, because the filter manager does not allow the minifilter driver or minifilter driver instance to unload while outstanding work items are still being processed.

The filter manager also provides support for opportunistic lock (oplock) operations. For oplock operations, a minifilter driver can use such filter manager routines as [**FltInitializeOplock**](https://msdn.microsoft.com/library/windows/hardware/ff543289) and [**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398), which are equivalent to the **FsRtlInitializeOplock** and **FsRtlOplockFsctrl** routines that are used by file systems and legacy filter drivers.

### <span id="Filter_Manager_Routines_for_Processing_I_O_Operations"></span><span id="filter_manager_routines_for_processing_i_o_operations"></span><span id="FILTER_MANAGER_ROUTINES_FOR_PROCESSING_I_O_OPERATIONS"></span>Filter Manager Routines for Processing I/O Operations

The filter manager provides the following support routines for pending I/O in [**preoperation**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and [**postoperation**](https://msdn.microsoft.com/library/windows/hardware/ff551107) callback routines:

[**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897)

[**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913)

[**FltDoCompletionProcessingWhenSafe**](https://msdn.microsoft.com/library/windows/hardware/ff542047)

The following routines are used for queuing work items in preoperation and postoperation callback routines:

[**FltAllocateDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff541720)

[**FltAllocateGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff541749)

[**FltFreeDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff542955)

[**FltFreeGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff542971)

[**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449)

[**FltQueueGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543452)

The following routines provide cancel-safe queue support:

[*FltCbdqDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541796)

[*FltCbdqEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541799)

[*FltCbdqInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff541802)

[*FltCbdqInsertIo*](https://msdn.microsoft.com/library/windows/hardware/ff541815)

[*FltCbdqRemoveIo*](https://msdn.microsoft.com/library/windows/hardware/ff541821)

[*FltCbdqRemoveNextIo*](https://msdn.microsoft.com/library/windows/hardware/ff541825)

The following routines provide oplock support:

[*FltCheckOplock*](https://msdn.microsoft.com/library/windows/hardware/ff541844)

[**FltCurrentBatchOplock**](https://msdn.microsoft.com/library/windows/hardware/ff541946)

[**FltInitializeOplock**](https://msdn.microsoft.com/library/windows/hardware/ff543289)

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398)

[**FltOplockIsFastIoPossible**](https://msdn.microsoft.com/library/windows/hardware/ff543404)

[**FltUninitializeOplock**](https://msdn.microsoft.com/library/windows/hardware/ff544598)

### <span id="Minifilter_Driver_Callback_Routines_for_Processing_I_O_Operations"></span><span id="minifilter_driver_callback_routines_for_processing_i_o_operations"></span><span id="MINIFILTER_DRIVER_CALLBACK_ROUTINES_FOR_PROCESSING_I_O_OPERATIONS"></span>Minifilter Driver Callback Routines for Processing I/O Operations

The following callback routines are stored in the [**FLT\_OPERATION\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544668) structure for each type of I/O operation that the minifilter driver handles:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Routine Name</th>
<th align="left">Callback Routine Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>PostOperation</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551107" data-raw-source="[&lt;strong&gt;PFLT_POST_OPERATION_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551107)"><strong>PFLT_POST_OPERATION_CALLBACK</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><em>PreOperation</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551109" data-raw-source="[&lt;strong&gt;PFLT_PRE_OPERATION_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551109)"><strong>PFLT_PRE_OPERATION_CALLBACK</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




