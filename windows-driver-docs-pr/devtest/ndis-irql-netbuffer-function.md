---
title: Irql\_NetBuffer\_Function rule (ndis)
description: The Irql\_NetBuffer\_Function rule specifies that the NET\_BUFFER-related functions must be called at correct IRQL levels.
ms.assetid: e3b43ba1-3b58-4bc8-9d90-7be31c9e0a09
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_NetBuffer_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_NetBuffer_Function
api_type:
- NA
---

# Irql\_NetBuffer\_Function rule (ndis)


The Irql\_NetBuffer\_Function rule specifies that the NET\_BUFFER-related functions must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisAdvanceNetBufferDataStart**
**disAdvanceNetBufferListDataStart**
**NdisAllocateCloneNetBufferList**
**NdisAllocateFragmentNetBufferList**
**NdisAllocateMdl**
**NdisAllocateNetBuffer**
**NdisAllocateNetBufferAndNetBufferList**
**NdisAllocateNetBufferList**
**NdisAllocateNetBufferListContext**
**NdisAllocateNetBufferListPool**
**NdisAllocateNetBufferMdlAndData**
**NdisAllocateNetBufferPool**
**NdisAllocateReassembledNetBufferList**
**NdisCopyFromNetBufferToNetBuffer**
**NdisCopyReceiveNetBufferListInfo**
**NdisCopySendNetBufferListInfo**
**NdisFreeCloneNetBufferList**
**NdisFreeFragmentNetBufferList**
**NdisFreeMdl**
**NdisFreeNetBuffer**
**NdisFreeNetBufferList**
**NdisFreeNetBufferListContext**
**NdisFreeNetBufferListPool**
**NdisFreeNetBufferPool**
**NdisFreeReassembledNetBufferList**
**NdisGetDataBuffer**
**NdisGetMdlPhysicalArraySize**
**NdisGetPoolFromNetBuffer**
**NdisGetPoolFromNetBufferList**
**NdisQueryMdl**
**NdisQueryMdlOffset**
**NdisQueryNetBufferPhysicalCount**
**NdisRetreatNetBufferDataStart**
**NdisRetreatNetBufferListDataStart**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_NetBuffer_Function</strong> rule.</p>
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

[**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703)
[**NdisAdvanceNetBufferListDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560704)
[**NdisAllocateCloneNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff560705)
[**NdisAllocateFragmentNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff560707)
[**NdisAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff561605)
[**NdisAllocateNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff561607)
[**NdisAllocateNetBufferAndNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561608)
[**NdisAllocateNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561609)
[**NdisAllocateNetBufferListContext**](https://msdn.microsoft.com/library/windows/hardware/ff561610)
[**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611)
[**NdisAllocateNetBufferMdlAndData**](https://msdn.microsoft.com/library/windows/hardware/ff561612)
[**NdisAllocateNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff561613)
[**NdisAllocateReassembledNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561614)
[**NdisCopyFromNetBufferToNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff561718)
[**NdisCopyReceiveNetBufferListInfo**](https://msdn.microsoft.com/library/windows/hardware/ff561722)
[**NdisCopySendNetBufferListInfo**](https://msdn.microsoft.com/library/windows/hardware/ff561724)
[**NdisFreeCloneNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561841)
[**NdisFreeFragmentNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561847)
[**NdisFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff562575)
[**NdisFreeNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562582)
[**NdisFreeNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff562583)
[**NdisFreeNetBufferListContext**](https://msdn.microsoft.com/library/windows/hardware/ff562587)
[**NdisFreeNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff562590)
[**NdisFreeNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff562592)
[**NdisFreeReassembledNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff562594)
[**NdisGetDataBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562631)
[**NdisGetMdlPhysicalArraySize**](https://msdn.microsoft.com/library/windows/hardware/ff562639)
[**NdisGetPoolFromNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562657)
[**NdisGetPoolFromNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff562659)
[**NdisQueryMdl**](https://msdn.microsoft.com/library/windows/hardware/ff563757)
[**NdisQueryMdlOffset**](https://msdn.microsoft.com/library/windows/hardware/ff563761)
[**NdisQueryNetBufferPhysicalCount**](https://msdn.microsoft.com/library/windows/hardware/ff563766)
[**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527)
[**NdisRetreatNetBufferListDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564529)
 

 





