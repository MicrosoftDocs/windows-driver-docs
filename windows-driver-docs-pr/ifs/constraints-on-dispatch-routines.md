---
title: Constraints on Dispatch Routines
description: Constraints on Dispatch Routines
keywords:
- IRP dispatch routines WDK file system , constraints
ms.date: 02/23/2023
---

# Constraints on Dispatch Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

The following guidelines briefly discuss how legacy file system filter drivers can avoid common programming errors in dispatch routines.

## IRQL-Related Constraints

For information about which types of IRPs are used in paging I/O, see [Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md).

- Dispatch routines in the paging I/O path should never call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) at any IRQL above APC_LEVEL. If a dispatch routine raises IRQL, it must lower it before calling **IoCallDriver**.

- Dispatch routines in the paging path, such as read and write, can't safely call any kernel-mode routines that require callers to be running at IRQL PASSIVE_LEVEL.

- Dispatch routines that are in the paging file I/O path can't safely call any kernel-mode routines that require a caller to be running at IRQL < DISPATCH_LEVEL.

- Dispatch routines that aren't in the paging I/O path should never call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) at any IRQL above PASSIVE_LEVEL. If a dispatch routine raises IRQL, it must lower it before calling **IoCallDriver**.

## Constraints on Processing IRPs

- If the IRP parameters include any user-space addresses, these addresses must be validated before they're used. For more information, see [Errors in Buffered I/O](../kernel/failure-to-check-the-size-of-buffers.md).

- Additionally, if the IRP contains an IOCTL or FSCTL buffer that was sent from a 32-bit platform to a 64-bit platform, the buffer contents may need to be thunked. For more information, see [Supporting 32-Bit I/O in Your 64-Bit Driver](../kernel/supporting-32-bit-i-o-in-your-64-bit-driver.md).

- Unlike file systems, file system filter drivers should never call [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) or [**FsRtlExitFileSystem**](./fsrtlexitfilesystem.md) except before calling [**ExAcquireFastMutexUnsafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirefastmutexunsafe) or [**ExAcquireResourceExclusiveLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquireresourceexclusivelite). **FsRtlEnterFileSystem** and **FsRtlExitFileSystem** disable normal kernel APCs, which are needed by most file systems.

## Constraints on Completing IRPs

- File system filter drivers should use only success and error status values when completing IRPs.

- Although STATUS_PENDING is a success NTSTATUS value, it's a programming error to complete an IRP with STATUS_PENDING.

- After a dispatch routine calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest), the IRP pointer is no longer valid and can't safely be dereferenced.

## Constraints on Setting a Completion Routine

For information about setting completion routines, see [Using Completion Routines](using-irp-completion-routines.md).

- When a dispatch routine calls [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine), it can optionally pass a *Context* pointer to a structure for the completion routine to use when processing the given IRP. This structure must be allocated from nonpaged pool, because the completion routine can be called IRQL DISPATCH_LEVEL.

- If a dispatch routine sets a completion routine that may return STATUS_MORE_PROCESSING_REQUIRED, it must do one of the following to prevent the I/O Manager from completing the IRP prematurely:
  - Mark the IRP pending, call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver), and return STATUS_PENDING.
  - Call [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) to wait for the completion routine to execute, then call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the IRP.

### Constraints on Passing IRPs Down

- After a dispatch routine calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver), the IRP pointer is no longer valid and can't safely be dereferenced, unless the dispatch routine waits for the completion routine to signal that it has been called.

- It's a programming error to call [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) from a file system filter driver. (**PoCallDriver** is used to pass IRP_MJ_POWER requests to lower-level drivers. File system filter drivers never receive IRP_MJ_POWER requests.)

## Constraints on Returning Status

- Except when completing an IRP, a dispatch routine that doesn't set a completion routine should always return the NTSTATUS value returned by [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver). Unless this value is STATUS_PENDING, it must match the value of **Irp->IoStatus.Status** set by the driver that completed the IRP.

- When [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) returns STATUS_PENDING, the dispatch routine should also return STATUS_PENDING, unless it waits for the completion routine to signal an event.

- When the dispatch routine posts the IRP to a worker queue for later processing, it should mark the IRP pending and return STATUS_PENDING.

- When the dispatch routine sets a completion routine that might post the IRP to a worker queue for later processing, it should mark the IRP pending and return STATUS_PENDING.

- A dispatch routine that marks an IRP pending must return STATUS_PENDING.

- Oplock operations can't be pended (posted to a worker queue), and dispatch routines can't return STATUS_PENDING for them.

## Constraints on Posting IRPs to a Work Queue

- If a dispatch routine posts IRPs to a work queue, it must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) before posting each IRP to the worker queue. Otherwise, the IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.
