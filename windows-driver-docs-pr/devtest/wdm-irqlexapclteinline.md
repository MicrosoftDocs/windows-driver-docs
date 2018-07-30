---
title: IrqlExApcLteInline rule (wdm)
description: The IrqlExApcLteInline rule specifies that DDIs are only called at proper IRQL levels.
ms.assetid: 9BE8633E-9390-40FA-8E2E-1FA130B6E638
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlExApcLteInline rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExApcLteInline
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExApcLteInline rule (wdm)


The **IrqlExApcLteInline** rule specifies that DDIs are only called at proper IRQL levels

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlExApcLteInline</strong> rule.</p>
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

 

 





