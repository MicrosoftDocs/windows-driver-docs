---
title: Irql\_Gather\_DMA\_Function rule (ndis)
description: The Irql\_Gather\_DMA\_Function rule specifies that the NDIS scatter/gather DMA functions must be called at correct IRQL levels.
ms.assetid: 2ac0d238-4ca0-4b07-9318-159cd9a64d35
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Gather_DMA_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Gather_DMA_Function
api_type:
- NA
---

# Irql\_Gather\_DMA\_Function rule (ndis)


The Irql\_Gather\_DMA\_Function rule specifies that the NDIS scatter/gather DMA functions must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisMAllocateNetBufferSGList**
**NdisMAllocateSharedMemoryAsyncEx**
**NdisMDeregisterScatterGatherDma**
**NdisMFreeNetBufferSGList**
**NdisMRegisterScatterGatherDma**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Gather_DMA_Function</strong> rule.</p>
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

[**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776)
[**NdisMAllocateSharedMemoryAsyncEx**](https://msdn.microsoft.com/library/windows/hardware/ff562784)
[**NdisMDeregisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563581)
[**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586)
[**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659)
 

 





