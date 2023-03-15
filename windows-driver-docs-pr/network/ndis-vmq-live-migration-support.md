---
title: NDIS VMQ Live Migration Support
description: NDIS VMQ Live Migration Support
ms.date: 03/02/2023
---

# NDIS VMQ Live Migration Support





To support live migration, a virtual machine (VM) can be paused at any instruction or pending I/O boundary. That is, the VM might not finish pending receive requests. So, the network virtual service provider (VSP) returns all of the received packets to the underlying network adapter that the VM did not return.

**Note**  In Hyper-V, a child partition is also known as a VM.

 

When the VM is restarted on another host, the network VSP on the new host handles the receive packets that the resumed VM returns and does not pass them down to the new underlying in miniport driver. After the migration is complete, the receive queue that was associated with the VM is freed and it can be reused for another VM.

**Note**  The new network adapter might not support VMQ.

 

When NDIS requests a miniport driver to free a VMQ receive queue, it follows these steps:

1.  The network adapter stops the DMA transfer of data to receive buffers that are associated with the receive queue, after which the queue must enter the DMA Stopped state. The network adapter probably stopped the DMA activity when it received the [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](./oid-receive-filter-clear-filter.md) OID request to clear the last set filter on the receive queue.

2.  The miniport driver generates an [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](./ndis-status-receive-queue-state.md) status indication with the **QueueState** member of the [**NDIS\_RECEIVE\_QUEUE\_STATE**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_receive_queue_state) structure set to **NdisReceiveQueueOperationalStateDmaStopped** to notify NDIS that the DMA transfer has been stopped.

3.  The miniport driver waits for all the indicated receive packets for that queue to be returned to the miniport driver.

4.  The miniport driver frees all the shared memory that it allocated for the network adapter's receive buffers that are associated with the queue by calling [**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory).

5.  The miniport driver completes the [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](./oid-receive-filter-free-queue.md) OID request to free the receive queue.

For more information about queue states, see [NDIS VM Queue States](ndis-virtual-machine-queue-states.md).

 

