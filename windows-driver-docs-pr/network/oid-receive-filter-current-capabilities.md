---
title: OID_RECEIVE_FILTER_CURRENT_CAPABILITIES
description: Overlying drivers issue OID query requests of OID_RECEIVE_FILTER_CURRENT_CAPABILITIES to obtain the currently enabled receive filtering capabilities of a network adapter.
ms.assetid: bd4f5b9b-e33b-42ba-a430-b3b6108c80b1
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES


Overlying drivers issue OID query requests of OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES to obtain the currently enabled receive filtering capabilities of a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

Remarks
-------

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](https://msdn.microsoft.com/library/windows/hardware/hh464026).

-   [Single Root I/O Virtualization (SR-IOV)](https://msdn.microsoft.com/library/windows/hardware/hh440235). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440224).

-   [Virtual Machine Queue (VMQ)](https://msdn.microsoft.com/library/windows/hardware/ff571035). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](https://msdn.microsoft.com/library/windows/hardware/ff570780).

Starting with NDIS 6.20, miniport drivers register the currently enabled receive filtering hardware capabilities of the network adapter when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. Miniport drivers register these capabilities by following these steps:

1.  The driver initializes an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure with the currently enabled receive filtering hardware capabilities.

2.  The driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure and sets the **CurrentReceiveFilterCapabilities** member to a pointer to the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

3.  The miniport driver calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and sets the *MiniportAttributes* parameter to a pointer to an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

Overlying protocol and filter drivers do not have to issue OID query requests of OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES. NDIS provides the currently enabled receive filtering capabilities to these drivers in the following way:

-   NDIS provides the currently enabled receive filtering capabilities of an underlying network adapter to overlying protocol drivers in the **ReceiveFilterCapabilities** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure during the bind operation.

-   NDIS provides the currently enabled receive filtering capabilities of an underlying network adapter to overlying filter drivers in the **ReceiveFilterCapabilities** member of the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure during the attach operation.

### Return status codes

NDIS handles the OID query request of OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES for miniport drivers, and returns one of the following status codes:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS passes the final status code and results to the OID request completion handler of the caller after the request has completed.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.

<a href="" id="ndis-status-not-supported"></a>NDIS\_STATUS\_NOT\_SUPPORTED  
The network adapter does not support receive filtering.

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


[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864)

 

 




