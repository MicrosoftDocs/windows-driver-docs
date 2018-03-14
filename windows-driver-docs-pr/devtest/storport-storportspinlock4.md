---
title: StorPortSpinLock4 rule (storport)
description: This rule is the release counterpart of StorPortSpinLock. It is similar to the SpinLockRelease rule.
ms.assetid: D6003108-7B97-48A5-9A8B-007DEFB5DF6C
keywords: ["StorPortSpinLock4 rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortSpinLock4
api_type:
- NA
---

# StorPortSpinLock4 rule (storport)


This rule is the *release* counterpart of **StorPortSpinLock**. It is similar to the **SpinLockRelease** rule.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortSpinLock4</strong> rule.</p>
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
 

 





