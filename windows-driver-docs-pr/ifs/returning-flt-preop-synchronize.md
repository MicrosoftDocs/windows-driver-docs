---
title: Returning FLT_PREOP_SYNCHRONIZE
description: Returning FLT_PREOP_SYNCHRONIZE
keywords:
- FLT_PREOP_SYNCHRONIZE
- synchronization WDK file system minifilter
ms.date: 07/19/2022
---

# Returning FLT_PREOP_SYNCHRONIZE

> [!NOTE]
> A minifilter driver should not use FLT_PREOP_SYNCHRONIZE to hold a resource across pre- and post-operation calls (same as it should not hold a resource across an I/O call). To do so is unsafe as it can result in deadlocks.

If a minifilter driver's [**pre-operation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) synchronizes an I/O operation by returning FLT_PREOP_SYNCHRONIZE, Filter Manager calls that filter's [**post-operation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) during I/O completion:

* If the filter is not draining, Filter Manager calls that filter's post-operation callback routine in the same thread context as the pre-operation callback, at IRQL <= APC_LEVEL. (Note that this thread context is not necessarily the context of the originating thread.)
* If the filter is draining, Filter Manager does not sync back to the original thread.

> [!NOTE]
> If a filter's pre-operation callback routine returns FLT_PREOP_SYNCHRONIZE, it must implement a post-operation callback routine for the operation.

If the filter's pre-operation callback routine returns FLT_PREOP_SYNCHRONIZE, it can return a non-NULL value in its **CompletionContext** output parameter. This parameter is an optional context pointer that is passed to the corresponding post-operation callback routine. The post-operation callback routine receives this pointer in its **CompletionContext** input parameter.

A minifilter driver's pre-operation callback routine should return FLT_PREOP_SYNCHRONIZE only for IRP-based I/O operations. However, this status value can be returned for other operation types. If it is returned for an I/O operation that is not an IRP-based I/O operation, Filter Manager treats this return value as if it were FLT_PREOP_SUCCESS_WITH_CALLBACK. To determine whether an operation is an IRP-based I/O operation, use the [**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85)) macro.

Filters should not return FLT_PREOP_SYNCHRONIZE for create operations, because these operations are already synchronized by Filter Manager. If a minifilter driver has registered pre-operation and post-operation callback routines for IRP_MJ_CREATE operations, the post-create callback routine is called at IRQL = PASSIVE_LEVEL, in the same thread context as the pre-create callback routine.

Minifilter drivers must never return FLT_PREOP_SYNCHRONIZE for asynchronous read or write operations. Doing so can severely degrade both minifilter driver and system performance and can even cause deadlocks if, for example, the modified page writer thread is blocked. Before returning FLT_PREOP_SYNCHRONIZE for an IRP-based read or write operation, a minifilter driver should verify that the operation is synchronous by calling [**FltIsOperationSynchronous**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltisoperationsynchronous).

The following types of I/O operations cannot be synchronized:

* Oplock file system control (FSCTL) operations (**MajorFunction** is IRP_MJ_FILE_SYSTEM_CONTROL; **FsControlCode** is [**FSCTL_REQUEST_FILTER_OPLOCK**](./fsctl-request-filter-oplock.md), [**FSCTL_REQUEST_BATCH_OPLOCK**](./fsctl-request-batch-oplock.md), [**FSCTL_REQUEST_OPLOCK_LEVEL_1**](./fsctl-request-oplock-level-1.md), or [**FSCTL_REQUEST_OPLOCK_LEVEL_2**](./fsctl-request-oplock-level-2.md).)

* Notify change directory operations (**MajorFunction** is IRP_MJ_DIRECTORY_CONTROL; **MinorFunction** is IRP_MN_NOTIFY_CHANGE_DIRECTORY.)

* Byte-range lock requests (**MajorFunction** is IRP_MJ_LOCK_CONTROL; **MinorFunction** is IRP_MN_LOCK.)

FLT_PREOP_SYNCHRONIZE cannot be returned for any of these operations.
