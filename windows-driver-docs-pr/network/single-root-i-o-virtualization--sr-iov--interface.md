---
title: Single Root I/O Virtualization (SR-IOV) Interface
description: Single Root I/O Virtualization (SR-IOV) Interface
ms.assetid: B65160F9-DB7E-427E-999C-09BD00173076
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Single Root I/O Virtualization (SR-IOV) Interface


The SR-IOV interface allows for the partitioning of the hardware resources on a PCI Express (PCIe) network adapter into one or more virtual interfaces, known as *virtual functions (VFs)*. This allows the adapter resources to be shared in a virtual environment. SR-IOV enables network traffic to bypass the virtual software switch layer by assigning a VF to the Hyper-V child partition directly. By doing this, the I/O overhead in the software emulation layer is diminished and network throughput achieves nearly the same performance as in nonvirtualized environments.

Each PCIe VF is assigned a unique Requester ID, which allows an I/O memory management unit (IOMMU) to do the following:

-   Distinguish between different traffic streams on each PCIe function of the network adapter. This allows the IOMMU to apply memory and interrupt translations so that these traffic streams can be delivered directly to the appropriate child or parent partition.

-   Isolate traffic flows between partitions. This guarantees that traffic flow from a partition does not affect other partitions on the device.

The following figure shows the VF data path within the SR-IOV interface.

![diagram illustrating the synthetic device data paths with sr-iov](images/sriovarchitecture.png)

The use of the VF data path provides the following benefits:

-   All data packets flow directly between the protocol stacks in the guest operating system and the VF. This eliminates the overhead of the synthetic data path in which data packets flow between the Hyper-V child and parent partitions. Once forwarded to the parent partition, the Hyper-V extensible switch module forwards these packets to other child partitions or to the physical network interface on the underlying SR-IOV physical adapter.

-   The VF data path bypasses any involvement by the management operating system in packet traffic from a Hyper-V child partition. The VF provides independent memory space, interrupts and DMA streams for the child partition to which it is attached. This achieves networking performance that is almost compatible with nonvirtualized environments.

-   The routing of packets over the VF data path is performed by the NIC switch on the SR-IOV network adapter. Packets are sent or received over the external network through the physical port of the adapter. Packets are also forwarded to or from other child partitions to which a VF is attached.

    **Note**  Packets to or from child partitions to which no VF is attached are forwarded by the NIC switch to the extensible switch module. This module runs in the Hyper-V parent partition and delivers these packets to the child partition by using the synthetic data path.

     

For more information about the SR-IOV interface, see [Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md).

 

 





