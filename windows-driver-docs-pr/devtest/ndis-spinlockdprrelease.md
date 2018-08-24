---
title: SpinLockDprRelease rule (ndis)
description: The SpinLockDprRelease rule verifies that calls to NdisAcquireSpinLock or NdisDprAcquireSpinLock are called only when the SpinLock is the \ 0034;unlocked \ 0034; state.
ms.assetid: B726B1AD-F49D-479B-AF1B-99E8901E2315
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinLockDprRelease</strong> rule.</p>
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
[**NdisAllocateSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561617)
[**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749)
[**NdisDprReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561753)
[**NdisReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff564524)
 

 





