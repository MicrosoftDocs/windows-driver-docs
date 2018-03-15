---
title: ReqSendWhileSpinlock rule (kmdf)
description: The ReqSendWhileSpinlock rule specifies that no requests are sent while the driver holds a spinlock.
ms.assetid: f038f4ca-aa24-4df3-9c31-d8eec928c306
keywords: ["ReqSendWhileSpinlock rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqSendWhileSpinlock
api_type:
- NA
---

# ReqSendWhileSpinlock rule (kmdf)


The **ReqSendWhileSpinlock** rule specifies that no requests are sent while the driver holds a spinlock.

If the driver sends any requests while it holds a spinlock, it could cause a deadlock or clash with the lower driver that receives the requests, if the lower driver also attempts to acquire a lock or access shared resources.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqSendWhileSpinlock</strong> rule.</p>
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

[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040)
[**WdfSpinLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff550044)
[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
See also
--------

[Completing I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff540740)
[Synchronizing Cancel and Completion Code](https://msdn.microsoft.com/library/windows/hardware/ff544726)
 

 





