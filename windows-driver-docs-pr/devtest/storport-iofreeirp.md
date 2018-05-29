---
title: IoFreeIrp rule (storport)
description: This rule verifies that an IRP that was allocated by IoAllocateIrp either will be freed by IoFreeIrp or its completion routine will get set by IoSetCompletionRoutine.
ms.assetid: CAEDE78A-B0FF-4963-8C9B-146E4A489E1D
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoFreeIrp rule (storport)"]
topic_type:
- apiref
api_name:
- IoFreeIrp
api_type:
- NA
---

# IoFreeIrp rule (storport)


This rule verifies that an IRP that was allocated by **IoAllocateIrp** either will be freed by **IoFreeIrp** or its completion routine will get set by **IoSetCompletionRoutine**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoFreeIrp</strong> rule.</p>
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

[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
 

 





