---
title: SpinLockRelease rule (storport)
description: This rule verifies that the driver does not attempt to release a lock via KeReleaseSpinLock without first acquiring it via KeAquireSpinlock or KeAcquireSpinLockRaiseToDpc. The rule passes when the acquired spin lock is released.
ms.assetid: CD4287CB-EF0C-476C-BF10-B46B96AB7D11
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinLockRelease rule (storport)"]
topic_type:
- apiref
api_name:
- SpinLockRelease
api_type:
- NA
---

# SpinLockRelease rule (storport)


This rule verifies that the driver does not attempt to release a lock via **KeReleaseSpinLock** without first acquiring it via **KeAquireSpinlock** or **KeAcquireSpinLockRaiseToDpc**. The rule passes when the acquired spin lock is released.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinLockRelease</strong> rule.</p>
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
 

 





