---
title: NdisAllocateGenericObject rule (ndis)
description: The NdisAllocateGenericObject rule specifies that NdisAllocateGenericObject and NdisFreeGenericObject are called in alternate order. The ultimate goal is to make sure all generic objects are freed when MiniportHaltEx ends.
ms.assetid: A247B43F-1958-4A57-AA60-37C995A96DF7
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisAllocateGenericObject rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateGenericObject
api_type:
- NA
---

# NdisAllocateGenericObject rule (ndis)


The **NdisAllocateGenericObject** rule specifies that [**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603) and [**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850) are called in alternate order. The ultimate goal is to make sure all generic objects are freed when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.

The rule uses three different states. The state changes when an NDIS generic object is allocated or freed. If an NDIS generic object is still allocated when the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, the rule will fail.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisAllocateGenericObject</strong> rule.</p>
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

[**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603)
[**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850)
 

 





