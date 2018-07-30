---
title: SpinlockRelease rule (wdm)
description: The SpinlockRelease rule specifies that calls to KeReleaseSpinLock are made in strict alternation with KeAcquireSpinLock and KeAcquireSpinLockRaiseToDpc.
ms.assetid: e001a818-03d4-4aa9-995a-6b99e1a7cee3
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinlockRelease rule (wdm)"]
topic_type:
- apiref
api_name:
- SpinlockRelease
api_type:
- NA
ms.localizationpriority: medium
---

# SpinlockRelease rule (wdm)


The **SpinlockRelease** rule specifies that calls to [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) are made in strict alternation with [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928). That is, the driver must call **KeReleaseSpinLock** after calling **KeAcquireSpinLock** or **KeAcquireSpinLockRaiseToDpc** and before subsequent calls to **KeAcquireSpinLock** or to **KeAcquireSpinLockRaiseToDpc**.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0004000B) |

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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking (additional)](https://msdn.microsoft.com/library/windows/hardware/hh454208#ddi-compliance-checking-additional) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
[**KeTryToAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553317)
 

 





