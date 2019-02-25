---
title: Virtualized networking enhancements in NDIS 6.30
description: This section describes virtualized networking enhancements in NDIS 6.30
ms.assetid: AA1EC2E2-2903-453A-B214-947CA3C4C931
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtualized Networking Enhancements in NDIS 6.30


NDIS supports virtualized networking interface that allow Hyper-V parent and child partitions to interface the underlying physical networking interface.

NDIS 6.20 included the virtual machine queue (VMQ) interface to support Microsoft Hyper-V network performance improvements. For more information about VMQ, see [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md).

NDIS 6.30 extends the support for virtualized networking interfaces with the following technologies, as described in [Overview of Virtualized Networking](overview-of-virtualized-networking.md):

### Single Root I/O Virtualization (SR-IOV)

The SR-IOV interface allows for the partitioning of the hardware resources on a PCI Express (PCIe) network adapter into one or more virtual interfaces, known as *virtual functions (VFs)*. This allows the adapter resources to be shared in a virtual environment. SR-IOV enables network traffic to bypass the virtual software switch layer by assigning a VF to the Hyper-V child partition directly. By doing this, the I/O overhead in the software emulation layer is diminished and network throughput achieves almost the same performance as in non-virtualized environments.

For more information about the SR-IOV interface, see [Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md).

### Hyper-V Extensible Switch

The Hyper-V Extensible Switch is a virtualized Ethernet switch that runs in the management operating system of the Hyper-V parent partition. Each instance of the extensible switch routes packets between ports that are connected to the following types of network adapters:

-   The external and internal network adapters that are exposed in the management operating system that runs in the Hyper-V parent partition.

-   The synthetic or emulated network adapters that are exposed in the guest operating system that runs in a Hyper-V child partition.

Starting with NDIS 6.30, the Hyper-V Extensible Switch supports an extensibility interface. This interface allows instances of NDIS filter drivers (known as *extensions*) to bind within the Hyper-V Extensible Switch driver stack. Once bound and enabled within the driver stack, extensions are exposed to all packet traffic within the extensible switch data path. This allows extensions to monitor, modify, and forward packets to extensible switch ports. This also allows extensions to inspect and inject packets in the virtual network interfaces that are used by the various Hyper-V partitions.

For more information about the Hyper-V extensible switch interface, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

 

 





