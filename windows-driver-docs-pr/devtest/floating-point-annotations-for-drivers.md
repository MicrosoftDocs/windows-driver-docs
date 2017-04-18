---
title: Floating Point Annotations for drivers
description: Floating point annotations can help the code analysis tool detect the use of floating point in kernel-mode code and can report errors if the floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.
ms.assetid: 86FF1A21-674F-4BDA-AC03-C1E5F06A4439
---

# Floating Point Annotations for drivers


Floating point annotations can help the code analysis tool detect the use of floating point in kernel-mode code and can report errors if the floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.

For some processor families, particularly x86 processors, using floating-point operations from within kernel-mode code must be done only within the scope of functions that save and restore floating-point state. Violations of this rule can be particularly difficult to find because they will only sporadically cause problems at run time (but these problems can be very serious). With the proper use of annotations, the code analysis tools are effective at detecting the use of floating point in kernel-mode code and reporting an error if floating-point state is not properly protected. Floating-point rules are checked only for kernel-mode code.

Add the following annotations to function parameters to indicate what they do with the floating-point state.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Floating-point annotation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_Kernel_float_saved_"></span><span id="_kernel_float_saved_"></span><span id="_KERNEL_FLOAT_SAVED_"></span>_Kernel_float_saved_</p></td>
<td align="left"><p>The annotated function saves the floating-point hardware state, when the function returns successfully.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_Kernel_float_restored_"></span><span id="_kernel_float_restored_"></span><span id="_KERNEL_FLOAT_RESTORED_"></span>_Kernel_float_restored_</p></td>
<td align="left"><p>The annotated function restores the floating-point hardware state when the function returns successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_Kernel_float_used_"></span><span id="_kernel_float_used_"></span><span id="_KERNEL_FLOAT_USED_"></span>_Kernel_float_used_</p></td>
<td align="left"><p>If the function is called safely by a calling function, you can use the _Kernel_float_used_ annotation to suppress the reporting of errors. However, if the calling function is not also annotated with _Kernel_float_used_ or the function call does not occur between functions annotated with _Kernel_float_saved and _Kernel_float_restored_, respectively, the code analysis tools will report an error.</p></td>
</tr>
</tbody>
</table>

 

These annotations are already applied to KeSaveFloatingPoint state and KeRestoreFloatingPointState system functions, in addition to annotations for acquiring and releasing resources to prevent leaks. The similar EngXxx functions are also annotated in this way. However, functions that wrap these functions should also use these annotations.

If the function as a whole is called safely by some calling function, the function can be annotated with \_Kernel\_float\_used\_ annotation. This suppresses the warning and also causes the code analysis tools to confirm that the caller is using the function safely. Additional levels of \_Kernel\_float\_used\_ can be added as required. The \_Kernel\_float\_used\_ annotation is automatically provided by the code analysis tools when either the function result or one of the function's parameters is a floating point type, but it does not hurt to provide the annotation explicitly.

For example, the \_Kernel\_float\_saved\_ annotation indicates that floating-point state is stored in the FloatingState parameter of the KeSaveFloatingPointState system function.

```ManagedCPlusPlus
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

``` syntax
_Kernel_float_used_
void
    MyDoesFloatingPoint(arguments);
 
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Floating%20Point%20Annotations%20for%20drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





