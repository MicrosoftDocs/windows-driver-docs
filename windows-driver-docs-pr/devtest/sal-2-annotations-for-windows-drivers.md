---
title: SAL 2.0 Annotations for Windows Drivers
description: The Microsoft Source Code Annotation Language (SAL) includes annotations that are specific to the analysis of Windows drivers and the related kernel code.
ms.date: 08/25/2023
---

# SAL 2.0 annotations for Windows drivers

The Microsoft Source Code Annotation Language (SAL) includes annotations that are specific to the analysis of Windows drivers and the related kernel code. The annotation language provides a way of describing properties of functions, parameters, return values, structures, and structure fields. Annotations are like comments that you add to your code and are ignored by the compiler but are used by the static analysis tools. The use of annotations helps improve developer effectiveness, helps improve the accuracy of the results from static analysis, and allows the tools to better determine whether a particular bug exists. The driver annotations are not intended for use in non-driver or non-kernel-related code. The driver annotations are defined in Driverspecs.h.

**Note**  Windows 8 introduces SAL 2.0, which replaces SAL 1.0. For information about SAL 2.0, see [Using SAL Annotations to Reduce C/C++ Code Defects](/cpp/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects). SAL 2.0 replaces SAL 1.0. SAL 2.0 should be used with the Windows Driver Kit (WDK) 8 for Windows 8. If you need information about the SAL 1.0 for drivers, refer to the documentation that ships with the WDK for Windows 7.

## IRQL annotations

Use the [IRQL annotations](irql-annotations-for-drivers.md) to specify the range of IRQL levels at which a function should run. The IRQL annotations help the code analysis tool to more accurately find errors.

`_IRQL_requires_max_(value)`

`_IRQL_requires_min_(value)`

`_IRQL_raises_(value)`

`_IRQL_requires_(value)`

`_IRQL_raises_(value)`

`_IRQL_saves_`

`_IRQL_restores_`

`_IRQL_saves_global_(kind, param)`

`_IRQL_restores_global_(kind, param)`

`_IRQL_always_function_min_(value)`

`_IRQL_always_function_max_(value)`

`_IRQL_requires_same_`

`_IRQL_is_cancel_` - Use the \_IRQL_is_cancel annotation to help ensure correct behavior of a DRIVER\_CANCEL callback function.

## Floating point annotations for drivers

`_Kernel_float_saved_`

`_Kernel_float_restored_`

`_Kernel_float_used_`

Use the [Floating point annotations for drivers](floating-point-annotations-for-drivers.md) to help the code analysis tool detect the use of floating point in kernel-mode code and to report errors if the floating-point state is not properly protected.

## DO_DEVICE_INITIALIZING annotation

`_Kernel_clear_do_init_`

Use the [DO_DEVICE_INITIALIZING annotation](do-device-initializing-annotation-for-drivers.md)
 to specify whether the annotated function is expected to clear the DO\_DEVICE\_INITIALIZING bit in the Flags field of the device object.

## Kernel_IoGetDmaAdapter annotation

`_Kernel_IoGetDmaAdapter_`

Use the [_Kernel_IoGetDmaAdapter_ annotation](-kernel-iogetdmaadapter--annotation-for-drivers.md)
to direct the code analysis tools to look for misuse of DMA pointers.

## Annotations for interlocked operands

`_Interlocked_operand_`

Use the [Annotations for interlocked operands](driver-annotations-for-interlocked-operands.md) for function parameters to identify them as an interlocked operands. A number of functions take as one of their parameters the address of a variable that should be accessed by using an interlocked processor instruction. These are cache read-through atomic instructions, and if the operands are used incorrectly, very subtle bugs result.

## Annotations for driver dispatch routines

`_Dispatch_type_`

Use the [Annotations for Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines) when you declare WDM driver dispatch routines. 
For more information, see [Declaring Functions Using Function Role Types for WDM Drivers](declaring-functions-using-function-role-types-for-wdm-drivers.md) and [Annotating Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines).

##  File System Minifilter pre-operation callback \_Flt\_CompletionContext\_Outptr\_ annotation

`_Flt_CompletionContext_Outptr_`

Use the [File System Minifilter pre-operation callback \_Flt\_CompletionContext\_Outptr\_ annotation](-flt-completioncontext-outptr--annotation.md) when you declare file system minifilter pre-operation callback functions [PFLT_PRE_OPERATION_CALLBACK](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback).

Place this annotation on the CompletionContext parameter. This annotation directs the code analysis tool to check that the CompletionContext is correct for the FLT\_PREOP\_CALLBACK\_STATUS return value.

## See also

[Using SAL Annotations to Reduce C/C++ Code Defects](/cpp/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects)
