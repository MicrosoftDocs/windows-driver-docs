---
title: Virtual Ports (VPorts)
description: A VPort is a data object that represents an internal port on the NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV).
ms.date: 03/09/2022
---

# Virtual Ports (VPorts)


A virtual port (VPort) is a data object that represents an internal port on the NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). Each NIC switch has the following ports for network connectivity:

-   One external physical port for connectivity to the external physical network.

-   One or more internal VPorts which are connected to the PCI Express Physical Function (PF) or virtual functions (VFs).

    The PF is attached to the Hyper-V parent partition and is exposed as a virtual network adapter in the management operating system that runs in that partition.

    A VF is attached to the Hyper-V child partition and is exposed as a virtual network adapter in the guest operating system that runs in that partition.

The NIC switch bridges network traffic from the physical port to one or more VPorts. This provides virtualized access to the underlying physical network interface.

Each VPort has a unique identifier (*VPortId*) that is unique for the NIC switch on the network adapter. A default VPort always exists on the default NIC switch and can never be deleted. The default VPort has the VPortId of NDIS\_DEFAULT\_VPORT\_ID.

When the PF miniport driver handles an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md), it creates the NIC switch and the default VPort for that switch. The default VPort is always attached to the PF and is always in an operational state.

Nondefault VPorts are created through OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md). Only one nondefault VPort can be attached to a VF. Once attached, the default is in an operational state. One or more nondefault VPorts can also be created and attached to the PF. These VPorts are nonoperational when created and can become operational through an OID set request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md).

> [!NOTE]
> After a VPort becomes operational, it can only become nonoperational when it is deleted through an OID request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md).



Each VPort has one or more hardware queue pairs associated with it for receiving and transmitting packets. The default queue pair on the network adapter is reserved for use by the default VPort. Queue pairs for nondefault VPorts are allocated and assigned when the VPort is created through the [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md) request.

Nondefault VPorts are created and configured through OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md). The default VPort and nondefault VPorts are reconfigured through OID set requests of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md). Each OID request contains an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure that specifies the following configuration parameters:

-   The PCIe function to which the VPort is attached.

    Each VPort can be either attached to the PF or with a VF at any time. After the VPort is created and attached to a PCIe function, the attachment cannot be dynamically changed to another PCIe function.

    > [!NOTE]
    > The default VPort is always attached to the PF on the network adapter.




Starting with NDIS 6.30 in Windows Server 2012, only one nondefault VPort can be attached to a VF. However, multiple nondefault VPorts along with the default VPort can be attached to the PF.


-   The number of hardware queue pairs that are assigned to a VPort.

    Each VPort has a set of hardware queue pairs that are available to it. Each queue pair consists of a separate transmit and receive queue on the network adapter.

    Queue pairs are limited resources on the network adapter. The total number of queue pairs reserved for use by the default and nondefault VPorts is specified when the NIC switch is created. This allows the number of queue pairs that are assigned to the default VPort to differ from the nondefault VPorts.

    Each nondefault VPort can be configured to have a different number of queue pairs. This is known as *asymmetric allocation* of queue pairs. If the NIC does not allow for such an asymmetric allocation, each nondefault VPort is configured to have equal number of queue pairs. This is known as *symmetric allocation* of queue pairs. For more information, see [Symmetric and Asymmetric Assignment of Queue Pairs](symmetric-and-asymmetric-assignment-of-queue-pairs.md).

    > [!NOTE]
    > The PF miniport driver reports on whether it supports asymmetric allocation of queue pairs during [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). For more information, see [Initializing a PF Miniport Driver](initializing-a-pf-miniport-driver.md).




The number of queue pairs assigned to each VPort is not changed dynamically. The number of queue pairs assigned to a VPort cannot be changed after the VPort has been created.

> [!NOTE]
> One or more queue pairs assigned to the nondefault VPorts can be used for receive side scaling (RSS) by the VF miniport driver that runs in the guest operating system.




-   Interrupt moderation parameters for the VPort.

    Different interrupt moderation types can be specified for different VPorts. This allows the virtualization stack to control the number of interrupts generated by a particular VPort.

In addition to configuration parameters, overlying drivers can configure receive filters for each VPort by issuing OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md). The NIC switch performs the specified receive filtering on a VPort basis.

Receive filters parameters for VPorts include packet filtering conditions, such as a list of media access control (MAC) addresses and the virtual LAN (VLAN) identifiers. Filters for MAC addresses and VLAN identifiers are always specified together in the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) associated with the [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) request. The NIC switch must filter incoming packets to the switch whose destination MAC address and VLAN identifier matches any receive filter condition that was set on the VPort. The NIC switch filters packets received from either another VPort or from the external physical port. If the packet matches a filter, the NIC switch must forward it to the VPort.

Multiple MAC address and VLAN identifier pairs may be set on the VPort. If only a MAC address is set, the receive filter specifies that the VPort should receive packets that match the following condition:

-   The packet's destination MAC address matches the filter's MAC address.

-   The packet has a VLAN tag or (if a VLAN tag is present) a VLAN identifier of zero.

Nondefault VPorts are deleted through OID set requests of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-create-vport.md). The default VPort is only deleted when the NIC switch is deleted through an OID set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](./oid-nic-switch-delete-switch.md).
