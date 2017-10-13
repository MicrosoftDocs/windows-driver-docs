---
title: OID_SWITCH_NIC_CONNECT
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_CONNECT to notify underlying extensible switch extensions that a network connection between an extensible switch port and a network adapter is completely established. The protocol edge previously notified extensions that this connection is being established when it issued an OID set request of OID\_SWITCH\_NIC\_CREATE.
ms.assetid: 98A4AD28-2716-40DD-AE46-70969A23FAB7
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_NIC_CONNECT Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_CONNECT


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_CONNECT to notify underlying extensible switch extensions that a network connection between an extensible switch port and a network adapter is completely established. The protocol edge previously notified extensions that this connection is being established when it issued an OID set request of [OID\_SWITCH\_NIC\_CREATE](oid-switch-nic-create.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the extensible switch port for which the connect notification is being made. The extensible switch extension can obtain the parameter information for this port and other extensible switch ports in the following ways:

-   By issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md). The extension issues this OID on [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) only when OID\_SWITCH\_PARAMETERS returns an [**NDIS\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598220) structure with **IsActive** set to TRUE. If **IsActive** is FALSE, the extension issues the OID when the **NetEventSwitchActivate** [**NET\_PNP\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff568751) is issued by the extension miniport adapter.

-   By inspecting the various OID sets requests of [OID\_SWITCH\_PORT\_CREATE](oid-switch-port-create.md) and [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the index of a network adapter for which the connection notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

When it receives the OID set request of OID\_SWITCH\_NIC\_CONNECT, the extension must follow these guidelines:

-   When the OID\_SWITCH\_NIC\_CONNECT request completes with NDIS\_STATUS\_SUCCESS, the network connection and extensible switch port are fully operational. The extension can generate or forward packet traffic to the port's network connection. The extension can also issue extensible switch OIDs or status indications that use the port as the source port. The extension can also call [*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) to increment the extensible switch reference counter for the port.

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure that is associated with the OID request.

-   The extension must always call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID request to underlying extensions. The extension must not complete the OID request itself.

-   The extensible switch external network adapter can bind to one or more underlying physical adapters. For every physical network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of OID\_SWITCH\_NIC\_CONNECT. Each OID set request specifies a different network adapter connection index value. For more information on these values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

    The extension must maintain the connection state for each underlying physical adapter that is bound to the external network adapter. For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](https://msdn.microsoft.com/library/windows/hardware/hh582274).

**Note**  The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_CONNECT.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

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
[**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

[OID\_SWITCH\_NIC\_CREATE](oid-switch-nic-create.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_NIC_CONNECT%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


