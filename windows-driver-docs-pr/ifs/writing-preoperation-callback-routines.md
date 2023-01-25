---
title: Writing Pre-operation Callback Routines
description: Writing Preoperation Callback Routines
keywords:
- preoperation callback routines WDK minifilter , writing
- writing callback routines
- IRQL, preoperation callback routine
ms.date: 01/24/2023
---

# Writing Pre-operation Callback Routines

A minifilter driver uses one or more *pre-operation callback routines* to filter I/O operations. [**Pre-operation callback routines**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) are similar to the [dispatch routines used in the legacy filter model](/windows-hardware/drivers/ifs/writing-irp-dispatch-routines).

A minifilter registers a pre-operation callback routine for a particular type of I/O operation by storing the callback routine's entry point in the **OperationRegistration** member of the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure. The minifilter passes this member to *FltMgr* as a parameter to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) in its [**DriverEntry**](writing-a-driverentry-routine-for-a-minifilter-driver.md) routine.

Minifilters receive only those types of I/O operations for which they've registered a pre-operation or post-operation callback routine. A minifilter can register a pre-operation callback routine for a given type of I/O operation without registering a [**post-operation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback), and vice versa.

Every pre-operation callback routine is defined as follows:

```cpp
typedef FLT_PREOP_CALLBACK_STATUS 
(*PFLT_PRE_OPERATION_CALLBACK) ( 
    IN OUT PFLT_CALLBACK_DATA Data, 
    IN PCFLT_RELATED_OBJECTS FltObjects, 
    OUT PVOID *CompletionContext 
    ); 
```

When *FltMgr* calls a minifilter's pre-operation callback routine for a given I/O operation, the minifilter temporarily controls the I/O operation. The minifilter retains this control until it either:

- Returns a status value other than FLT_PREOP_PENDING from its pre-operation callback routine.

- Calls [**FltCompletePendedPreOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpreoperation) from a work routine that has processed an operation that was previously pended in its pre-operation callback routine.

The following table lists a few possible usage scenarios of a minifilter's pre-operation callback routine and provides implementation details and the return value for each scenario.

| Usage Scenario | Implementation | Value Returned |
| -------------- | -------------- | -------------- |
| The routine isn't relevant for the operation and doesn't require the final status of the operation or it has no post-operation callback. | Pass the I/O operation through and tell *FltMgr* to not call the minifilter's post-operation callback on completion. | FLT_PREOP_SUCCESS_NO_CALLBACK |
| The routine requires the final status of the operation. | Pass the operation through and tell *FltMgr* to call the minifilter's post-operation callback routine. | FLT_PREOP_SUCCESS_WITH_CALLBACK |
| The minifilter must complete or continue processing this operation in the future. | Put the operation into a pending state. Use [**FltCompletePendedPreOperation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcompletependedpreoperation) to complete the operation later. There may be an acceptable race between the pre-operation routine returning FLT_PREOP_PENDING, and **FltCompletePendingOperation** being called. *FltMgr* handles this scenario without input from the driver. | FLT_PREOP_PENDING |
| The post-operation processing must occur in the context of the same thread that the dispatch routine was called. This condition ensures consistent IRQL and maintains your local variable state. | Synchronize the operation with the post-operation. | FLT_PREOP_SYNCHRONIZE |
| The pre-operation callback routine needs to complete the operation. | Stop processing for the operation and assign final NTSTATUS value. | FLT_PREOP_COMPLETE  |

## IRQL and pre-operation callback routines

FltMgr has no way of knowing what a minifilter might do in its pre-operation callback (or any callback). So FltMgr has no way of knowing whether a call to the miniport's pre-op callback might cause an issue. (There are things you can safely do at elevated IRQL and things that you can't). *Therefore, it's up to the minifilter to be aware of IRQL and handle it appropriately. A minifilter can safely and cheaply call [**KeGetCurrentIRQL**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kegetcurrentirql) for situations in which it needs to know the IRQL at which it was called.*

The following information about a minifilter's pre-operation callback routine IRQL is useful to know:

- A pre-operation callback can be called at IRQL = PASSIVE_LEVEL or IRQL = APC_LEVEL. Most pre-operation callbacks are called at IRQL = PASSIVE_LEVEL, in the context of the thread that originated the I/O request. Only a handful of pre-operation callbacks might be called at IRQL = APC_LEVEL.

- For fast I/O and file system filter (FsFilter) operations, a pre-operation callback routine is always called at IRQL = PASSIVE_LEVEL. IRQL > PASSIVE_LEVEL applies only to IRP-based operations.

- For IRP-based operations, a minifilter's pre-operation callback can be called in the context of a system worker thread if a higher filter or minifilter driver pends the operation for processing by the worker thread. A pre-operation callback is the equivalent of a legacy filter's dispatch routine, so knowing the [IRQL and thread context of a legacy filter's dispatch routine](dispatch-routine-irql-and-thread-context.md) might be helpful.

- Context objects can't be retrieved in post-operation routines at IRQL > APC_LEVEL. Instead, either get the context object during a pre-operation routine and pass it to the post-operation routine or perform post-operation processing at IRQL <= APC_LEVEL. For more information about contexts, see [Managing Contexts](managing-contexts.md).

## Related articles

[Passing an I/O Operation Down the Minifilter Instance Stack](passing-an-i-o-operation-down-the-minifilter-driver-instance-stack.md)

[Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md)

[Disallowing a Fast I/O Operation in a Preoperation Callback Routine](disallowing-a-fast-i-o-operation-in-a-preoperation-callback-routine.md)

[Pending an I/O Operation in a Preoperation Callback Routine](pending-an-i-o-operation-in-a-preoperation-callback-routine.md)
