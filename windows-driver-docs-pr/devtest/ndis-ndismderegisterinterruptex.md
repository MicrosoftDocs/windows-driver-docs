---
title: NdisMDeregisterInterruptEx rule (ndis)
description: After NdisMDeregisterInterruptEx returns control, the miniport driver cannot call the NdisMSynchronizeWithInterruptEx function.
ms.assetid: 49AC090C-157C-4CD2-9C7A-BDD5F3C6D58F
ms.date: 05/21/2018
keywords: ["NdisMDeregisterInterruptEx rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisMDeregisterInterruptEx
api_type:
- NA
ms.localizationpriority: medium
---

# NdisMDeregisterInterruptEx rule (ndis)


After [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) returns control, the miniport driver cannot call the [**NdisMSynchronizeWithInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563681) function.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>NdisMDeregisterInterruptEx</strong> rule.</p>
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

[**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575)
[**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649)
[**NdisMSynchronizeWithInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563681)
 

 





