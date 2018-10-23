---
title: NdisAllocateNetBuffer rule (ndis)
description: The NdisAllocateNetBuffer rule specifies that NdisAllocateNetBuffer and NdisFreeNetBuffer are called in alternate order. The ultimate goal is to make sure all instances of NET\_BUFFER are freed when MiniportHaltEx ends.
ms.assetid: 218708DA-ADDF-4E59-900A-4F8B5CBF00B7
ms.date: 05/21/2018
keywords: ["NdisAllocateNetBuffer rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateNetBuffer
api_type:
- NA
ms.localizationpriority: medium
---

# NdisAllocateNetBuffer rule (ndis)


The **NdisAllocateNetBuffer** rule specifies that [**NdisAllocateNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff561607) and [**NdisFreeNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562582) are called in alternate order. The ultimate goal is to make sure all instances of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) are freed when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.

The rule uses three different states. The state changes when a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) is allocated or freed. If a **NET\_BUFFER** is still allocated when the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, the rule reports the defect.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisAllocateNetBuffer</strong> rule.</p>
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

[**NdisAllocateNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff561607)
[**NdisFreeNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562582)
 

 





