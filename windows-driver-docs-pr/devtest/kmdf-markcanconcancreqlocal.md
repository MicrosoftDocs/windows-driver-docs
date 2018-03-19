---
title: MarkCancOnCancReqLocal rule (kmdf)
description: The MarkCancOnCancReqLocal rule specifies that WdfRequestMarkCancelable method cannot be called two consecutive times on the same I/O request.
ms.assetid: f09158bd-272c-480b-bf25-036f11c96ad8
keywords: ["MarkCancOnCancReqLocal rule (kmdf)"]
topic_type:
- apiref
api_name:
- MarkCancOnCancReqLocal
api_type:
- NA
---

# MarkCancOnCancReqLocal rule (kmdf)


The **MarkCancOnCancReqLocal** rule specifies that [**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983) method cannot be called two consecutive times on the same I/O request.

The **MarkCancOnCancReqLocal** rule performs this check only within the default I/O queue callback functions.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MarkCancOnCancReqLocal</strong> rule.</p>
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
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





