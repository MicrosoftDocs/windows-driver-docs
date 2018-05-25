---
title: IoAllocateIrpSignalEventInCompletionTimeout rule (wdm)
description: The IoAllocateIrpSignalEventInCompletionTimeout rule reports a defect if it detects that this driver will wait indefinitely until the lower driver returns, as the IRP’s event is required to be signaled in the completion routine.
ms.assetid: 7E00F7EC-3FB9-4BFB-AE10-D846282B37AA
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoAllocateIrpSignalEventInCompletionTimeout rule (wdm)"]
topic_type:
- apiref
api_name:
- IoAllocateIrpSignalEventInCompletionTimeout
api_type:
- NA
---

# IoAllocateIrpSignalEventInCompletionTimeout rule (wdm)


The **IoAllocateIrpSignalEventInCompletionTimeout** rule reports a defect if it detects that this driver will wait indefinitely until the lower driver returns, as the IRP’s event is required to be signaled in the completion routine.

This rule is for locally created asynchronous IRPs.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoAllocateIrpSignalEventInCompletionTimeout</strong> rule.</p>
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

[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





