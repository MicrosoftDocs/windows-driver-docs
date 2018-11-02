---
title: SpinLockDprRelease rule (ndis)
description: The SpinLockDprRelease rule verifies that calls to NdisAcquireSpinLock or NdisDprAcquireSpinLock are called only when the SpinLock is the \ 0034;unlocked \ 0034; state.
ms.assetid: B726B1AD-F49D-479B-AF1B-99E8901E2315
ms.date: 05/21/2018
keywords: ["SpinLockDprRelease rule (ndis)"]
topic_type:
- apiref
api_name:
- SpinLockDprRelease
api_type:
- NA
ms.localizationpriority: medium
---

# SpinLockDprRelease rule (ndis)


The **SpinLockDprRelease** rule verifies that calls to [**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699) or [**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749) are called only when the SpinLock is the "unlocked" state. This rule also checks that before exiting the miniport handler routine the SpinLock has been release.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>SpinLockDprRelease</strong> rule.</p>
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

[**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699)
[**NdisAllocateSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561617)
[**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749)
[**NdisDprReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561753)
[**NdisReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff564524)
 

 





