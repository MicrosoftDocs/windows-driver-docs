---
title: Creating a Virtual Port
description: Creating a Virtual Port
ms.assetid: 6102576D-3236-4FDD-8963-83A9E90FF7F0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Virtual Port


A virtual port (VPort) is a data object that represents an internal port on the NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). Each NIC switch has the following ports for network connectivity:

-   One external physical port for connectivity to the external physical network.

-   One or more internal VPorts which are connected to the PCI Express (PCIe) Physical Function (PF) or Virtual Functions (VFs).

    The PF is attached to the Hyper-V parent partition and is exposed as a virtual network adapter in the management operating system that runs in that partition.

    A VF is attached to the Hyper-V child partition and is exposed as a virtual network adapter in the guest operating system that runs in that partition.

There are two types of VPorts:

<a href="" id="default-vport"></a>Default VPort  
The default VPort provides network connectivity to the networking components that run in the management operating system. The default VPort has an identifier of NDIS\_DEFAULT\_VPORT\_ID.

When the PF miniport driver creates and configures the default NIC switch, the driver implicitly creates the default VPort and attaches it to the PF. The default VPort cannot be attached to a VF.

The default VPort is always in an activated state and cannot be explicitly deleted. The PF miniport driver implicitly deletes the default VPort only when it deletes the default NIC switch.

For more information on how to create a NIC switch and the default VPort on the switch, see [Creating a NIC Switch](creating-a-nic-switch.md).

<a href="" id="nondefault-vport"></a>Nondefault VPort  
Nondefault VPorts are not created implicitly when the NIC switch is created. An overlying driver, such as the virtualization stack, explicitly creates these ports by issuing OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816). Nondefault VPorts may be attached to the PF or to a VF, and can only be created after the NIC switch has been created.

A nondefault VPort that is attached to a VF provides network connectivity to the networking components that run in the guest operating system. After it is created and attached to the VF, the nondefault VPort is in an activated state.

A nondefault VPort that is attached to the PF provides additional network offload capabilities to the networking components that run in the management operating system. For example, nondefault VPorts on the PF could be used to provide offload capabilities similar to the virtual machine queue (VMQ) interface.

**Note**  Nondefault VPorts can only be created after the NIC switch has been created.



An overlying driver issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) to create a nondefault VPort on a specified NIC switch. This OID request also attaches the created VPort to the network adapter's PF or a previously allocated VF.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the[**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure. After a successful return from the [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) request, the **VPortId** member of the **NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS** structure has a VPort identifier that is unique across the VPorts on the NIC switch.

The overlying driver initializes the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure with the configuration information about the nondefault VPort to be created. The configuration information includes the PCIe function to which the nondefault VPort is attached and the number of queue pairs for the nondefault VPort.

When it initializes the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure, the overlying driver must do the following:

-   The **SwitchId** member must be set to the identifier of a NIC switch that was previously created on the network adapter through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815).

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*. When creating a nondefault VPort, the overlying driver must set the **SwitchId** member to the NDIS\_DEFAULT\_SWITCH\_ID identifier.



-   The **VPortId** member must be set to NDIS\_DEFAULT\_VPORT\_ID.

-   The **AttachedFunctionId** member must be set to the identifier of the VF or PF on which the nondefault VPort is to be attached.

    A value of NDIS\_PF\_FUNCTION\_ID specifies the PF. Otherwise, the value must be set to the identifier of a VF whose resources were previously allocated through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814).

    **Note**  The attachment of a nondefault VPort to a VF or PF cannot be changed after the nondefault VPort has been created.



The overlying driver can also specify the number of queue pairs assigned to the VPort. A queue pair is a transmit and receive queue on the network adapter that is assigned to the VPort. If the network adapter supports asymmetric queue pairs for nondefault VPorts, the overlying driver may specify a different number of queue pairs for each VPort that the driver creates. For more information, see [Symmetric and Asymmetric Assignment of Queue Pairs](symmetric-and-asymmetric-assignment-of-queue-pairs.md).

The overlying driver calls [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) to issue the [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) request to the underlying PF miniport driver. Before NDIS forwards the OID method request to the miniport driver, it does the following:

1.  NDIS validates the parameters within the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure. If the parameters are in error, NDIS fails the OID method request and does not pass the request to the PF miniport driver.

2.  NDIS assigns an identifier for the nondefault VPort within the range from one to (**NumVPorts**– 1), where **NumVPorts** is the number of VPorts that the miniport driver has configured on the network adapter. The driver specifies this number in the **NumVPorts** member of the [**NDIS\_NIC\_SWITCH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451582) structure. The driver returns this structure through an OID query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](https://msdn.microsoft.com/library/windows/hardware/hh451819).

    **Note**  A VPort identifier of NDIS\_DEFAULT\_VPORT\_ID is reserved for the default VPort that is attached to the PF on the default NIC switch.




The assigned VPort identifier uniquely identifies the nondefault VPort on the NIC switch of the network adapter.


3.  NDIS sets the **VPortId** member of the NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS structure with the assigned VPort identifier.

When the PF miniport driver is issued the OID request, the driver allocates the hardware and software resources associated with the specified nondefault VPort. After all of the resources are successfully allocated, the PF miniport driver completes the OID successfully by returning NDIS\_STATUS\_SUCCESS from [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416).

If the [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) request is completed successfully, the PF miniport driver and the overlying driver must retain the **VPortId** value of the nondefault VPort for successive operations. The **VPortId** value is used during these operations:

-   NDIS and the overlying drivers use the **VPortId** value to identify the nondefault VPort in successive OID requests related to this VPort, such as [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825) and [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818).

-   During send operations, NDIS specifies the **VPortId** value to identify the VPort from which a packet was sent. This value is specified within the out-of-band (OOB) [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) data of the [NET\_BUFFER\_LIST](net-buffer-list-structure.md) structure.

-   During receive operations, the PF miniport driver specifies the **VPortId** value to which a packet is to be forwarded. This value is also specified in the OOB [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) data of the [NET\_BUFFER\_LIST](net-buffer-list-structure.md) structure.

The following points apply to the creation of nondefault VPorts:

-   Receive filters for media access control (MAC) and virtual LAN (VLAN) identifiers are configured on the VPort after it has been created. Overlying drivers dynamically set these receive filters by issuing OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). Receive filters can also be moved from one VPort to another through OID set requests of [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](https://msdn.microsoft.com/library/windows/hardware/hh451845).

-   A nondefault VPort attached to the VF is in an activated state when it is created. The VPort cannot be deactivated if it is attached to the VF.

    A nondefault VPort attached to the PF is in a deactivated state when it is created. An overlying driver, such as the Hyper-V extensible switch module, explicitly activates the nondefault VPort attached to the PF after the VPort has been created successfully. This is done by issuing an OID method request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825) to the PF miniport driver.

    When the overlying driver issues this OID request, it passes an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure with the **VPortState** member set to **NdisNicSwitchVPortStateActivated**.

    After a nondefault VPort is in an activated state, the PF miniport driver can allocate shared memory for the VPort by calling [**NdisAllocateSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561616). The driver must set the **VPortId** member in the [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567303) structure to the VPort's identifier value.

**Note**  When a nondefault VPort is in an activated state, it is only set to a deactivated state when it is deleted through an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818).











