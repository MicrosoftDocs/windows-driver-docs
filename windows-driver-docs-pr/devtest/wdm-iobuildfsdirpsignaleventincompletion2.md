---
title: IoBuildFsdIrpSignalEventInCompletion2 rule (wdm)
description: The IoBuildFsdIrpSignalEventInCompletion2 rule specifies that KeSetEvent needs to be called in the completion routine when the Irp- PendingReturned flag is set and the completion routine is processing a locally created asynchronous IRP.
ms.assetid: 2077EB25-4EAE-4F76-BEB1-C637DA39C07D
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoBuildFsdIrpSignalEventInCompletion2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildFsdIrpSignalEventInCompletion2
api_type:
- NA
---

# IoBuildFsdIrpSignalEventInCompletion2 rule (wdm)


The **IoBuildFsdIrpSignalEventInCompletion2** rule specifies that [**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253) needs to be called in the completion routine when the **Irp-&gt;PendingReturned** flag is set and the completion routine is processing a locally created asynchronous IRP.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildFsdIrpSignalEventInCompletion2</strong> rule.</p>
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
 

 





