---
title: OID_SWITCH_NIC_DELETE
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_DELETE to the extensible switch driver stack.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_DELETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_DELETE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_DELETE to the extensible switch driver stack. This OID request notifies underlying extensible switch extensions about the deletion of a connection between an extensible switch port and a network adapter. The protocol edge of the extensible switch previously notified extensions that this connection is being deleted when it issued an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure.

## Remarks

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the port for which the deletion notification is being made. The extensible switch extension can obtain the parameter information for this and other ports on the extensible switch by issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the index of a network adapter for which the deletion notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](./network-adapter-index-values.md).

Before the protocol edge of the extensible switch issues the OID\_SWITCH\_NIC\_DELETE request, it guarantees that all pending send or receive packet requests for the specified network adapter connection have been completed. The protocol edge also guarantees that all pending OID requests for the adapter connection have been completed, and the extensible switch reference counters for the adapter connection have a zero value.

**Note**  If the extension had incremented an extensible switch reference counter for the network adapter by calling [*ReferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_nic), the OID\_SWITCH\_NIC\_DELETE request is not issued while the reference counter is nonzero. The extension decrements the extensible switch reference counter by calling [*DereferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_nic).

 

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_NIC\_DELETE:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure that is associated with the OID request.

-   The extension must always forward this OID set request to underlying extensions. The extension must not complete the request.

-   The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_DELETE.

-   The extensible switch external network adapter can bind to one or more underlying physical adapters. For every physical network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of OID\_SWITCH\_NIC\_DELETE. Each OID set request specifies a different network adapter connection index value. For more information on these index values, see [Network Adapter Index Values](./network-adapter-index-values.md).

    The extension must maintain the connection state for each underlying physical adapter. For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](./types-of-physical-network-adapter-configurations.md).

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](./hyper-v-extensible-switch-port-and-network-adapter-states.md).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_DELETE and returns the following status code.

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
[*DereferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_nic)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)

[OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_nic)

 

