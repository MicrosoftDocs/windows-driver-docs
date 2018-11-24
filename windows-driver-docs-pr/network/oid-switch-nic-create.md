---
title: OID_SWITCH_NIC_CREATE
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_CREATE to notify underlying extensible switch extensions that a new connection is being established between an extensible switch port and an external or virtual network adapter. After the connection is fully established, the protocol edge of the extensible switch issues an OID set request of OID_SWITCH_NIC_CONNECT.
ms.assetid: 1D6B2C6B-A63E-4A20-B534-AF12714F5FB5
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_CREATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_CREATE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_CREATE to notify underlying extensible switch extensions that a new connection is being established between an extensible switch port and an external or virtual network adapter. After the connection is fully established, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the extensible switch port for which the creation notification is being made. The extensible switch extension can obtain the parameter information for this and other ports on the extensible switch by issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the index of a network adapter for which the creation notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

When it receives the OID set request of OID\_SWITCH\_NIC\_CREATE, the extension must follow these guidelines:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure that is associated with the OID request.

-   The OID\_SWITCH\_NIC\_CREATE request only notifies the extension that a new extensible switch connection is being brought up and that packet traffic may soon begin to occur over the specified port. However, the extension cannot use the port until the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md). Until that OID is issued, the extension must not do the following:

    -   Generate any packet traffic to the network adapter connection on the extensible switch port for which the OID\_SWITCH\_NIC\_CREATE OID request was issued.

    -   Forward or originate OID requests of [OID\_SWITCH\_NIC\_REQUEST](oid-switch-nic-request.md) to an underlying network adapter for which the OID\_SWITCH\_NIC\_CREATE OID request was issued.

    -   Forward or originate NDIS status indications of [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/hh598205) from an underlying network adapter for which the OID\_SWITCH\_NIC\_CREATE OID request was issued.

    -   Call [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) to increment the extensible switch reference counter for the specified network adapter connection on the extensible switch port.

    **Note**  The extension may intercept send or receive packets for the specified port between the OID requests of OID\_SWITCH\_NIC\_CREATE and [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md). In this case, the extension should forward the send or receive packet requests instead of canceling them.

     

-   The extension can veto the creation notification by returning NDIS\_STATUS\_DATA\_NOT\_ACCEPTED for the OID request. For example, if an extension cannot satisfy its configured policies on the specified port, the extension should veto the creation notification.

    If the extension returns other NDIS\_STATUS\_*Xxx* status codes, the creation notification is also vetoed. However, returning status codes for transitory scenarios, such as returning NDIS\_STATUS\_RESOURCES, could result in a retry of the creation notification.

    If the extension does not veto the OID request, it should monitor the status when the request is completed. The extension should do this to determine whether the OID request was vetoed by underlying extensions in the extensible switch control path or by the extensible switch interface.

    **Note**  The extension can only veto the OID request if the **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies a network adapter index value of zero.

     

-   If the extension does not veto the creation notification, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID request to underlying extensions in the extensible switch driver stack.

    **Note**  The extension should monitor the completion status of this OID request. The extension does this to detect whether underlying extensions in the extensible switch driver stack have vetoed the creation notification.

     

-   If the extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID request, the extension will not immediately receive any packet traffic to or from the extensible switch port. In addition, the extension cannot immediately inject send or receive traffic for the extensible switch port.

-   The extension can only forward packet traffic to the extensible switch port after the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md).

    **Note**  In some situations, packet traffic may be forwarded by the extensible switch to the port before an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md) is issued.

     

-   The extensible switch external network adapter can bind to one or more underlying physical adapters. For every physical network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of OID\_SWITCH\_NIC\_CREATE. Each OID set request specifies a different network adapter connection index value. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

    The extension must maintain the connection state for each underlying physical adapter. For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](https://msdn.microsoft.com/library/windows/hardware/hh582274).

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

**Note**  The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_CREATE.

 

### Return Status Codes

If the extension completes the OID set request of OID\_SWITCH\_NIC\_CREATE, it returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_DATA_NOT_ACCEPTED</p></td>
<td><p>The extension vetoed the creation notification.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_RESOURCES</p></td>
<td><p>The extension vetoed the creation notification due to a low resource condition.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_<em>Xxx</em></p></td>
<td><p>The extension vetoed the creation notification for other reasons.</p></td>
</tr>
</tbody>
</table>

 

**Note**  If the extension completes the OID set request, it must not return NDIS\_STATUS\_SUCCESS.

 

If the extension does not complete the OID set request of OID\_SWITCH\_NIC\_CREATE, the request is completed by the underlying miniport edge of the extensible switch. The underlying miniport edge returns the following status code for this OID set request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

[OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295)

 

 




