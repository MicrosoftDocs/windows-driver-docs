---
title: SpIrql rule (storport)
description: This rule verifies that the routines TdiRegisterPnPHandlers and TdiDeregisterPnPHandlers are only called at IRQL lower than DISPATCH\_LEVEL. However, if ExFreeToNPagedLookasideList is called, the rule passes.
ms.assetid: 895E3982-F50E-4B7A-9904-8D0D742A9B64
ms.date: 05/21/2018
keywords: ["SpIrql rule (storport)"]
topic_type:
- apiref
api_name:
- SpIrql
api_type:
- NA
ms.localizationpriority: medium
---

# SpIrql rule (storport)


This rule verifies that the routines **TdiRegisterPnPHandlers** and **TdiDeregisterPnPHandlers** are only called at IRQL lower than **DISPATCH\_LEVEL**. However, if **ExFreeToNPagedLookasideList** is called, the rule passes.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpIrql</strong> rule.</p>
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

[**ExFreeToNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544601)
 

 





