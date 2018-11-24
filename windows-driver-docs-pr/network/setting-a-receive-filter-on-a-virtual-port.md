---
title: Setting a Receive Filter on a Virtual Port
description: Setting a Receive Filter on a Virtual Port
ms.assetid: F0137D59-1701-4DFC-BB30-27E477FC0706
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting a Receive Filter on a Virtual Port


After a virtual port (VPort) is created on the NIC switch of the network adapter, overlying drivers can set receive filters on the VPort. Only the driver that created the VPort can set a receive filter on that VPort

This topic contains the following information:

[Setting a Receive Filter on a VPort](#set)

[Using the NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO Flag](#flag)

[Using the Filter Identifier](#filter-id)

[Handling Receive Filters on a VPort](#handle)

For more information on how to create a VPort, see [Creating a Virtual Port](creating-a-virtual-port.md).

**Note**  Because the default VPort always exists and is never explicitly created, any overlying driver can set a receive filter on the default VPort. Overlying drivers do not own the default VPort. Therefore, all protocol drivers that are bound to a network adapter can use the default VPort. The default VPort has an identifier value of NDIS\_DEFAULT\_VPORT\_ID.

 

## Setting a Receive Filter on a VPort


To set and configure a filter on a VPort, an overlying driver issues an object identifier (OID) method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

Before the overlying driver issues this OID method request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. The driver must set the members of this structure in the following way:

-   The **FilterType** member must be set to an [**NDIS\_RECEIVE\_FILTER\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567186) enumeration value.

    **Note**  Starting with NDIS 6.30, only **NdisReceiveFilterTypeVMQueue** filter types are supported for the single root I/O virtualization (SR-IOV) interface.

     

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821).

-   The **FilterId** member must be set to NDIS\_DEFAULT\_RECEIVE\_FILTER\_ID.

    **Note**  NDIS assigns a unique filter identifier in this member before it forwards the OID request to the miniport driver for processing.

     

-   The **FieldParametersArrayOffset**, **FieldParametersArrayNumElements**, and **FieldParametersArrayElementSize** members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure must be set appropriately to define an array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures. Each **NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS** structure in the array sets the filter test criterion for one field in a network header.

    For the SR-IOV interface, the following field test parameters are defined:

    -   The destination media access control (MAC) address in the packet equals the specified MAC address.

    -   The virtual LAN (VLAN) identifier in the packet equals the specified VLAN identifier.

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure with a new filter identifier.

## Using the NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO Flag


The **Flags** member of the [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure specify actions to be performed for the receive filter. The following points apply to the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag:

-   If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is set in the **Flags** member, the network adapter must indicate only received packets that match all of the following test criteria:

    -   A packet with a matching MAC address.

    -   A packet that has no VLAN tag or has a VLAN identifier of zero.

    If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is set, the network adapter must not indicate packets that have a matching MAC address and a nonzero VLAN identifier.

    **Note**  If the virtualization stack sets the MAC address filter and no VLAN identifier filter is configured by the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) set request, the switch also sets the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag.

     

-   Starting with NDIS 6.30, if the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is not set and there is no VLAN identifier filter configured by the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) method request, the miniport driver must do either one of the following:

    -   The miniport driver must return a failed status for the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) method request.

    -   The miniport driver must configure the network adapter to inspect and filter the specified MAC address fields. If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must put the VLAN tag in an [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) that is associated with the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

-   If a protocol driver sets a MAC address filter and a VLAN identifier filter with the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) method request, it does not set the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag in either of the filter fields. In this case, the miniport driver should indicate packets that match both the specified MAC address and the VLAN identifier. That is, the miniport driver should not indicate packets with a matching MAC address that have a zero VLAN identifier or are untagged packets.

## Using the Filter Identifier


NDIS assigns a filter identifier in the **FilterId** member of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure and passes the OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) to the underlying miniport driver. Each filter that is set on a VPort has a unique filter identifier for a network adapter. That is, the filter identifiers are not duplicated on different queues that the network adapter manages.

The overlying driver must use the filter identifier that NDIS provides in later OID requests to change the filter parameters or to free a filter.

When NDIS receives an OID request to set a filter on a VPort, it verifies the filter parameters. After NDIS allocates the necessary resources and the filter identifier, it submits the OID request to the underlying network adapter. If the network adapter can successfully allocate the necessary software and hardware resources for the filter, it completes the OID request with **NDIS\_STATUS\_SUCCESS**.

The miniport driver must retain the filter identifiers for the allocated receive filters. NDIS uses the filter identifier of a filter with later OID requests to change the receive filter parameters or clear the receive filter. For more information about how to change parameters and clear filters, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md) and [Clearing a VMQ Filter](clearing-a-vmq-filter.md).

## Handling Receive Filters on a VPort


The miniport driver programs the network adapter based on the filters in the following way:

-   All field test parameters for a particular filter must match to assign a packet to the VPort.

-   Multiple filters can be set on a VPort.

-   Packets must be assigned to the VPort if any of the filters pass.

The network adapter combines the results from all the field tests with a logical **AND** operation. That is, if any field test that is included in the array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures fails, the network packet does not meet the specified filter criterion.

When a network adapter tests a received packet against these filter criteria, it must ignore all fields in the packet that have no test criteria that were specified.

 

 





