---
title: InvalidReqAccessLocal rule (kmdf)
description: The InvalidReqAccessLocal rule specifies that locally created requests are not accessed after they are completed or canceled.
ms.date: 05/21/2018
keywords: ["InvalidReqAccessLocal rule (kmdf)"]
topic_type:
- apiref
api_name:
- InvalidReqAccessLocal
api_type:
- NA
ms.localizationpriority: medium
---

# InvalidReqAccessLocal rule (kmdf)


The **InvalidReqAccessLocal** rule specifies that locally created requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.

A request is considered invalid if it is completed, marked cancelable, or canceled after it was sent. After the request is considered invalid, the request cannot be passed to **WdfRequest***Xxx* functions, except when the driver calls **WdfRequestUnmarkCancelable** if the request was previously marked cancelable.

This rule is similar to the [**InvalidReqAccess**](kmdf-invalidreqaccess.md) rule; however, the **InvalidReqAccessLocal** rule is only performed within the default I/O queue callback functions.

**Driver model: KMDF**

## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>InvalidReqAccessLocal</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete)  
[**WdfRequestAllocateTimer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestallocatetimer)  
[**WdfRequestCancelSentRequest**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest)  
[**WdfRequestChangeTarget**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestchangetarget)  
[**WdfRequestCreate**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate)  
[**WdfRequestFormatRequestUsingCurrentType**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestformatrequestusingcurrenttype)  
[**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue)  
[**WdfRequestGetCompletionParams**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetcompletionparams)  
[**WdfRequestGetFileObject**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetfileobject)  
[**WdfRequestGetInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetinformation)  
[**WdfRequestGetIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetioqueue)  
[**WdfRequestGetParameters**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetparameters)  
[**WdfRequestGetRequestorMode**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestormode)  
[**WdfRequestIsFrom32BitProcess**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestisfrom32bitprocess)  
[**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable)  
[**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex)  
[**WdfRequestProbeAndLockUserBufferForRead**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestprobeandlockuserbufferforread)  
[**WdfRequestProbeAndLockUserBufferForWrite**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestprobeandlockuserbufferforwrite)  
[**WdfRequestRequeue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestrequeue)  
[**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)  
[**WdfRequestRetrieveInputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)  
[**WdfRequestRetrieveInputWdmMdl**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)  
[**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)  
[**WdfRequestRetrieveOutputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)  
[**WdfRequestRetrieveOutputWdmMdl**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl)  
[**WdfRequestRetrieveUnsafeUserInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer)  
[**WdfRequestRetrieveUnsafeUserOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer)  
[**WdfRequestReuse**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestreuse)  
[**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)  
[**WdfRequestSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine)  
[**WdfRequestSetInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetinformation)  
[**WdfRequestUnmarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable)  
[**WdfRequestWdmFormatUsingStackLocation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestwdmformatusingstacklocation)  
[**WdfRequestWdmGetIrp**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestwdmgetirp)  
[**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist)  
