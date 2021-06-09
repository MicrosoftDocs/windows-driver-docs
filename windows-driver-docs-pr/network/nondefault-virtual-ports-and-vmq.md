---
title: Nondefault Virtual Ports and VMQ
description: Nondefault Virtual Ports and VMQ
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Nondefault Virtual Ports and VMQ


The default NIC switch is a component of a network adapter that supports the single root I/O virtualization (SR-IOV) interface. The switch always attaches the default virtual port (VPort) to the PCI Express (PCIe) Physical Function (PF). The switch can attach one or more nondefault VPorts to the PF. For more information, see [Creating a Virtual Port](creating-a-virtual-port.md).

The virtualization stack runs in the management operating system of the Hyper-V parent partition. This stack creates VPorts by issuing object identifier (OID) method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md). However, the stack can create more VPorts than the number of active PCIe Virtual Functions (VFs) for which resources have been allocated through OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](./oid-nic-switch-allocate-vf.md).

If SR-IOV is enabled on a network adapter, full VMQ functionality must be disabled. However, nondefault VPorts that are attached to the PF and not attached to a VF can provide the same functionality as the virtual machine queue (VMQ) interface. The following points discuss how VPorts can provide hardware-accelerated data paths for packet transfer that is similar to VMQ:

-   VMQ determines the target VM by media access control (MAC) filtering in hardware. This avoids the overhead of a determining the target VM in the virtualization stack.

    Starting with Windows Server 2012, the virtualization stack configures the receive filters on the VPort by issuing OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md). For this OID request, the virtualization stack passes an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure that specifies the MAC address and virtual LAN (VLAN) identifier that is associated with the virtual network adapter. Similar to VMQ, it can configure multiple MAC address and VLAN ID pairs on the VPort. The virtualization stack also specifies the target VPort to which the receive filter will be set.

    The SR-IOV network adapter performs similar hardware filtering based on the filtering criteria that is specified through the [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) request. When a packet is received on the hardware receive queue of a VPort, the miniport driver specifies the source VPort identifier in the out-of-band (OOB) data of a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for the packet. Based on the VPort identifier, the virtualization stack determines the target VM and indicates the packets to the network stack that runs in the VM.

    Similarly, the virtualization stack specifies the target VPort identifier in the OOB data of a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for a transmit packet. When the driver handles the send request for the packet, it places the packet in the hardware transmit queue of the specified VPort.

    The VPort identifier can be obtained from the packet's OOB data by using the [**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID**](/windows-hardware/drivers/ddi/ndis/nf-ndis-net_buffer_list_receive_filter_vport_id) macro.

    For more information about this process, see [Packet Flow over a Virtual Port](packet-flow-over-a-virtual-port.md).

    For more information about the receive filtering requirements for an SR-IOV network adapter, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md).

-   VMQ provides interrupt and DPC concurrency.

    Starting with NDIS 6.30 and Windows Server 2012, a VPort attached to the PF can be configured to have a specific CPU affinity. The virtualization stack configures the CPU affinity and interrupt moderation parameters for a VPort by using OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md) or [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md). By doing this, the virtualization stack configures interrupt-based parameters similar to VMQ for interrupt and DPC concurrency.

    For example, when the SR-IOV network adapter receives packets on a VPort that is configured to have a specific CPU affinity, the adapter generates the interrupts on the specified CPU. The miniport driver indicates the received packets to NDIS and the virtualization stack for that CPU.

The PF miniport driver advertises its SR-IOV capabilities within the context of the call to [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). The driver initializes an [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure with its capabilities and calls [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) to register its capabilities. For more information, see [Determining SR-IOV Capabilities](determining-sr-iov-capabilities.md).

The following members of the [**NDIS_NIC_SWITCH_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure affect the way that VPorts are allocated:

-   **MaxNumVPorts**, which specifies the maximum number of VPorts that can be created on the network adapter.

-   **MaxNumVFs**, which specifies the maximum number of VFs that can be allocated on the network adapter.

Starting with NDIS 6.30, when the miniport driver initializes the [**NDIS_NIC_SWITCH_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure, it can set the NDIS\_NIC\_SWITCH\_CAPS\_SINGLE\_VPORT\_POOL flag in the **NicSwitchCapabilities** member. This flag specifies that the nondefault VPorts can be created in a nonreserved manner from the VPort pool on the network adapter. This allows available nondefault VPorts to be created and assigned on an as-needed basis to the PF and allocated VFs. If the network adapter supports the VMQ interface, nondefault VPorts that are assigned to the PF can also be used for VM receive queues.

If the NDIS\_NIC\_SWITCH\_CAPS\_SINGLE\_VPORT\_POOL flag is set, available nondefault VPorts are created and assigned to the PF and allocated VFs. The maximum number of VPorts that can be created and assigned to the PF is the same value that the driver reports in the **MaxNumVPorts** member. The miniport driver must reserve one VPort to be used as the default VPort that is assigned to the PF. As a result, the maximum number of nondefault VPorts that can be assigned to the PF and used for VM receive queues is (**MaxNumVPorts**– 1).

> [!NOTE]
> If this flag is set, the creation and assignment of nondefault VPorts are not reserved for VF allocation. As a result, situations may occur where a VF may not be assigned a VPort if the pool has been exhausted of available VPorts. 

If the NDIS\_NIC\_SWITCH\_CAPS\_SINGLE\_VPORT\_POOL flag is not set, the creation and assignment of nondefault VPorts is reserved for VF assignment. The maximum number of additional nondefault VPorts that can be created and assigned to the PF and used for VM receive queues is (**MaxNumVPorts**–**MaxNumVFs**).

For more information about VMQ, see [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md).
