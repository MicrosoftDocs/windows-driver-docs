---
title: Guidelines for Porting Legacy Filter Drivers
author: windows-driver-content
description: Guidelines for Porting Legacy Filter Drivers
ms.assetid: 6dd9637e-e9b3-4434-996c-c3f8ce6584c4
keywords: ["filter manager WDK file system minifilter , porting legacy drivers", "porting legacy filter drivers", "legacy filter drivers WDK file system minifilter"]
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
<p>See [Returning FLT_PREOP_SUCCESS_NO_CALLBACK](returning-flt-preop-success-no-callback.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Pass-through operation with a completion routine</p></td>
<td align="left"><p>Return FLT_PREOP_SUCCESS_WITH_CALLBACK from the preoperation callback routine.</p>
<p>See [Returning FLT_PREOP_SUCCESS_WITH_CALLBACK](returning-flt-preop-success-with-callback.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Pend operation in the preoperation callback routine</p></td>
<td align="left"><p>Call [<strong>FltLockUserBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543371) as needed to ensure that any user buffers are properly locked so that they can be accessed in a worker thread.</p>
<p>Queue the work to a worker thread by calling support routines such as [<strong>FltAllocateDeferredIoWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541720) and [<strong>FltQueueDeferredIoWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543449).</p>
<p>Return FLT_PREOP_PENDING from the preoperation callback routine.</p>
<p>When ready to return the I/O operation to the filter manager, call [<strong>FltCompletePendedPreOperation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541913).</p>
<p>See [Pending an I/O Operation in a Preoperation Callback Routine](pending-an-i-o-operation-in-a-preoperation-callback-routine.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Pend operation in the postoperation callback routine</p></td>
<td align="left"><p>In the preoperation callback routine, call [<strong>FltLockUserBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543371) to ensure that user buffers are properly locked so that they can be accessed in a worker thread.</p>
<p>Queue the work to a worker thread by calling support routines such as [<strong>FltAllocateGenericWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541749) and [<strong>FltQueueGenericWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543452).</p>
<p>Return FLT_POSTOP_MORE_PROCESSING_REQUIRED from the postoperation callback routine.</p>
<p>When ready to return the I/O operation to the filter manager, call [<strong>FltCompletePendedPostOperation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541897).</p>
<p>See [Pending an I/O Operation in a Postoperation Callback Routine](pending-an-i-o-operation-in-a-postoperation-callback-routine.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Synchronize the operation</p></td>
<td align="left"><p>Return FLT_PREOP_SYNCHRONIZE from the preoperation callback routine.</p>
<p>See [Returning FLT_PREOP_SYNCHRONIZE](returning-flt-preop-synchronize.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Complete the operation in the preoperation callback routine</p></td>
<td align="left"><p>Set the final operation status and information in the <strong>IoStatus</strong> member of the [<strong>FLT_CALLBACK_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure for the operation.</p>
<p>Return FLT_PREOP_COMPLETE from the preoperation callback routine.</p>
<p>See [Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Complete the operation after it has been pended in the preoperation callback routine</p></td>
<td align="left"><p>Set the final operation status and information in the <strong>IoStatus</strong> member of the [<strong>FLT_CALLBACK_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure for the operation.</p>
<p>Call [<strong>FltCompletePendedPreOperation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541913) from the worker thread processing the I/O operation, passing FLT_PREOP_COMPLETE as the <em>CallbackStatus</em> parameter.</p>
<p>See [Completing an I/O Operation in a Preoperation Callback Routine](completing-an-i-o-operation-in-a-preoperation-callback-routine.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Do all completion work in the completion routine</p></td>
<td align="left"><p>Return FLT_POSTOP_FINISHED_PROCESSING from the postoperation callback routine.</p>
<p>See [Writing Postoperation Callback Routines](writing-postoperation-callback-routines.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Do completion work at safe IRQL</p></td>
<td align="left"><p>Call [<strong>FltDoCompletionProcessingWhenSafe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542047) from the postoperation callback routine.</p>
<p>See [Ensuring that Completion Processing is Performed at Safe IRQL](ensuring-that-completion-processing-is-performed-at-safe-irql.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Signal an event from the completion routine</p></td>
<td align="left"><p>Return FLT_PREOP_SYNCHRONIZE from the preoperation callback routine for this operation.</p>
<p>The filter manager calls the postoperation callback routine in the same thread context as the preoperation callback routine, at IRQL &lt;= APC_LEVEL.</p>
<p>See [Returning FLT_PREOP_SYNCHRONIZE](returning-flt-preop-synchronize.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Fail a successful create operation</p></td>
<td align="left"><p>Call [<strong>FltCancelFileOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541784) from the postoperation callback routine for the create operation.</p>
<p>Set an appropriate error NTSTATUS value in the <strong>IoStatus</strong> member of the [<strong>FLT_CALLBACK_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure for the operation.</p>
<p>Return FLT_POSTOP_FINISHED_PROCESSING.</p>
<p>See [Failing an I/O Operation in a Postoperation Callback Routine](failing-an-i-o-operation-in-a-postoperation-callback-routine.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Disallow I/O through the fast I/O path for an I/O operation</p></td>
<td align="left"><p>Return FLT_STATUS_DISALLOW_FAST_IO from the preoperation callback routine for the operation.</p>
<p>See [Disallowing a Fast I/O Operation in a Preoperation Callback Routine](disallowing-a-fast-i-o-operation-in-a-preoperation-callback-routine.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Modify the parameters for an I/O operation</p></td>
<td align="left"><p>Set the modified parameter values in the <strong>Iopb</strong> member of the [<strong>FLT_CALLBACK_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure for the operation.</p>
<p>Mark the FLT_CALLBACK_DATA structure as dirty by calling [<strong>FltSetCallbackDataDirty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544383), except when you have modified the contents of the <strong>IoStatus</strong> member of the FLT_CALLBACK_DATA structure.</p>
<p>See [Modifying the Parameters for an I/O Operation](modifying-the-parameters-for-an-i-o-operation.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Lock the user buffer for the operation</p></td>
<td align="left"><p>Use the techniques and guidelines described in [Accessing the User Buffers for an I/O Operation](accessing-the-user-buffers-for-an-i-o-operation.md).</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Guidelines%20for%20Porting%20Legacy%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


