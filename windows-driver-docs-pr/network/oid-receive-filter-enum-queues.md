---
title: OID_RECEIVE_FILTER_ENUM_QUEUES
description: Overlying drivers and user-mode applications issue object identifier (OID) query requests of OID_RECEIVE_FILTER_ENUM_QUEUES to obtain a list of all the receive queues that are allocated on a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_ENUM_QUEUES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_ENUM\_QUEUES


Overlying drivers and user-mode applications issue object identifier (OID) query requests of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES to obtain a list of all the receive queues that are allocated on a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info_array) structure that is followed by an [**NDIS\_RECEIVE\_QUEUE\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info) structure for each filter.

## Remarks

NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md) and [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md) OID requests.

Overlying drivers and user-mode applications issue OID query requests of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES to enumerate the receive queues on a network adapter.

If a protocol driver issues the request, the request type inside the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure is set to **NdisRequestQueryInformation** and this OID returns an array of all the receive queues that the protocol driver allocated on the network adapter. If a user-mode application issued the request, the request type inside the **NDIS\_OID\_REQUEST** structure is set to **NdisRequestQueryStatistics**, and this OID returns an array of information for all the receive queues on the network adapter.

### Return Status Codes

NDIS handles the OID query request of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES for miniport drivers, and returns one of the following status codes.

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info_array" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_QUEUE_INFO_ARRAY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info_array)"><strong>NDIS_RECEIVE_QUEUE_INFO_ARRAY</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request has completed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_RECEIVE\_QUEUE\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info)

[**NDIS\_RECEIVE\_QUEUE\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info_array)

[OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md)

[OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md)

