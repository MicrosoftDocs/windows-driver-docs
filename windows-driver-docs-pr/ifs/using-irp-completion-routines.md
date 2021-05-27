---
title: Using IRP Completion Routines
description: Using IRP Completion Routines
keywords:
- filter drivers WDK file system , IRP completion routines
- file system filter drivers WDK , IRP completion routines
- IRP completion routines WDK file system
- IRPs WDK file system
- completing I/O requests WDK file system
- IRP completion routines WDK file system , about IRP completion routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using IRP Completion Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

File system filter drivers use completion routines that are similar to those used by device drivers. A *completion routine* performs completion processing on an IRP. Any driver routine that passes an IRP down to the next-lower-level driver can optionally register a completion routine for the IRP by calling [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) before calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

Every IRP completion routine is defined as follows:

```cpp
NTSTATUS
(*PIO_COMPLETION_ROUTINE) (
    IN PDEVICE_OBJECT DeviceObject,
    IN PIRP Irp,
    IN PVOID Context
    );
```

Completion routines are called at IRQL <= DISPATCH_LEVEL, in an arbitrary thread context.

Because they can be called at IRQL DISPATCH_LEVEL, completion routines cannot call kernel-mode routines that must be called at a lower IRQL, such as [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice). For the same reason, any data structures that are used in a completion routine must be allocated from nonpaged pool.

This section discusses the following topics:

[How Completion Processing Is Performed](how-completion-processing-is-performed.md)

[Checking the PendingReturned Flag](checking-the-pendingreturned-flag.md)

[Returning Status from Completion Routines](returning-status-from-completion-routines.md)

[Example: Simple Pass-Through Dispatch and Completion](example--simple-pass-through-dispatch-and-completion.md)

[Constraints on Completion Routines](constraints-on-completion-routines.md)
