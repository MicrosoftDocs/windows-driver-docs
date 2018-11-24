---
title: VMQ Receive Path
description: VMQ Receive Path
ms.assetid: e59907fc-94dc-45c4-943d-1628c63961dc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VMQ Receive Path





A network adapter indicates a received packet on a queue only if it passes all the filter field tests for a filter that is set on that queue. For more information about filter tests, see [VMQ Filter Operations](vmq-filter-operations.md).

If the overlying protocol driver set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_PER\_QUEUE\_RECEIVE\_INDICATION** flag in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure, the miniport driver must not mix [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for other receive queues with the **NET\_BUFFER\_LIST** structures for this queue in a single call to the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. Also, the driver must set the **NDIS\_RECEIVE\_FLAGS\_SINGLE\_QUEUE** flag in the *ReceiveFlags* parameter of the **NdisMIndicateReceiveNetBufferLists** function.

If **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_PER\_QUEUE\_RECEIVE\_INDICATION** was not set, miniport drivers can link [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for frames from different VM queues and indicate them in a single call to [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). In this case, the indicated linked list of **NET\_BUFFER\_LIST** structures is not required to be sorted by queue number. **NET\_BUFFER\_LIST** structures for different queues are not required to be grouped together.

When a protocol driver sets **NDIS\_RETURN\_FLAGS\_SINGLE\_QUEUE** and it returns receive buffers, all of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures in the *NetBufferLists* parameter of the [**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534) function must belong to the same VM queue. However, protocol drivers are not required to return all the **NET\_BUFFER\_LIST** structures that were indicated in a single call to the [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) function in a single call to **NdisReturnNetBufferLists**. Also, the returned list can include **NET\_BUFFER\_LIST** structures from multiple receive indications if they belong to the same VM queue.

Protocol drivers set the **NDIS\_RETURN\_FLAGS\_SINGLE\_QUEUE** bit on the *ReturnFlags* parameter of [**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534) to indicate that all of the returned [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures belong to the same VM queue.

VMQ receive indications must include the following out of band (OOB) information in the **NetBufferListInfo** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures.

-   Specify the queue identifier in the **NetBufferListFilteringInfo** information.

-   Set the filter identifier in the **NetBufferListFilteringInfo** information to zero.

The **NetBufferListFilteringInfo** information is specified in an [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) structure. To access the NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO structure in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) OOB data, an NDIS driver calls the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro and specifies the **NetBufferListFilteringInfo** information type.

To access the filter identifier and queue identifier directly, use the [**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568406) and [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macros.

VMQ receive indications must define shared memory information at the **SharedMemoryInfo** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

**Note**  When a VMQ is deleted (for example, during VM live migration), it is possible for the miniport driver to receive an NBL that contains an invalid **QueueId** value. If this happens, the miniport should ignore the invalid queue ID and use 0 (the default queue) instead. The **QueueId** is found in the **NetBufferListFilteringInfo** portion of the NBL's OOB data, and is retrieved by using the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro.

 

To indicate that the [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) pointer at **SharedMemoryInfo** is valid, the miniport driver must set the NDIS\_RECEIVE\_FLAGS\_SHARED\_MEMORY\_INFO\_VALID flag in the *ReceiveFlags* parameter of the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. For more information about the layout of shared memory buffers in VMQ receive buffers, see [Shared Memory in Receive Buffers](shared-memory-in-receive-buffers.md).

The receive indication must include the following information in the [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

<a href="" id="nextsharedmemorysegment"></a>**NextSharedMemorySegment**  
A pointer to the next [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure in a **NULL**-terminated linked list of such structures.

<a href="" id="sharedmemoryhandle"></a>**SharedMemoryHandle**  
An NDIS shared memory handle that [**NdisAllocateSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561616) returned.

<a href="" id="sharedmemoryoffset"></a>**SharedMemoryOffset**  
An offset, in bytes, to the start of the data from the beginning of the shared memory buffer.

<a href="" id="sharedmemorylength"></a>**SharedMemoryLength**  
The length, in bytes, of the shared memory segment.

If the overlying protocol driver set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED** flag in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure, each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) includes:

-   Two MDLs and corresponding **SharedMemoryInfo** structures.

-   A post-lookahead buffer with backfill space.

If necessary, the protocol driver copies the contents of the lookahead buffer to the backfill area. However, backfill space must exist even if the packet is entirely in the lookahead buffer.

If the overlying driver does not set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED** flag, each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure includes a single MDL and a single **SharedMemoryInfo** structure.

The byte count and byte offset in the MDL and the **DataLength** and **DataOffset** members in the [**NET\_BUFFER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568381) structure are set in the same way as they are set for drivers that do not use VMQ. The **SharedMemoryLength** and **SharedMemoryOffset** members in the **SharedMemoryInfo** structure can be set once during initialization. The miniport driver is not required to update the **SharedMemoryLength** and **SharedMemoryOffset** members for every packet that is received because the overlying drivers and NDIS can use the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) **DataLength** member and the MDL byte count to determine the packet start and size.

**Note**  Starting with NDIS 6.30 and Windows Server 2012, splitting packet data into separate lookahead buffers is no longer supported. The overlying protocol driver will not set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED** flag.

 

 

 





