---
title: DoubleExFreePool rule (storport)
description: This rule verifies that the driver does not attempt to free the same block of pool memory twice.
ms.assetid: D7EAD257-02CA-418C-B67D-FADCB4F7A6C1
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleExFreePool</strong> rule.</p>
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

[**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)
[**RemoveEntryList**](https://msdn.microsoft.com/library/windows/hardware/ff561029)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





