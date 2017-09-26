---
title: OID\_RECEIVE\_FILTER\_PARAMETERS
author: windows-driver-content
description: An overlying driver issues an OID method request of OID\_RECEIVE\_FILTER\_PARAMETERS to obtain the current configuration parameters of a filter on a network adapter.
ms.assetid: 1bb12945-0dad-47b9-9f44-e05efe292979
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_RECEIVE_FILTER_PARAMETERS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_RECEIVE_FILTER_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


