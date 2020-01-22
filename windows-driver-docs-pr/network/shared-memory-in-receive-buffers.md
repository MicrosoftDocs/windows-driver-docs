---
title: Shared Memory in Receive Buffers
description: Shared Memory in Receive Buffers
ms.assetid: 3e4d0534-3cbd-40df-b7c1-4f2c15bcd757
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Shared Memory in Receive Buffers





This section describes the layout of the shared memory in VMQ receive buffers.For more information about using the buffers in receive indications, see [VMQ Receive Path](vmq-receive-path.md).

If the overlying protocol driver set the NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED flag in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_parameters) structure, the network adapter should split a received packet at an offset equal to or greater than the requested lookahead size and use DMA to transfer the lookahead data and the post-lookahead data to separate shared memory segments.

Miniport drivers specify the settings for the lookahead type (**NdisSharedMemoryUsageReceiveLookahead**) or other shared memory types when the shared memory is allocated. For example, the miniport driver calls the [**NdisAllocateSharedMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatesharedmemory) function and sets the **Usage** member in the [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_shared_memory_parameters) structure to **NdisSharedMemoryUsageReceiveLookahead**. Miniport drivers should allocated shared memory for a queue when the queue allocation is complete. For information about allocating and freeing shared memory resources for queues, see [Shared Memory Resource Allocation](shared-memory-resource-allocation.md).

The following illustration shows the relationships for the network data when the incoming data is split into two shared memory buffers.

![diagram illustrating the relationships for the network data when the incoming data is split into two shared memory buffers](images/vmqpacket.png)

The [**NET\_BUFFER\_SHARED\_MEMORY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_shared_memory) structure specifies shared memory information. There can be a linked list of such shared memory buffers that are associated with a [**NET\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer) structure.

Use the [**NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-shared-mem-next-segment), [**NET\_BUFFER\_SHARED\_MEM\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-shared-mem-flags), [**NET\_BUFFER\_SHARED\_MEM\_HANDLE**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-shared-mem-handle), [**NET\_BUFFER\_SHARED\_MEM\_OFFSET**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-shared-mem-offset), and [**NET\_BUFFER\_SHARED\_MEM\_LENGTH**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-shared-mem-length) macros to access the NET\_BUFFER\_SHARED\_MEMORY in a NET\_BUFFER structure. The **SharedMemoryInfo** member of the NET\_BUFFER structure contains the first NET\_BUFFER\_SHARED\_MEMORY structure in the linked list.

**Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Starting with Windows Server 2012, the overlying protocol driver will not set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED** flag in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_parameters) structure.

 

 

 





