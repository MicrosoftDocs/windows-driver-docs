---
title: Using IRP Completion Routines
description: Using IRP Completion Routines
ms.assetid: 82b9ba2b-17db-40e5-be3f-fd77cd986781
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


## <span id="ddk_using_irp_completion_routines_if"></span><span id="DDK_USING_IRP_COMPLETION_ROUTINES_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

File system filter drivers use completion routines that are similar to those used by device drivers. A *completion routine* performs completion processing on an IRP. Any driver routine that passes an IRP down to the next-lower-level driver can optionally register a completion routine for the IRP by calling [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) before calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

Every IRP completion routine is defined as follows:

```cpp
NTSTATUS 
(*PIO_COMPLETION_ROUTINE) ( 
    IN PDEVICE_OBJECT DeviceObject, 
    IN PIRP Irp, 
    IN PVOID Context 
    ); 
```

Completion routines are called at IRQL &lt;= DISPATCH\_LEVEL, in an arbitrary thread context.

Because they can be called at IRQL DISPATCH\_LEVEL, completion routines cannot call kernel-mode routines that must be called at a lower IRQL, such as [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083). For the same reason, any data structures that are used in a completion routine must be allocated from nonpaged pool.

This section discusses the following topics:

[How Completion Processing Is Performed](how-completion-processing-is-performed.md)

[Checking the PendingReturned Flag](checking-the-pendingreturned-flag.md)

[Returning Status from Completion Routines](returning-status-from-completion-routines.md)

[Example: Simple Pass-Through Dispatch and Completion](example--simple-pass-through-dispatch-and-completion.md)

[Constraints on Completion Routines](constraints-on-completion-routines.md)

 

 




