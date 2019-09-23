---
title: Freeing a VM Queue
description: Freeing a VM Queue
ms.assetid: 32679638-eeef-4e11-bf56-c96f047e4de7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Freeing a VM Queue





To free a receive queue, an overlying driver issues an [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-free-queue) set OID request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_FREE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_receive_queue_free_parameters) structure with a queue identifier of type **NDIS\_RECEIVE\_QUEUE\_ID**.

[OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-free-queue) frees a receive queue that an overlying driver allocated by using the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-allocate-queue) OID. For more information about allocating a receive queue, see [Allocating a VM Queue](allocating-a-vm-queue.md).

**Note**  The default queue, which has a queue identifier of **NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID**, is always allocated and cannot be freed.

 

An overlying driver must free all the filters that it sets on a queue before it frees the queue. Also, an overlying driver must free all the receive queues that it allocated on a network adapter before it calls the [**NdisCloseAdapterEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndiscloseadapterex) function to close a binding to the network adapter. NDIS frees all the queues that are allocated on a network adapter before it calls the miniport driver's [*MiniportHaltEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_halt) function.

When a miniport driver receives a request to free a queue, it does the following:

-   Must immediately stop DMA to shared memory resources that are associated with the queue.

-   Generates a status indication to indicate that the DMA is stopped.

-   Waits for all outstanding [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures, which are associated with the queue, to be returned.

-   Frees the associated shared memory and hardware resources.

When a miniport driver receives an [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-free-queue) set request, the queue must enter the Stop DMA state, it stops the DMA on a queue and the miniport driver must indicate the status change by using the [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-receive-queue-state) status indication. For more information about queue states, see [Queue States and Operations](queue-states-and-operations.md).

After the miniport driver issues the [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-receive-queue-state) status indication, it must wait for all the pending receive indications to complete before it can free the associated shared memory. For more information about freeing shared memory, see [Shared Memory Resource Allocation](shared-memory-resource-allocation.md).

 

 





