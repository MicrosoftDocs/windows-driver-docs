---
title: QueuedSpinLock rule (wdm)
description: The QueuedSpinLock rule specifies that the driver calls KeAcquireInStackQueuedSpinLock before calling KeReleaseInStackQueuedSpinLock and that the driver calls KeReleaseInStackQueuedSpinLock before any subsequent calls to KeAcquireInStackQueuedSpinLock.
ms.assetid: a34a3f9f-4b7a-4a63-b498-62adcd4fffee
ms.date: 05/21/2018
keywords: ["QueuedSpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- QueuedSpinLock
api_type:
- NA
ms.localizationpriority: medium
---

# QueuedSpinLock rule (wdm)


The **QueuedSpinLock** rule specifies that the driver calls [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) before calling [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) and that the driver calls **KeReleaseInStackQueuedSpinLock** before any subsequent calls to **KeAcquireInStackQueuedSpinLock**.

Nested calls are permitted if they are acquiring and releasing different resources. Nested calls to acquire or release the same resources violate this rule.

This rule also specifies that the driver has called **KeReleaseInStackQueuedSpinLock** to release all queued spin locks before the dispatch routine or cancel routine ends.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00040006) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>QueuedSpinLock</strong> rule.</p>
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

[**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899)
[**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130)
 

 





