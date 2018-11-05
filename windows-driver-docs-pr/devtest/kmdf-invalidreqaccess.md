---
title: InvalidReqAccess rule (kmdf)
description: The InvalidReqAccess rule specifies that requests are not accessed after they are completed or canceled.
ms.assetid: dc7609a5-8b18-44b9-88b0-a9616bc220d4
ms.date: 05/21/2018
keywords: ["InvalidReqAccess rule (kmdf)"]
topic_type:
- apiref
api_name:
- InvalidReqAccess
api_type:
- NA
ms.localizationpriority: medium
---

# InvalidReqAccess rule (kmdf)


The **InvalidReqAccess** rule specifies that requests are not accessed after they are completed or canceled. This rule might overlap with other rules, such as rules that check for double completion, or rules that check for requests have been marked cancelable two times.

A request is considered invalid if it is completed, marked cancelable, or canceled after it was sent. After the request is considered invalid, the request cannot be passed to **WdfRequest***Xxx* functions, except when the driver calls **WdfRequestUnmarkCancelable** if the request was previously marked cancelable.

This rule is similar to the [**InvalidReqAccessLocal**](kmdf-invalidreqaccesslocal.md) rule; however, the **InvalidReqAccessLocal** rule is only performed within the default I/O queue callback functions.

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>InvalidReqAccess</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfRequestAllocateTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549938)
[**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941)
[**WdfRequestChangeTarget**](https://msdn.microsoft.com/library/windows/hardware/ff549943)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestFormatRequestUsingCurrentType**](https://msdn.microsoft.com/library/windows/hardware/ff549955)
[**WdfRequestForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549958)
[**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961)
[**WdfRequestGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff549963)
[**WdfRequestGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549965)
[**WdfRequestGetIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549968)
[**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969)
[**WdfRequestGetRequestorMode**](https://msdn.microsoft.com/library/windows/hardware/ff549971)
[**WdfRequestIsFrom32BitProcess**](https://msdn.microsoft.com/library/windows/hardware/ff549978)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestProbeAndLockUserBufferForRead**](https://msdn.microsoft.com/library/windows/hardware/ff549987)
[**WdfRequestProbeAndLockUserBufferForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff549989)
[**WdfRequestRequeue**](https://msdn.microsoft.com/library/windows/hardware/ff550012)
[**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)
[**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015)
[**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016)
[**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)
[**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019)
[**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021)
[**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022)
[**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024)
[**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030)
[**WdfRequestSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550032)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
[**WdfRequestWdmFormatUsingStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550036)
[**WdfRequestWdmGetIrp**](https://msdn.microsoft.com/library/windows/hardware/ff550037)
 

 





