---
title: SpNoWait rule (storport)
description: This rule verifies that waits or data allocation are not performed inside StartIo.
ms.assetid: 4E1FABD1-AA6B-4EA1-BDD8-0C7A46AFF19B
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpNoWait rule (storport)"]
topic_type:
- apiref
api_name:
- SpNoWait
api_type:
- NA
---

# SpNoWait rule (storport)


This rule verifies that waits or data allocation are not performed inside **StartIo**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpNoWait</strong> rule.</p>
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

[**StorPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff567508)
[**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)
[**ExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff544501)
[**ExAllocatePoolWithQuota**](https://msdn.microsoft.com/library/windows/hardware/ff544506)
[**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513)
[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)
[**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523)
[**ExWaitForRundownProtectionRelease**](https://msdn.microsoft.com/library/windows/hardware/jj569378)
[**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224)
[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoWMIAllocateInstanceIds**](https://msdn.microsoft.com/library/windows/hardware/ff550429)
[**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324)
[**KeWaitForMutexObject**](https://msdn.microsoft.com/library/windows/hardware/ff553344)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479)
[**MmAllocatePagesForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554482)
[**ZwAllocateLocallyUniqueId**](https://msdn.microsoft.com/library/windows/hardware/ff566415)
[**ZwAllocateVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566416)
[**ZwWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff567120)
 

 





