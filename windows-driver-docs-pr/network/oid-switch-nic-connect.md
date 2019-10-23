---
title: OID_SWITCH_NIC_CONNECT
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_CONNECT to notify underlying extensible switch extensions that a network connection between an extensible switch port and a network adapter is completely established. The protocol edge previously notified extensions that this connection is being established when it issued an OID set request of OID_SWITCH_NIC_CREATE.
ms.assetid: 98A4AD28-2716-40DD-AE46-70969A23FAB7
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_CONNECT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_CONNECT


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_CONNECT to notify underlying extensible switch extensions that a network connection between an extensible switch port and a network adapter is completely established. The protocol edge previously notified extensions that this connection is being established when it issued an OID set request of [OID\_SWITCH\_NIC\_CREATE](oid-switch-nic-create.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the extensible switch port for which the connect notification is being made. The extensible switch extension can obtain the parameter information for this port and other extensible switch ports in the following ways:

-   By issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md). The extension issues this OID on [*FilterAttach*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) only when OID\_SWITCH\_PARAMETERS returns an [**NDIS\_SWITCH\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_parameters) structure with **IsActive** set to TRUE. If **IsActive** is FALSE, the extension issues the OID when the **NetEventSwitchActivate** [**NET\_PNP\_EVENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event) is issued by the extension miniport adapter.

-   By inspecting the various OID sets requests of [OID\_SWITCH\_PORT\_CREATE](oid-switch-port-create.md) and [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the index of a network adapter for which the connection notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](https://docs.microsoft.com/windows-hardware/drivers/network/network-adapter-index-values).

When it receives the OID set request of OID\_SWITCH\_NIC\_CONNECT, the extension must follow these guidelines:

-   When the OID\_SWITCH\_NIC\_CONNECT request completes with NDIS\_STATUS\_SUCCESS, the network connection and extensible switch port are fully operational. The extension can generate or forward packet traffic to the port's network connection. The extension can also issue extensible switch OIDs or status indications that use the port as the source port. The extension can also call [*ReferenceSwitchPort*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port) to increment the extensible switch reference counter for the port.

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure that is associated with the OID request.

-   The extension must always call [**NdisFOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward this OID request to underlying extensions. The extension must not complete the OID request itself.

-   The extensible switch external network adapter can bind to one or more underlying physical adapters. For every physical network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of OID\_SWITCH\_NIC\_CONNECT. Each OID set request specifies a different network adapter connection index value. For more information on these values, see [Network Adapter Index Values](https://docs.microsoft.com/windows-hardware/drivers/network/network-adapter-index-values).

    The extension must maintain the connection state for each underlying physical adapter that is bound to the external network adapter. For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](https://docs.microsoft.com/windows-hardware/drivers/network/types-of-physical-network-adapter-configurations).

**Note**  The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_CONNECT.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://docs.microsoft.com/windows-hardware/drivers/network/hyper-v-extensible-switch-port-and-network-adapter-states).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID set request of OID\_SWITCH\_NIC\_CONNECT and returns the following status code.

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
[**NdisFReturnNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists)

[**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)

[**NdisFOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest)

[OID\_SWITCH\_NIC\_CREATE](oid-switch-nic-create.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port)

 

 




