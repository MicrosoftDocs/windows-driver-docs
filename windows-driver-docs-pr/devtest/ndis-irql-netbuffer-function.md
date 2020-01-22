---
title: Irql\_NetBuffer\_Function rule (ndis)
description: The Irql\_NetBuffer\_Function rule specifies that the NET\_BUFFER-related functions must be called at correct IRQL levels.
ms.assetid: e3b43ba1-3b58-4bc8-9d90-7be31c9e0a09
ms.date: 05/21/2018
keywords: ["Irql_NetBuffer_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_NetBuffer_Function
api_type:
- NA
ms.localizationpriority: medium
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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Irql_NetBuffer_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisAdvanceNetBufferDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisadvancenetbufferdatastart)
[**NdisAdvanceNetBufferListDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisadvancenetbufferlistdatastart)
[**NdisAllocateCloneNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateclonenetbufferlist)
[**NdisAllocateFragmentNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatefragmentnetbufferlist)
[**NdisAllocateMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatemdl)
[**NdisAllocateNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbuffer)
[**NdisAllocateNetBufferAndNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferandnetbufferlist)
[**NdisAllocateNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferlist)
[**NdisAllocateNetBufferListContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferlistcontext)
[**NdisAllocateNetBufferListPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferlistpool)
[**NdisAllocateNetBufferMdlAndData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbuffermdlanddata)
[**NdisAllocateNetBufferPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferpool)
[**NdisAllocateReassembledNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatereassemblednetbufferlist)
[**NdisCopyFromNetBufferToNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscopyfromnetbuffertonetbuffer)
[**NdisCopyReceiveNetBufferListInfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscopyreceivenetbufferlistinfo)
[**NdisCopySendNetBufferListInfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscopysendnetbufferlistinfo)
[**NdisFreeCloneNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreeclonenetbufferlist)
[**NdisFreeFragmentNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreefragmentnetbufferlist)
[**NdisFreeMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreemdl)
[**NdisFreeNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbuffer)
[**NdisFreeNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbufferlist)
[**NdisFreeNetBufferListContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbufferlistcontext)
[**NdisFreeNetBufferListPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbufferlistpool)
[**NdisFreeNetBufferPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbufferpool)
[**NdisFreeReassembledNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreereassemblednetbufferlist)
[**NdisGetDataBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetdatabuffer)
[**NdisGetMdlPhysicalArraySize**](https://docs.microsoft.com/windows-hardware/drivers/network/ndisgetmdlphysicalarraysize)
[**NdisGetPoolFromNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetpoolfromnetbuffer)
[**NdisGetPoolFromNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetpoolfromnetbufferlist)
[**NdisQueryMdl**](https://docs.microsoft.com/windows-hardware/drivers/network/ndisquerymdl)
[**NdisQueryMdlOffset**](https://docs.microsoft.com/windows-hardware/drivers/network/ndisquerymdloffset)
[**NdisQueryNetBufferPhysicalCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisquerynetbufferphysicalcount)
[**NdisRetreatNetBufferDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisretreatnetbufferdatastart)
[**NdisRetreatNetBufferListDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisretreatnetbufferlistdatastart)








