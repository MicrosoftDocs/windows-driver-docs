---
title: IrqlExFree3 rule (wdm)
description: The IrqlExFree3 rule specifies that ExFreePool and ExFreePoolWithTag are called at proper IRQL.
ms.assetid: D3916378-2032-4575-941F-F1EA9A3678F8
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlExFree3 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExFree3
api_type:
- NA
---

# IrqlExFree3 rule (wdm)


The **IrqlExFree3** rule specifies that [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) and [**ExFreePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544593) are called at proper IRQL.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlExFree3</strong> rule.</p>
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

[**ExFreePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544593)
 

 





