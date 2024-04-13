---
title: OID_RECEIVE_FILTER_CLEAR_FILTER
ms.topic: reference
description: Overlying drivers issue OID set requests of OID_RECEIVE_FILTER_CLEAR_FILTER to clear a receive filter on a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_CLEAR_FILTER Network Drivers Starting with Windows Vista
---

# OID\_RECEIVE\_FILTER\_CLEAR\_FILTER


Overlying drivers issue OID set requests of OID\_RECEIVE\_FILTER\_CLEAR\_FILTER to clear a receive filter on a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure.

## Remarks

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](./ndis-packet-coalescing.md). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](./guidelines-for-managing-packet-coalescing-receive-filters.md).

-   [Single Root I/O Virtualization (SR-IOV)](./single-root-i-o-virtualization--sr-iov-.md). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](./setting-a-receive-filter-on-a-virtual-port.md).

-   [Virtual Machine Queue (VMQ)](./virtual-machine-queue--vmq--in-ndis-6-20.md). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](./setting-and-clearing-vmq-filters.md).

The OID set request of OID\_RECEIVE\_FILTER\_CLEAR\_FILTER is mandatory for miniport drivers that support the NDIS packet coalescing, SR-IOV, or VMQ interface.

An overlying driver, such as an NDIS protocol or filter driver, uses the OID\_RECEIVE\_FILTER\_CLEAR\_FILTER set request to clear a previously set filter. Only the driver that set the receive filter can clear it.

The overlying driver clears a receive filter by setting the **FilterId** member of the [**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters) structure to the identifier for the filter. The driver obtained the filter identifier from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md).

### Additional Instructions for NDIS Packet Coalescing

The following point applies to miniport and overlying drivers that support NDIS packet coalescing:

-   An overlying driver must clear all the receive filters that it set on the miniport driver before it unbinds or detaches from the driver.

### Additional Guidelines for the SR-IOV Interface

The following points apply to miniport and overlying drivers that support the SR-IOV interface:

-   An overlying driver must clear all the filters that it set on a SR-IOV VPort before it frees the VPort. The overlying driver must also clear all the filters that it set on the default VPort before it closes its binding to the network adapter.

-   A miniport driver must not indicate packets on a nondefault VPort if it has completed the OID request of OID\_RECEIVE\_FILTER\_CLEAR\_FILTER to clear the last filter on the VPort.

    **Note**  A miniport driver also must not indicate packets on a nondefault VPort if it has completed an OID request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md) to free the VPort.

     

### Additional Guidelines for the VMQ Interface

The following points apply to miniport and overlying drivers that support the VMQ interface:

-   An overlying driver must clear all the filters that it set on a VMQ receive queue before it frees the queue. The overlying driver must also clear all the filters that it set on the default or drop queues before it closes its binding to the network adapter.

-   A miniport driver must not indicate packets on a receive queue if it has completed the OID request of OID\_RECEIVE\_FILTER\_CLEAR\_FILTER to clear the last filter on the receive queue.

    **Note**  A miniport driver also must not indicate packets on a receive queue if it has completed an OID request of [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](oid-receive-filter-free-queue.md) to free the receive queue.

     

### Return status codes

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
<td><p>The miniport adapter has been surprise removed.</p></td>
</tr>
</tbody>
</table>

 

NDIS returns one of the following status codes for this request:

<a href="" id="ndis-status-success"></a>**NDIS\_STATUS\_SUCCESS**  
The specified filter was cleared successfully.

<a href="" id="ndis-status-pending"></a>**NDIS\_STATUS\_PENDING**  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-file-not-found"></a>**NDIS\_STATUS\_FILE\_NOT\_FOUND**  
The filter identifier is not valid.

<a href="" id="ndis-status-invalid-length"></a>**NDIS\_STATUS\_INVALID\_LENGTH**  
The information buffer is too small. NDIS sets the **DATA.SET\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure to the minimum buffer size that is required.

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


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_RECEIVE\_FILTER\_CLEAR\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_clear_parameters)

[OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md)

[OID\_RECEIVE\_FILTER\_FREE\_QUEUE](oid-receive-filter-free-queue.md)

[OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md)
