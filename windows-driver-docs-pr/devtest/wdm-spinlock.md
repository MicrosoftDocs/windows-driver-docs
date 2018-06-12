---
title: SpinLock rule (wdm)
description: The SpinLock rule specifies that, after calling KeAcquireSpinLock, the driver calls KeReleaseSpinLock before subsequent calls to KeAcquireSpinLock or to KeAcquireSpinLockRaiseToDpc.
ms.assetid: 3add467d-72b9-439f-b9a3-68f3d1e5b772
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- SpinLock
api_type:
- NA
---

# SpinLock rule (wdm)


The **SpinLock** rule specifies that, after calling [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917), the driver calls [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) before subsequent calls to **KeAcquireSpinLock** or to [**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928).

Nested calls are permitted if they are acquiring and releasing locks for different resources. Nested calls to acquire or release locks for the same resources violate this rule.

This rule also specifies that the driver has used [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) to release all spin locks before the dispatch routine or cancel routine ends.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00040009) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
[**KeTryToAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553317)
 

 





