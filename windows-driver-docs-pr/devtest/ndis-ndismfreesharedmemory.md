---
title: NdisMFreeSharedMemory rule (ndis)
description: NdisMFreeSharedMemory cannot be called from a MiniportShutdownEx function.
ms.assetid: 86109F0F-38ED-4A20-9BFF-7738D7944DD8
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisMFreeSharedMemory rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisMFreeSharedMemory
api_type:
- NA
ms.localizationpriority: medium
---

# NdisMFreeSharedMemory rule (ndis)


[**NdisMFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563589) cannot be called from a [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisMFreeSharedMemory</strong> rule.</p>
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

[**NdisMFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563589)
 

 





