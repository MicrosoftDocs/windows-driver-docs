---
title: RequestProcessing Rule Set (KMDF)
description: Use these rules to verify that your driver correctly completes or cancels I/O request packets (IRP).
ms.date: 05/21/2018
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
<td align="left"><p><a href="kmdf-changequeuestate.md" data-raw-source="[&lt;strong&gt;ChangeQueueState&lt;/strong&gt;](kmdf-changequeuestate.md)"><strong>ChangeQueueState</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-changequeuestate.md" data-raw-source="[&lt;strong&gt;ChangeQueueState&lt;/strong&gt;](kmdf-changequeuestate.md)"><strong>ChangeQueueState</strong></a> rule specifies that the WDF driver doesn't try to change the state of the Queue from concurrent threads or doesn’t call state changing DDIs one after another from within the same thread. Queue state changing callback functions are <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop" data-raw-source="[&lt;strong&gt;WdfIoQueueStop&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop)"><strong>WdfIoQueueStop</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueStopSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously)"><strong>WdfIoQueueStopSynchronously</strong></a>,<a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurge" data-raw-source="[&lt;strong&gt;WdfIoQueuePurge&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurge)"><strong>WdfIoQueuePurge</strong></a>,<a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueuePurgeSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously)"><strong>WdfIoQueuePurgeSynchronously</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain" data-raw-source="[&lt;strong&gt;WdfIoQueueDrain&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain)"><strong>WdfIoQueueDrain</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueDrainSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously)"><strong>WdfIoQueueDrainSynchronously</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurge" data-raw-source="[&lt;strong&gt;WdfIoQueueStopAndPurge&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurge)"><strong>WdfIoQueueStopAndPurge</strong></a> and <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueStopAndPurgeSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously)"><strong>WdfIoQueueStopAndPurgeSynchronously</strong></a>. If these DDIs are called when a Queue state change is already in progress it will cause a computer to crash or to become unresponsive.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-completecanceledreq.md" data-raw-source="[&lt;strong&gt;CompleteCanceledReq&lt;/strong&gt;](kmdf-completecanceledreq.md)"><strong>CompleteCanceledReq</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-completecanceledreq.md" data-raw-source="[&lt;strong&gt;CompleteCanceledReq&lt;/strong&gt;](kmdf-completecanceledreq.md)"><strong>CompleteCanceledReq</strong></a> rule specifies that if the request has already been canceled, the request is no longer valid, and the driver should not complete it. While the driver unmarks a request that was previously marked cancelable, it must check that the request has not already been canceled. If the driver does not make this check, the driver might complete a request that has been freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-doublecompletion.md" data-raw-source="[&lt;strong&gt;DoubleCompletion&lt;/strong&gt;](kmdf-doublecompletion.md)"><strong>DoubleCompletion</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-doublecompletion.md" data-raw-source="[&lt;strong&gt;DoubleCompletion&lt;/strong&gt;](kmdf-doublecompletion.md)"><strong>DoubleCompletion</strong></a> rule specifies that drivers must not complete an I/O request twice. The following methods should not be called twice in a row for the same request: <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete" data-raw-source="[&lt;strong&gt;WdfRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)"><strong>WdfRequestComplete</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation" data-raw-source="[&lt;strong&gt;WdfRequestCompleteWithInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation)"><strong>WdfRequestCompleteWithInformation</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost" data-raw-source="[&lt;strong&gt;WdfRequestCompleteWithPriorityBoost&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost)"><strong>WdfRequestCompleteWithPriorityBoost</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-doublecompletionlocal.md" data-raw-source="[&lt;strong&gt;DoubleCompletionLocal&lt;/strong&gt;](kmdf-doublecompletionlocal.md)"><strong>DoubleCompletionLocal</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-doublecompletionlocal.md" data-raw-source="[DoubleCompletionLocal](kmdf-doublecompletionlocal.md)">DoubleCompletionLocal</a> rule specifies that drivers must not complete an I/O request twice.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-evtiostopcancel.md" data-raw-source="[&lt;strong&gt;EvtIoStopCancel&lt;/strong&gt;](kmdf-evtiostopcancel.md)"><strong>EvtIoStopCancel</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtiostopcancel.md" data-raw-source="[&lt;strong&gt;EvtIoStopCancel&lt;/strong&gt;](kmdf-evtiostopcancel.md)"><strong>EvtIoStopCancel</strong></a> rule specifies that within the <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> callback function, the driver calls one of following methods for I/O requests that are not cancelable.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-evtiostopcompleteorstopack.md" data-raw-source="[&lt;strong&gt;EvtIoStopCompleteOrStopAck&lt;/strong&gt;](kmdf-evtiostopcompleteorstopack.md)"><strong>EvtIoStopCompleteOrStopAck</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtiostopcompleteorstopack.md" data-raw-source="[&lt;strong&gt;EvtIoStopCompleteOrStopAck&lt;/strong&gt;](kmdf-evtiostopcompleteorstopack.md)"><strong>EvtIoStopCompleteOrStopAck</strong></a> rule specifies that within the <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> callback function the driver calls one of the following methods for each I/O request that is presented by the framework. If this is not done, the driver might block the system from entering another lower power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-evtsurpriseremovenosuspendqueue.md" data-raw-source="[&lt;strong&gt;EvtSurpriseRemoveNoSuspendQueue&lt;/strong&gt;](kmdf-evtsurpriseremovenosuspendqueue.md)"><strong>EvtSurpriseRemoveNoSuspendQueue</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtsurpriseremovenosuspendqueue.md" data-raw-source="[&lt;strong&gt;EvtSurpriseRemoveNoSuspendQueue&lt;/strong&gt;](kmdf-evtsurpriseremovenosuspendqueue.md)"><strong>EvtSurpriseRemoveNoSuspendQueue</strong></a> rule specifies that WDF Drivers shouldn’t drain, stop, or purge the queue from <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal)"><em>EvtDeviceSurpriseRemoval</em></a> callback function, instead self-managed I/O callback functions should be used. The <em>EvtDeviceSurpriseRemoval</em> callback function isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-fileobjectconfigured.md" data-raw-source="[&lt;strong&gt;FileObjectConfigured&lt;/strong&gt;](kmdf-fileobjectconfigured.md)"><strong>FileObjectConfigured</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-fileobjectconfigured.md" data-raw-source="[&lt;strong&gt;FileObjectConfigured&lt;/strong&gt;](kmdf-fileobjectconfigured.md)"><strong>FileObjectConfigured</strong></a> rule specifies that a call to the <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetfileobject" data-raw-source="[&lt;strong&gt;WdfRequestGetFileObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetfileobject)"><strong>WdfRequestGetFileObject</strong></a> method is preceded by a call to <a href="/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig" data-raw-source="[&lt;strong&gt;WdfDeviceInitSetFileObjectConfig&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig)"><strong>WdfDeviceInitSetFileObjectConfig</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-internalioctlreqs.md" data-raw-source="[&lt;strong&gt;InternalIoctlReqs&lt;/strong&gt;](kmdf-internalioctlreqs.md)"><strong>InternalIoctlReqs</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-internalioctlreqs.md" data-raw-source="[&lt;strong&gt;InternalIoctlReqs&lt;/strong&gt;](kmdf-internalioctlreqs.md)"><strong>InternalIoctlReqs</strong></a> rule specifies that internal IOCTL requests are not passed to inappropriate KMDF request-send device driver interfaces (DDIs).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-invalidreqaccess.md" data-raw-source="[&lt;strong&gt;InvalidReqAccess&lt;/strong&gt;](kmdf-invalidreqaccess.md)"><strong>InvalidReqAccess</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-invalidreqaccess.md" data-raw-source="[&lt;strong&gt;InvalidReqAccess&lt;/strong&gt;](kmdf-invalidreqaccess.md)"><strong>InvalidReqAccess</strong></a> rule specifies that requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-invalidreqaccesslocal.md" data-raw-source="[&lt;strong&gt;InvalidReqAccessLocal&lt;/strong&gt;](kmdf-invalidreqaccesslocal.md)"><strong>InvalidReqAccessLocal</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-invalidreqaccesslocal.md" data-raw-source="[&lt;strong&gt;InvalidReqAccessLocal&lt;/strong&gt;](kmdf-invalidreqaccesslocal.md)"><strong>InvalidReqAccessLocal</strong></a> rule specifies that locally created requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-ioctlreqs.md" data-raw-source="[&lt;strong&gt;IoctlReqs&lt;/strong&gt;](kmdf-ioctlreqs.md)"><strong>IoctlReqs</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-ioctlreqs.md" data-raw-source="[&lt;strong&gt;IoctlReqs&lt;/strong&gt;](kmdf-ioctlreqs.md)"><strong>IoctlReqs</strong></a> rule specifies that IOCTL requests must not be passed to inappropriate KMDF request or send device driver interfaces (DDIs).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-markcanconcancreqlocal.md" data-raw-source="[&lt;strong&gt;MarkCancOnCancReqLocal&lt;/strong&gt;](kmdf-markcanconcancreqlocal.md)"><strong>MarkCancOnCancReqLocal</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-markcanconcancreqlocal.md" data-raw-source="[&lt;strong&gt;MarkCancOnCancReqLocal&lt;/strong&gt;](kmdf-markcanconcancreqlocal.md)"><strong>MarkCancOnCancReqLocal</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable" data-raw-source="[&lt;strong&gt;WdfRequestMarkCancelable&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable)"><strong>WdfRequestMarkCancelable</strong></a> method cannot be called two consecutive times on the same I/O request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="noioqueuepurgesynchronously.md" data-raw-source="[&lt;strong&gt;NoIoQueuePurgeSynchronously&lt;/strong&gt;](noioqueuepurgesynchronously.md)"><strong>NoIoQueuePurgeSynchronously</strong></a></p></td>
<td align="left"><p>The <a href="noioqueuepurgesynchronously.md" data-raw-source="[&lt;strong&gt;NoIoQueuePurgeSynchronously&lt;/strong&gt;](noioqueuepurgesynchronously.md)"><strong>NoIoQueuePurgeSynchronously</strong></a> rule verifies that WDF drivers don't call the <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueStopSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously)"><strong>WdfIoQueueStopSynchronously</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueDrainSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously)"><strong>WdfIoQueueDrainSynchronously</strong></a>, <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueueStopAndPurgeSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously)"><strong>WdfIoQueueStopAndPurgeSynchronously</strong></a>, or <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously" data-raw-source="[&lt;strong&gt;WdfIoQueuePurgeSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously)"><strong>WdfIoQueuePurgeSynchronously</strong></a> functions from the following EvtIO queue object event callback functions:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-outputbufferapi.md" data-raw-source="[&lt;strong&gt;OutputBufferAPI&lt;/strong&gt;](kmdf-outputbufferapi.md)"><strong>OutputBufferAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-outputbufferapi.md" data-raw-source="[&lt;strong&gt;OutputBufferAPI&lt;/strong&gt;](kmdf-outputbufferapi.md)"><strong>OutputBufferAPI</strong></a> rule specifies that the correct DDIs for buffer retrieval are used in the <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_write" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_write)"><em>EvtIoWrite</em></a> callback function. Within the <em>EvtIoWrite</em> callback function, the following DDIs cannot be called for buffer retrieval:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-readreqs.md" data-raw-source="[&lt;strong&gt;ReadReqs&lt;/strong&gt;](kmdf-readreqs.md)"><strong>ReadReqs</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-readreqs.md" data-raw-source="[&lt;strong&gt;ReadReqs&lt;/strong&gt;](kmdf-readreqs.md)"><strong>ReadReqs</strong></a> rule specifies that read requests are not passed to inappropriate KMDF methods.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-reqcompletionroutine.md" data-raw-source="[&lt;strong&gt;ReqCompletionRoutine&lt;/strong&gt;](kmdf-reqcompletionroutine.md)"><strong>ReqCompletionRoutine</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqcompletionroutine.md" data-raw-source="[&lt;strong&gt;ReqCompletionRoutine&lt;/strong&gt;](kmdf-reqcompletionroutine.md)"><strong>ReqCompletionRoutine</strong></a> rule specifies that a completion routine must be set before a request is sent to an I/O target.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-reqdelete.md" data-raw-source="[&lt;strong&gt;ReqDelete&lt;/strong&gt;](kmdf-reqdelete.md)"><strong>ReqDelete</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqdelete.md" data-raw-source="[&lt;strong&gt;ReqDelete&lt;/strong&gt;](kmdf-reqdelete.md)"><strong>ReqDelete</strong></a> rule specifies that driver-created requests are not passed to <em>WdfRequestCompleteXxx</em> functions. Instead, the request should be deleted upon completion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-reqiscanconcancreq.md" data-raw-source="[&lt;strong&gt;ReqIsCancOnCancReq&lt;/strong&gt;](kmdf-reqiscanconcancreq.md)"><strong>ReqIsCancOnCancReq</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqiscanconcancreq.md" data-raw-source="[&lt;strong&gt;ReqIsCancOnCancReq&lt;/strong&gt;](kmdf-reqiscanconcancreq.md)"><strong>ReqIsCancOnCancReq</strong></a> rule specifies that the <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled" data-raw-source="[&lt;strong&gt;WdfRequestIsCanceled&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled)"><strong>WdfRequestIsCanceled</strong></a> method can only be called on a request that is not marked as cancelable.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-reqmarkcancelablesend.md" data-raw-source="[&lt;strong&gt;ReqMarkCancelableSend&lt;/strong&gt;](kmdf-reqmarkcancelablesend.md)"><strong>ReqMarkCancelableSend</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqmarkcancelablesend.md" data-raw-source="[&lt;strong&gt;ReqMarkCancelableSend&lt;/strong&gt;](kmdf-reqmarkcancelablesend.md)"><strong>ReqMarkCancelableSend</strong></a> rule specifies that requests forwarded by the driver are not marked as cancelable by calling <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable" data-raw-source="[&lt;strong&gt;WdfRequestMarkCancelable&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable)"><strong>WdfRequestMarkCancelable</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-requestcompleted.md" data-raw-source="[&lt;strong&gt;RequestCompleted&lt;/strong&gt;](kmdf-requestcompleted.md)"><strong>RequestCompleted</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-deferredrequestcompleted.md" data-raw-source="[&lt;strong&gt;DeferredRequestCompleted&lt;/strong&gt;](kmdf-deferredrequestcompleted.md)"><strong>DeferredRequestCompleted</strong></a> rule specifies that for a non-filter driver each request presented to the driver's default I/O queue must be completed, unless the request is deferred or forwarded, or if <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge" data-raw-source="[&lt;strong&gt;WdfRequestStopAcknowledge&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge)"><strong>WdfRequestStopAcknowledge</strong></a> is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-requestformattedvalid.md" data-raw-source="[&lt;strong&gt;RequestFormattedValid&lt;/strong&gt;](kmdf-requestformattedvalid.md)"><strong>RequestFormattedValid</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-requestformattedvalid.md" data-raw-source="[&lt;strong&gt;RequestFormattedValid&lt;/strong&gt;](kmdf-requestformattedvalid.md)"><strong>RequestFormattedValid</strong></a> rule specifies that the driver formats all requests, except for a WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET request, before it sends them to an I/O target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-requestgetstatusvalid.md" data-raw-source="[&lt;strong&gt;RequestGetStatusValid&lt;/strong&gt;](kmdf-requestgetstatusvalid.md)"><strong>RequestGetStatusValid</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-requestgetstatusvalid.md" data-raw-source="[&lt;strong&gt;RequestGetStatusValid&lt;/strong&gt;](kmdf-requestgetstatusvalid.md)"><strong>RequestGetStatusValid</strong></a> rule that specifies that <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetstatus" data-raw-source="[&lt;strong&gt;WdfRequestGetStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetstatus)"><strong>WdfRequestGetStatus</strong></a> should be called for a request in one of the following situations:</p>
<ul>
<li>When <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)"><strong>WdfRequestSend</strong></a> returns failure.</li>
<li>When the request has been sent with WDF_REQUEST_SEND_OPTION_SYNCHRONOUS.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-requestsendandforgetnoformatting.md" data-raw-source="[&lt;strong&gt;RequestSendAndForgetNoFormatting&lt;/strong&gt;](kmdf-requestsendandforgetnoformatting.md)"><strong>RequestSendAndForgetNoFormatting</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-requestsendandforgetnoformatting.md" data-raw-source="[&lt;strong&gt;RequestSendAndForgetNoFormatting&lt;/strong&gt;](kmdf-requestsendandforgetnoformatting.md)"><strong>RequestSendAndForgetNoFormatting</strong></a> rule verifies that the driver doesn't format a request using the I/O target formatting functions before sending it to an I/O target with the send option WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-requestsendandforgetnoformatting2.md" data-raw-source="[&lt;strong&gt;RequestSendAndForgetNoFormatting2&lt;/strong&gt;](kmdf-requestsendandforgetnoformatting2.md)"><strong>RequestSendAndForgetNoFormatting2</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-requestsendandforgetnoformatting2.md" data-raw-source="[&lt;strong&gt;RequestSendAndForgetNoFormatting2&lt;/strong&gt;](kmdf-requestsendandforgetnoformatting2.md)"><strong>RequestSendAndForgetNoFormatting2</strong></a> rule verifies that the driver doesn't format a request using the I/O target formatting functions before sending it to an I/O target with the send option WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-stopackwithinevtiostop.md" data-raw-source="[&lt;strong&gt;StopAckWithinEvtIoStop&lt;/strong&gt;](kmdf-stopackwithinevtiostop.md)"><strong>StopAckWithinEvtIoStop</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-stopackwithinevtiostop.md" data-raw-source="[&lt;strong&gt;StopAckWithinEvtIoStop&lt;/strong&gt;](kmdf-stopackwithinevtiostop.md)"><strong>StopAckWithinEvtIoStop</strong></a> rule specifies that the <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge" data-raw-source="[&lt;strong&gt;WdfRequestStopAcknowledge&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge)"><strong>WdfRequestStopAcknowledge</strong></a> function is only called from within <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-wdfioqueuefindrequestfailed.md" data-raw-source="[&lt;strong&gt;WdfIoQueueFindRequestFailed&lt;/strong&gt;](kmdf-wdfioqueuefindrequestfailed.md)"><strong>WdfIoQueueFindRequestFailed</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfioqueuefindrequestfailed.md" data-raw-source="[&lt;strong&gt;WdfIoQueueFindRequestFailed&lt;/strong&gt;](kmdf-wdfioqueuefindrequestfailed.md)"><strong>WdfIoQueueFindRequestFailed</strong></a> rule specifies that <a href="kmdf-wdfioqueueretrievefoundrequest.md" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveFoundRequest&lt;/strong&gt;](kmdf-wdfioqueueretrievefoundrequest.md)"><strong>WdfIoQueueRetrieveFoundRequest</strong></a> or <a href="/windows-hardware/drivers/wdf/wdfobjectdereference" data-raw-source="[&lt;strong&gt;WdfObjectDereference&lt;/strong&gt;](../wdf/wdfobjectdereference.md)"><strong>WdfObjectDereference</strong></a> should only be called after <strong>WdfIoQueueFindRequestFailed</strong> returns STATUS_SUCCESS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-wdfioqueueretrievefoundrequest.md" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveFoundRequest&lt;/strong&gt;](kmdf-wdfioqueueretrievefoundrequest.md)"><strong>WdfIoQueueRetrieveFoundRequest</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfioqueueretrievefoundrequest.md" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveFoundRequest&lt;/strong&gt;](kmdf-wdfioqueueretrievefoundrequest.md)"><strong>WdfIoQueueRetrieveFoundRequest</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievefoundrequest" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveFoundRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievefoundrequest)"><strong>WdfIoQueueRetrieveFoundRequest</strong></a> method is called only after <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest" data-raw-source="[&lt;strong&gt;WdfIoQueueFindRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest)"><strong>WdfIoQueueFindRequest</strong></a> is called and returned STATUS_SUCCESS and no <a href="/windows-hardware/drivers/wdf/wdfobjectdereference" data-raw-source="[&lt;strong&gt;WdfObjectDereference&lt;/strong&gt;](../wdf/wdfobjectdereference.md)"><strong>WdfObjectDereference</strong></a> is called on the same request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-wdfioqueueretrievenextrequest.md" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveNextRequest&lt;/strong&gt;](kmdf-wdfioqueueretrievenextrequest.md)"><strong>WdfIoQueueRetrieveNextRequest</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfioqueueretrievenextrequest.md" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveNextRequest&lt;/strong&gt;](kmdf-wdfioqueueretrievenextrequest.md)"><strong>WdfIoQueueRetrieveNextRequest</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievenextrequest" data-raw-source="[&lt;strong&gt;WdfIoQueueRetrieveNextRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievenextrequest)"><strong>WdfIoQueueRetrieveNextRequest</strong></a> is not called after <a href="/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest" data-raw-source="[&lt;strong&gt;WdfIoQueueFindRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest)"><strong>WdfIoQueueFindRequest</strong></a> is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-writereqs.md" data-raw-source="[&lt;strong&gt;WriteReqs&lt;/strong&gt;](kmdf-writereqs.md)"><strong>WriteReqs</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-writereqs.md" data-raw-source="[&lt;strong&gt;WriteReqs&lt;/strong&gt;](kmdf-writereqs.md)"><strong>WriteReqs</strong></a> rule specifies that a write request is not passed to inappropriate KMDF methods.</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

