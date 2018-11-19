---
title: Overview of Single Root I/O Virtualization (SR-IOV)
description: Overview of Single Root I/O Virtualization (SR-IOV)
ms.assetid: B241F468-F568-4500-9356-E576CEBA8F3B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Single Root I/O Virtualization (SR-IOV)


The single root I/O virtualization (SR-IOV) interface is an extension to the PCI Express (PCIe) specification. SR-IOV allows a device, such as a network adapter, to separate access to its resources among various PCIe hardware functions. These functions consist of the following types:

-   A PCIe Physical Function (PF). This function is the primary function of the device and advertises the device's SR-IOV capabilities. The PF is associated with the Hyper-V parent partition in a virtualized environment.

-   One or more PCIe Virtual Functions (VFs). Each VF is associated with the device's PF. A VF shares one or more physical resources of the device, such as a memory and a network port, with the PF and other VFs on the device. Each VF is associated with a Hyper-V child partition in a virtualized environment.

Each PF and VF is assigned a unique PCI Express Requester ID (RID) that allows an I/O memory management unit (IOMMU) to differentiate between different traffic streams and apply memory and interrupt translations between the PF and VFs. This allows traffic streams to be delivered directly to the appropriate Hyper-V parent or child partition. As a result, nonprivileged data traffic flows from the PF to VF without affecting other VFs.

SR-IOV enables network traffic to bypass the software switch layer of the Hyper-V virtualization stack. Because the VF is assigned to a child partition, the network traffic flows directly between the VF and child partition. As a result, the I/O overhead in the software emulation layer is diminished and achieves network performance that is nearly the same performance as in nonvirtualized environments.

For more information, see the following topics:

[SR-IOV Architecture](sr-iov-architecture.md)

[SR-IOV Data Paths](sr-iov-data-paths.md)

 

 





