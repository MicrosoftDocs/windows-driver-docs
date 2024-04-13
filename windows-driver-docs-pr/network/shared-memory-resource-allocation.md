---
title: Shared Memory Resource Allocation
description: Shared Memory Resource Allocation
ms.date: 04/20/2017
---

# Shared Memory Resource Allocation





To allocate shared memory resources for a VM queue, a miniport driver calls the [**NdisAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatesharedmemory) function. For example, the miniport driver allocates shared memory when it receives the [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](./oid-receive-filter-queue-allocation-complete.md) OID. Also, a miniport driver can allocate shared memory for the default queue during network adapter initialization. For more information about allocating queues, see [Allocating a VM Queue](allocating-a-vm-queue.md).

The miniport driver can allocate more memory for the queue until the queue is freed. For more information about freeing a queue, see [Freeing a VM Queue](freeing-a-vm-queue.md).

The [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_shared_memory_parameters) structure specifies the shared memory parameters for a shared memory allocation request. Miniport drivers pass this structure to the [**NdisAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatesharedmemory) function. NDIS passes this structure to the [**NetAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nc-ndis-allocate_shared_memory_handler) function (that is, the ALLOCATE\_SHARED\_MEMORY\_HANDLER entry point).

When a miniport driver allocates shared memory, it specifies the following:

-   Queue identifier.

-   Shared memory length.

-   How the shared memory is used. For example, the miniport driver specifies **NdisSharedMemoryUsageReceive** if the shared memory is to be used for receive buffers.

If the NDIS\_SHARED\_MEM\_PARAMETERS\_CONTIGOUS flag is not set in the **Flags** member, shared memory can be specified in a scatter-gather list that is contained in non-contiguous memory.

The [**NDIS\_SHARED\_MEMORY\_USAGE**](/windows-hardware/drivers/ddi/ndis/ne-ndis-_ndis_shared_memory_usage) enumeration specifies how shared memory is used. The NDIS\_SHARED\_MEMORY\_USAGE enumeration is used in the [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_shared_memory_parameters) and [**NDIS\_SCATTER\_GATHER\_LIST\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_scatter_gather_list_parameters) structures. For information about shared memory parameters in VMQ receive data buffers, see [Shared Memory in Receive Buffers](shared-memory-in-receive-buffers.md).

The [**NdisAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatesharedmemory) function provides the following to the caller:

-   Virtual address of the allocated memory.

-   Scatter-gather list.

-   Shared memory handle - for receive indications.

-   Allocation handle - used to identify the memory later.

Miniport drivers call the [**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory) function to free shared memory for a queue. If the miniport driver allocated the shared memory for a nondefault queue, it frees the shared memory in the context of the [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](./oid-receive-filter-free-queue.md) OID while it is freeing the queue. Miniport drivers free shared memory that they allocated for the default queue in the context of the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function.

 

