---
title: RequestProcessing rule set (KMDF)
description: Use these rules to verify that your driver correctly completes or cancels I/O request packets (IRP).
ms.assetid: 25162982-6A98-4018-82B3-8DD3E0A0A002
---

# RequestProcessing rule set (KMDF)


Use these rules to verify that your driver correctly completes or cancels I/O request packets (IRP).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>ChangeQueueState</strong>](kmdf-changequeuestate.md)</p></td>
<td align="left"><p>The [<strong>ChangeQueueState</strong>](kmdf-changequeuestate.md) rule specifies that the WDF driver doesn't try to change the state of the Queue from concurrent threads or doesn’t call state changing DDIs one after another from within the same thread. Queue state changing callback functions are [<strong>WdfIoQueueStop</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548482), [<strong>WdfIoQueueStopSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548489),[<strong>WdfIoQueuePurge</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548442),[<strong>WdfIoQueuePurgeSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548449), [<strong>WdfIoQueueDrain</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547406), [<strong>WdfIoQueueDrainSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547412), [<strong>WdfIoQueueStopAndPurge</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439289) and [<strong>WdfIoQueueStopAndPurgeSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439293). If these DDIs are called when a Queue state change is already in progress it will cause a computer to crash or to become unresponsive.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CompleteCanceledReq</strong>](kmdf-completecanceledreq.md)</p></td>
<td align="left"><p>The [<strong>CompleteCanceledReq</strong>](kmdf-completecanceledreq.md) rule specifies that if the request has already been canceled, the request is no longer valid, and the driver should not complete it. While the driver unmarks a request that was previously marked cancelable, it must check that the request has not already been canceled. If the driver does not make this check, the driver might complete a request that has been freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DoubleCompletion</strong>](kmdf-doublecompletion.md)</p></td>
<td align="left"><p>The [<strong>DoubleCompletion</strong>](kmdf-doublecompletion.md) rule specifies that drivers must not complete an I/O request twice. The following methods should not be called twice in a row for the same request: [<strong>WdfRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549945), [<strong>WdfRequestCompleteWithInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549948), [<strong>WdfRequestCompleteWithPriorityBoost</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549949).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DoubleCompletionLocal</strong>](kmdf-doublecompletionlocal.md)</p></td>
<td align="left"><p>The [DoubleCompletionLocal](kmdf-doublecompletionlocal.md) rule specifies that drivers must not complete an I/O request twice.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EvtIoStopCancel</strong>](kmdf-evtiostopcancel.md)</p></td>
<td align="left"><p>The [<strong>EvtIoStopCancel</strong>](kmdf-evtiostopcancel.md) rule specifies that within the [<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function, the driver calls one of following methods for I/O requests that are not cancelable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EvtIoStopCompleteOrStopAck</strong>](kmdf-evtiostopcompleteorstopack.md)</p></td>
<td align="left"><p>The [<strong>EvtIoStopCompleteOrStopAck</strong>](kmdf-evtiostopcompleteorstopack.md) rule specifies that within the [<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function the driver calls one of the following methods for each I/O request that is presented by the framework. If this is not done, the driver might block the system from entering another lower power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EvtSurpriseRemoveNoSuspendQueue</strong>](kmdf-evtsurpriseremovenosuspendqueue.md)</p></td>
<td align="left"><p>The [<strong>EvtSurpriseRemoveNoSuspendQueue</strong>](kmdf-evtsurpriseremovenosuspendqueue.md) rule specifies that WDF Drivers shouldn’t drain, stop, or purge the queue from [<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function, instead self-managed I/O callback functions should be used. The <em>EvtDeviceSurpriseRemoval</em> callback function isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FileObjectConfigured</strong>](kmdf-fileobjectconfigured.md)</p></td>
<td align="left"><p>The [<strong>FileObjectConfigured</strong>](kmdf-fileobjectconfigured.md) rule specifies that a call to the [<strong>WdfRequestGetFileObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549963) method is preceded by a call to [<strong>WdfDeviceInitSetFileObjectConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546107).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InternalIoctlReqs</strong>](kmdf-internalioctlreqs.md)</p></td>
<td align="left"><p>The [<strong>InternalIoctlReqs</strong>](kmdf-internalioctlreqs.md) rule specifies that internal IOCTL requests are not passed to inappropriate KMDF request-send device driver interfaces (DDIs).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InvalidReqAccess</strong>](kmdf-invalidreqaccess.md)</p></td>
<td align="left"><p>The [<strong>InvalidReqAccess</strong>](kmdf-invalidreqaccess.md) rule specifies that requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InvalidReqAccessLocal</strong>](kmdf-invalidreqaccesslocal.md)</p></td>
<td align="left"><p>The [<strong>InvalidReqAccessLocal</strong>](kmdf-invalidreqaccesslocal.md) rule specifies that locally created requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IoctlReqs</strong>](kmdf-ioctlreqs.md)</p></td>
<td align="left"><p>The [<strong>IoctlReqs</strong>](kmdf-ioctlreqs.md) rule specifies that IOCTL requests must not be passed to inappropriate KMDF request or send device driver interfaces (DDIs).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MarkCancOnCancReqLocal</strong>](kmdf-markcanconcancreqlocal.md)</p></td>
<td align="left"><p>The [<strong>MarkCancOnCancReqLocal</strong>](kmdf-markcanconcancreqlocal.md) rule specifies that [<strong>WdfRequestMarkCancelable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549983) method cannot be called two consecutive times on the same I/O request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NoIoQueuePurgeSynchronously</strong>](noioqueuepurgesynchronously.md)</p></td>
<td align="left"><p>The [<strong>NoIoQueuePurgeSynchronously</strong>](noioqueuepurgesynchronously.md) rule verifies that WDF drivers don't call the [<strong>WdfIoQueueStopSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548489), [<strong>WdfIoQueueDrainSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547412), [<strong>WdfIoQueueStopAndPurgeSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439293), or [<strong>WdfIoQueuePurgeSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548449) functions from the following EvtIO queue object event callback functions:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>OutputBufferAPI</strong>](kmdf-outputbufferapi.md)</p></td>
<td align="left"><p>The [<strong>OutputBufferAPI</strong>](kmdf-outputbufferapi.md) rule specifies that the correct DDIs for buffer retrieval are used in the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function. Within the <em>EvtIoWrite</em> callback function, the following DDIs cannot be called for buffer retrieval:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ReadReqs</strong>](kmdf-readreqs.md)</p></td>
<td align="left"><p>The [<strong>ReadReqs</strong>](kmdf-readreqs.md) rule specifies that read requests are not passed to inappropriate KMDF methods.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ReqCompletionRoutine</strong>](kmdf-reqcompletionroutine.md)</p></td>
<td align="left"><p>The [<strong>ReqCompletionRoutine</strong>](kmdf-reqcompletionroutine.md) rule specifies that a completion routine must be set before a request is sent to an I/O target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ReqDelete</strong>](kmdf-reqdelete.md)</p></td>
<td align="left"><p>The [<strong>ReqDelete</strong>](kmdf-reqdelete.md) rule specifies that driver-created requests are not passed to <em>WdfRequestCompleteXxx</em> functions. Instead, the request should be deleted upon completion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ReqIsCancOnCancReq</strong>](kmdf-reqiscanconcancreq.md)</p></td>
<td align="left"><p>The [<strong>ReqIsCancOnCancReq</strong>](kmdf-reqiscanconcancreq.md) rule specifies that the [<strong>WdfRequestIsCanceled</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549976) method can only be called on a request that is not marked as cancelable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ReqMarkCancelableSend</strong>](kmdf-reqmarkcancelablesend.md)</p></td>
<td align="left"><p>The [<strong>ReqMarkCancelableSend</strong>](kmdf-reqmarkcancelablesend.md) rule specifies that requests forwarded by the driver are not marked as cancelable by calling [<strong>WdfRequestMarkCancelable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549983).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RequestCompleted</strong>](kmdf-requestcompleted.md)</p></td>
<td align="left"><p>The [<strong>DeferredRequestCompleted</strong>](kmdf-deferredrequestcompleted.md) rule specifies that for a non-filter driver each request presented to the driver's default I/O queue must be completed, unless the request is deferred or forwarded, or if [<strong>WdfRequestStopAcknowledge</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550033) is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RequestFormattedValid</strong>](kmdf-requestformattedvalid.md)</p></td>
<td align="left"><p>The [<strong>RequestFormattedValid</strong>](kmdf-requestformattedvalid.md) rule specifies that the driver formats all requests, except for a WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET request, before it sends them to an I/O target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RequestGetStatusValid</strong>](kmdf-requestgetstatusvalid.md)</p></td>
<td align="left"><p>The [<strong>RequestGetStatusValid</strong>](kmdf-requestgetstatusvalid.md) rule that specifies that [<strong>WdfRequestGetStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549974) should be called for a request in one of the following situations:</p>
<ul>
<li>When [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027) returns failure.</li>
<li>When the request has been sent with WDF_REQUEST_SEND_OPTION_SYNCHRONOUS.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RequestSendAndForgetNoFormatting</strong>](kmdf-requestsendandforgetnoformatting.md)</p></td>
<td align="left"><p>The [<strong>RequestSendAndForgetNoFormatting</strong>](kmdf-requestsendandforgetnoformatting.md) rule verifies that the driver doesn't format a request using the I/O target formatting functions before sending it to an I/O target with the send option WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RequestSendAndForgetNoFormatting2</strong>](kmdf-requestsendandforgetnoformatting2.md)</p></td>
<td align="left"><p>The [<strong>RequestSendAndForgetNoFormatting2</strong>](kmdf-requestsendandforgetnoformatting2.md) rule verifies that the driver doesn't format a request using the I/O target formatting functions before sending it to an I/O target with the send option WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StopAckWithinEvtIoStop</strong>](kmdf-stopackwithinevtiostop.md)</p></td>
<td align="left"><p>The [<strong>StopAckWithinEvtIoStop</strong>](kmdf-stopackwithinevtiostop.md) rule specifies that the [<strong>WdfRequestStopAcknowledge</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550033) function is only called from within [<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WdfIoQueueFindRequestFailed</strong>](kmdf-wdfioqueuefindrequestfailed.md)</p></td>
<td align="left"><p>The [<strong>WdfIoQueueFindRequestFailed</strong>](kmdf-wdfioqueuefindrequestfailed.md) rule specifies that [<strong>WdfIoQueueRetrieveFoundRequest</strong>](kmdf-wdfioqueueretrievefoundrequest.md) or [<strong>WdfObjectDereference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548739) should only be called after <strong>WdfIoQueueFindRequestFailed</strong> returns STATUS_SUCCESS.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WdfIoQueueRetrieveFoundRequest</strong>](kmdf-wdfioqueueretrievefoundrequest.md)</p></td>
<td align="left"><p>The [<strong>WdfIoQueueRetrieveFoundRequest</strong>](kmdf-wdfioqueueretrievefoundrequest.md) rule specifies that [<strong>WdfIoQueueRetrieveFoundRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548456) method is called only after [<strong>WdfIoQueueFindRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547415) is called and returned STATUS_SUCCESS and no [<strong>WdfObjectDereference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548739) is called on the same request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WdfIoQueueRetrieveNextRequest</strong>](kmdf-wdfioqueueretrievenextrequest.md)</p></td>
<td align="left"><p>The [<strong>WdfIoQueueRetrieveNextRequest</strong>](kmdf-wdfioqueueretrievenextrequest.md) rule specifies that [<strong>WdfIoQueueRetrieveNextRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548462) is not called after [<strong>WdfIoQueueFindRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547415) is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WriteReqs</strong>](kmdf-writereqs.md)</p></td>
<td align="left"><p>The [<strong>WriteReqs</strong>](kmdf-writereqs.md) rule specifies that a write request is not passed to inappropriate KMDF methods.</p></td>
</tr>
</tbody>
</table>

 

**To select the RequestProcessing rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **RequestProcessing**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **RequestProcessing.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:RequestProcessing.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20RequestProcessing%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




