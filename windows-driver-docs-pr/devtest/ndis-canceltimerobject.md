---
title: CancelTimerObject rule (ndis)
description: The CancelTimerObject rule specifies that NdisSetTimerObject and NdisCancelTimerObject are called in alternate order. The ultimate goal is to make sure all timers are cancelled when MiniportHaltEx ends.
ms.assetid: F31AF8D2-4F40-43A3-893E-53FCC2299730
ms.date: 05/21/2018
keywords: ["CancelTimerObject rule (ndis)"]
topic_type:
- apiref
api_name:
- CancelTimerObject
api_type:
- NA
ms.localizationpriority: medium
---

# CancelTimerObject rule (ndis)


The **CancelTimerObject** rule specifies that [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) and [**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624) are called in alternate order. The ultimate goal is to make sure all timers are cancelled when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.

The rule uses three different states. The state changes when a timer is set or cancelled. If the timer is still set when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, the rule reports the defect.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CancelTimerObject</strong> rule.</p>
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

 

 





