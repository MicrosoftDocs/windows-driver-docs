---
title: Performing Completion Processing for an I/O Operation
description: Performing Completion Processing for an I/O Operation
ms.assetid: 7e65c21c-d38f-4804-8c07-6cd89f6a6dd6
keywords:
- postoperation callback routines WDK file system minifilter , completion processing
- completing I/O requests WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Completion Processing for an I/O Operation


## <span id="ddk_performing_completion_processing_for_an_io_operation_if"></span><span id="DDK_PERFORMING_COMPLETION_PROCESSING_FOR_AN_IO_OPERATION_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) is called when an I/O operation has been completed by the underlying file system, by a legacy filter, or by another minifilter driver that is at a lower altitude in the minifilter driver instance stack.

In addition, when a minifilter driver instance is being torn down, the filter manager "drains" any I/O operations for which the instance has received a [**preoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and is awaiting a [**postoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551107). In this situation, the filter manager calls the minifilter driver's postoperation callback routine, even if the I/O operation has not been completed, and sets the FLTFL\_POST\_OPERATION\_DRAINING flag in the *Flags* input parameter.

When the FLTFL\_POST\_OPERATION\_DRAINING flag is set, the minifilter driver must not perform normal completion processing. Instead, it should perform only necessary cleanup, such as freeing memory that the minifilter driver allocated for the *CompletionContext* parameter in its preoperation callback routine, and return FLT\_POSTOP\_FINISHED\_PROCESSING.

This section includes the following topic:

[Ensuring that Completion Processing is Performed at Safe IRQL](ensuring-that-completion-processing-is-performed-at-safe-irql.md)

 

 




