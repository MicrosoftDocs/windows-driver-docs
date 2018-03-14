---
title: ReqIsCancOnCancReq rule (kmdf)
description: The ReqIsCancOnCancReq rule specifies that the WdfRequestIsCanceled method can only be called on a request that is not marked as cancelable.
ms.assetid: d9138a90-4707-485b-a1be-a6b90a410272
keywords: ["ReqIsCancOnCancReq rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqIsCancOnCancReq
api_type:
- NA
---

# ReqIsCancOnCancReq rule (kmdf)


The **ReqIsCancOnCancReq** rule specifies that the [**WdfRequestIsCanceled**](https://msdn.microsoft.com/library/windows/hardware/ff549976) method can only be called on a request that is not marked as cancelable.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqIsCancOnCancReq</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestIsCanceled**](https://msdn.microsoft.com/library/windows/hardware/ff549976)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





