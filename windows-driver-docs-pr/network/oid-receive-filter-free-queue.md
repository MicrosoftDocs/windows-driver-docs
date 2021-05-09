---
title: OID_RECEIVE_FILTER_FREE_QUEUE
description: NDIS protocol drivers issue object identifier (OID) set requests of OID_RECEIVE_FILTER_FREE_QUEUE to free a receive queue.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_FREE_QUEUE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_FREE\_QUEUE


NDIS protocol drivers issue object identifier (OID) set requests of OID\_RECEIVE\_FILTER\_FREE\_QUEUE to free a receive queue.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_FREE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_free_parameters) structure with a queue identifier of type **NDIS\_RECEIVE\_QUEUE\_ID**.

## Remarks

The OID set request of OID\_RECEIVE\_FILTER\_FREE\_QUEUE is optional for NDIS 6.20 and later miniport drivers. It is mandatory for miniport drivers that support the virtual machine queue interface.

After an overlying driver issues the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md) OID to allocate a receive queue, it issues the OID\_RECEIVE\_FILTER\_FREE\_QUEUE OID to free the receive queue.

When NDIS requests a miniport driver to free a VMQ receive queue, it follows these steps:

1.  The network adapter stops the DMA transfer of data to receive buffers that are associated with the receive queue, after which the queue must enter the DMA Stopped state. The network adapter probably stopped the DMA activity when it received the [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](oid-receive-filter-clear-filter.md) OID request to clear the last set filter on the receive queue.

2.  The miniport driver generates an [**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](./ndis-status-receive-queue-state.md) status indication with the **QueueState** member of the [**NDIS\_RECEIVE\_QUEUE\_STATE**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_receive_queue_state) structure set to **NdisReceiveQueueOperationalStateDmaStopped** to notify NDIS that the DMA transfer has been stopped.

3.  The miniport driver waits for all the indicated receive packets for that queue to be returned to the miniport driver.

4.  The miniport driver frees all the shared memory that it allocated for the network adapter's receive buffers that are associated with the queue by calling [**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory).

5.  The miniport driver completes the OID\_RECEIVE\_FILTER\_FREE\_QUEUE OID request to free the receive queue.

Miniport drivers call the [**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory) function to free shared memory for a queue. If the miniport driver allocated the shared memory for a nondefault queue, the driver frees the shared memory in the context of the OID\_RECEIVE\_FILTER\_FREE\_QUEUE OID while it is freeing the queue. Miniport drivers free shared memory that they allocated for the default queue in the context of the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function.

An overlying driver must free all the filters that it set on a queue before it frees the queue. Also, an overlying driver must free all the receive queues that it allocated on a network adapter before it calls the [**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex) function to close a binding to the network adapter. NDIS frees all the queues that are allocated on a network adapter before it calls the miniport driver's [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function.

### Return Status Codes

The miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)"><strong>NdisMOidRequestComplete</strong></a> function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset)"><em>MiniportResetEx</em></a> function.</p></td>
</tr>
</tbody>
</table>

 

NDIS returns one of the following status codes for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The requested queue was freed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler for the caller after the request has completed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_PARAMETER</strong></p></td>
<td><p>The queue identifier is invalid.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer is too short. NDIS sets the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_RECEIVE\_QUEUE\_FREE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_free_parameters)

[**NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE**](./ndis-status-receive-queue-state.md)

[**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex)

[**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory)

[OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md)

