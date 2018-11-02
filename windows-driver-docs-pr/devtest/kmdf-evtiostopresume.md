---
title: EvtIoStopResume rule (kmdf)
description: The EvtIoStopResume rule specifies that if a driver registers a EvtIoStop callback function and then calls WdfRequestStopAcknowledge with the Requeue parameter equal to FALSE, the driver must register a EvtIoResume callback function.
ms.assetid: 52bcaf8a-545c-4607-89c3-d4474bd50376
ms.date: 05/21/2018
keywords: ["EvtIoStopResume rule (kmdf)"]
topic_type:
- apiref
api_name:
- EvtIoStopResume
api_type:
- NA
ms.localizationpriority: medium
---

# EvtIoStopResume rule (kmdf)


The **EvtIoStopResume** rule specifies that if a driver registers a [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function and then calls [**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033) with the *Requeue* parameter equal to **FALSE**, the driver must register a [*EvtIoResume*](https://msdn.microsoft.com/library/windows/hardware/ff541779) callback function. The framework delivers requests to the **EvtIoResume** callback function when the device enters the D0 state again.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>EvtIoStopResume</strong> rule.</p>
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

[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
 

 





