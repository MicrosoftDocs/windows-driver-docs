---
title: ReqDelete rule (kmdf)
description: The ReqDelete rule specifies that driver-created requests are not passed to WdfRequestCompleteXxx functions. Instead, the request should be deleted upon completion.
ms.assetid: 66e86353-46f7-4aa4-a4be-16277f4924e3
ms.date: 05/21/2018
keywords: ["ReqDelete rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqDelete
api_type:
- NA
ms.localizationpriority: medium
---

# ReqDelete rule (kmdf)


The **ReqDelete** rule specifies that driver-created requests are not passed to *WdfRequestCompleteXxx* functions. Instead, the request should be deleted upon completion.

If the driver creates a framework request object in a call to [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951), the request should be deleted by using [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) when the driver is finished with the request.

The driver cannot call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948) or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) functions on the request object. The *WdfRequestCompleteXxx* functions are reserved for framework-supplied requests.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>ReqDelete</strong> rule.</p>
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

[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951)
 

 





