---
title: Setting a VMQ Filter
description: Setting a VMQ Filter
ms.assetid: d40b6806-6ba8-4073-b802-57cb886ffcfb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting a VMQ Filter


After a receive queue is allocated, overlying drivers can set filters on the receive queue. Only the driver that allocated a receive queue can set a filter on that queue.

**Note**  Because the default receive queue (**NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID**) always exists, overlying drivers can always set a receive filter on the default queue. Overlying drivers do not own the default queue. Therefore, all protocol drivers that are bound to a network adapter can use the default queue.

 

## Setting a Filter on a Receive Queue


To set a filter on a receive queue with an initial set of configuration parameters, an overlying driver issues an [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) method object identifier (OID) request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure with a new filter identifier.

The overlying driver initializes the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure with the following filter configuration parameters for the receive queue:

-   The filter type that is specified through an [**NDIS\_RECEIVE\_FILTER\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567186) enumeration value.

    **Note**  Starting with NDIS 6.20, only **NdisReceiveFilterTypeVMQueue** filter types are supported for the virtual machine queue (VMQ) interface.

     

-   The queue identifier.

-   One or more field test parameters that are formatted as [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures. For VMQ, the following field test parameters are defined.

    -   The destination media access control (MAC) address in the packet equals the specified MAC address.

    -   The virtual LAN (VLAN) identifier in the packet equals the specified VLAN identifier.

The [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure is used with the [OID\_RECEIVE\_FILTER\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569792) OID and the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) OID to specify the configuration parameters of a filter.

The **FieldParametersArrayOffset**, **FieldParametersArrayNumElements**, and **FieldParametersArrayElementSize** members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure define an array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures. Each **NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS** structure in the array sets the filter test criterion for one field in a network header.

The **Flags** member of the [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure specifies actions to be performed for the receive filter. The following points apply to the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag:

-   If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is set in the **Flags** member of the [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure, the network adapter must indicate only received packets that match all of the following test criteria:

    -   A packet with a matching MAC address.

    -   A packet that has no VLAN tag or has a VLAN identifier of zero.

    If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is set, the network adapter must not indicate packets that have a matching MAC address and a nonzero VLAN identifier.

    **Note**  If the Hyper-V extensible switch sets the MAC address filter and no VLAN identifier filter is configured in [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795), the switch also sets the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag.

     

-   If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is not set and there is no VLAN identifier filter configured by an OID set request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795), the miniport driver must do one of the following:

    -   If the miniport driver supports NDIS 6.20, it must return a failed status for the OID request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795).

    -   If the miniport driver supports NDIS 6.30 or later versions of NDIS, it must configure the network adapter to inspect and filter the specified MAC address fields. If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must put the VLAN tag in an [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) that is associated with the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

-   If a protocol driver sets a MAC address filter and a VLAN identifier filter with the [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) OID, it does not set the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag in either of the filter fields. In this case, the miniport driver should indicate packets that match both the specified MAC address and the VLAN identifier. That is, the miniport driver should not indicate packets with a matching MAC address that have a zero VLAN identifier or are untagged packets.

## Using the Filter Identifier


NDIS assigns a filter identifier in the **FilterId** member of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure and passes the OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) to the underlying miniport driver. Each filter that is set on a receive queue has a unique filter identifier for a network adapter. That is, the filter identifiers are not duplicated on different queues that the network adapter manages.

The overlying driver must use the filter identifier that NDIS provides in later OID requests; for example, to modify the filter parameters or to free a filter.

When NDIS receives an OID request to set a filter on a receive queue, it verifies the filter parameters. After NDIS allocates the necessary resources and the filter identifier, it submits the OID request to the underlying network adapter. If the network adapter can successfully allocate the necessary software and hardware resources for the filter, it completes the OID request with **NDIS\_STATUS\_SUCCESS**.

The miniport driver must retain the filter identifiers for the allocated receive filters. NDIS uses the filter identifier of a filter with later OID requests in order to change the receive filter parameters or clear the receive filter. For more information about how to change parameters and clear filters, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md) and [Clearing a VMQ Filter](clearing-a-vmq-filter.md).

## Handling the Filter on a Receive Queue


The miniport driver programs the network adapter based on the filters in the following way:

-   All field test parameters for a particular filter must match in order to assign a packet to the queue.

-   Multiple filters can be set on a queue.

-   Packets must be assigned to the receive queue if any of the filters pass.

The network adapter combines the results from all the field tests with a logical **AND** operation. That is, if any field test that is included in the array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures fails, the network packet does not meet the specified filter criterion.

When a network adapter tests a received packet against these filter criteria, it must ignore all fields in the packet that have no test criteria specified.

## Receiving Packets from a Receive Queue


After a miniport driver receives an [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) request and has filters that are set on the queue, the queue is in the *Running* state. While the queue is in this state, the miniport driver can indicate packets on the queue. For more information about queue states, see [Queue States and Operations](queue-states-and-operations.md).

If the miniport driver has received an [OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/ff569793) OID request for a queue but there are no filters set on the queue, the miniport driver must not indicate any receive packets on that queue. In this case, when the miniport driver receives an [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) OID request for the queue, and possibly before it completes the OID request, it can indicate packets on that queue. If the miniport driver indicates packets on a queue while it is processing an OID\_RECEIVE\_FILTER\_SET\_FILTER OID request, the miniport driver must complete the OID\_RECEIVE\_FILTER\_SET\_FILTER request that has an **NDIS\_STATUS\_SUCCESS** return code.

 

 





