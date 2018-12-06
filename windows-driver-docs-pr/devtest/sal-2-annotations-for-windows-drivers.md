---
title: SAL 2.0 Annotations for Windows Drivers
description: The Microsoft Source Code Annotation Language (SAL) includes annotations that are specific to the analysis of Windows drivers and the related kernel code.
ms.assetid: 2CD181B8-4E1D-457A-9FF9-DAB3AB932730
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><strong><em>IRQL_requires_max</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_requires_min</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_raises</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_requires</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_raises</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_saves</em></strong></p>
<p><strong><em>IRQL_restores</em></strong></p>
<p><strong><em>IRQL_saves_global</em></strong>(<em>kind</em>, <em>param</em>)</p>
<p><strong><em>IRQL_restores_global</em></strong>(<em>kind</em>, <em>param</em>)</p>
<p><strong><em>IRQL_always_function_min</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_always_function_max</em></strong>(<em>value</em>)</p>
<p><strong><em>IRQL_requires_same</em></strong></p></td>
<td align="left"><a href="irql-annotations-for-drivers.md" data-raw-source="[IRQL annotations](irql-annotations-for-drivers.md)">IRQL annotations</a></td>
<td align="left"><p>Use the IRQL annotations to specify the range of IRQL levels at which a function should run. The IRQL annotations help the code analysis tool to more accurately find errors.</p></td>
</tr>
<tr class="even">
<td align="left"><strong><em>IRQL_is_cancel</em></strong></td>
<td align="left"><a href="irql-annotations-for-drivers.md" data-raw-source="[IRQL annotations](irql-annotations-for-drivers.md)">IRQL annotations</a></td>
<td align="left"><p>Use the <em>IRQL_is_cancel</em> annotation can help ensure correct behavior of a <strong>DRIVER_CANCEL</strong> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>Kernel_float_saved</em></strong></p>
<p><strong><em>Kernel_float_restored</em></strong></p>
<p><strong><em>Kernel_float_used</em></strong></p></td>
<td align="left"><a href="floating-point-annotations-for-drivers.md" data-raw-source="[Floating point annotations for drivers](floating-point-annotations-for-drivers.md)">Floating point annotations for drivers</a></td>
<td align="left"><p>Use the floating point annotations to help the code analysis tool detect the use of floating point in kernel-mode code and to report errors if the floating-point state is not properly protected.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><em>Kernel_clear_do_init</em></strong></p></td>
<td align="left"><a href="do-device-initializing-annotation-for-drivers.md" data-raw-source="[DO_DEVICE_INITIALIZING annotation](do-device-initializing-annotation-for-drivers.md)">DO_DEVICE_INITIALIZING annotation</a></td>
<td align="left"><p>Use the <em>Kernel_clear_do_init</em> annotation to specify whether the annotated function is expected to clear the DO_DEVICE_INITIALIZING bit in the Flags field of the device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>Kernel_IoGetDmaAdapter</em></strong></p></td>
<td align="left"><a href="-kernel-iogetdmaadapter--annotation-for-drivers.md" data-raw-source="[_Kernel_IoGetDmaAdapter_ Annotation](-kernel-iogetdmaadapter--annotation-for-drivers.md)"><em>Kernel_IoGetDmaAdapter</em> Annotation</a></td>
<td align="left"><p>Use the <em>Kernel_IoGetDmaAdapter</em> annotation to direct the code analysis tools to look for misuse of DMA pointers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><em>Interlocked_operand</em></strong></p></td>
<td align="left"><a href="driver-annotations-for-interlocked-operands.md" data-raw-source="[Annotations for interlocked operands](driver-annotations-for-interlocked-operands.md)">Annotations for interlocked operands</a></td>
<td align="left"><p>Use the <em>Interlocked_operand</em> annotation for function parameters to identify them as an interlocked operands. A number of functions take as one of their parameters the address of a variable that should be accessed by using an interlocked processor instruction. These are cache read-through atomic instructions, and if the operands are used incorrectly, very subtle bugs result.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>Dispatch_type</em></strong></p></td>
<td align="left"><a href="declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines" data-raw-source="[Annotations for Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines)">Annotations for Driver Dispatch Routines</a>.</td>
<td align="left"><p>Use the <em>Dispatch_type</em> annotation used when you declare WDM driver dispatch routines. See <a href="declaring-functions-using-function-role-types-for-wdm-drivers.md" data-raw-source="[Declaring Functions Using Function Role Types for WDM Drivers](declaring-functions-using-function-role-types-for-wdm-drivers.md)">Declaring Functions Using Function Role Types for WDM Drivers</a> and <a href="declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines" data-raw-source="[Annotating Driver Dispatch Routines](declaring-functions-using-function-role-types-for-wdm-drivers.md#annotating_driver_dispatch_routines)">Annotating Driver Dispatch Routines</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><em>Flt_CompletionContext_Outptr</em></strong></p></td>
<td align="left"><a href="-flt-completioncontext-outptr--annotation.md" data-raw-source="[_Flt_CompletionContext_Outptr_ Annotation](-flt-completioncontext-outptr--annotation.md)"><em>Flt_CompletionContext_Outptr</em> Annotation</a></td>
<td align="left"><p>Use the <strong><em>Flt_CompletionContext_Outptr</em></strong> annotation when you declare file system minifilter pre-operation callback functions (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109" data-raw-source="[&lt;strong&gt;PFLT_PRE_OPERATION_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551109)"><strong>PFLT_PRE_OPERATION_CALLBACK</strong></a>). Place this annotation on the <em>CompletionContext</em> parameter. This annotation directs the code analysis tool to check that the <em>CompletionContext</em> is correct for the FLT_PREOP_CALLBACK_STATUS return value.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283)

 

 






