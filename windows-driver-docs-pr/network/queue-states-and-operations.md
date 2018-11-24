---
title: Queue States and Operations
description: Queue States and Operations
ms.assetid: 892f8f19-b94e-4950-af88-334c9a8b8c0d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Queue States and Operations





For each queue, a network adapter must support the following set of operational states:

<a href="" id="undefined"></a>Undefined  
The queue is not allocated. To allocate a queue, an overlying driver sends an [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569784) OID request.

<a href="" id="allocated"></a>Allocated  
The *Allocated* state is the initial state for a queue. When a queue is in the Allocated state, the overlying driver usually sets filters on the queue with the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) OID or completes the queue allocation with the [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) OID request.

<a href="" id="set"></a>Set  
In the *Set* state, a queue has at least one filter allocated but the overlying driver has not sent the [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) OID.

<a href="" id="running"></a>Running  
In the *Running* state, the queue has filters set, the queue allocation is complete and the miniport adapter is indicating receive packets for the queue.

<a href="" id="paused"></a>Paused  
In the *Paused* state, the network adapter does not indicate received network data for the queue. Either there were no filters set on the queue before the [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) OID request or all of the filters that were set on the queue were cleared with the [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569785) OID request.

<a href="" id="dma-stopped"></a>DMA Stopped  
In the *DMA Stopped* state, a miniport driver received an [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789) OID request. When the DMA is stopped and the driver has issued the DMA-stopped status indication (with [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567417)), the driver enters the Freeing state.

<a href="" id="freeing"></a>Freeing  
In the *Freeing* state, a miniport driver completes the operations that are required to stop send and receive operations for the queue, and releases the associated resources. After all of the outstanding receive indications are complete, the queue is deleted and the queue is Undefined.

In the following table, the headings are the queue states. Major events are listed in the first column. The rest of the entries in the table specify the next state that the queue enters after an event occurs within a state. The blank entries represent invalid event/state combinations.

<table>
<colgroup>
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event \ State</th>
<th align="left">Undefined</th>
<th align="left">Allocated</th>
<th align="left">Set</th>
<th align="left">Running</th>
<th align="left">Paused</th>
<th align="left">Stop DMA</th>
<th align="left">Freeing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_ALLOCATE_QUEUE - method (set)</p></td>
<td align="left"><p>Allocated</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_QUEUE_PARAMETERS - method (query) request</p></td>
<td align="left"></td>
<td align="left"><p>Allocated</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_QUEUE_PARAMETERS - set request</p></td>
<td align="left"></td>
<td align="left"><p>Allocated</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_SET_FILTER - method (set) request</p></td>
<td align="left"></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_CLEAR_FILTER - set request (last filter)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Allocated</p></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_CLEAR_FILTER - set request (not last filter)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_ENUM_FILTERS - method (query request)</p></td>
<td align="left"></td>
<td align="left"><p>Allocated</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_PARAMETERS - method (query) request</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE - method (set) request</p></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Receive packet</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>OID_RECEIVE_FILTER_FREE_QUEUE set request</p></td>
<td align="left"></td>
<td align="left"><p>Stop DMA</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Stop DMA</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DMA is stopped and NDIS_STATUS_RECEIVE_QUEUE_STATE status indication was sent (Note: DMA was probably already stopped in Allocated or Paused state)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Freeing</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>All receive indications are complete and the queue resources are freed</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Undefined</p></td>
</tr>
</tbody>
</table>

 

**Note**  The events listed in the preceding table include some secondary events that do not result in a state change. These secondary events are included in the table to specify the states where these events are valid.

 

The primary queue events are defined as follows:

<a href="" id="oid-receive-filter-allocate-queue---method--set--request"></a>OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE - method (set) request  
An overlying driver allocated a queue. For more information about allocating queues, see [Allocating and Freeing VM Queues](allocating-and-freeing-vm-queues.md).

<a href="" id="oid-receive-filter-set-filter---method--set--request"></a>OID\_RECEIVE\_FILTER\_SET\_FILTER - method (set) request  
An overlying driver set a filter on a queue. If the overlying driver has not sent the [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) OID, the queue is in the Set state. Otherwise, the queue is in the Running state. For more information about setting filters on queues, see [Setting and Clearing VMQ Filters](setting-and-clearing-vmq-filters.md).

<a href="" id="oid-receive-filter-clear-filter---set-request"></a>OID\_RECEIVE\_FILTER\_CLEAR\_FILTER - set request  
An overlying driver cleared a filter on a queue. If the last filter was cleared on a running queue, the DMA can be stopped; receive indications are stopped and the queue should be cleared of received data, if any. For more information about clearing filters on queues, see [Setting and Clearing VMQ Filters](setting-and-clearing-vmq-filters.md).

<a href="" id="oid-receive-filter-queue-allocation-complete---method--set--request"></a>OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE - method (set) request  
An overlying driver completed the queue allocation. If there are filters set on the queue, it is in the Running state and receive indications can start. For more information about completing queue allocation, see [Allocating and Freeing VM Queues](allocating-and-freeing-vm-queues.md).

<a href="" id="receive-packet"></a>Receive packet  
A miniport driver can only indicate receive packets for a queue that is in the Running state. For more information about indicating received data for queues, see [VMQ Send and Receive Operations](vmq-send-and-receive-operations.md).

<a href="" id="oid-receive-filter-free-queue-set-request-"></a>OID\_RECEIVE\_FILTER\_FREE\_QUEUE set request.  
An overlying driver freed a queue. The driver issues the DMA-stopped status indication (with [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567417)), the driver enters the Freeing state. When all of the outstanding receive indications are complete and the queue resources are freed, the queue is undefined.

 

 





