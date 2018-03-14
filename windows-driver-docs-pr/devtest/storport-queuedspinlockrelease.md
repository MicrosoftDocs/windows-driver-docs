---
title: QueuedSpinLockRelease rule (storport)
description: This rule verifies that the driver does not call KeReleaseInStackQueuedSpinLock without first acquiring the lock via KeAcquireInStackQueuedSpinLock.
ms.assetid: F523D77B-F848-4128-9B6D-7D92E01C4632
keywords: ["QueuedSpinLockRelease rule (storport)"]
topic_type:
- apiref
api_name:
- QueuedSpinLockRelease
api_type:
- NA
---

# QueuedSpinLockRelease rule (storport)


This rule verifies that the driver does not call **KeReleaseInStackQueuedSpinLock** without first acquiring the lock via **KeAcquireInStackQueuedSpinLock**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>QueuedSpinLockRelease</strong> rule.</p>
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

[**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899)
[**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130)
 

 





