---
title: IrqlKeReleaseSpinLock rule (storport)
description: This rule verifies that KeReleaseSpinLock is called at IRQL DISPATCH\_LEVEL only. It must also set the IRQL to the previous IRQL level. Typically this call would be preceded by a call to KeAcquireSpinLock.
ms.assetid: A1AEE8C9-F5F1-4BBE-8291-1E61D73AFC6A
ms.date: 05/21/2018
keywords: ["IrqlKeReleaseSpinLock rule (storport)"]
topic_type:
- apiref
api_name:
- IrqlKeReleaseSpinLock
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeReleaseSpinLock rule (storport)


This rule verifies that **KeReleaseSpinLock** is called at **IRQL = DISPATCH\_LEVEL** only. It must also set the IRQL to the previous IRQL level. Typically this call would be preceded by a call to **KeAcquireSpinLock**.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlKeReleaseSpinLock</strong> rule.</p>
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

[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
 

 





