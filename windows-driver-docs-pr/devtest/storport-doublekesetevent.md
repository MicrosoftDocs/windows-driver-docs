---
title: DoubleKeSetEvent rule (storport)
description: This rule verifies that KeSetEvent is not called twice on the same event object. If the same event object is passed to the routine, the driver fails the rule.
ms.assetid: A9BA2D40-865B-4BD4-86A3-78D695F2DB4D
keywords: ["DoubleKeSetEvent rule (storport)"]
topic_type:
- apiref
api_name:
- DoubleKeSetEvent
api_type:
- NA
---

# DoubleKeSetEvent rule (storport)


This rule verifies that **KeSetEvent** is not called twice on the same event object. If the same event object is passed to the routine, the driver fails the rule.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleKeSetEvent</strong> rule.</p>
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

[**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253)
 

 





