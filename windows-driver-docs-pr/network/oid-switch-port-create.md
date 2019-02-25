---
title: OID_SWITCH_PORT_CREATE
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_PORT_CREATE to notify extensible switch extensions about the creation of an extensible switch port.
ms.assetid: 579D51CD-0594-4A06-998E-3886E7325D97
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PORT_CREATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PORT\_CREATE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_CREATE to notify extensible switch extensions about the creation of an extensible switch port.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure specifies the port for which the creation notification is being made.

The extensible switch extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_PORT\_CREATE:

-   The extension must not modify the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure that is associated with the OID request.

-   The extension can veto the creation notification by returning NDIS\_STATUS\_DATA\_NOT\_ACCEPTED for the OID request. For example, if an extension cannot allocate resources to enforce its configured policies on the port, the driver should veto the creation notification.

    If the extension returns other NDIS\_STATUS\_*Xxx* error status codes, the creation notification is also vetoed. However, returning status codes for transitory scenarios, such as returning NDIS\_STATUS\_RESOURCES, could result in a retry of the creation notification.

    If the extension does not veto the OID request, it should monitor the status when the request is completed. The extension should do this to determine whether the OID request was vetoed by underlying extensions in the extensible switch control path or by the extensible switch interface.

    For more information on port policies, see [Managing Hyper-V Extensible Switch Policies](https://msdn.microsoft.com/library/windows/hardware/hh598195).

-   If the extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID set request, the extension should monitor the completion status of this OID request. The extension does this to detect whether underlying extensions in the extensible switch driver stack have vetoed the port creation notification.

-   After the OID request is forwarded and completes successfully, the extension can issue OIDs requests for the port, such as [OID\_SWITCH\_PORT\_PROPERTY\_ENUM](oid-switch-port-property-enum.md), until an OID request of [OID\_SWITCH\_PORT\_TEARDOWN](oid-switch-port-teardown.md) is issued. This OID request notifies the extension that the port will begin the deletion process from the extensible switch.

-   Extensions cannot forward packets to the specified port in the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure until an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md) is issued and is completed successfully.

**Note**  Extensions must not issue OID set requests of OID\_SWITCH\_PORT\_CREATE.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

### Return Status Codes

If the extension completes the OID set request of OID\_SWITCH\_PORT\_CREATE, it returns one of the following status codes.

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

 

If the extension does not complete the OID set request of OID\_SWITCH\_PORT\_CREATE, the request is completed by the underlying miniport edge of the extensible switch. The underlying miniport edge returns the following status code for this OID set request.

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

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

[OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[OID\_SWITCH\_PORT\_PROPERTY\_ENUM](oid-switch-port-property-enum.md)

 

 




