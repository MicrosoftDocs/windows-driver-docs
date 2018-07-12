---
title: CancelSpinLock rule (wdm)
description: The CancelSpinLock rule specifies that the driver calls IoAcquireCancelSpinLock before calling IoReleaseCancelSpinLock and that the driver calls IoReleaseCancelSpinLock before any subsequent calls to IoAcquireCancelSpinLock.
ms.assetid: 8f21a70f-a82b-4b2b-abff-892a1950da41
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CancelSpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- CancelSpinLock
api_type:
- NA
---

# CancelSpinLock rule (wdm)


The CancelSpinLock rule specifies that the driver calls [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) before calling [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) and that the driver calls **IoReleaseCancelSpinLock** before any subsequent calls to **IoAcquireCancelSpinLock**.

This rule also specifies that the driver must not hold any spin locks when the dispatch routine or cancel routine ends. Nested calls are permitted.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CancelSpinLock</strong> rule.</p>
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

[**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196)
[**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





