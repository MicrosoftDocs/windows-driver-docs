---
title: SpinLockDpc rule (storport)
description: This rule verifies that a call to KeAcquireSpinLockRaiseToDpc is promptly followed by a call to KeReleaseSpinlock.
ms.assetid: 955B5A37-5E14-4380-A30D-3D019C4D5B59
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinLockDpc rule (storport)"]
topic_type:
- apiref
api_name:
- SpinLockDpc
api_type:
- NA
---

# SpinLockDpc rule (storport)


This rule verifies that a call to **KeAcquireSpinLockRaiseToDpc** is promptly followed by a call to **KeReleaseSpinlock**. If a driver calls **KeAcquireSpinLock** or **KeAcquireSpinLockRaiseToDpc** again prior to releasing the lock, it fails the rule. In addition, before exiting the dispatch or cancel routine, the driver must release the spin lock.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinLockDpc</strong> rule.</p>
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

[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
 

 





