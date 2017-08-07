---
title: OID\_SWITCH\_NIC\_DISCONNECT
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_DISCONNECT to notify underlying extensible switch extensions that a connection between an extensible switch port and a network adapter is being torn down. After the connection is completely torn down, the protocol edge of the extensible switch will issue an OID set request of OID\_SWITCH\_NIC\_DELETE.
ms.assetid: 367081A7-F259-4132-B857-C956C0F2829C
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SWITCH_NIC_DISCONNECT Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_DISCONNECT


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_DISCONNECT to notify underlying extensible switch extensions that a connection between an extensible switch port and a network adapter is being torn down. After the connection is completely torn down, the protocol edge of the extensible switch will issue an OID set request of [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](ndis-switch-nic-parameters.md) structure.

Remarks
-------

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](ndis-switch-nic-parameters.md) structure specifies the index of a network adapter for which the disconnect notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

The extension must follow these guidelines when it handles OID set requests of OID\_SWITCH\_NIC\_DISCONNECT:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](ndis-switch-nic-parameters.md) structure that is associated with the OID request.

-   The OID\_SWITCH\_NIC\_DISCONNECT request only notifies the extension that the extensible switch connection is being torn down between the specified network adapter and extensible switch port. After the extension handles this OID request, it must not do the following:

    -   Generate any packet traffic to the network adapter connection on the extensible switch port for which the OID\_SWITCH\_NIC\_DISCONNECT OID request was issued.

    -   Call [*ReferenceSwitchNic*](referenceswitchnic.md) to increment the extensible switch reference counter for the specified network adapter connection on the extensible switch port.

    -   Forward or originate OID requests of [OID\_SWITCH\_NIC\_REQUEST](oid-switch-nic-request.md) to an underlying network adapter for which the OID\_SWITCH\_NIC\_DISCONNECT OID request was issued.

        **Note**  If the extension called [*ReferenceSwitchNic*](referenceswitchnic.md) to increment the extensible switch reference counter before the OID\_SWITCH\_NIC\_DISCONNECT is issued, the extension can still forward or originate OID requests.

         

    -   Forward or originate NDIS status indications of [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/hh598205) from an underlying network adapter for which the OID\_SWITCH\_NIC\_DISCONNECT OID request was issued.

        **Note**  If the extension called [*ReferenceSwitchNic*](referenceswitchnic.md) to increment the extensible switch reference counter before the OID\_SWITCH\_NIC\_DISCONNECT is issued, the extension can still forward or originate NDIS status indications.

         

    **Note**  If the extension previously called [*ReferenceSwitchNic*](referenceswitchnic.md) to increment the extensible switch reference counter, it does not need to synchronize its calls to originate or forward OID requests or NDIS status indications with its code that manages Hyper-V extensible switch OID requests. After the extension increments the reference counter, the extensible switch interface will not issue an OID set request of [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md).

     

-   The extension must always forward this OID set request to underlying extensions. The extension must not complete the request.

-   The extensible switch external network adapter can bind to one or more underlying physical adapters. For every physical network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of OID\_SWITCH\_NIC\_DISCONNECT. Each OID set request specifies a different network adapter connection index value. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

    The extension must maintain the connection state for each underlying physical adapter. For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](https://msdn.microsoft.com/library/windows/hardware/hh582274).

**Note**  The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_DISCONNECT.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_DISCONNECT and returns the following status code.

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
[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](ndis-switch-nic-parameters.md)

[OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchPort*](referenceswitchport.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_NIC_DISCONNECT%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


