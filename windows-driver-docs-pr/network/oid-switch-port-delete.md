---
title: OID_SWITCH_PORT_DELETE
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_PORT_DELETE to notify extensible switch extensions about the deletion of an extensible switch port.
ms.assetid: D8893395-3D33-4777-B8F0-4DD6BE9B8A37
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PORT_DELETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PORT\_DELETE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_DELETE to notify extensible switch extensions about the deletion of an extensible switch port.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure specifies the extensible switch port for which the delete notification is being made.

If a network adapter is connected to the specified port, the protocol edge of the extensible switch will delete the connection before it deletes the port. In this case, the protocol edge will follow these steps before it deletes the port:

-   The protocol edge issues an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md) to notify the extension that the connection between a network adapter and the extensible switch port is being deleted.

-   After all pending packets for the specified extensible switch port have been canceled or completed, the protocol edge issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md) to notify the extension that the connection between a network adapter and the extensible switch port has been deleted.

    At this point, the protocol edge can start to delete the port.

The protocol edge of the extensible switch follows these steps when it deletes an extensible switch port:

1.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](oid-switch-port-teardown.md). This OID request notifies underlying extensible switch extensions about the start of the deletion process for an extensible switch port.

2.  The protocol edge issues an OID set request of OID\_SWITCH\_PORT\_DELETE after all OID requests to the extensible switch port have completed.

    **Note**  If the extension had previously called [*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) to increment the port's reference counter, it must call [*DereferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598142) before the protocol edge issues the [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md) request.

     

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_PORT\_DELETE:

-   The extension must not modify the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure that is associated with the OID request.

-   The extension must always forward this OID set request to underlying extensions. The extension must not fail the request.

-   After the OID\_SWITCH\_PORT\_DELETE request is completed with NDIS\_STATUS\_SUCCESS, the extension will not receive any packets or OID requests for the deleted port. The extension cannot forward packets to the deleted port. The extension also cannot issue OID requests nor call the [*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) function for the deleted port.

**Note**  Extensible switch extensions must not issue OID set requests of OID\_SWITCH\_PORT\_DELETE.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID set request of OID\_SWITCH\_PORT\_DELETE and returns the following status code.

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
[*DereferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598142)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

[OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295)

 

 




