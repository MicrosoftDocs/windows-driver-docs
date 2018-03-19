---
title: ReqMarkCancelableSend rule (kmdf)
description: The ReqMarkCancelableSend rule specifies that requests forwarded by the driver are not marked as cancelable by calling WdfRequestMarkCancelable.
ms.assetid: 8fb40977-7a34-4bb8-ba98-16e98fbd9137
keywords: ["ReqMarkCancelableSend rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqMarkCancelableSend
api_type:
- NA
---

# ReqMarkCancelableSend rule (kmdf)


The **ReqMarkCancelableSend** rule specifies that requests forwarded by the driver are not marked as cancelable by calling [**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983).

To mark the request as cancelable, the driver must own the request. When the request is sent to another driver, the previous driver no longer has ownership and must call [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) on the request if it was previously marked cancelable.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqMarkCancelableSend</strong> rule.</p>
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

[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





