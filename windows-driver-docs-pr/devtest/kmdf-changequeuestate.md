---
title: ChangeQueueState rule (kmdf)
description: The ChangeQueueState rule specifies that the WDF driver doesn't try to change the state of the Queue from concurrent threads or doesn’t call state changing DDIs one after another from within the same thread.
ms.assetid: C05A04E8-F8F2-4339-AAB7-FD62BE1DAAA2
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ChangeQueueState rule (kmdf)"]
topic_type:
- apiref
api_name:
- ChangeQueueState
api_type:
- NA
---

# ChangeQueueState rule (kmdf)


The **ChangeQueueState** rule specifies that the WDF driver doesn't try to change the state of the Queue from concurrent threads or doesn’t call state changing DDIs one after another from within the same thread. Queue state changing callback functions are [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482), [**WdfIoQueueStopSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548489),[**WdfIoQueuePurge**](https://msdn.microsoft.com/library/windows/hardware/ff548442),[**WdfIoQueuePurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548449), [**WdfIoQueueDrain**](https://msdn.microsoft.com/library/windows/hardware/ff547406), [**WdfIoQueueDrainSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff547412), [**WdfIoQueueStopAndPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439289) and [**WdfIoQueueStopAndPurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/hh439293). If these DDIs are called when a Queue state change is already in progress it will cause a computer to crash or to become unresponsive.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ChangeQueueState</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175)
[**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401)
[**WdfIoQueueDrain**](https://msdn.microsoft.com/library/windows/hardware/ff547406)
[**WdfIoQueueDrainSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff547412)
[**WdfIoQueuePurge**](https://msdn.microsoft.com/library/windows/hardware/ff548442)
[**WdfIoQueuePurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548449)
[**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482)
[**WdfIoQueueStopAndPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439289)
[**WdfIoQueueStopAndPurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/hh439293)
[**WdfIoQueueStopSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548489)
 

 





