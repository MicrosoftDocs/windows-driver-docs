---
title: NdisStallExecution\_Delay rule (ndis)
description: The NdisStallExecution\_Delay rule specifies that NdisStallExecution must never be called by using a value for MicrosecondsToStall that is greater than 50 microseconds.
ms.assetid: 4c9368d0-4da7-4adc-bc63-4f21af90b682
ms.date: 05/21/2018
keywords: ["NdisStallExecution_Delay rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisStallExecution_Delay
api_type:
- NA
ms.localizationpriority: medium
---

# NdisStallExecution\_Delay rule (ndis)


The NdisStallExecution\_Delay rule specifies that **NdisStallExecution** must never be called by using a value for *MicrosecondsToStall* that is greater than 50 microseconds.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisStallExecution_Delay</strong> rule.</p>
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

[**NdisStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff564568)
 

 





