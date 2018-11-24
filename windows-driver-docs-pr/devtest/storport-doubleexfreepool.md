---
title: DoubleExFreePool rule (storport)
description: This rule verifies that the driver does not attempt to free the same block of pool memory twice.
ms.assetid: D7EAD257-02CA-418C-B67D-FADCB4F7A6C1
ms.date: 05/21/2018
keywords: ["DoubleExFreePool rule (storport)"]
topic_type:
- apiref
api_name:
- DoubleExFreePool
api_type:
- NA
ms.localizationpriority: medium
---

# DoubleExFreePool rule (storport)


This rule verifies that the driver does not attempt to free the same block of pool memory twice.

The rule keeps track of the memory pointer that is first passed to **ExFreePool**. If the same pointer is passed again, the driver fails the rule. If the driver calls **RemoveHeadList** or **RemoveEntryList**, the rule passes.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>DoubleExFreePool</strong> rule.</p>
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

[**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)
[**RemoveEntryList**](https://msdn.microsoft.com/library/windows/hardware/ff561029)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





