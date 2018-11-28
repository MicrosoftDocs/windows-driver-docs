---
title: Constraints on Completion Routines
description: Constraints on Completion Routines
ms.assetid: 3873fd27-cfa8-414d-9437-c0789b20ff27
keywords:
- IRP completion routines WDK file system , constraints
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Constraints on Completion Routines


## <span id="ddk_constraints_on_completion_routines_if"></span><span id="DDK_CONSTRAINTS_ON_COMPLETION_ROUTINES_IF"></span>


The following guidelines briefly discuss how to avoid common programming errors in file system filter driver completion routines.

### <span id="IRQL-Related_Constraints"></span><span id="irql-related_constraints"></span><span id="IRQL-RELATED_CONSTRAINTS"></span>IRQL-Related Constraints

Because completion routines can be called at IRQL DISPATCH\_LEVEL, they are subject to the following constraints:

-   Completion routines cannot safely call kernel-mode routines that require a lower IRQL, such as [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) or [**ObQueryNameString**](https://msdn.microsoft.com/library/windows/hardware/ff550990).

-   Any data structures used in completion routines must be allocated from nonpaged pool.

-   Completion routines cannot be made pageable.

-   Completion routines cannot acquire resources, mutexes, or fast mutexes. However, they can acquire spin locks.

### <span id="Checking_the_PendingReturned_Flag"></span><span id="checking_the_pendingreturned_flag"></span><span id="CHECKING_THE_PENDINGRETURNED_FLAG"></span>Checking the PendingReturned Flag

-   Unless the completion routine signals an event, it must check the **Irp-&gt;PendingReturned** flag. If this flag is set, the completion routine must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) to mark the IRP as pending.

-   If a completion routine signals an event, it should not call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422).

### <span id="Constraints_on_Returning_Status"></span><span id="constraints_on_returning_status"></span><span id="CONSTRAINTS_ON_RETURNING_STATUS"></span>Constraints on Returning Status

-   A file system filter driver completion routine must return either STATUS\_SUCCESS or STATUS\_MORE\_PROCESSING\_REQUIRED. All other NTSTATUS values are reset to STATUS\_SUCCESS by the I/O Manager.

### <span id="Constraints_on_Returning_STATUS_MORE_PROCESSING_REQUIRED"></span><span id="constraints_on_returning_status_more_processing_required"></span><span id="CONSTRAINTS_ON_RETURNING_STATUS_MORE_PROCESSING_REQUIRED"></span>Constraints on Returning STATUS\_MORE\_PROCESSING\_REQUIRED

There are three cases when completion routines should return STATUS\_MORE\_PROCESSING\_REQUIRED:

-   When the corresponding dispatch routine is waiting for an event to be signaled by the completion routine. In this case, it is important to return STATUS\_MORE\_PROCESSING\_REQUIRED to prevent the I/O Manager from completing the IRP prematurely after the completion routine returns.

-   When the completion routine has posted the IRP to a worker queue and the corresponding dispatch routine has returned STATUS\_PENDING. In this case as well, it is important to return STATUS\_MORE\_PROCESSING\_REQUIRED to prevent the I/O Manager from completing the IRP prematurely after the completion routine returns.

-   When the same driver created the IRP by calling [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) or [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310). Because the driver did not receive this IRP from a higher-level driver, it can safely free the IRP in the completion routine. After calling [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113), the completion routine must return STATUS\_MORE\_PROCESSING\_REQUIRED to indicate that no further completion processing is needed.

A completion routine cannot return STATUS\_MORE\_PROCESSING\_REQUIRED for an oplock operation. Oplock operations cannot be pended (posted to a worker queue), and dispatch routines cannot return STATUS\_PENDING for them.

### <span id="Constraints_on_Posting_IRPs_to_a_Work_Queue"></span><span id="constraints_on_posting_irps_to_a_work_queue"></span><span id="CONSTRAINTS_ON_POSTING_IRPS_TO_A_WORK_QUEUE"></span>Constraints on Posting IRPs to a Work Queue

-   If a completion routine posts IRPs to a work queue, it must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) before posting each IRP to the worker queue. Otherwise, the IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.

 

 




