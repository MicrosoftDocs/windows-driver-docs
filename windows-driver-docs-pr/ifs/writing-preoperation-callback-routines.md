---
title: Writing Preoperation Callback Routines
author: windows-driver-content
description: Writing Preoperation Callback Routines
ms.assetid: 3f863c44-152e-43c9-8ef5-ec426986a3fe
keywords: ["preoperation callback routines WDK file system minifilter , writing", "writing callback routines"]
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
| The minifilter must complete or continue processing this operation in the future.                                                                                                     | Put the operation into a pending state. Use [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) to complete the operation later. | FLT\_PREOP\_PENDING                 |
| The postoperation processing must occur in the context of the same thread that the dispatch routine was called. This ensures consistent IRQL and maintains your local variable state. | Synchronize the operation with the postoperation.                                                                                                    | FLT\_PREOP\_SYNCHRONIZE             |
| The preoperation callback routine needs to complete the operation.                                                                                                                    | Stop processing for the operation and assign final NTSTATUS value.                                                                                   | FLT\_PREOP\_COMPLETE                |

 

Every preoperation callback routine is defined as follows:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20Preoperation%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


