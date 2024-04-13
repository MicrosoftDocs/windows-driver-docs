---
title: OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE
ms.topic: reference
description: NDIS protocol drivers issue object identifier (OID) method requests of OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE to notify the miniport driver that an allocation has completed for the current batch of receive queues.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE Network Drivers Starting with Windows Vista
---

# OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE


NDIS protocol drivers issue object identifier (OID) method requests of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE to notify the miniport driver that an allocation has completed for the current batch of receive queues.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_array) structure that is followed by an [**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_parameters) structure for each queue. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to the same array of structures, and the **CompletionStatus** member of each **NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS** structure contains the completion status for each queue.

## Remarks

The OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE is optional for NDIS 6.20 and later miniport drivers. It is mandatory for miniport drivers that support the virtual machine queue (VMQ) interface.

After allocating one or more receive queues and optionally setting the initial filters, the protocol driver must issue the OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE in order to notify the miniport driver that the allocation has completed for the current batch of receive queues. This allows the miniport driver to balance the hardware resources among multiple receive queues; if necessary, it can allocate resources such as shared memory for the receive queues.

After a miniport driver receives an OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE request and it has filters that are set on the queue, the queue is in the Running state. In this state, the miniport driver can start indications of packets in the queue by calling [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists).

### Return Status Codes

The miniport driver returns one of the following status codes for the OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE.

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
<td><p>The queue allocation has completed. The information buffer contains the updated <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_array" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_QUEUE_ALLOCATION_COMPLETE_ARRAY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_array)"><strong>NDIS_RECEIVE_QUEUE_ALLOCATION_COMPLETE_ARRAY</strong></a> structure and parameter structures with the completion status for the queue allocation.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_PARAMETER</strong></p></td>
<td><p>One or more of the parameters that the overlying driver provided were not valid.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_SUPPORTED</strong></p></td>
<td><p>The NDIS version of the miniport driver is earlier than version 6.20.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_FAILURE</strong></p></td>
<td><p>The request failed for other reasons.</p></td>
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


[**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_array)

[**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_allocation_complete_parameters)

