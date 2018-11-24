---
title: Passing I/O Operations Down the Minifilter Driver Instance Stack
description: Passing an I/O Operation Down the Minifilter Driver Instance Stack
ms.assetid: b2661e1e-2190-4def-be6c-27057c631304
keywords:
- preoperation callback routines WDK file system minifilter , passing down driver instance stack
- passing I/O ops down minifilter driver stack WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Passing I/O Operations Down the Minifilter Driver Instance Stack


## <span id="ddk_passing_an_io_operation_down_the_minifilter_instance_stack_if"></span><span id="DDK_PASSING_AN_IO_OPERATION_DOWN_THE_MINIFILTER_INSTANCE_STACK_IF"></span>


When a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) or work routine returns an I/O operation to the filter manager, the filter manager sends the operation to minifilter drivers below the current minifilter driver in the minifilter driver instance stack and to legacy filters and the file system for further processing.

A minifilter driver's preoperation callback routine returns an I/O operation to the filter manager for further processing by returning one of the following status values:

-   FLT\_PREOP\_SUCCESS\_NO\_CALLBACK (all operation types)

-   FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK (all operation types)

-   FLT\_PREOP\_SYNCHRONIZE (IRP-based I/O operations only)

**Note**   Although FLT\_PREOP\_SYNCHRONIZE should be returned only for IRP-based I/O operations, you can return this status value for other operation types. If it is returned for an I/O operation that is not an IRP-based I/O operation, the filter manager treats this return value as if it were FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK.

 

Alternatively, the work routine for an operation that was pended in a preoperation callback routine returns an I/O operation to the filter manager by passing one of the preceding status values in the *CallbackStatus* parameter when it calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) to resume processing for the pended I/O operation.

This section includes:

[Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK](returning-flt-preop-success-with-callback.md)

[Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK](returning-flt-preop-success-no-callback.md)

[Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md)

 

 




