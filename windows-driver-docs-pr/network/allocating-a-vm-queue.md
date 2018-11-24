---
title: Allocating a VM Queue
description: Allocating a VM Queue
ms.assetid: 2645a6e5-3824-469c-84d5-8e49fa01f494
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating a VM Queue





To allocate a queue with an initial set of configuration parameters, an overlying driver issues an [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569784) method OID request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** structure that has a new queue identifier and an MSI-X table entry.

The [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure is used in the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569784) OID and the [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569794) OID. For more information about VM queue parameters, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md).

The overlying driver initializes the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure with the following queue configuration parameters:

-   The queue type (**NdisReceiveQueueTypeVMQueue** from the [**NDIS\_RECEIVE\_QUEUE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567217) enumeration.)

-   The processor affinity for the queue.

-   The queue name and the virtual machine name.

-   The lookahead-split parameters.

    **Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported.

     

**Note**  The overlying driver can set the NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_PER\_QUEUE\_RECEIVE\_INDICATION and NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED flags in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. The other flags are not used for queue allocation.

 

When NDIS receives an OID request to allocate a receive queue, it verifies the queue parameters. After NDIS allocates the necessary resources and the queue identifier, it submits the OID request to the underlying miniport driver. The queue identifier is unique to the associated network adapter.

If the miniport driver can successfully allocate the necessary software and hardware resources for the receive queue, it completes the OID request with a success status.

Before NDIS sends the OID request to the miniport driver, NDIS assigns a queue identifier in the **QueueId** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure and passes the method request to the miniport driver. The miniport driver provides the MSI-X table entry in the **MSIXTableEntry** member.

The miniport driver must retain the queue identifiers for the allocated receive queues. NDIS uses the queue identifier of a receive queue for subsequent calls to the miniport driver to set a receive filter on the receive queue, change the receive queue parameters, or free the receive queue.

**Note**  The default queue (queue identifier zero) is always allocated and cannot be freed.

 

The overlying driver must use the queue identifier that NDIS provides in subsequent OID requests, for example, to modify the queue parameters or free the queue. The queue identifier is also included in the OOB data on all [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that are associated with the queue. Drivers use the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro to retrieve the queue identifier in a NET\_BUFFER\_LIST structure.

**Note**  A protocol driver can set VMQ filters at any time after it successfully allocates a queue and before the queue is deleted.

 

The protocol driver issues an [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) method OID request to complete the queue allocation. The miniport driver can allocate shared memory and other resources when the allocation is complete. For more information about allocating shared memory resources, see [Shared Memory Resource Allocation](shared-memory-resource-allocation.md).

After a miniport driver receives an OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION OID request and handles it successfully, the queue is in the *Allocated* state. For more information about queue states, see [Queue States and Operations](queue-states-and-operations.md).

After an overlying driver allocates one or more receive queues (and optionally sets the initial filters), it must issue [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) set OID requests to notify the miniport driver that the allocation is complete for the current batch of receive queues.

The miniport driver must not retain any packets in a receive queue if there are no filters set on that queue. If a queue never had any filters set or all the filters were cleared, the queue should be empty and any packets should be discarded. That is, they are not indicated up the driver stack or retained in the queue.

Overlying drivers use the [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789) OID to free queues that they allocate. For more information about freeing queues, see [Freeing a VM Queue](freeing-a-vm-queue.md).

 

 





