---
title: IrqlKeRaiseLower2 rule (wdm)
description: The IrqlKeRaiseLower2 rule specifies that drivers use KeLowerIrql to restore the original IRQL raised by a preceding call to KeRaiseIrql or KeRaiseIrqlToDpcLevel.
ms.assetid: 7e256237-e649-45de-bcd9-b06795a5c5c9
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlKeRaiseLower2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeRaiseLower2
api_type:
- NA
---

# IrqlKeRaiseLower2 rule (wdm)


The **IrqlKeRaiseLower2** rule specifies that drivers use [**KeLowerIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552968) to restore the original IRQL raised by a preceding call to [**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079) or [**KeRaiseIrqlToDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553084).

This rule permits nested calls to **KeRaiseIrql**, **KeRaiseIrqlToDpcLevel** and **KeLowerIrql**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeRaiseLower2</strong> rule.</p>
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

[**KeLowerIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552968)
[**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079)
See also
--------

[**IrqlKeDispatchLte**](wdm-irqlkedispatchlte.md)
[**IrqlKeRaiseLower**](wdm-irqlkeraiselower.md)
 

 





