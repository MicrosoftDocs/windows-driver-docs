---
title: OID_RECEIVE_FILTER_ENUM_FILTERS
description: An overlying driver issues an OID method request of OID_RECEIVE_FILTER_ENUM_FILTERS to obtain a list of all the filters that are configured on a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_ENUM_FILTERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_ENUM\_FILTERS


An overlying driver issues an OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS to obtain a list of all the filters that are configured on a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure.

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure that specifies a list of receive filters that are currently configured on a miniport driver.

-   An array of [**NDIS\_RECEIVE\_FILTER\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info) structures. Each structure specifies the parameters of a receive filter that is currently configured on a miniport driver.

## Remarks

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](./ndis-packet-coalescing.md). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](./guidelines-for-managing-packet-coalescing-receive-filters.md).

-   [Single Root I/O Virtualization (SR-IOV)](./single-root-i-o-virtualization--sr-iov-.md). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](./setting-a-receive-filter-on-a-virtual-port.md).

-   [Virtual Machine Queue (VMQ)](./virtual-machine-queue--vmq--in-ndis-6-20.md). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](./setting-and-clearing-vmq-filters.md).

Overlying drivers or applications issue OID method requests of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS to enumerate the receive filters that were set on a network adapter. This includes receive filters that were set on an SR-IOV virtual port (VPort) or a VMQ receive queue.

### Additional Guidelines for the NDIS Packet Coalescing Interface

Starting with Windows Server 2012, NDIS packet coalescing only supports the default receive queue of a network adapter.

To enumerate the packet coalescing receive filters, the overlying driver must set the **QueueId** member of the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

### Additional Guidelines for the SR-IOV Interface

Starting with Windows Server 2012, the SR-IOV interface only supports the default receive queue of a virtual port (VPort).

To enumerate the VPort receive filters, the overlying driver must set the **QueueId** member of the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

### Additional Guidelines for the VMQ Interface

An overlying driver can issue OID method requests of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS to enumerate the receive filters that were set on a VMQ receive queue. When the overlying driver initializes the [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure, it sets the **QueueId** member to one of the following values:

-   The queue identifier value for a nondefault receive queue. The overlying driver obtained the queue identifier input value from an earlier OID method request of [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md) or an OID query request of [OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](oid-receive-filter-enum-queues.md).

-   The queue identifier value of NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID, which specifies the default receive queue.

### Return status codes

NDIS handles the OID method request of OID\_RECEIVE\_FILTER\_ENUM\_FILTERS for miniport drivers, and returns one of the following status codes:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS passes the final status code and results to the OID request completion handler of the caller after the request has completed.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for other reasons.

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

[**NDIS\_RECEIVE\_FILTER\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info)

[**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array)

[OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md)

[OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](oid-receive-filter-enum-queues.md)

[OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md)

