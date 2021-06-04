---
title: Setting the Parameters of a Virtual Port
description: Setting the Parameters of a Virtual Port
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Parameters of a Virtual Port


An overlying driver can change the parameters for a virtual port (VPort) on a NIC switch on a network adapter that supports single root I/O virtualization (SR-IOV). The driver issues an object identifier (OID) set request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md) to change these parameters.

Before the overlying driver issues this OID set request, it must initialize an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure with the parameters to be changed on the VPort. The driver then initializes an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the OID request, and sets the **InformationBuffer** member to a pointer to the **NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS** structure.

Only a limited subset of configuration parameters for a VPort can be changed. The overlying driver specifies the parameter to change by setting the following members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure:

-   The **SwitchId** member must be set to the identifier of the NIC switch for which parameters are to be returned.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*. The **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md).

-   The appropriate NDIS\_NIC\_SWITCH\_VPORT\_PARAMS\_*Xxx*\_CHANGED flags must be set in the **Flags** member. Members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure can only be changed if a corresponding NDIS\_NIC\_SWITCH\_VPORT\_PARAMS\_*Xxx*\_CHANGED flag is defined in Ntddndis.h.

-   The members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure, which correspond to the NDIS\_NIC\_SWITCH\_VPORT\_PARAMS\_*Xxx*\_CHANGED flags set in the **Flags** member, are set with the VPort configuration parameters that are to be changed.

Starting with Windows Server 2012, only the following members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure can be changed through an OID set request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md):

<a href="" id="portname"></a>**PortName**  
This member contains a user-friendly description of the VPort.

<a href="" id="interruptmoderation"></a>**InterruptModeration**  
This member specifies the interrupt moderation setting of the VPort.

<a href="" id="processoraffinity"></a>**ProcessorAffinity**  
This member specifies the group number and a bitmap of the CPUs that this VPort can be associated with.

The overlying driver must follow these guidelines for changing the **ProcessorAffinity** member for a VPort:

-   This member is valid only for the VPorts attached to the PF. This field is not valid for nondefault VPorts that are attached to a VF.

-   For nondefault VPorts that are attached to the PF, at least one processor must be specified when the VPort is created. The processor affinity associated with the nondefault VPort can be changed after VPort creation.

    **Note**  Nondefault VPorts are created through OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

     

<a href="" id="vportstate"></a>**VPortState**  
This member specifies the current state of the VPort.

The overlying driver must follow these guidelines for changing the **VPortState** member for a VPort:

-   For a nondefault VPort that is attached to a VF, the **VPortState** member must always be set to **NdisNicSwitchVPortStateActivated**.

-   For a nondefault VPort that is attached to the PF, the **VPortState** member must be set to **NdisNicSwitchVPortStateDeactivated** when the VPort is created. The PF VPort is activated only after an OID set request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md) is issued by the overlying drivers to change the VPortState to an activated state.

    When the nondefault VPort is activated, the PF miniport driver can allocate resources for the VPort, such as shared memory that is allocated through [**NdisAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatesharedmemory). The PF miniport driver may allocate resources for VPort any time after it is activated until the driver deletes the VPort through an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md).

-   The default VPort is always in an activated state. The value of the **VPortState** member must always be set to **NdisNicSwitchVPortStateActivated** for the default VPort.

-   When a VPort is in an activated state, it cannot be deactivated. A PF miniport driver can receive and transmit packets from a VPort only if it is in an activated state and the corresponding MAC filters are set on the VPort. However, after the VPort is deleted through an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md), the driver must free the resources that were allocated for the VPort. The driver must also cancel all pending transmit or receive operations for packets on the VPort.

After the PF miniport driver receives the OID set request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md), the driver configures the hardware with the configuration parameters. The driver can only change those configuration parameters identified by NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS\_*Xxx*\_CHANGED flags in the **Flags** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure.

 

