---
title: Performing Completion Processing for an I/O Operation
description: Performing Completion Processing for an I/O Operation
ms.assetid: 7e65c21c-d38f-4804-8c07-6cd89f6a6dd6
keywords: ["postoperation callback routines WDK file system minifilter , completion processing", "completing I/O requests WDK file system"]
---

# Performing Completion Processing for an I/O Operation


## <span id="ddk_performing_completion_processing_for_an_io_operation_if"></span><span id="DDK_PERFORMING_COMPLETION_PROCESSING_FOR_AN_IO_OPERATION_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) is called when an I/O operation has been completed by the underlying file system, by a legacy filter, or by another minifilter driver that is at a lower altitude in the minifilter driver instance stack.

In addition, when a minifilter driver instance is being torn down, the filter manager "drains" any I/O operations for which the instance has received a [**preoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and is awaiting a [**postoperation callback**](https://msdn.microsoft.com/library/windows/hardware/ff551107). In this situation, the filter manager calls the minifilter driver's postoperation callback routine, even if the I/O operation has not been completed, and sets the FLTFL\_POST\_OPERATION\_DRAINING flag in the *Flags* input parameter.

When the FLTFL\_POST\_OPERATION\_DRAINING flag is set, the minifilter driver must not perform normal completion processing. Instead, it should perform only necessary cleanup, such as freeing memory that the minifilter driver allocated for the *CompletionContext* parameter in its preoperation callback routine, and return FLT\_POSTOP\_FINISHED\_PROCESSING.

This section includes the following topic:

[Ensuring that Completion Processing is Performed at Safe IRQL](ensuring-that-completion-processing-is-performed-at-safe-irql.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Performing%20Completion%20Processing%20for%20an%20I/O%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




