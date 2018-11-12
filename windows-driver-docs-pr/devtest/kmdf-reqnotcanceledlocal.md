---
title: ReqNotCanceledLocal rule (kmdf)
description: The ReqNotCanceledLocal rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the WdfRequestUnmarkCancelable method must be called on the I/O request before completion.
ms.assetid: 3cc3d517-6fb9-46b2-9d22-6bdbef442007
ms.date: 05/21/2018
keywords: ["ReqNotCanceledLocal rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqNotCanceledLocal
api_type:
- NA
ms.localizationpriority: medium
---

# ReqNotCanceledLocal rule (kmdf)


The **ReqNotCanceledLocal** rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) method must be called on the I/O request before completion. The I/O request must be completed, unless the request is canceled before it calls **WdfRequestUnmarkCancelable**.

If a request that was marked as cancelable by [**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983) is completed (by calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)), the [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) method must be called before the I/O request is completed. The request can be completed unless the **WdfRequestUnmarkCancelable** method returns status that is equal to **STATUS\_CANCELLED**.

The default I/O queue callback functions for a request are [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757), [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758), [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768).

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>ReqNotCanceledLocal</strong> rule.</p>
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

[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





