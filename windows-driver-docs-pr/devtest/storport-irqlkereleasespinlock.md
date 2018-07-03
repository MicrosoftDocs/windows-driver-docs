---
title: IrqlKeReleaseSpinLock rule (storport)
description: This rule verifies that KeReleaseSpinLock is called at IRQL DISPATCH\_LEVEL only. It must also set the IRQL to the previous IRQL level. Typically this call would be preceded by a call to KeAcquireSpinLock.
ms.assetid: A1AEE8C9-F5F1-4BBE-8291-1E61D73AFC6A
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlKeReleaseSpinLock rule (storport)"]
topic_type:
- apiref
api_name:
- IrqlKeReleaseSpinLock
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeReleaseSpinLock</strong> rule.</p>
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

[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
 

 





