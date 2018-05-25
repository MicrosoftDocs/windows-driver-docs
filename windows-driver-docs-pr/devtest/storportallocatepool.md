---
title: StorPortAllocatePool rule (storport)
description: This rule verifies that the miniport must not attempt to call StorPortFreePool on an deallocated buffer.
ms.assetid: DEE1768C-5BFF-4A8A-8AE9-9690FDA653C3
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortAllocatePool rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortAllocatePool
api_type:
- NA
---

# StorPortAllocatePool rule (storport)


This rule verifies that the miniport must not attempt to call [**StorPortFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff567065) on an deallocated buffer.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortAllocatePool</strong> rule.</p>
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

[**StorPortAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff567031)
[**StorPortFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff567065)
 

 





