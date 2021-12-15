---
title: SR-IOV Virtual Functions (VFs)
description: SR-IOV Virtual Functions (VFs)
ms.date: 04/20/2017
---

# SR-IOV Virtual Functions (VFs)


A PCI Express (PCIe) Virtual Function (VF) is a lightweight PCIe function on a network adapter that supports single root I/O virtualization (SR-IOV). The VF is associated with the PCIe Physical Function (PF) on the network adapter, and represents a virtualized instance of the network adapter. Each VF has its own PCI Configuration space. Each VF also shares one or more physical resources on the network adapter, such as an external network port, with the PF and other VFs.

A VF is not a full-fledged PCIe device. However, it provides a basic mechanism for directly transferring data between a Hyper-V child partition and the underlying SR-IOV network adapter. Software resources associated for data transfer are directly available to the VF and are isolated from use by the other VFs or the PF. However, the configuration of most of these resources is performed by the PF miniport driver that runs in the management operating system of the Hyper-V parent partition.

A VF is exposed as a virtual network adapter (*VF network adapter*) in the guest operating system that runs in a Hyper-V child partition. After the VF is associated with a virtual port (VPort) on the NIC switch of the SR-IOV network adapter, the virtual PCI (VPCI) driver that runs in the VM exposes the VF network adapter. Once exposed, the PnP manager in the guest operating system loads the VF miniport driver.

**Note**  A Hyper-V child partition is also known as a *virtual machine (VM)*.

 

The VF miniport driver is an NDIS miniport driver that is installed in the VM to manage the VF. Any operation that is performed by the VF miniport driver must not affect any other VF or the PF on the same network adapter.

The VF miniport driver can function like any PCI device driver. It can read and write to the VF's PCI configuration space. However, access to the virtual PCI device is a privileged operation and is managed by the PF miniport driver in the following way:

-   When the VF miniport driver calls [**NdisMGetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetbusdata) to read data from the PCI configuration space of the VF network adapter, the virtualization stack is notified. This stack runs in the management operating system of the Hyper-V parent partition. When the stack is notified of the read request, it issues an object identifier (OID) method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](./oid-sriov-read-vf-config-space.md) to the PF miniport driver. The data to be read is specified in an [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure that is contained in the OID request.

    The driver reads the requested data from the VF PCI configuration space and returns the data by completing the OID request. This data is then returned to the VF miniport driver when the call to [**NdisMGetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetbusdata) completes.

-   When the VF miniport driver calls [**NdisMSetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetbusdata) to write data to the PCI configuration space of the VF network adapter, the virtualization stack is notified of the write request. It issues an OID method request of [OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE](./oid-sriov-write-vf-config-space.md) to the PF miniport driver. The data to be written is specified in an [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure that is contained in the OID request.

    The driver writes the data to the VF PCI configuration space and returns the status of the request when it completes the OID request. This status is returned to the VF miniport driver after the call to [**NdisMSetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetbusdata) completes.

The VF miniport driver may also communicate with the PF miniport driver. This communication path is over a backchannel interface. For more information, see [SR-IOV PF/VF Backchannel Communication](sr-iov-pf-vf-backchannel-communication.md).

**Note**  The VF miniport driver must be aware that it is running in a virtualized environment so that it can communicate with the PF miniport driver for certain operations. For more information on how the driver does this, see [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

 

 

