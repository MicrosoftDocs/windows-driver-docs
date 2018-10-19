---
title: IoBuildFsdIrpSignalEventInCompletionTimeout rule (wdm)
description: The IoBuildFsdIrpSignalEventInCompletionTimeout rule reports a defect when the driver waits indefinitely until the lower driver returns, as the IRP’s event is required to be signaled in the completion routine.
ms.assetid: EE191EDB-62BE-46F3-92B2-CE9090AD02E2
ms.date: 05/21/2018
keywords: ["IoBuildFsdIrpSignalEventInCompletionTimeout rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildFsdIrpSignalEventInCompletionTimeout
api_type:
- NA
ms.localizationpriority: medium
---

# IoBuildFsdIrpSignalEventInCompletionTimeout rule (wdm)


The **IoBuildFsdIrpSignalEventInCompletionTimeout** rule reports a defect when the driver waits indefinitely until the lower driver returns, as the IRP’s event is required to be signaled in the completion routine.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildFsdIrpSignalEventInCompletionTimeout</strong> rule.</p>
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

[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
 

 





