---
title: WithinCriticalRegion rule (wdm)
description: The WithinCriticalRegion rule specifies that the driver's calls to particular synchronization functions appear only after calling KeEnterCriticalRegion and before calling KeLeaveCriticalRegion.
ms.assetid: 9b74b868-6025-4e81-b5ba-21e0da734cd9
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WithinCriticalRegion rule (wdm)"]
topic_type:
- apiref
api_name:
- WithinCriticalRegion
api_type:
- NA
---

# WithinCriticalRegion rule (wdm)


The **WithinCriticalRegion** rule specifies that the driver's calls to particular synchronization functions appear only after calling [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) and before calling [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964).

The affected synchronization functions are the following:

-   [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

-   [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

-   [**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)

-   [**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

-   [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)

-   [**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)

This rule does not recognize other methods of disabling normal APC delivery. For more information, see [**Disabling APCs**](https://msdn.microsoft.com/library/windows/hardware/ff543219).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WithinCriticalRegion</strong> rule.</p>
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

[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)
[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)
[**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)
[**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)
[**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)
[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)
[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)
[**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028)
[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)
[**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 





