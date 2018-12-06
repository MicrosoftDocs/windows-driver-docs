---
title: IoBuildFsdIrpSignalEventInCompletion3 rule (wdm)
description: The IoBuildFsdIrpSignalEventInCompletion3 rule specifies that KeSetEvent needs to be called in the completion routine when the Irp- PendingReturned flag is set and the completion routine is processing a locally created asynchronous IRP.
ms.assetid: 9A9A8169-AEDC-4B13-B407-22F549678526
ms.date: 05/21/2018
keywords: ["IoBuildFsdIrpSignalEventInCompletion3 rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildFsdIrpSignalEventInCompletion3
api_type:
- NA
ms.localizationpriority: medium
---

# IoBuildFsdIrpSignalEventInCompletion3 rule (wdm)


The **IoBuildFsdIrpSignalEventInCompletion3** rule specifies that [**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253) needs to be called in the completion routine when the **Irp-&gt;PendingReturned** flag is set and the completion routine is processing a locally created asynchronous IRP.

In this case the completion routine will not be called.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IoBuildFsdIrpSignalEventInCompletion3</strong> rule.</p>
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

[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
 

 





