---
title: NdisQueryBindInstanceName rule (ndis)
description: NdisQueryBindInstanceName allocates memory for the string that specifies the friendly name. After the caller finishes using this memory, the caller must call the NdisFreeMemory function to release the memory.
ms.assetid: C332698F-8DA5-4A9A-AF2E-5D8B43815488
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisQueryBindInstanceName rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisQueryBindInstanceName
api_type:
- NA
---

# NdisQueryBindInstanceName rule (ndis)


[**NdisQueryBindInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff563748) allocates memory for the string that specifies the friendly name. After the caller finishes using this memory, the caller must call the [**NdisFreeMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562577) function to release the memory.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisQueryBindInstanceName</strong> rule.</p>
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

[**NdisFreeMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562577)
[**NdisQueryBindInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff563748)
 

 





