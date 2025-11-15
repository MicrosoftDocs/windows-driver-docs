---
title: Learn about supported driver type
description: Learn about supported NDIS driver types for Windows-based operating systems.
keywords:
- network drivers WDK , documentation
ms.date: 11/14/2025
ms.topic: concept-article
---

# Learn about supported driver types

Microsoft Windows-based operating systems support several types of kernel-mode network drivers. This topic briefly describes the supported types of network drivers and explains which articles you should read before writing each type of network driver.

The most recent version of the Network Driver Interface Specification (NDIS) interface is version [**6.89**](introduction-to-ndis-6-89.md). For more information on all supported versions of NDIS and their features, see [Overview of NDIS versions](overview-of-ndis-versions.md).

## Supported driver types

Windows Vista and later operating system versions support the following types of kernel-mode NDIS-based network drivers:

### Miniport Drivers
  
A [*miniport driver*](learning-about-miniport-drivers.md) manages miniport adapters and provides an interface to the adapters for higher-level drivers. A *miniport adapter* is a conceptual entity that can represent either a physical device or a virtual device. For example, a miniport adapter can represent a network interface card (NIC) or a virtual device that is associated with an intermediate driver.

There are many variations of miniport drivers, such as a *connection-oriented miniport call manager (MCM),* a *Windows Driver Model (WDM) miniport driver,* and the upper edge of an intermediate driver.

### Protocol Drivers

A [*protocol driver*](learning-about-protocol-drivers.md) provides high-level services in a driver stack. A protocol driver binds to underlying miniport adapters. An *upper-level protocol driver* implements an interface, possibly an application-specific interface, at its upper edge to provide services to users of the network. At its lower edge, a protocol driver provides a protocol interface to pass network data to and receive incoming data from the next-lower driver.

There are many variations of protocol drivers, such as a *connection-oriented call manager (MCM), a connection-oriented client,* and the lower edge of an intermediate driver.

### Filter Drivers

A [*filter driver*](learning-about-filter-drivers.md) filters information on the interface between protocol drivers and miniport drivers. *Filter modules* are attached in the binding between the protocol driver and the miniport adapter and are generally transparent to the other drivers. Filter drivers can implement *modifying or monitoring filters*. For example, a filter driver can enhance the services that the underlying miniport adapter provides or simply collect statistics.

### Intermediate Drivers

An [*intermediate driver*](learning-about-intermediate-drivers.md) interfaces between upper-level protocol drivers and miniport drivers. Intermediate drivers provide a miniport driver interface at their upper-edge to bind to overlying protocol drivers. Intermediate drivers provide a protocol driver interface at their lower edge to bind to underlying miniport adapters. Intermediate drivers are typically used to implement *n* to *m* multiplexer services. For example, an intermediate driver can implement load balance and failover solutions.

Intermediate drivers can also manage hardware when they are configured as a *miniport-intermediate driver*.

## Additional supported driver models

The following driver models are available to use particular hardware technologies and architectures. https://review.learn.microsoft.com/en-us/windows-hardware/drivers/ddi/_netvista/?branch=main#winsock-kernel-wsk

| Technology | Description |
|------------|-------------|
| [Scalable Networking](/windows-hardware/drivers/ddi/_netvista#scalable-networking) | Networking technologies that support the offloading of tasks to a network adapter, such as <br><br>[Header-Data Split](header-data-split.md) - A service that splits the header and the data in received Ethernet frames into separate buffers.<br>[Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md) - A network driver technology that improves network performance on multiprocessor systems.<br>[TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload) - An offload of the data-transfer part of the TCP protocol processing to a network adapter that has the appropriate capabilities.<br>[TCP/IP Offload](tcp-ip-offload.md) - An offload of tasks or connections to a network adapter that has the appropriate capabilities.<br>[Network Direct Kernel Provider Interface (NDKPI)](overview-of-network-direct-kernel-provider-interface--ndkpi-.md) - Enables kernel-mode Windows components, such as SMB server and client, to use remote direct memory access (RDMA) functionality that is provided by independent hardware vendors (IHVs).<br>[Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) - Makes it possible to use Generic Routing Encapsulation (GRE)-encapsulated packets with <br><br>Large Send Offload (LSO)<br>Virtual Machine Queue (VMQ)<br>Transmit (Tx) checksum offload<br>Receive (Rx) checksum offload. |
| [Virtualized Networking](overview-of-hyper-v.md) | Networking technologies that support Hyper-V virtualization environments, such as<br><br> [Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md)<br>[Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq--in-ndis-6-20.md)<br>[Hyper-V Extensible Switch](hyper-v-extensible-switch.md). |
| [Wireless Networking](/windows-hardware/drivers/ddi/_netvista#wireless-networking) | Networking capabilities that include Native 802.11 Wireless LAN. |
| [Network Module Registrar](/windows-hardware/drivers/ddi/_netvista/) | A system facility that allows a driver to attach network modules to one another. |
| [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista#winsock-kernel-wsk) | A kernel-mode Network Programming Interface (NPI). |
| [IP Helper](ip-helper.md) | A set of utility functions that enable drivers to retrieve and modify information about the network configuration of the local computer. |
| [Windows Filtering Platform Callout Drivers](introduction-to-windows-filtering-platform-callout-drivers.md) | A kernel-mode interface that enables deep inspection, packet modification, stream modification, and logging of network data. |
| [System Area Networks](system-area-networks.md) | A type of network connection that uses Windows Sockets Direct to support a high-performance, connection-oriented network. |
