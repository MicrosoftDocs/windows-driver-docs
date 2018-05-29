---
title: IrqlKeSetEvent rule (wdm)
description: The IrqlKeSetEvent rule specifies that the KeSetEvent routine is only called at IRQL�  DISPATCH\_LEVEL when Wait is set to FALSE, and at IRQL�  APC\_LEVEL when Wait is set to TRUE.
ms.assetid: 6274c70c-f61c-4e48-8ee9-a68107158cce
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlKeSetEvent rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeSetEvent
api_type:
- NA
---

# IrqlKeSetEvent rule (wdm)


The **IrqlKeSetEvent** rule specifies that the [**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253) routine is only called at IRQL &lt;= DISPATCH\_LEVEL when *Wait* is set to **FALSE**, and at IRQL &lt;= APC\_LEVEL when *Wait* is set to **TRUE**.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020016) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeSetEvent</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253)
 

 





