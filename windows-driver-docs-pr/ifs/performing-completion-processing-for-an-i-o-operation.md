---
title: Performing Completion Processing for an I/O Operation
description: Performing Completion Processing for an I/O Operation
keywords:
- postoperation callback routines WDK file system minifilter , completion processing
- completing I/O requests WDK file system
ms.date: 04/20/2017
---

# Performing Completion Processing for an I/O Operation


## <span id="ddk_performing_completion_processing_for_an_io_operation_if"></span><span id="DDK_PERFORMING_COMPLETION_PROCESSING_FOR_AN_IO_OPERATION_IF"></span>


A minifilter driver's [**postoperation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) is called when an I/O operation has been completed by the underlying file system, by a legacy filter, or by another minifilter driver that is at a lower altitude in the minifilter driver instance stack.

In addition, when a minifilter driver instance is being torn down, the filter manager "drains" any I/O operations for which the instance has received a [**preoperation callback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) and is awaiting a [**postoperation callback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback). In this situation, the filter manager calls the minifilter driver's postoperation callback routine, even if the I/O operation has not been completed, and sets the FLTFL\_POST\_OPERATION\_DRAINING flag in the *Flags* input parameter.

When the FLTFL\_POST\_OPERATION\_DRAINING flag is set, the minifilter driver must not perform normal completion processing. Instead, it should perform only necessary cleanup, such as freeing memory that the minifilter driver allocated for the *CompletionContext* parameter in its preoperation callback routine, and return FLT\_POSTOP\_FINISHED\_PROCESSING.

This section includes the following topic:

[Ensuring that Completion Processing is Performed at Safe IRQL](ensuring-that-completion-processing-is-performed-at-safe-irql.md)

 

