---
title: SAL 2.0 Annotations for Windows Drivers
description: The Microsoft Source Code Annotation Language (SAL) includes annotations that are specific to the analysis of Windows drivers and the related kernel code.
ms.assetid: 2CD181B8-4E1D-457A-9FF9-DAB3AB932730
---

# SAL 2.0 Annotations for Windows Drivers


The Microsoft Source Code Annotation Language (SAL) includes annotations that are specific to the analysis of Windows drivers and the related kernel code. The annotation language provides a way of describing properties of functions, parameters, return values, structures, and structure fields. Annotations are like comments that you add to your code and are ignored by the compiler but are used by the static analysis tools. The use of annotations helps improve developer effectiveness, helps improve the accuracy of the results from static analysis, and allows the tools to better determine whether a particular bug exists. The driver annotations are not intended for use in non-driver or non-kernel-related code. The driver annotations are defined in Driverspecs.h.

**Note**  Windows 8 introduces SAL 2.0, which replaces SAL 1.0. For information about SAL 2.0, see [Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283). SAL 2.0 replaces SAL 1.0. SAL 2.0 should be used with the Windows Driver Kit (WDK) 8 for Windows 8. If you need information about the SAL 1.0 for drivers, refer to the documentation that ships with the WDK for Windows 7.

 

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver annotations</th>
<th align="left">Category</th>
<th align="left">Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>_IRQL_requires_max_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_requires_min_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_raises_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_requires_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_raises_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_saves_</strong></p>
<p><strong>_IRQL_restores_</strong></p>
<p><strong>_IRQL_saves_global_</strong>(<em>kind</em>, <em>param</em>)</p>
<p><strong>_IRQL_restores_global_</strong>(<em>kind</em>, <em>param</em>)</p>
<p><strong>_IRQL_always_function_min_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_always_function_max_</strong>(<em>value</em>)</p>
<p><strong>_IRQL_requires_same_</strong></p></td>
<td align="left">[IRQL annotations](irql-annotations-for-drivers.md)</td>
<td align="left"><p>Use the IRQL annotations to specify the range of IRQL levels at which a function should run. The IRQL annotations help the code analysis tool to more accurately find errors.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>_IRQL_is_cancel_</strong></td>
<td align="left">[IRQL annotations](irql-annotations-for-drivers.md)</td>
<td align="left"><p>Use the _IRQL_is_cancel_ annotation can help ensure correct behavior of a <strong>DRIVER_CANCEL</strong> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>_Kernel_float_saved_</strong></p>
<p><strong>_Kernel_float_restored_</strong></p>
<p><strong>_Kernel_float_used_</strong></p></td>
<td align="left">[Floating point annotations for drivers](floating-point-annotations-for-drivers.md)</td>
<td align="left"><p>Use the floating point annotations to help the code analysis tool detect the use of floating point in kernel-mode code and to report errors if the floating-point state is not properly protected.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>_Kernel_clear_do_init_</strong></p></td>
<td align="left">[DO_DEVICE_INITIALIZING annotation](do-device-initializing-annotation-for-drivers.md)</td>
<td align="left"><p>Use the _Kernel_clear_do_init_ annotation to specify whether the annotated function is expected to clear the DO_DEVICE_INITIALIZING bit in the Flags field of the device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>_Kernel_IoGetDmaAdapter_</strong></p></td>
<td align="left">[_Kernel_IoGetDmaAdapter_ Annotation](-kernel-iogetdmaadapter--annotation-for-drivers.md)</td>
<td align="left"><p>Use the _Kernel_IoGetDmaAdapter_ annotation to direct the code analysis tools to look for misuse of DMA pointers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>_Interlocked_operand_</strong></p></td>
<td align="left">[Annotations for interlocked operands](driver-annotations-for-interlocked-operands.md)</td>
<td align="left"><p>Use the _Interlocked_operand_ annotation for function parameters to identify them as an interlocked operands. A number of functions take as one of their parameters the address of a variable that should be accessed by using an interlocked processor instruction. These are cache read-through atomic instructions, and if the operands are used incorrectly, very subtle bugs result.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>_Dispatch_type_</strong></p></td>
<td align="left">[Annotations for Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines).</td>
<td align="left"><p>Use the _Dispatch_type_ annotation used when you declare WDM driver dispatch routines. See [Declaring Functions Using Function Role Types for WDM Drivers](declaring-functions-using-function-role-types-for-wdm-drivers.md) and [Annotating Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>_Flt_CompletionContext_Outptr_</strong></p></td>
<td align="left">[_Flt_CompletionContext_Outptr_ Annotation](-flt-completioncontext-outptr--annotation.md)</td>
<td align="left"><p>Use the <strong>_Flt_CompletionContext_Outptr_</strong> annotation when you declare file system minifilter pre-operation callback functions ([<strong>PFLT_PRE_OPERATION_CALLBACK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551109)). Place this annotation on the <em>CompletionContext</em> parameter. This annotation directs the code analysis tool to check that the <em>CompletionContext</em> is correct for the FLT_PREOP_CALLBACK_STATUS return value.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20SAL%202.0%20Annotations%20for%20Windows%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





