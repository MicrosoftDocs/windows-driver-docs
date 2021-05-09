---
title: OID_RECEIVE_FILTER_GLOBAL_PARAMETERS
description: Overlying drivers issue OID query requests of OID_RECEIVE_FILTER_GLOBAL_PARAMETERS to obtain the global receive filtering parameters of a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_GLOBAL_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS


Overlying drivers issue OID query requests of OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS to obtain the global receive filtering parameters of a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_global_parameters) structure.

## Remarks

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](./ndis-packet-coalescing.md). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](./guidelines-for-managing-packet-coalescing-receive-filters.md).

-   [Single Root I/O Virtualization (SR-IOV)](./single-root-i-o-virtualization--sr-iov-.md). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](./setting-a-receive-filter-on-a-virtual-port.md).

-   [Virtual Machine Queue (VMQ)](./virtual-machine-queue--vmq--in-ndis-6-20.md). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](./setting-and-clearing-vmq-filters.md).

Starting with NDIS 6.20, protocol drivers use OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS to query the current global configuration parameters for receive filtering on a network adapter. For example, protocol drivers can use this OID to determine whether types of receive filters or receive queues are enabled or disabled.

### Return status codes

NDIS handles the OID query request of OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS for miniport drivers, and returns one of the following status codes:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS passes the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the minimum buffer size that is required.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
The request failed because it tried to enable a capability that the underlying network adapter does not support.

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

[**NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_global_parameters)

