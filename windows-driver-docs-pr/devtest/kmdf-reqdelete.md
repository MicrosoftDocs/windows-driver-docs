---
title: ReqDelete rule (kmdf)
description: The ReqDelete rule specifies that driver-created requests are not passed to WdfRequestCompleteXxx functions. Instead, the request should be deleted upon completion.
ms.assetid: 66e86353-46f7-4aa4-a4be-16277f4924e3
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ReqDelete rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqDelete
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqDelete</strong> rule.</p>
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

[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951)
 

 





