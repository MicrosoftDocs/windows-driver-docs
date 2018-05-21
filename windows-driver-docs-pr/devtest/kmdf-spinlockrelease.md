---
title: SpinlockRelease rule (kmdf)
description: The SpinlockRelease rule specifies that calls to KeAcquireSpinLock, KeAcquireSpinLockRaiseToDpc, and KeReleaseSpinLock are used in a balanced way within a KMDF callback. At the end of any KMDF callback routine, the driver should not hold the spin lock.
ms.assetid: 23BEB857-309D-4C11-A361-D72F87C84154
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinlockRelease rule (kmdf)"]
topic_type:
- apiref
api_name:
- SpinlockRelease
api_type:
- NA
---

# SpinlockRelease rule (kmdf)


The **SpinlockRelease** rule specifies that calls to [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917), [**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928), and [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) are used in a balanced way within a KMDF callback. At the end of any KMDF callback routine, the driver should not hold the spin lock.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinlockRelease</strong> rule.</p>
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
 

 





