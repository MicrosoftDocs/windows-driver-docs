---
title: OID_SWITCH_PORT_TEARDOWN
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_PORT_TEARDOWN to notify underlying extensible switch extensions that an extensible switch port will begin the deletion process.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PORT_TEARDOWN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PORT\_TEARDOWN


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_TEARDOWN to notify underlying extensible switch extensions that an extensible switch port will begin the deletion process. This process is started when the protocol driver issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure.

## Remarks

The **PortId** member of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure specifies the extensible switch port for which the connect notification is being made. The extensible switch extension must update any cached information about the port that it obtained in the following ways:

-   By issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md). The extension issues this OID on [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) only when [OID\_SWITCH\_PARAMETERS](oid-switch-parameters.md) returns an [**NDIS\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_parameters) structure with **IsActive** set to TRUE. If **IsActive** is FALSE, the extension issues the OID when the **NetEventSwitchActivate** [**NET\_PNP\_EVENT**](/windows-hardware/drivers/ddi/netpnp/ns-netpnp-_net_pnp_event) is issued by the extension miniport.

-   By inspecting the various OID sets requests of [OID\_SWITCH\_PORT\_CREATE](oid-switch-port-create.md) and [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The protocol edge of the extensible switch issues an OID set request of OID\_SWITCH\_PORT\_TEARDOWN to notify the extension that a port is in the process of being deleted from the extensible switch. Before this OID request is issued, the protocol edge of the extensible switch had previously issued the following OIDs if the port had an active network adapter connection:

-   [OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md), which notified underlying extensions that the network adapter is no longer connected to the port that is specified in the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure.

-   [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md), which notified underlying extensions that the network connection between the network adapter and extensible switch port has been deleted.

    The protocol edge issues this OID set request after all pending packets for the specified extensible switch port have been canceled or completed.

After the extension completes this OID set request and the reference counter for the extensible switch port is zero, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md). This OID request deletes the port from the extensible switch.

**Note**  An extension increments the reference counter for an extensible switch port by calling [*ReferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port). An extension decrements the reference counter by calling [*DereferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_port).

 

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_PORT\_TEARDOWN:

-   The extension must always forward this OID set request to underlying extensions. The extension must not fail the request.

    **Note**  The extension must not modify the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure that is associated with the OID request.

     

-   After the extension forwards this OID request, it cannot forward packets to the deleted port. The extension also cannot issue OID requests nor call the [*ReferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port) function for the deleted port.

**Note**  The extension must not issue OID set requests of OID\_SWITCH\_PORT\_TEARDOWN.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](./hyper-v-extensible-switch-port-and-network-adapter-states.md).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID set request of OID\_SWITCH\_PORT\_TEARDOWN and returns the following status code.

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

 

## Requirements

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
[*DereferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_port)

[*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_parameters)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters)

[**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest)

[**NET\_PNP\_EVENT**](/windows-hardware/drivers/ddi/netpnp/ns-netpnp-_net_pnp_event)

[OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md)

[OID\_SWITCH\_PARAMETERS](oid-switch-parameters.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port)

 

