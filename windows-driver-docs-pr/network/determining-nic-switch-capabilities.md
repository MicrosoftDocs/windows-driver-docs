---
title: Determining NIC Switch Capabilities
description: Determining NIC Switch Capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining NIC Switch Capabilities


This topic describes how NDIS and overlying drivers determine the NIC switch capabilities of a network adapter that supports single root I/O virtualization (SR-IOV). This topic contains the following information:

[Reporting NIC Switch Capabilities during *MiniportInitializeEx*](#reporting-nic-switch-capabilities-during-miniportinitializeex)

[Querying NIC Switch Capabilities by Overlying Drivers](#querying-nic-switch-capabilities-by-overlying-drivers)

**Note**  Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of an SR-IOV network adapter can report NIC switch capabilities. Miniport drivers for PCIe Virtual Functions (VFs) must not report the NIC switch capabilities of the SR-IOV adapter.

 

For more information on NIC switches, see [NIC Switches](nic-switches.md).

## Reporting NIC Switch Capabilities during *MiniportInitializeEx*


When NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver provides the following NIC switch capabilities:

-   The complete set of hardware capabilities for a NIC switch that the network adapter can support.

    **Note**  Starting with NDIS 6.30, only one NIC switch is created on the network adapter. This switch is known as the *default NIC switch*.     

-   The NIC switch capabilities that are currently enabled on the network adapter.

The miniport driver reports the NIC switch hardware capabilities of the underlying network adapter through an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure that is initialized in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

    Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_NIC\_SWITCH\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_NIC\_SWITCH\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver sets appropriate flags in the **NicSwitchCapabilities** member of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure to the NIC switch capabilities of the SR-IOV network adapter. For example, the miniport driver sets the NDIS\_NIC\_SWITCH\_CAPS\_PER\_VPORT\_INTERRUPT\_MODERATION\_SUPPORTED flag if the NIC switch supports interrupt moderation on each virtual port (VPort) that is created on the switch.

3.  The miniport driver sets the other members of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure to the range of values for the NIC switch capabilities of the SR-IOV network adapter. For example, the miniport driver sets the **MaxNumVFs** and **MaxNumVPorts** members to the maximum number of VFs and VPorts that the adapter can support.

    **Note**  Depending on the available hardware resources on the network adapter, the miniport driver can set the **MaxNumVFs** member to a value that is less than its **\*NumVFs** keyword. For more information about this keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

     

When NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver registers the NIC switch capabilities of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure.

    The miniport driver sets the **HardwareNicSwitchCapabilities** member to a pointer to a previously initialized [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of one, the network adapter is currently enabled for NIC switch creation and configuration. The miniport driver sets the **CurrentNicSwitchCapabilities** members to a pointer to the same [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of zero, the network adapter is not currently enabled for NIC switch creation and configuration. The miniport driver must set the **CurrentNicSwitchCapabilities** member to NULL.

    For more information about the **\*SRIOV** INF keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

2.  The driver calls [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

## Creating a NIC switch without SR-IOV

Miniport drivers in NDIS 6.60 and later must adhere to the following requirements for the coexistence of a NIC switch and VMQ capabilities when SR-IOV is not enabled. When SR-IOV is enabled, the miniport driver should adhere to the existing requirements in the previous section.

- The miniport driver advertises both NIC switch and VMQ capabilities.
- The NIC can toggle between NIC switch and VMQ mode without a NIC restart.
    - When the NIC starts initially, it is ready to be in either mode (either creating a NIC switch or creating VMQ queues).
        - If a NIC switch is created, the miniport fails any subsequent VMQ queue allocation callbacks.
        - If a VMQ queue is created first, the miniport driver succeeds the VMQ queue allocation and fails any NIC switch allocation calls.
    - When the NIC switch is deleted or all VMQ queues are deleted, the miniport driver returns to the initial state and is ready to go into either of these modes again.

To advertise that a NIC switch can be created without the use of SR-IOV, the miniport driver sets the **NDIS_NIC_SWITCH_CAPS_NIC_SWITCH_WITHOUT_IOV_SUPPORTED** flag in the **NicSwitchCapabilities** member of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

## Querying NIC Switch Capabilities by Overlying Drivers


NDIS passes the network adapter's currently enabled NIC switch capabilities to overlying drivers that bind to the network adapter in the following way:

-   When NDIS calls an overlying filter driver's [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function, NDIS passes the network adapter's NIC switch capabilities through the *AttachParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure. The **NicSwitchCapabilities** member of this structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

-   When NDIS calls an overlying protocol driver's [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function, NDIS passes the network adapter's NIC switch capabilities through the *BindParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure. The **NicSwitchCapabilities** member of this structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

NDIS also returns the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure when it handles object identifier (OID) query requests of [OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES](./oid-nic-switch-hardware-capabilities.md) and [OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](./oid-nic-switch-current-capabilities.md) that are issued by overlying protocol or filter drivers.

 

