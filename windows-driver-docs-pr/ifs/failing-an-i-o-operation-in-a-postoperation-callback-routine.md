---
title: Failing an I/O Operation in a Postoperation Callback Routine
description: Failing an I/O Operation in a Postoperation Callback Routine
ms.assetid: 45897bca-1573-42c5-ad00-3198b7362d9e
keywords:
- postoperation callback routines WDK file system minifilter , failing operations
- failing I/O operations WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Failing an I/O Operation in a Postoperation Callback Routine


## <span id="ddk_failing_an_io_operation_in_a_postoperation_callback_routine_if"></span><span id="DDK_FAILING_AN_IO_OPERATION_IN_A_POSTOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) can fail a successful I/O operation, but simply failing an I/O operation does not undo the effect of the operation. The minifilter driver is responsible for performing any processing that is needed to undo the operation.

For example, a minifilter driver's post-create callback routine can fail a successful IRP\_MJ\_CREATE operation by performing the following steps:

1.  Calling [**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784) to close the file that was created or opened by the create operation. Note that **FltCancelFileOpen** does not undo any modifications to the file. For example, **FltCancelFileOpen** does not delete a newly created file or restore a truncated file to its previous size.

2.  Setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation. This value must be a valid error NTSTATUS value, such as STATUS\_ACCESS\_DENIED.

3.  Setting the callback data structure's **IoStatus.Information** field to zero.

4.  Returning FLT\_POSTOP\_FINISHED\_PROCESSING.

When setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation, the minifilter driver must specify a valid error NTSTATUS value. Note that minifilter drivers cannot specify STATUS\_FLT\_DISALLOW\_FAST\_IO; only the filter manager can use this NTSTATUS value.

Callers of [**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784) must be running at IRQL &lt;= APC\_LEVEL. However, a minifilter driver can safely call this routine from a post-create callback routine, because, for IRP\_MJ\_CREATE operations, the postoperation callback routine is called at IRQL = PASSIVE\_LEVEL, in the context of the thread that originated the create operation.

 

 




