---
title: Irql\_NetBuffer\_Function rule (ndis)
description: The Irql\_NetBuffer\_Function rule specifies that the NET\_BUFFER-related functions must be called at correct IRQL levels.
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

**Driver model: NDIS**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Irql_NetBuffer_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**NdisAdvanceNetBufferDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisadvancenetbufferdatastart)
[**NdisAdvanceNetBufferListDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisadvancenetbufferlistdatastart)
[**NdisAllocateCloneNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocateclonenetbufferlist)
[**NdisAllocateFragmentNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatefragmentnetbufferlist)
[**NdisAllocateMdl**](/windows-hardware/drivers/ddi/mdlapi/nf-mdlapi-ndisallocatemdl)
[**NdisAllocateNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbuffer)
[**NdisAllocateNetBufferAndNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferandnetbufferlist)
[**NdisAllocateNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlist)
[**NdisAllocateNetBufferListContext**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistcontext)
[**NdisAllocateNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool)
[**NdisAllocateNetBufferMdlAndData**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbuffermdlanddata)
[**NdisAllocateNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferpool)
[**NdisAllocateReassembledNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatereassemblednetbufferlist)
[**NdisCopyFromNetBufferToNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndiscopyfromnetbuffertonetbuffer)
[**NdisCopyReceiveNetBufferListInfo**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndiscopyreceivenetbufferlistinfo)
[**NdisCopySendNetBufferListInfo**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndiscopysendnetbufferlistinfo)
[**NdisFreeCloneNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreeclonenetbufferlist)
[**NdisFreeFragmentNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreefragmentnetbufferlist)
[**NdisFreeMdl**](/windows-hardware/drivers/ddi/mdlapi/nf-mdlapi-ndisfreemdl)
[**NdisFreeNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbuffer)
[**NdisFreeNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlist)
[**NdisFreeNetBufferListContext**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlistcontext)
[**NdisFreeNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlistpool)
[**NdisFreeNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferpool)
[**NdisFreeReassembledNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreereassemblednetbufferlist)
[**NdisGetDataBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisgetdatabuffer)
[**NdisGetMdlPhysicalArraySize**](../network/ndisgetmdlphysicalarraysize.md)
[**NdisGetPoolFromNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisgetpoolfromnetbuffer)
[**NdisGetPoolFromNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisgetpoolfromnetbufferlist)
[**NdisQueryMdl**](../network/ndisquerymdl.md)
[**NdisQueryMdlOffset**](../network/ndisquerymdloffset.md)
[**NdisQueryNetBufferPhysicalCount**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisquerynetbufferphysicalcount)
[**NdisRetreatNetBufferDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisretreatnetbufferdatastart)
[**NdisRetreatNetBufferListDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisretreatnetbufferlistdatastart)
