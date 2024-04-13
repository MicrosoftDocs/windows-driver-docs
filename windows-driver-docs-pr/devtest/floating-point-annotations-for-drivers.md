---
title: Floating Point Annotations for Drivers
description: Floating point annotations can help the code analysis tool detect the use of floating point in kernel-mode code and can report errors if the floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.
ms.date: 08/25/2023
---

# Floating point annotations for drivers

Floating point annotations can help the code analysis tool detect the use of floating point in kernel-mode code and can report errors if the floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.

For some processor families, particularly x86 processors, using floating-point operations from within kernel-mode code must be done only within the scope of functions that save and restore floating-point state. Violations of this rule can be particularly difficult to find because they will only sporadically cause problems at run time (but these problems can be very serious). With the proper use of annotations, the code analysis tools are effective at detecting the use of floating point in kernel-mode code and reporting an error if floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.

Add the following annotations to function parameters to indicate what they do with the floating-point state.

|Floating-point annotation|Description|
|------------------------ |---------- |
|\_Kernel_float_saved_|The annotated function saves the floating-point hardware state, when the function returns successfully.|
|\_Kernel_float_restored_|The annotated function restores the floating-point hardware state when the function returns successfully.|
|\_Kernel_float_used_|If the function is called safely by a calling function, you can use the \_Kernel_float_used_ annotation to suppress the reporting of errors. However, if the calling function is not also annotated with \_Kernel_float_used_ or the function call does not occur between functions annotated with \_Kernel_float_saved_ and \_Kernel_float_restored_, respectively, the code analysis tools will report an error.|

These annotations are already applied to KeSaveFloatingPoint state and KeRestoreFloatingPointState system functions, in addition to annotations for acquiring and releasing resources to prevent leaks. The similar EngXxx functions are also annotated in this way. However, functions that wrap these functions should also use these annotations.

If the function as a whole is called safely by some calling function, the function can be annotated with \_Kernel\_float\_used\_ annotation. This suppresses the warning and also causes the code analysis tools to confirm that the caller is using the function safely. Additional levels of \_Kernel\_float\_used\_ can be added as required. The \_Kernel\_float\_used\_ annotation is automatically provided by the code analysis tools when either the function result or one of the function's parameters is a floating point type, but it does not hurt to provide the annotation explicitly.

For example, the \_Kernel\_float\_saved\_ annotation indicates that floating-point state is stored in the FloatingState parameter of the KeSaveFloatingPointState system function.

```cpp
_Must_inspect_result_  
_IRQL_requires_max_(DISPATCH_LEVEL)  
__drv_valueIs(<0;==0)  
_When_(return==0, _Kernel_float_saved_)  
_At_(*FloatingState, _Kernel_requires_resource_not_held_(FloatState) _When_(return==0, _Kernel_acquires_resource_(FloatState)))  
__forceinline  
NTSTATUS  
KeSaveFloatingPointState (  
    _Out_ PVOID FloatingState  
    )  
```

In the following example, the \_Kernel\_float\_used\_ annotation suppresses warnings about the use of the floating-point state. The annotation also causes the code analysis tools to confirm that any calls to MyDoesFloatingPoint occur in a safe floating-point context.

```
_Kernel_float_used_
void
    MyDoesFloatingPoint(arguments);
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)










