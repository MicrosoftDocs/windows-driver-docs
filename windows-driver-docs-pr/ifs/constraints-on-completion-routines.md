---
title: Constraints on Completion Routines
description: Constraints on Completion Routines
keywords:
- IRP completion routines WDK file system , constraints
ms.date: 02/23/2023
---

# Constraints on Completion Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

The following guidelines briefly discuss how to avoid common programming errors in legacy file system filter driver completion routines.

## IRQL-Related Constraints

Because completion routines can be called at IRQL DISPATCH_LEVEL, they're subject to the following constraints:

- Completion routines can't safely call kernel-mode routines that require a lower IRQL, such as [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice) or [**ObQueryNameString**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-obquerynamestring).

- Any data structures used in completion routines must be allocated from nonpaged pool.

- Completion routines can't be made pageable.

- Completion routines can't acquire resources, mutexes, or fast mutexes. However, they can acquire spin locks.

## Checking the PendingReturned Flag

- Unless the completion routine signals an event, it must check the **Irp->PendingReturned** flag. If this flag is set, the completion routine must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) to mark the IRP as pending.

- If a completion routine signals an event, it shouldn't call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending).

## Constraints on Returning Status

- A file system filter driver completion routine must return either STATUS_SUCCESS or STATUS_MORE_PROCESSING_REQUIRED. All other NTSTATUS values are reset to STATUS_SUCCESS by the I/O Manager.

## Constraints on Returning STATUS_MORE_PROCESSING_REQUIRED

There are three cases when completion routines should return STATUS_MORE_PROCESSING_REQUIRED:

- When the corresponding dispatch routine is waiting for the completion routine to signal an event. In this case, it's important to return STATUS_MORE_PROCESSING_REQUIRED to prevent the I/O Manager from completing the IRP prematurely after the completion routine returns.

- When the completion routine has posted the IRP to a worker queue and the corresponding dispatch routine has returned STATUS_PENDING. In this case as well, it's important to return STATUS_MORE_PROCESSING_REQUIRED to prevent the I/O Manager from completing the IRP prematurely after the completion routine returns.

- When the same driver created the IRP by calling [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) or [**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest). Because the driver didn't receive this IRP from a higher-level driver, it can safely free the IRP in the completion routine. After the completion routine calls [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp), it must return STATUS_MORE_PROCESSING_REQUIRED to indicate that no further completion processing is needed.

A completion routine can't return STATUS_MORE_PROCESSING_REQUIRED for an oplock operation. Oplock operations can't be pended (posted to a worker queue), and dispatch routines can't return STATUS_PENDING for them.

## Constraints on Posting IRPs to a Work Queue

- If a completion routine posts IRPs to a work queue, it must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) before posting each IRP to the worker queue. Otherwise, the IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.
