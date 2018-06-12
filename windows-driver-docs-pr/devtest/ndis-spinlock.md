---
title: SpinLock rule (ndis)
description: The SpinLock rule verifies the correct use of the NDIS spin lock interface.
ms.assetid: 27A20B0C-A1B9-40E6-BA9D-64BB9F58B027
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinLock rule (ndis)"]
topic_type:
- apiref
api_name:
- SpinLock
api_type:
- NA
---

# SpinLock rule (ndis)


The **SpinLock** rule verifies the correct use of the NDIS spin lock interface. This rule specifies that calls to [**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699) are made only when the SpinLock is in the unlocked state. This rule also verifies that the SpinLock is released before the miniport handler routine exits.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinLock</strong> rule.</p>
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

[**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699)
[**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749)
[**NdisDprReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561753)
[**NdisReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff564524)
 

 





