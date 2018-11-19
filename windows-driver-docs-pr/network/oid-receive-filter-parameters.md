---
title: OID_RECEIVE_FILTER_PARAMETERS
description: An overlying driver issues an OID method request of OID_RECEIVE_FILTER_PARAMETERS to obtain the current configuration parameters of a filter on a network adapter.
ms.assetid: 1bb12945-0dad-47b9-9f44-e05efe292979
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_PARAMETERS


An overlying driver issues an OID method request of OID\_RECEIVE\_FILTER\_PARAMETERS to obtain the current configuration parameters of a filter on a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. NDIS uses the **FilterId** member in the input structure to identify the filter.

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure that specifies the parameters for an NDIS receive filter.

-   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures that specifies the filter test criterion for a field in a network packet header.

Remarks
-------

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](https://msdn.microsoft.com/library/windows/hardware/hh464026).

-   [Single Root I/O Virtualization (SR-IOV)](https://msdn.microsoft.com/library/windows/hardware/hh440235). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440224).

-   [Virtual Machine Queue (VMQ)](https://msdn.microsoft.com/library/windows/hardware/ff571035). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](https://msdn.microsoft.com/library/windows/hardware/ff570780).

Overlying drivers issue OID method requests of OID\_RECEIVE\_FILTER\_PARAMETERS to obtain the configuration parameters for a receive filter that was set on a network adapter. This includes a receive filter that was set on a VMQ receive queue or SR-IOV virtual port (VPort), as well as a packet coalescing filter that was downloaded to the miniport driver.

The overlying driver obtained the filter identifier from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md) or from OID requests of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](oid-receive-filter-enum-filters.md).

### Return status codes

NDIS handles the OID request of OID\_RECEIVE\_FILTER\_PARAMETERS for miniport drivers, and returns one of the following status codes:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS passes the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
The overlying driver or application provided an invalid filter identifier. A filter identifier is not valid if it is zero or if it specifies an undefined filter.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. NDIS sets the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.

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


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](oid-receive-filter-enum-filters.md)

[**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181)

[OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md)

 

 




