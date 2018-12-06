---
title: StorPortAllocatePool rule (storport)
description: This rule verifies that the miniport must not attempt to call StorPortFreePool on an deallocated buffer.
ms.assetid: DEE1768C-5BFF-4A8A-8AE9-9690FDA653C3
ms.date: 05/21/2018
keywords: ["StorPortAllocatePool rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortAllocatePool
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortAllocatePool rule (storport)


This rule verifies that the miniport must not attempt to call [**StorPortFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff567065) on an deallocated buffer.

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>StorPortAllocatePool</strong> rule.</p>
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

[**StorPortAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff567031)
[**StorPortFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff567065)
 

 





