---
title: EvtSurpriseRemoveNoRequestComplete rule (kmdf)
description: The EvtSurpriseRemoveNoRequestComplete rule specifies that WDF drivers shouldn’t complete requests from EvtDeviceSurpriseRemoval callback, instead self-managed I/O callback functions should be used.
ms.assetid: A815CFA0-72A9-4FBC-8432-6212CB696F99
ms.date: 05/21/2018
keywords: ["EvtSurpriseRemoveNoRequestComplete rule (kmdf)"]
topic_type:
- apiref
api_name:
- EvtSurpriseRemoveNoRequestComplete
api_type:
- NA
ms.localizationpriority: medium
---

# EvtSurpriseRemoveNoRequestComplete rule (kmdf)


The **EvtSurpriseRemoveNoRequestComplete** rule specifies that WDF drivers shouldn’t complete requests from [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback, instead self-managed I/O callback functions should be used. *EvtDeviceSurpriseRemoval* callback isn’t synchronized with the power-down path.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>EvtSurpriseRemoveNoRequestComplete</strong> rule.</p>
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
 

 





