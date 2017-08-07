---
title: OID\_SWITCH\_PORT\_TEARDOWN
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_TEARDOWN to notify underlying extensible switch extensions that an extensible switch port will begin the deletion process.
ms.assetid: 94FA23AC-2064-40C8-B99C-D8D3DC10BFF9
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SWITCH_PORT_TEARDOWN Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_PORT\_TEARDOWN


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_TEARDOWN to notify underlying extensible switch extensions that an extensible switch port will begin the deletion process. This process is started when the protocol driver issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure specifies the extensible switch port for which the connect notification is being made. The extensible switch extension must update any cached information about the port that it obtained in the following ways:

-   By issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md). The extension issues this OID on [*FilterAttach*](filterattach.md) only when [OID\_SWITCH\_PARAMETERS](oid-switch-parameters.md) returns an [**NDIS\_SWITCH\_PARAMETERS**](ndis-switch-parameters.md) structure with **IsActive** set to TRUE. If **IsActive** is FALSE, the extension issues the OID when the **NetEventSwitchActivate** [**NET\_PNP\_EVENT**](net-pnp-event.md) is issued by the extension miniport.

-   By inspecting the various OID sets requests of [OID\_SWITCH\_PORT\_CREATE](oid-switch-port-create.md) and [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md).

The protocol edge of the extensible switch issues an OID set request of OID\_SWITCH\_PORT\_TEARDOWN to notify the extension that a port is in the process of being deleted from the extensible switch. Before this OID request is issued, the protocol edge of the extensible switch had previously issued the following OIDs if the port had an active network adapter connection:

-   [OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md), which notified underlying extensions that the network adapter is no longer connected to the port that is specified in the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure.

-   [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md), which notified underlying extensions that the network connection between the network adapter and extensible switch port has been deleted.

    The protocol edge issues this OID set request after all pending packets for the specified extensible switch port have been canceled or completed.

After the extension completes this OID set request and the reference counter for the extensible switch port is zero, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](oid-switch-port-delete.md). This OID request deletes the port from the extensible switch.

**Note**  An extension increments the reference counter for an extensible switch port by calling [*ReferenceSwitchPort*](referenceswitchport.md). An extension decrements the reference counter by calling [*DereferenceSwitchPort*](dereferenceswitchport.md).

 

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_PORT\_TEARDOWN:

-   The extension must always forward this OID set request to underlying extensions. The extension must not fail the request.

    **Note**  The extension must not modify the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure that is associated with the OID request.

     

-   After the extension forwards this OID request, it cannot forward packets to the deleted port. The extension also cannot issue OID requests nor call the [*ReferenceSwitchPort*](referenceswitchport.md) function for the deleted port.

**Note**  The extension must not issue OID set requests of OID\_SWITCH\_PORT\_TEARDOWN.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

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
[*DereferenceSwitchPort*](dereferenceswitchport.md)

[*FilterAttach*](filterattach.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_SWITCH\_PARAMETERS**](ndis-switch-parameters.md)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md)

[**NdisFOidRequest**](ndisfoidrequest.md)

[**NET\_PNP\_EVENT**](net-pnp-event.md)

[OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md)

[OID\_SWITCH\_PARAMETERS](oid-switch-parameters.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](referenceswitchport.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_PORT_TEARDOWN%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


