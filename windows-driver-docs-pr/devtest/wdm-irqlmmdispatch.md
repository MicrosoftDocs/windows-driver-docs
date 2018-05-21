---
title: IrqlMmDispatch rule (wdm)
description: The IrqlMmDispatch rule specifies that the driver calls MmFreeContiguousMemory only when it is executing at IRQL DISPATCH\_LEVEL.
ms.assetid: C8F1CE43-C3E0-4ED3-8AEE-8E5D20FAC6E7
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlMmDispatch rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlMmDispatch
api_type:
- NA
---

# IrqlMmDispatch rule (wdm)


The **IrqlMmDispatch** rule specifies that the driver calls [**MmFreeContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554503) only when it is executing at **IRQL &lt;= DISPATCH\_LEVEL**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlMmDispatch</strong> rule.</p>
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

[**MmFreeContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554503)
 

 





