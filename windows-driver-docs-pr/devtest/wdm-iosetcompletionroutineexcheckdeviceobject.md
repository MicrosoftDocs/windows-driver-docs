---
title: IoSetCompletionRoutineExCheckDeviceObject rule (wdm)
description: The IoSetCompletionRoutineExCheckDeviceObject rule specifies that if the current device object is not passed to IoSetCompletionRoutineEx and the lower device object is, this can lead to a race condition where the current device object could be unloaded even though the completion routine has not run.
ms.assetid: 037E4CED-FBC7-480F-B81F-561396A217C6
ms.date: 05/21/2018
keywords: ["IoSetCompletionRoutineExCheckDeviceObject rule (wdm)"]
topic_type:
- apiref
api_name:
- IoSetCompletionRoutineExCheckDeviceObject
api_type:
- NA
ms.localizationpriority: medium
---

# IoSetCompletionRoutineExCheckDeviceObject rule (wdm)


The **IoSetCompletionRoutineExCheckDeviceObject** rule specifies that if the current device object is not passed to [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686) and the lower device object is, this can lead to a race condition where the current device object could be unloaded even though the completion routine has not run.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IoSetCompletionRoutineExCheckDeviceObject</strong> rule.</p>
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

[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
 

 





