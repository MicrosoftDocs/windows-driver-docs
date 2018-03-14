---
title: StorPortSpinLock rule (storport)
description: This rule verifies that locks that are acquired via StorPortAcquireSpinLock are promptly released via StorPortReleaseSpinLock.
ms.assetid: B7B918A0-3042-4961-8D33-EFDC15819D1F
keywords: ["StorPortSpinLock rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortSpinLock
api_type:
- NA
---

# StorPortSpinLock rule (storport)


This rule verifies that locks that are acquired via **StorPortAcquireSpinLock** are promptly released via **StorPortReleaseSpinLock**. The miniport driver fails the rule if it attempts to acquire a lock that it had already acquired, or if it attempts to release a lock that it had not acquired. In addition, at the end of the dispatch or cancel routine, the driver should not hold any spin locks.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortSpinLock</strong> rule.</p>
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

[**StorPortAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff567025)
[**StorPortReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff567496)
 

 





