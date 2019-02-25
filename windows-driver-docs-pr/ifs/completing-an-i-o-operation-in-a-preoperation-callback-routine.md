---
title: Completing an I/O Operation in a Preoperation Callback Routine
description: Completing an I/O Operation in a Preoperation Callback Routine
ms.assetid: 1f339779-dc88-4673-87d5-36cee0b27fc2
keywords:
- preoperation callback routines WDK file system minifilter , completing I/O operations
- completing I/O requests WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing an I/O Operation in a Preoperation Callback Routine


## <span id="ddk_completing_an_io_operation_in_a_preoperation_callback_routine_if"></span><span id="DDK_COMPLETING_AN_IO_OPERATION_IN_A_PREOPERATION_CALLBACK_ROUTINE_IF"></span>


To *complete* an I/O operation means to halt processing for the operation, assign it a final NTSTATUS value, and return it to the filter manager.

When a minifilter driver completes an I/O operation, the filter manager does the following:

-   Does not send the operation to minifilter drivers below the current minifilter driver, to legacy filters, or to the file system.

-   Calls the [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107) of the minifilter drivers above the current minifilter driver in the minifilter driver instance stack.

-   Does not call the current minifilter driver's postoperation callback routine for the operation, if one exists.

A minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) completes an I/O operation by performing the following steps:

1.  Setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation.

2.  Returning FLT\_PREOP\_COMPLETE.

A preoperation callback routine that completes an I/O operation cannot set a non-NULL completion context (in the *CompletionContext* output parameter).

A minifilter driver can also complete an operation in the work routine for a previously pended I/O operation by performing the following steps:

1.  Setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation.

2.  Passing FLT\_PREOP\_COMPLETE in the *CallbackStatus* parameter when the work routine calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913).

When completing an I/O operation, a minifilter driver must set the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation, but this NTSTATUS value cannot be STATUS\_PENDING or STATUS\_FLT\_DISALLOW\_FAST\_IO. For a cleanup or close operation, the field must be STATUS\_SUCCESS. These operations cannot be completed with any other NTSTATUS value.

Completing an I/O operation is often referred to as succeeding or failing the operation, depending on the NTSTATUS value:

-   To *succeed* an I/O operation means to complete it with a success or informational NTSTATUS value, such as STATUS\_SUCCESS.

-   To *fail* an I/O operation means to complete it with an error or warning NTSTATUS value, such as STATUS\_INVALID\_DEVICE\_REQUEST or STATUS\_BUFFER\_OVERFLOW.

NTSTATUS values are defined in ntstatus.h. These values fall into four categories: success, informational, warning, and error. For more information about these values, see [Using NTSTATUS Values](https://msdn.microsoft.com/library/windows/hardware/ff565436).

 

 




