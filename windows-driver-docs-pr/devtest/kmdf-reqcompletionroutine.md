---
title: ReqCompletionRoutine rule (kmdf)
description: The ReqCompletionRoutine rule specifies that a completion routine must be set before a request is sent to an I/O target.
ms.assetid: 0ddf6980-0540-4224-9800-3cd534f03230
keywords: ["ReqCompletionRoutine rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqCompletionRoutine
api_type:
- NA
---

# ReqCompletionRoutine rule (kmdf)


The **ReqCompletionRoutine** rule specifies that a completion routine must be set before a request is sent to an I/O target.

If a request is not sent synchronously, or is not sent as send and forget, (specified by the **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET** flag), the driver should set a completion routine so that the I/O target can notify the driver when the request is completed.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqCompletionRoutine</strong> rule.</p>
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

[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030)
See also
--------

[Completing I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff540740)
[Synchronizing Cancel and Completion Code](https://msdn.microsoft.com/library/windows/hardware/ff544726)
[**WDF\_REQUEST\_SEND\_OPTIONS\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff552493)
[**WDF\_REQUEST\_SEND\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff552491)
 

 





