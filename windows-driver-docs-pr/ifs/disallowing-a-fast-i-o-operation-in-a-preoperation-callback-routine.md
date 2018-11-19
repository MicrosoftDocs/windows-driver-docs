---
title: Disallow a Fast I/O Operation in a Preoperation Callback Routine
description: Disallow a Fast I/O Operation in a Preoperation Callback Routine
ms.assetid: 20797d8c-ffcf-46df-b870-839d5c02d2d4
keywords:
- preoperation callback routines WDK file system minifilter , disallowing fast I/O
- disallow fast I/O operations WDK file system minifilter
- fast I/O disallowed WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disallow a Fast I/O Operation in a Preoperation Callback Routine


## <span id="ddk_disallowing_a_fast_io_operation_in_a_preoperation_callback_routine"></span><span id="DDK_DISALLOWING_A_FAST_IO_OPERATION_IN_A_PREOPERATION_CALLBACK_ROUTINE"></span>


In certain circumstances, a minifilter driver might choose to disallow a fast I/O operation instead of completing it. Disallowing a fast I/O operation prevents the fast I/O path from being used for the operation.

Like completing an I/O operation, disallowing a fast I/O operation means to halt processing on it and return it to the filter manager. However, disallowing a fast I/O operation is different from completing it. If a minifilter driver disallows a fast I/O operation that was issued by the I/O manager, the I/O manager may reissue the same operation as an equivalent IRP-based operation.

When a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) disallows a fast I/O operation, the filter manager does the following:

-   Does not send the operation to minifilter drivers below the current minifilter driver, to legacy filters, or to the file system.

-   Calls the [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107) of the minifilter drivers above the current minifilter driver in the minifilter driver instance stack.

-   Does not call the current minifilter driver's postoperation callback routine for the operation, if one exists.

A minifilter driver disallows a fast I/O operation by returning FLT\_PREOP\_DISALLOW\_FASTIO from the preoperation callback routine for the operation.

The preoperation callback routine should not set the callback data structure's **IoStatus.Status** field, because the filter manager automatically sets this field to STATUS\_FLT\_DISALLOW\_FAST\_IO.

FLT\_PREOP\_DISALLOW\_FASTIO can only be returned for fast I/O operations. To determine whether an operation is a fast I/O operation, see [**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645).

Minifilter drivers cannot return FLT\_PREOP\_DISALLOW\_FASTIO for IRP\_MJ\_SHUTDOWN, IRP\_MJ\_VOLUME\_MOUNT, or IRP\_MJ\_VOLUME\_DISMOUNT operations.

 

 




