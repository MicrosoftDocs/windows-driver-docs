---
title: OID_SWITCH_NIC_REQUEST
description: An object identifier (OID) method request of OID_SWITCH_NIC_REQUEST is used to encapsulate and forward OID requests to the Hyper-V extensible switch external network adapter.
ms.assetid: 7EF4D950-D18E-400A-B1DD-39768A16E4C4
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_REQUEST


An object identifier (OID) method request of OID\_SWITCH\_NIC\_REQUEST is used to encapsulate and forward OID requests to the Hyper-V extensible switch external network adapter. This allows the encapsulated OID request to be delivered to the driver for the underlying physical network adapter that is bound to the external network adapter.

This OID request is also used to encapsulate OID requests that were issued to other network adapters that are connected to extensible switch ports. In this case, the encapsulated OID request is forwarded through the extensible switch driver stack for inspection by extensions.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214) structure. This structure specifies the forwarding information for the OID request. This structure also contains a pointer to the original **NDIS\_OID\_REQUEST** structure of the OID request that is being forwarded.

Remarks
-------

When OID requests arrive at the Hyper-V extensible switch interface, it encapsulates them in order to forward them down the extensible switch control path. These OID requests include the following:

-   Hardware offload OID requests, including requests for Internet Protocol security (IPsec), virtual machine queue (VMQ), and single root I/O virtualization (SR-IOV). These OID requests are issued by an overlying protocol or filter driver that runs in the management operating system of the Hyper-V parent partition.

    When these OID requests arrive at the extensible switch interface, the protocol edge of the extensible switch encapsulates the OID request within an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214) structure. The protocol edge sets the members of this structure in the following way:

    -   The **DestinationPortId** and **DestinationNicIndex** members are set to the corresponding values for the external network adapter.

    -   If the OID request was originated from a Hyper-V child partition, the **SourcePortId** and **SourceNicIndex** members are set to the corresponding values for the port and network adapter that are used by the partition. Otherwise, the **SourcePortId** and **SourceNicIndex** members are set to zero.

        **Note**  The extension must retain the values of these members if it forwards or redirects the OID request.



    -   The **OidRequest** member is set to a pointer to the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the encapsulated OID request.

    The protocol edge then issues the OID\_SWITCH\_NIC\_REQUEST request to forward the encapsulated OID request down the extensible switch control path to the external network adapter.

    An underlying forwarding extension can redirect encapsulated hardware offload OID requests to a physical network adapter that is bound to the external network adapter. For example, if the extension supports physical network adapters from an extensible switch team that are bound to the external network adapter, it can forward the OID\_SWITCH\_NIC\_REQUEST request to a physical adapter in the load balancing failover (LBFO) team that supports the hardware offload. For more information on this procedure, see [Managing Hardware Offload OID Requests to Physical Network Adapters](https://msdn.microsoft.com/library/windows/hardware/hh598194).

    For more information about extensible switch teams, see [Types of Physical Network Adapter Configurations](https://msdn.microsoft.com/library/windows/hardware/hh582274).

-   Multicast OID requests, including [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](oid-802-3-add-multicast-address.md) and [OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](oid-802-3-delete-multicast-address.md). These OID requests are issued by overlying protocol and filter drivers that run in either the management operating system or the guest operating system of a Hyper-V child partition.

    When these OID requests arrive at the extensible switch interface, the protocol edge of the extensible switch encapsulates the OID request within an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214) structure. The protocol edge also sets the **SourcePortId** and **SourceNicIndex** members to the corresponding values for the port and network adapter from which the OID request originated. The protocol edge then issues the OID\_SWITCH\_NIC\_REQUEST request to forward the encapsulated OID request down the extensible switch control path for inspection by underlying extensions.

    **Note**  In this case, the protocol edge sets the **DestinationPortId** and **DestinationNicIndex** members to zero. This specifies that the encapsulated OID request is to be delivered to extensions in the control path.

    Underlying forwarding extensions can inspect these encapsulated OID requests and retain the multicast address information that they specify. For example, the extension may need this information if it originates multicast packets that it forwards to an extensible switch port.

    For more information, see [Forwarding OID Requests from a Hyper-V Child Partition](https://msdn.microsoft.com/library/windows/hardware/hh598150).

A forwarding extension can also issue an OID\_SWITCH\_NIC\_REQUEST in order to forward encapsulated OID requests to a physical network adapter that is bound to the external network adapter. This allows the extension to originate its own OID request or redirect an existing OID request to a physical network adapter that is bound to the external network adapter. In order to do this, the extension must follow these steps:

1.  The extension calls [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) to increment a reference counter for the index of the destination physical network adapter. This guarantees that the extensible switch interface will not delete the physical network adapter connection while its reference counter is nonzero.

    **Note**  The extensible switch interface could disconnect the physical network adapter connection while its reference counter is nonzero. For more information, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

2.  The extension encapsulates the OID request by initializing an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214) structure in the following way:

    -   The **DestinationPortId** member must be set to the identifier of the extensible switch port to which the external network adapter is connected.
    -   The **DestinationNicIndex** member must be set to the nonzero index value of the underlying physical network adapter.
    -   If the extension is originating on behalf of a Hyper-V child partition, the **SourcePortId** and **SourceNicIndex** members are set to the corresponding values for the port and network adapter that are used by the partition. Otherwise, the **SourcePortId** and **SourceNicIndex** members are set to zero.

        For example, if the extension is managing hardware offload resources for a child partition, it must set the **SourcePortId** and **SourceNicIndex** members to specify which partition the encapsulated hardware offload OID request is for.

    -   The **OidRequest** member must be set to a pointer to an initialized [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the encapsulated OID request.

3.  The extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request to the specified destination extensible switch port and network adapter.

4.  When NDIS calls the [*FilterOidRequestComplete*](https://msdn.microsoft.com/library/windows/hardware/ff549956) function, the extension calls [*DereferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598141) to clear the reference counter for the index of the destination physical network adapter.

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_REQUEST and returns one of the following status codes.

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
<tr class="even">
<td><p>NDIS_STATUS_<em>Xxx</em></p></td>
<td><p>The request failed for other reasons.</p></td>
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
[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214)