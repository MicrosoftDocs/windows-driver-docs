---
title: Writing Postoperation Callback Routines
description: Writing Postoperation Callback Routines
ms.assetid: 4940e38d-107b-45c4-aa71-6e8543330f39
keywords:
- postoperation callback routines WDK file system minifilter , writing
- writing callback routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Postoperation Callback Routines


## <span id="ddk_writing_postoperation_callback_routines_if"></span><span id="DDK_WRITING_POSTOPERATION_CALLBACK_ROUTINES_IF"></span>


A file system minifilter driver uses one or more *postoperation callback routines* to filter I/O operations.

A postoperation callback routine can take one of the following actions:

-   Accomplish completion work directly in postoperation routine. All the completion work can be accomplished at IRQL &lt;= DISPATCH\_LEVEL.
-   Accomplish completion work at a safe IRQL. Return FLT\_STATUS\_MORE\_PROCESSING\_REQUIRED and queue a worker thread to allow processing at safe IRQL. When processing is complete, the worker thread calls [**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897) to continue postoperation processing.
-   Cancel a successful CREATE operation.

[**Postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107) are similar to the *completion routines* that are used in legacy file system filter drivers.

A minifilter driver registers a postoperation callback routine for a particular type of I/O operation in the same way it registers a [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109)—that is, by storing the callback routine's entry point in the **OperationRegistration** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine.

Minifilter drivers receive only those types of I/O operations for which they have registered a preoperation or postoperation callback routine. A minifilter driver can register a preoperation callback routine for a given type of I/O operation without registering a postoperation callback, and vice versa.

Every postoperation callback routine is defined as follows:

```cpp
typedef FLT_POSTOP_CALLBACK_STATUS 
(*PFLT_POST_OPERATION_CALLBACK) ( 
    IN OUT PFLT_CALLBACK_DATA Data, 
    IN PCFLT_RELATED_OBJECTS FltObjects, 
    IN PVOID CompletionContext, 
    IN FLT_POST_OPERATION_FLAGS Flags 
    ); 
```

Like a completion routine, a postoperation callback routine is called at IRQL &lt;= DISPATCH\_LEVEL, in an arbitrary thread context.

Because it can be called at IRQL = DISPATCH\_LEVEL, a postoperation callback routine cannot call kernel-mode routines that must be called at a lower IRQL, such as [**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371) or [**RtlCompareUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561782). For the same reason, any data structures that are used in a postoperation callback routine must be allocated from nonpaged pool.

The following situations are several exceptions to the preceding rule:

-   If a minifilter driver's preoperation callback routine returns FLT\_PREOP\_SYNCHRONIZE for an IRP-based I/O operation, the corresponding postoperation callback routine is called at IRQL &lt;= APC\_LEVEL, in the same thread context as the preoperation callback routine.

-   The postoperation callback routine for a fast I/O operation is called at IRQL = PASSIVE\_LEVEL, in the same thread context as the preoperation callback routine.

-   Post-create callback routines are called at IRQL = PASSIVE\_LEVEL, in the context of the thread that originated the IRP\_MJ\_CREATE operation.

When the filter manager calls a minifilter driver's postoperation callback routine for a given I/O operation, the minifilter driver temporarily controls the I/O operation. The minifilter driver retains this control until it does one of the following:

-   Returns FLT\_POSTOP\_FINISHED\_PROCESSING from the postoperation callback routine.

-   Calls [**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897) from a work routine that has processed an IRP-based I/O operation that was pended in the postoperation callback routine.

This section includes:

[Performing Completion Processing for an I/O Operation](performing-completion-processing-for-an-i-o-operation.md)

[Pending an I/O Operation in a Postoperation Callback Routine](pending-an-i-o-operation-in-a-postoperation-callback-routine.md)

[Failing an I/O Operation in a Postoperation Callback Routine](failing-an-i-o-operation-in-a-postoperation-callback-routine.md)

 

 




