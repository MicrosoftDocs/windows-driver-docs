---
title: Constraints on Dispatch Routines
description: Constraints on Dispatch Routines
ms.assetid: 5b2acaea-1f66-4285-9a36-5ab0f440f6b4
keywords:
- IRP dispatch routines WDK file system , constraints
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Constraints on Dispatch Routines


## <span id="ddk_constraints_on_dispatch_routines_if"></span><span id="DDK_CONSTRAINTS_ON_DISPATCH_ROUTINES_IF"></span>


The following guidelines briefly discuss how to avoid common programming errors in dispatch routines for file system filter drivers.

### <span id="IRQL-Related_Constraints"></span><span id="irql-related_constraints"></span><span id="IRQL-RELATED_CONSTRAINTS"></span>IRQL-Related Constraints

Note: For information about which types of IRPs are used in paging I/O, see [Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md).

-   Dispatch routines in the paging I/O path should never call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) at any IRQL above APC\_LEVEL. If a dispatch routine raises IRQL, it must lower it before calling **IoCallDriver**.

-   Dispatch routines in the paging path, such as read and write, cannot safely call any kernel-mode routines that require callers to be running at IRQL PASSIVE\_LEVEL.

-   Dispatch routines that are in the paging file I/O path cannot safely call any kernel-mode routines that require a caller to be running at IRQL &lt; DISPATCH\_LEVEL.

-   Dispatch routines that are not in the paging I/O path should never call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) at any IRQL above PASSIVE\_LEVEL. If a dispatch routine raises IRQL, it must lower it before calling **IoCallDriver**.

### <span id="Constraints_on_Processing_IRPs"></span><span id="constraints_on_processing_irps"></span><span id="CONSTRAINTS_ON_PROCESSING_IRPS"></span>Constraints on Processing IRPs

-   If the IRP parameters include any user-space addresses, these must be validated before they are used. For more information, see [Errors in Buffered I/O](https://msdn.microsoft.com/library/windows/hardware/ff544293).

-   Additionally, if the IRP contains an IOCTL or FSCTL buffer that was sent from a 32-bit platform to a 64-bit platform, the buffer contents may need to be thunked. For more information, see [Supporting 32-Bit I/O in Your 64-Bit Driver](https://msdn.microsoft.com/library/windows/hardware/ff563897).

-   Unlike file systems, file system filter drivers should never call [**FsRtlEnterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff545900) or [**FsRtlExitFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff545908) except before calling [**ExAcquireFastMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff544340) or [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351). **FsRtlEnterFileSystem** and **FsRtlExitFileSystem** disable normal kernel APCs, which are needed by most file systems.

### <span id="Constraints_on_Completing_IRPs"></span><span id="constraints_on_completing_irps"></span><span id="CONSTRAINTS_ON_COMPLETING_IRPS"></span>Constraints on Completing IRPs

-   When completing IRPs, file system filter drivers should use only success and error status values.

-   Although STATUS\_PENDING is a success NTSTATUS value, it is a programming error to complete an IRP with STATUS\_PENDING.

-   After a dispatch routine calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), the IRP pointer is no longer valid and cannot safely be dereferenced.

### <span id="Constraints_on_Setting_a_Completion_Routine"></span><span id="constraints_on_setting_a_completion_routine"></span><span id="CONSTRAINTS_ON_SETTING_A_COMPLETION_ROUTINE"></span>Constraints on Setting a Completion Routine

Note: For information about setting completion routines, see [Using Completion Routines](using-irp-completion-routines.md).

-   When a dispatch routine calls [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679), it can optionally pass a *Context* pointer to a structure for the completion routine to use when processing the given IRP. This structure must be allocated from nonpaged pool, because the completion routine can be called IRQL DISPATCH\_LEVEL.

-   If a dispatch routine sets a completion routine that may return STATUS\_MORE\_PROCESSING\_REQUIRED, it must do one of the following to prevent the I/O Manager from completing the IRP prematurely:
    -   Mark the IRP pending, call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), and return STATUS\_PENDING.
    -   Call [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) to wait for the completion routine to execute, then call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP.

### <span id="Constraints_on_Passing_IRPs_Down"></span><span id="constraints_on_passing_irps_down"></span><span id="CONSTRAINTS_ON_PASSING_IRPS_DOWN"></span>Constraints on Passing IRPs Down

-   After a dispatch routine calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), the IRP pointer is no longer valid and cannot safely be dereferenced, unless the dispatch routine waits for the completion routine to signal that it has been called.

-   It is a programming error to call [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) from a file system filter driver. (**PoCallDriver** is used to pass IRP\_MJ\_POWER requests to lower-level drivers. File system filter drivers never receive IRP\_MJ\_POWER requests.)

### <span id="Constraints_on_Returning_Status"></span><span id="constraints_on_returning_status"></span><span id="CONSTRAINTS_ON_RETURNING_STATUS"></span>Constraints on Returning Status

-   Except when completing an IRP, a dispatch routine that does not set a completion routine should always return the NTSTATUS value returned by [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). Unless this value is STATUS\_PENDING, it must match the value of **Irp-&gt;IoStatus.Status** set by the driver that completed the IRP.

-   When [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) returns STATUS\_PENDING, the dispatch routine should also return STATUS\_PENDING, unless it waits for the completion routine to signal an event.

-   When posting the IRP to a worker queue for later processing, the dispatch routine should mark the IRP pending and return STATUS\_PENDING.

-   When setting a completion routine that might post the IRP to a worker queue for later processing, the dispatch routine should mark the IRP pending and return STATUS\_PENDING.

-   A dispatch routine that marks an IRP pending must return STATUS\_PENDING.

-   Oplock operations cannot be pended (posted to a worker queue), and dispatch routines cannot return STATUS\_PENDING for them.

### <span id="Constraints_on_Posting_IRPs_to_a_Work_Queue"></span><span id="constraints_on_posting_irps_to_a_work_queue"></span><span id="CONSTRAINTS_ON_POSTING_IRPS_TO_A_WORK_QUEUE"></span>Constraints on Posting IRPs to a Work Queue

-   If a dispatch routine posts IRPs to a work queue, it must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) before posting each IRP to the worker queue. Otherwise, the IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.

 

 




