---
title: Handling the OID_NIC_SWITCH_CREATE_SWITCH Request
description: Handling the OID_NIC_SWITCH_CREATE_SWITCH Request
ms.date: 04/20/2017
---

# Handling the OID\_NIC\_SWITCH\_CREATE\_SWITCH Request


NDIS issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) to do the following:

-   Enable a NIC switch on a network adapter that was statically created by the miniport driver for the PCI Express (PCIe) Physical Function (PF). The PF is a hardware component of the network adapter that supports single root I/O virtualization (SR-IOV).

    A NIC switch is statically created by the PF miniport driver from within the context to the call to [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). The driver allocates the resources and creates the switch based on parameters read from registry settings.

-   Dynamically create a NIC switch on a network adapter.

    If the PF miniport driver does not support static NIC switch creation, the miniport driver allocates the resources and creates the switch based on parameters that are specified in the OID request.

The PF miniport driver advertises its support of the SR-IOV interface when NDIS calls the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. If the PF miniport driver supports SR-IOV, NDIS reads the NIC switch configuration from the registry. Before NDIS issues an OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) to the PF miniport driver, NDIS formats an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure with the registry information in the following way:

-   NDIS sets the **SwitchType** member to the type of the NIC switch.

    Starting with Windows Server 2012, Windows only supports a switch type of **NdisNicSwitchTypeExternal**. An external switch specifies that the virtual ports (VPorts) that are connected to this type of switch can access the external network through the physical port on the network adapter.

    For more information about the NIC switch, see [SR-IOV Architecture](sr-iov-architecture.md).

-   NDIS sets the **SwitchId** member to an identifier value for the NIC switch. The switch identifier is an integer between zero and the number of switches that the network adapter supports. An NDIS\_DEFAULT\_SWITCH\_ID value indicates the default NIC switch.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface only supports the default NIC switch on the network adapter.

     

-   NDIS sets the **NumVFs** member that specifies the number of PCIe Virtual Function (VFs) that can be allocated on the NIC switch.

When it receives the OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md), the PF miniport driver must do the following:

1.  If the PF miniport driver supports static switch creation and configuration, it creates the NIC switch when NDIS calls [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). When the driver handles this OID request, it must verify the configuration parameters in the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure. The parameters must be the same as those used by the driver to create the switch during the call to *MiniportInitializeEx*. If this is not true, the driver must fail the OID request.

    For more information, see [Static Creation of a NIC Switch](static-creation-of-a-nic-switch.md).

2.  If the PF miniport driver supports dynamic switch creation and configuration, the driver must validate the configuration values of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure and create the NIC switch based on these values.

    For more information, see [Dynamic Creation of a NIC Switch](dynamic-creation-of-a-nic-switch.md).

3.  The PF miniport driver must allocate the necessary hardware and software resources for the default VPort on the NIC switch.

    **Note**  The default VPort is always created through an OID request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) and deleted through an OID request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](./oid-nic-switch-delete-switch.md). OID requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md) and [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md) are used for the creation and deletion of nondefault VPorts on the NIC switch.

     

4.  The PF miniport driver that supports dynamic switch creation and configuration must enable SR-IOV virtualization on the switch by calling [**NdisMEnableVirtualization**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismenablevirtualization). This call configures the **NumVFs** member and the **VF Enable** bit in the SR-IOV Extended Capability structure of the adapter's PCI Express (PCIe) configuration space.

    For more information about the SR-IOV configuration space, see the PCI-SIG [Single Root I/O Virtualization and Sharing 1.1](https://pcisig.com/specifications/iov/single_root) specification.

    **Note**  If the PF miniport driver supports static switch creation, it enables SR-IOV virtualization after it creates the switch when [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) is called.

     

If the PF miniport driver successfully completesthe OID method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH, it allows the following to occur:

-   VFs can be allocated on the NIC switch through OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](./oid-nic-switch-allocate-vf.md).

-   Nondefault VPorts can be created on the NIC switch through OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

    The miniport driver is responsible for managing its pool of nondefault VPorts. The driver specifies the number of nondefault VPorts in its pool through the **NumVPorts** member of the [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structure. The driver returns this structure through an OID query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](./oid-nic-switch-enum-switches.md).

    **Note**  The network adapter must always create a default VPort from its pool for the PF.

     

 

