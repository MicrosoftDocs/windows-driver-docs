---
title: IoSetCompletionRoutineExCheckDeviceObject rule (wdm)
description: The IoSetCompletionRoutineExCheckDeviceObject rule specifies that if the current device object is not passed to IoSetCompletionRoutineEx and the lower device object is, this can lead to a race condition where the current device object could be unloaded even though the completion routine has not run.
ms.assetid: 037E4CED-FBC7-480F-B81F-561396A217C6
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoSetCompletionRoutineExCheckDeviceObject rule (wdm)"]
topic_type:
- apiref
api_name:
- IoSetCompletionRoutineExCheckDeviceObject
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoSetCompletionRoutineExCheckDeviceObject</strong> rule.</p>
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

[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
 

 





