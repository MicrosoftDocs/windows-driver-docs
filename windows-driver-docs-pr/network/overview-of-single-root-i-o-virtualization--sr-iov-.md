---
title: Overview of Single Root I/O Virtualization (SR-IOV)
description: Learn about Single Root I/O Virtualization (SR-IOV), a PCIe extension that enables network adapters to separate resources among hardware functions for improved virtualization performance.
ms.date: 11/05/2025
ms.topic: concept-article
---

# Overview of Single Root I/O Virtualization (SR-IOV)

Single Root I/O Virtualization (SR-IOV) is an extension to the PCI Express (PCIe) specification that improves network performance in virtualized environments. SR-IOV allows devices, such as network adapters, to separate access to their resources among various PCIe hardware functions, enabling near-native network performance in Hyper-V virtual machines. These functions consist of the following types:

* A [PCIe Physical Function (PF)](/windows-hardware/drivers/network/sr-iov-physical-function--pf-). This function is the primary function of the device and advertises the device's SR-IOV capabilities. The PF is associated with the Hyper-V parent partition in a virtualized environment.

* One or more [PCIe Virtual Functions (VFs)](/windows-hardware/drivers/network/sr-iov-virtual-functions--vfs-). Each VF is associated with the device's PF. A VF shares one or more physical resources of the device, such as a memory and a network port, with the PF and other VFs on the device. Each VF is associated with a Hyper-V child partition in a virtualized environment.

Each PF and VF is assigned a unique PCI Express Requester ID (RID) that allows an I/O memory management unit (IOMMU) to differentiate between different traffic streams and apply memory and interrupt translations between the PF and VFs. This allows traffic streams to be delivered directly to the appropriate Hyper-V parent or child partition. As a result, non-privileged data traffic flows from the PF to VF without affecting other VFs.

SR-IOV enables network traffic to bypass the software switch layer of the Hyper-V virtualization stack. Because the VF is assigned to a child partition, the network traffic flows directly between the VF and child partition. As a result, the I/O overhead in the software emulation layer is diminished and achieves network performance that is nearly the same performance as in non-virtualized environments.

## Related content

[SR-IOV Architecture](/windows-hardware/drivers/network/sr-iov-architecture) - See how Physical Functions and Virtual Functions interact.

[SR-IOV Data Paths](/windows-hardware/drivers/network/sr-iov-data-paths) - Learn how network traffic flows through SR-IOV.
