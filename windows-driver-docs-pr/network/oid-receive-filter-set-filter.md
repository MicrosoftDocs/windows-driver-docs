---
title: OID_RECEIVE_FILTER_SET_FILTER
description: An overlying driver issues an OID method request of OID_RECEIVE_FILTER_SET_FILTER to set a filter on a network adapter.
ms.assetid: ec3e119e-662f-48a6-8c68-20da20590b24
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_SET_FILTER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_SET\_FILTER

An overlying driver issues an OID method request of OID\_RECEIVE\_FILTER\_SET\_FILTER to set a filter on a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure that specifies the parameters for an NDIS receive filter.

-   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures that specifies the filter test criterion for a field in a network packet header.

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. If the overlying driver is creating a new receive filter, NDIS updates this structure with a new filter identifier.

Remarks
-------

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](https://msdn.microsoft.com/library/windows/hardware/hh464026).

-   [Single Root I/O Virtualization (SR-IOV)](https://msdn.microsoft.com/library/windows/hardware/hh440235). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440224).

-   [Virtual Machine Queue (VMQ)](https://msdn.microsoft.com/library/windows/hardware/ff571035). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](https://msdn.microsoft.com/library/windows/hardware/ff570780).

The OID method request of OID\_RECEIVE\_FILTER\_SET\_FILTER is mandatory for miniport drivers that support the NDIS packet coalescing, SR-IOV, or VMQ interface.

The overlying driver initializes the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure with its requested filter configuration. NDIS assigns a filter identifier in the **FilterId** member of the NDIS\_RECEIVE\_FILTER\_PARAMETERS structure and passes the method request to the underlying miniport driver.

Each filter that is set on a receive queue has a unique filter identifier for a network adapter. That is, the filter identifiers are not duplicated on different queues that the network adapter manages. When NDIS receives an OID request to set a filter on a receive queue, it verifies the filter parameters. After NDIS allocates the necessary resources and the filter identifier, it submits the OID request to the underlying network adapter. If the network adapter can successfully allocate the necessary software and hardware resources for the filter, it completes the OID request with a return status of NDIS\_STATUS\_SUCCESS.

**Note**  Starting with NDIS 6.30, packet coalescing receive filter are only supported on the default receive queue of the network adapter. This receive queue has an identifier of NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.



The miniport driver must retain the filter identifiers for the allocated receive filters. NDIS uses the identifier of a filter in later OID requests to change the receive filter parameters or clear the receive filter.

After a miniport driver receives an [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](oid-receive-filter-queue-allocation-complete.md) request and it has filters that are set on the queue, the queue is in the *Running* state. In this state, the miniport driver can start indications of packets in the queue by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

### Additional Guidelines for the SR-IOV Interface

The following points apply to miniport drivers that support the SR-IOV interface:

-   For the SR-IOV interface, a receive queue is created on a default or nondefault virtual port (VPort).

    **Note**  Starting with Windows Server 2012, the SR-IOV interface only supports the default receive queue of a VPort.

    After an SR-IOV VPort is allocated through an OID set request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md), overlying drivers can set filters on the VPort with OID requests of OID\_RECEIVE\_FILTER\_SET\_FILTER.

    **Note**  Only the overlying driver that allocated the VPort can set a filter on that VPort.

-   Because the default VPort always exists, overlying drivers can always set a filter on the default VPort.

-   When the VPort is created, no receive filters are set on it. In this case, the miniport driver must not indicate any receive packets on that VPort before the miniport driver receives an OID request of OID\_RECEIVE\_FILTER\_SET\_FILTER for the VPort. After this OID request is issued, the miniport driver can indicate packets on that VPort.

    **Note**  If the miniport driver indicates packets on a VPort while it is processing an OID request of OID\_RECEIVE\_FILTER\_SET\_FILTER, it must complete the OID request and return an NDIS\_STATUS\_SUCCESS status code.

### Additional Guidelines for the VMQ Interface

The following points apply to miniport drivers that support the VMQ interface:

-   After a VMQ receive queue is allocated, overlying drivers can set filters on the receive queue with OID requests of OID\_RECEIVE\_FILTER\_SET\_FILTER.

    **Note**  Only the protocol driver that allocated a receive queue can set a filter on that queue.

-   Because the default queue always exists, overlying drivers can always set a filter on the default queue. If the network adapter supports a drop queue, overlying drivers can set a filter on the drop queue.

    Overlying drivers do not own the default or drop queues. Therefore, all protocol drivers that are bound to a network adapter use the default or drop queue.

-   When the receive queue is created, no receive filters are set on it. In this case, the miniport driver must not indicate any receive packets on that receive queue before the miniport driver receives an OID request of OID\_RECEIVE\_FILTER\_SET\_FILTER for the receive queue. After this OID request is issued, the miniport driver can indicate packets on that receive queue.

    **Note**  If the miniport driver indicates packets on a queue while it is processing an OID request of OID\_RECEIVE\_FILTER\_SET\_FILTER, it must complete the OID request and return an NDIS\_STATUS\_SUCCESS status code.

### Return status codes

The miniport driver returns one of the following status codes for the OID method request of OID\_RECEIVE\_FILTER\_SET\_FILTER:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The filter was set on the queue successfully. The information buffer contains the updated [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
One or more of the parameters that the overlying driver provided was not valid.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. NDIS sets the **DATA.METHOD\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.

<a href="" id="ndis-status-not-supported"></a>NDIS\_STATUS\_NOT\_SUPPORTED  
The NDIS version of the miniport driver is an earlier version than 6.20.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for other reasons.

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


[**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568406)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

[OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](oid-receive-filter-clear-filter.md)

[OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](oid-receive-filter-queue-allocation-complete.md)