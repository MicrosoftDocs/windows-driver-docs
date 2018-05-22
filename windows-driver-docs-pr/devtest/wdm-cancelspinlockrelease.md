---
title: CancelSpinlockRelease rule (wdm)
description: The CancelSpinlockRelease rule specifies that calls to IoAcquireCancelSpinLock and IoReleaseCancelSpinLock are used in strict alternation. That is, every call to IoAcquireCancelSpinLock must have a corresponding call to IoReleaseCancelSpinLock.
ms.assetid: dba280c7-18ac-4d87-8d45-d30c214ef90e
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CancelSpinlockRelease rule (wdm)"]
topic_type:
- apiref
api_name:
- CancelSpinlockRelease
api_type:
- NA
---

# CancelSpinlockRelease rule (wdm)


The **CancelSpinlockRelease** rule specifies that calls to [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) and [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) are used in strict alternation. That is, every call to **IoAcquireCancelSpinLock** must have a corresponding call to **IoReleaseCancelSpinLock**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CancelSpinlockRelease</strong> rule.</p>
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
 

 





