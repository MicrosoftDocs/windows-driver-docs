---
title: EvtIoStopCancel rule (kmdf)
description: The EvtIoStopCancel rule specifies that within the EvtIoStop callback function, the driver calls one of following methods for I/O requests that are not cancelable.
ms.assetid: 579f25d3-3db5-4fec-bd5b-a09c41ff652c
keywords: ["EvtIoStopCancel rule (kmdf)"]
topic_type:
- apiref
api_name:
- EvtIoStopCancel
api_type:
- NA
---

# EvtIoStopCancel rule (kmdf)


The **EvtIoStopCancel** rule specifies that within the [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function, the driver calls one of following methods for I/O requests that are not cancelable.

[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941)
[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>EvtIoStopCancel</strong> rule.</p>
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

[**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





