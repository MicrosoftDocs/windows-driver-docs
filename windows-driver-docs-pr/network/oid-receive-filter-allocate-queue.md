---
title: OID_RECEIVE_FILTER_ALLOCATE_QUEUE
description: Overlying drivers issue object identifier (OID) method requests of OID_RECEIVE_FILTER_ALLOCATE_QUEUE to allocate a queue that has an initial set of configuration parameters.
ms.assetid: 8dd7ab91-b752-46fd-ae1b-014dc0fb0157
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_ALLOCATE_QUEUE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE


Overlying drivers issue object identifier (OID) method requests of OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE to allocate a queue that has an initial set of configuration parameters.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** structure that has a new queue identifier.

Remarks
-------

The OID method request of OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE is optional for NDIS 6.20 and later miniport drivers. It is mandatory for miniport drivers that support the virtual machine queue (VMQ) interface.

The overlying driver initializes the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure with its requested queue configuration. NDIS assigns a queue identifier in the **QueueId** member of the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** structure and passes the method request to the miniport driver.

**Note**  The overlying driver can set the **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_PER\_QUEUE\_RECEIVE\_INDICATION** and **NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_LOOKAHEAD\_SPLIT\_REQUIRED** flags in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. The other flags are not used for queue allocation.

 

After a miniport driver is issued an OID request of OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE and handles it successfully, the queue is in the Paused state.

The overlying driver must use the queue identifier that NDIS provides in subsequent OID requests, for example, to modify the queue parameters or free the queue. The queue identifier is also included in the out-of-band (OOB) data on all [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that are associated with the queue. Drivers use the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro to retrieve the queue identifier in a **NET\_BUFFER\_LIST** structure.

When NDIS receives an OID request to allocate a receive queue, it verifies the queue parameters. After NDIS allocates the necessary resources and the queue identifier, it submits the OID request to the underlying miniport driver. The queue identifier is unique to the associated network adapter.

If the miniport driver can successfully allocate the necessary software and hardware resources for the receive queue, it completes the OID request by returning **NDIS\_STATUS\_SUCCESS**.

The miniport driver must retain the queue identifiers for the allocated receive queues. NDIS uses the queue identifier of a receive queue for subsequent calls to the miniport driver in order to set a receive filter on the receive queue, change the receive queue parameters, or free the receive queue.

After an overlying driver allocates one or more receive queues and optionally sets the initial filters, it must issue [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](oid-receive-filter-queue-allocation-complete.md) set OID requests to notify the miniport driver that the allocation is complete for the current batch of receive queues.

The miniport driver must not retain any packets in a receive queue if there are no filters set on that queue. If either a queue never had any filters set or all the filters were cleared, the queue should be empty and any packets should be discarded. That is, the packets are not indicated up the driver stack or retained in the queue.

Overlying drivers use OID requests of [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](oid-receive-filter-free-queue.md) to free queues that they allocate.

### Return Status Codes

Either NDIS or the miniport driver returns one of the following status codes for the OID method request of OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE.

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
<td><p>The queue was allocated successfully. The information buffer contains the updated <a href="https://msdn.microsoft.com/library/windows/hardware/ff567211" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_QUEUE_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567211)"><strong>NDIS_RECEIVE_QUEUE_PARAMETERS</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. The final status code and results will be passed to an OID request completion handler of the caller.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_PARAMETER</strong></p></td>
<td><p>One or more of the parameters that the overlying driver provided were not valid.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

 

Requirements
------------

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


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407)

[OID\_RECEIVE\_FILTER\_FREE\_QUEUE](oid-receive-filter-free-queue.md)

[OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](oid-receive-filter-queue-allocation-complete.md)

[**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211)

 

 




