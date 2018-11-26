---
title: Guidelines for Porting Legacy Filter Drivers
description: Guidelines for Porting Legacy Filter Drivers
ms.assetid: 6dd9637e-e9b3-4434-996c-c3f8ce6584c4
keywords:
- filter manager WDK file system minifilter , porting legacy drivers
- porting legacy filter drivers
- legacy filter drivers WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guidelines for Porting Legacy Filter Drivers


## <span id="ddk_when_the_filterunloadcallback_routine_is_called_if"></span><span id="DDK_WHEN_THE_FILTERUNLOADCALLBACK_ROUTINE_IS_CALLED_IF"></span>


Developers are encouraged to port legacy filter drivers to the filter manager model to obtain better functionality for their filter drivers and improve system reliability. Experienced developers should find it relatively easy to port a legacy filter driver to a minifilter driver. Filter driver developers at Microsoft recommend the following approach:

-   Start with a reliable regression test suite to verify behavior between the legacy filter driver and the ported minifilter driver.

-   Create a minifilter driver shell and systematically move functionality from the legacy filter driver to the minifilter driver. For example, get attachment working and then port one operation at a time, testing after each operation.

-   Change user-mode/kernel-mode communication last, so you can use existing tools to test the minifilter driver.

-   Compile with PREfast and test with the Filter Verifier I/O verification option in Driver Verifier enabled.

During the porting process, you should review all legacy filter driver code to take full advantage of filter manager capabilities. In particular, keep the following in mind:

-   IRP-based I/O and fast I/O operations can come through the same operation when appropriate, which helps reduce duplication of code.

-   When registering for operations, a minifilter driver can explicitly choose to ignore all paging I/O and cached I/O, which eliminates the need for code to check these.

-   Instance notifications greatly simplify attach/detach logic.

-   Register only for operations that your minifilter driver must handle; you can ignore everything else.

-   Take advantage of filter manager context and name management support.

-   Take advantage of filter manager support for issuing non-recursive I/O.

-   Unlike legacy filter drivers, minifilter drivers cannot rely on local variables to maintain context from preoperation processing to postoperation processing. Consider allocating a lookaside list to store operation state.

-   Be sure to release references when finished with a name or context.

-   Completion ports in user mode add a powerful technique for building queues. You will probably need only a single connection to a single named port.

The following table lists common operations in a legacy filter driver and how they map to the filter manager model.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Legacy filter driver model</th>
<th align="left">Filter manager model</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pass-through operation with no completion routine</p></td>
<td align="left"><p>If your minifilter driver never does work for this type of I/O operation, do not register a preoperation or postoperation callback routine for this operation.</p>
<p>Otherwise, return FLT_PREOP_SUCCESS_NO_CALLBACK from the preoperation callback routine registered for this operation.</p>
<p>See <a href="returning-flt-preop-success-no-callback.md" data-raw-source="[Returning FLT_PREOP_SUCCESS_NO_CALLBACK](returning-flt-preop-success-no-callback.md)">Returning FLT_PREOP_SUCCESS_NO_CALLBACK</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Pass-through operation with a completion routine</p></td>
<td align="left"><p>Return FLT_PREOP_SUCCESS_WITH_CALLBACK from the preoperation callback routine.</p>
<p>See <a href="returning-flt-preop-success-with-callback.md" data-raw-source="[Returning FLT_PREOP_SUCCESS_WITH_CALLBACK](returning-flt-preop-success-with-callback.md)">Returning FLT_PREOP_SUCCESS_WITH_CALLBACK</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Pend operation in the preoperation callback routine</p></td>
<td align="left"><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543371" data-raw-source="[&lt;strong&gt;FltLockUserBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543371)"><strong>FltLockUserBuffer</strong></a> as needed to ensure that any user buffers are properly locked so that they can be accessed in a worker thread.</p>
<p>Queue the work to a worker thread by calling support routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff541720" data-raw-source="[&lt;strong&gt;FltAllocateDeferredIoWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541720)"><strong>FltAllocateDeferredIoWorkItem</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543449" data-raw-source="[&lt;strong&gt;FltQueueDeferredIoWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543449)"><strong>FltQueueDeferredIoWorkItem</strong></a>.</p>
<p>Return FLT_PREOP_PENDING from the preoperation callback routine.</p>
<p>When ready to return the I/O operation to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541913" data-raw-source="[&lt;strong&gt;FltCompletePendedPreOperation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541913)"><strong>FltCompletePendedPreOperation</strong></a>.</p>
<p>See <a href="pending-an-i-o-operation-in-a-preoperation-callback-routine.md" data-raw-source="[Pending an I/O Operation in a Preoperation Callback Routine](pending-an-i-o-operation-in-a-preoperation-callback-routine.md)">Pending an I/O Operation in a Preoperation Callback Routine</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Pend operation in the postoperation callback routine</p></td>
<td align="left"><p>In the preoperation callback routine, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543371" data-raw-source="[&lt;strong&gt;FltLockUserBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543371)"><strong>FltLockUserBuffer</strong></a> to ensure that user buffers are properly locked so that they can be accessed in a worker thread.</p>
<p>Queue the work to a worker thread by calling support routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff541749" data-raw-source="[&lt;strong&gt;FltAllocateGenericWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541749)"><strong>FltAllocateGenericWorkItem</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452" data-raw-source="[&lt;strong&gt;FltQueueGenericWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543452)"><strong>FltQueueGenericWorkItem</strong></a>.</p>
<p>Return FLT_POSTOP_MORE_PROCESSING_REQUIRED from the postoperation callback routine.</p>
<p>When ready to return the I/O operation to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541897" data-raw-source="[&lt;strong&gt;FltCompletePendedPostOperation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541897)"><strong>FltCompletePendedPostOperation</strong></a>.</p>
<p>See <a href="pending-an-i-o-operation-in-a-postoperation-callback-routine.md" data-raw-source="[Pending an I/O Operation in a Postoperation Callback Routine](pending-an-i-o-operation-in-a-postoperation-callback-routine.md)">Pending an I/O Operation in a Postoperation Callback Routine</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Synchronize the operation</p></td>
<td align="left"><p>Return FLT_PREOP_SYNCHRONIZE from the preoperation callback routine.</p>
<p>See <a href="returning-flt-preop-synchronize.md" data-raw-source="[Returning FLT_PREOP_SYNCHRONIZE](returning-flt-preop-synchronize.md)">Returning FLT_PREOP_SYNCHRONIZE</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Complete the operation in the preoperation callback routine</p></td>
<td align="left"><p>Set the final operation status and information in the <strong>IoStatus</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620" data-raw-source="[&lt;strong&gt;FLT_CALLBACK_DATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544620)"><strong>FLT_CALLBACK_DATA</strong></a> structure for the operation.</p>
<p>Return FLT_PREOP_COMPLETE from the preoperation callback routine.</p>
<p>See <a href="completing-an-i-o-operation-in-a-preoperation-callback-routine.md" data-raw-source="[Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md)">Completing an I/O Operation in a Preoperation Callback Routine</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Complete the operation after it has been pended in the preoperation callback routine</p></td>
<td align="left"><p>Set the final operation status and information in the <strong>IoStatus</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620" data-raw-source="[&lt;strong&gt;FLT_CALLBACK_DATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544620)"><strong>FLT_CALLBACK_DATA</strong></a> structure for the operation.</p>
<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541913" data-raw-source="[&lt;strong&gt;FltCompletePendedPreOperation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541913)"><strong>FltCompletePendedPreOperation</strong></a> from the worker thread processing the I/O operation, passing FLT_PREOP_COMPLETE as the <em>CallbackStatus</em> parameter.</p>
<p>See <a href="completing-an-i-o-operation-in-a-preoperation-callback-routine.md" data-raw-source="[Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md)">Completing an I/O Operation in a Preoperation Callback Routine</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Do all completion work in the completion routine</p></td>
<td align="left"><p>Return FLT_POSTOP_FINISHED_PROCESSING from the postoperation callback routine.</p>
<p>See <a href="writing-postoperation-callback-routines.md" data-raw-source="[Writing Postoperation Callback Routines](writing-postoperation-callback-routines.md)">Writing Postoperation Callback Routines</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Do completion work at safe IRQL</p></td>
<td align="left"><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542047" data-raw-source="[&lt;strong&gt;FltDoCompletionProcessingWhenSafe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542047)"><strong>FltDoCompletionProcessingWhenSafe</strong></a> from the postoperation callback routine.</p>
<p>See <a href="ensuring-that-completion-processing-is-performed-at-safe-irql.md" data-raw-source="[Ensuring that Completion Processing is Performed at Safe IRQL](ensuring-that-completion-processing-is-performed-at-safe-irql.md)">Ensuring that Completion Processing is Performed at Safe IRQL</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Signal an event from the completion routine</p></td>
<td align="left"><p>Return FLT_PREOP_SYNCHRONIZE from the preoperation callback routine for this operation.</p>
<p>The filter manager calls the postoperation callback routine in the same thread context as the preoperation callback routine, at IRQL &lt;= APC_LEVEL.</p>
<p>See <a href="returning-flt-preop-synchronize.md" data-raw-source="[Returning FLT_PREOP_SYNCHRONIZE](returning-flt-preop-synchronize.md)">Returning FLT_PREOP_SYNCHRONIZE</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Fail a successful create operation</p></td>
<td align="left"><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541784" data-raw-source="[&lt;strong&gt;FltCancelFileOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541784)"><strong>FltCancelFileOpen</strong></a> from the postoperation callback routine for the create operation.</p>
<p>Set an appropriate error NTSTATUS value in the <strong>IoStatus</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620" data-raw-source="[&lt;strong&gt;FLT_CALLBACK_DATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544620)"><strong>FLT_CALLBACK_DATA</strong></a> structure for the operation.</p>
<p>Return FLT_POSTOP_FINISHED_PROCESSING.</p>
<p>See <a href="failing-an-i-o-operation-in-a-postoperation-callback-routine.md" data-raw-source="[Failing an I/O Operation in a Postoperation Callback Routine](failing-an-i-o-operation-in-a-postoperation-callback-routine.md)">Failing an I/O Operation in a Postoperation Callback Routine</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Disallow I/O through the fast I/O path for an I/O operation</p></td>
<td align="left"><p>Return FLT_STATUS_DISALLOW_FAST_IO from the preoperation callback routine for the operation.</p>
<p>See <a href="disallowing-a-fast-i-o-operation-in-a-preoperation-callback-routine.md" data-raw-source="[Disallowing a Fast I/O Operation in a Preoperation Callback Routine](disallowing-a-fast-i-o-operation-in-a-preoperation-callback-routine.md)">Disallowing a Fast I/O Operation in a Preoperation Callback Routine</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Modify the parameters for an I/O operation</p></td>
<td align="left"><p>Set the modified parameter values in the <strong>Iopb</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620" data-raw-source="[&lt;strong&gt;FLT_CALLBACK_DATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544620)"><strong>FLT_CALLBACK_DATA</strong></a> structure for the operation.</p>
<p>Mark the FLT_CALLBACK_DATA structure as dirty by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383" data-raw-source="[&lt;strong&gt;FltSetCallbackDataDirty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544383)"><strong>FltSetCallbackDataDirty</strong></a>, except when you have modified the contents of the <strong>IoStatus</strong> member of the FLT_CALLBACK_DATA structure.</p>
<p>See <a href="modifying-the-parameters-for-an-i-o-operation.md" data-raw-source="[Modifying the Parameters for an I/O Operation](modifying-the-parameters-for-an-i-o-operation.md)">Modifying the Parameters for an I/O Operation</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Lock the user buffer for the operation</p></td>
<td align="left"><p>Use the techniques and guidelines described in <a href="accessing-the-user-buffers-for-an-i-o-operation.md" data-raw-source="[Accessing the User Buffers for an I/O Operation](accessing-the-user-buffers-for-an-i-o-operation.md)">Accessing the User Buffers for an I/O Operation</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 




