---
title: Writing Preoperation Callback Routines
description: Writing Preoperation Callback Routines
ms.assetid: 3f863c44-152e-43c9-8ef5-ec426986a3fe
keywords:
- preoperation callback routines WDK file system minifilter , writing
- writing callback routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Preoperation Callback Routines


## <span id="ddk_writing_preoperation_callback_routines_if"></span><span id="DDK_WRITING_PREOPERATION_CALLBACK_ROUTINES_IF"></span>


A file system minifilter driver uses one or more *preoperation callback routines* to filter I/O operations. [**Preoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551109) are similar to the dispatch routines that are used in legacy file system filter drivers.

A minifilter driver registers a preoperation callback routine for a particular type of I/O operation by storing the callback routine's entry point in the **OperationRegistration** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure. The minifilter driver passes this member as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine.

Minifilter drivers receive only those types of I/O operations for which they have registered a preoperation or postoperation callback routine. A minifilter driver can register a preoperation callback routine for a given type of I/O operation without registering a [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107), and vice versa.

The following table shows the preoperation callback routine implementation for a specific usage scenario and its return value.

| Usage Scenario                                                                                                                                                                        | Implementation                                                                                                                                       | Value Returned                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| The routine is not relevant for the operation and does not require the final status of the operation or it has no postoperation callback.                                             | Pass the I/O operation through without calling the minifilter's postoperation callback on completion.                                                | FLT\_PREOP\_SUCCESS\_NO\_CALLBACK   |
| The routine requires the final status of the operation.                                                                                                                               | Pass the operation through, requiring the minifilter to call the postoperation callback routine.                                                     | FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK |
| The minifilter must complete or continue processing this operation in the future.                                                                                                     | Put the operation into a pending state. Use [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) to complete the operation later. Note that there may be an acceptable race between the pre-operation routine returning **FLT_PREOP_PENDING**, and **FltCompletePendingOperation** being called. The filter manager handles this scenario without input from the driver. | FLT\_PREOP\_PENDING                 |
| The postoperation processing must occur in the context of the same thread that the dispatch routine was called. This ensures consistent IRQL and maintains your local variable state. | Synchronize the operation with the postoperation.                                                                                                    | FLT\_PREOP\_SYNCHRONIZE             |
| The preoperation callback routine needs to complete the operation.                                                                                                                    | Stop processing for the operation and assign final NTSTATUS value.                                                                                   | FLT\_PREOP\_COMPLETE                |


Every preoperation callback routine is defined as follows:

```cpp
typedef FLT_PREOP_CALLBACK_STATUS 
(*PFLT_PRE_OPERATION_CALLBACK) ( 
    IN OUT PFLT_CALLBACK_DATA Data, 
    IN PCFLT_RELATED_OBJECTS FltObjects, 
    OUT PVOID *CompletionContext 
    ); 
```

Like a dispatch routine, a preoperation callback routine can be called at IRQL = PASSIVE\_LEVEL or at IRQL = APC\_LEVEL. Typically it is called at IRQL = PASSIVE\_LEVEL, in the context of the thread that originated the I/O request. For fast I/O and file system filter (FsFilter) operations, the preoperation callback routine is always called at IRQL = PASSIVE\_LEVEL. However, for an IRP-based operation, a minifilter driver's preoperation callback routine can be called in the context of a system worker thread if a higher filter or minifilter driver pends the operation for processing by the worker thread.

Context objects cannot be retrieved in postoperation routines at IRQL &gt; APC\_LEVEL. Instead, either get the context object during a preoperation routine and pass it to the postoperation routine or perform postoperation processing at IRQL &lt;= APC\_LEVEL. For more information about contexts, see [Managing Contexts](managing-contexts.md).

When the filter manager calls a minifilter driver's preoperation callback routine for a given I/O operation, the minifilter driver temporarily controls the I/O operation. The minifilter driver retains this control until it does one of the following:

-   Returns a status value other than FLT\_PREOP\_PENDING from the preoperation callback routine.

-   Calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) from a work routine that has processed an operation that was pended in the preoperation callback routine.

This section includes:

[Passing an I/O Operation Down the Minifilter Instance Stack](passing-an-i-o-operation-down-the-minifilter-driver-instance-stack.md)

[Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md)

[Disallowing a Fast I/O Operation in a Preoperation Callback Routine](disallowing-a-fast-i-o-operation-in-a-preoperation-callback-routine.md)

[Pending an I/O Operation in a Preoperation Callback Routine](pending-an-i-o-operation-in-a-preoperation-callback-routine.md)

 

 




