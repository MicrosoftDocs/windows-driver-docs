---
title: Irql\_NetBuffer\_Function rule (ndis)
description: The Irql\_NetBuffer\_Function rule specifies that the NET\_BUFFER-related functions must be called at correct IRQL levels.
ms.assetid: e3b43ba1-3b58-4bc8-9d90-7be31c9e0a09
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_NetBuffer_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




