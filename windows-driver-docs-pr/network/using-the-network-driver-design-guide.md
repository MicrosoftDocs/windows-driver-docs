---
title: Supported NDIS Network Driver Types
description: "Explore NDIS driver types for Windows: miniport, protocol, filter, and intermediate drivers. Learn which driver type fits your development needs."
keywords:
- network drivers WDK , documentation
ms.date: 11/14/2025
ms.topic: concept-article
---

# Learn about supported driver types

Windows-based operating systems support several types of kernel-mode NDIS network drivers, including miniport, protocol, filter, and intermediate drivers. This article describes each supported driver type and explains which documentation you should read before developing network drivers for Windows.

The most recent version of the Network Driver Interface Specification (NDIS) is version [**6.89**](introduction-to-ndis-6-89.md). For more information on all supported versions of NDIS and their features, see [Overview of NDIS versions](overview-of-ndis-versions.md).

## Supported driver types

Windows Vista and later operating system versions support the following types of kernel-mode NDIS-based network drivers:

### Miniport Drivers
  
A [*miniport driver*](learning-about-miniport-drivers.md) manages network adapters and provides an interface for higher-level drivers. Use miniport drivers when you need to control physical hardware like network interface cards (NICs) or virtual devices.

**Common miniport driver variations:**

- Connection-oriented miniport call manager (MCM)
- Windows Driver Model (WDM) miniport driver
- Upper edge of an intermediate driver

[Learn more about developing miniport drivers](learning-about-miniport-drivers.md)

### Protocol Drivers

A [*protocol driver*](learning-about-protocol-drivers.md) provides high-level services in a driver stack by binding to miniport adapters. Use protocol drivers when you need to implement network protocols or application-specific network interfaces.

**Common protocol driver variations:**

- Connection-oriented call manager (MCM)
- Connection-oriented client
- Lower edge of an intermediate driver

[Learn more about developing protocol drivers](learning-about-protocol-drivers.md)

### Filter Drivers

A [*filter driver*](learning-about-filter-drivers.md) filters information between protocol drivers and miniport drivers. Use filter drivers when you need to modify network traffic or monitor network activity without changing existing drivers.

**Common use cases:**

- Enhance services provided by miniport adapters
- Collect network statistics
- Implement modifying or monitoring filters

[Learn more about developing filter drivers](learning-about-filter-drivers.md)

### Intermediate Drivers

An [*intermediate driver*](learning-about-intermediate-drivers.md) sits between protocol drivers and miniport drivers, providing interfaces to both. Use intermediate drivers when you need to implement multiplexer services like load balancing or failover solutions.

**Key capabilities:**

- Implement *n* to *m* multiplexer services
- Provide load balancing and failover solutions
- Manage hardware as a miniport-intermediate driver

[Learn more about developing intermediate drivers](learning-about-intermediate-drivers.md)

## Additional supported driver models

Use the following driver models to work with particular hardware technologies and architectures. 

| Technology | Description |
|------------|-------------|
| [Scalable Networking](/windows-hardware/drivers/ddi/_netvista#scalable-networking) | Networking technologies that support the offloading of tasks to a network adapter, such as <br><br>[Header-Data Split](header-data-split.md) - A service that splits the header and the data in received Ethernet frames into separate buffers.<br>[Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md) - A network driver technology that improves network performance on multiprocessor systems.<br>[TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload) - An offload of the data-transfer part of the TCP protocol processing to a network adapter that has the appropriate capabilities.<br>[TCP/IP Offload](tcp-ip-offload.md) - An offload of tasks or connections to a network adapter that has the appropriate capabilities.<br>[Network Direct Kernel Provider Interface (NDKPI)](overview-of-network-direct-kernel-provider-interface--ndkpi-.md) - Enables kernel-mode Windows components, such as SMB server and client, to use remote direct memory access (RDMA) functionality that is provided by independent hardware vendors (IHVs).<br>[Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) - Makes it possible to use Generic Routing Encapsulation (GRE)-encapsulated packets with <br><br>Large Send Offload (LSO)<br>Virtual Machine Queue (VMQ)<br>Transmit (Tx) checksum offload<br>Receive (Rx) checksum offload. |
| [Virtualized Networking](overview-of-hyper-v.md) | Networking technologies that support Hyper-V virtualization environments, such as<br><br> [Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md)<br>[Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq--in-ndis-6-20.md)<br>[Hyper-V Extensible Switch](hyper-v-extensible-switch.md). |
| [Wireless Networking](/windows-hardware/drivers/ddi/_netvista#wireless-networking) | Networking capabilities that include Native 802.11 Wireless LAN. |
| [Network Module Registrar](introduction-to-the-network-module-registrar) | A system facility that allows a driver to attach network modules to one another. |
| [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista#winsock-kernel-wsk) | A kernel-mode Network Programming Interface (NPI). |
| [IP Helper](ip-helper.md) | A set of utility functions that enable drivers to retrieve and modify information about the network configuration of the local computer. |
| [Windows Filtering Platform Callout Drivers](introduction-to-windows-filtering-platform-callout-drivers.md) | A kernel-mode interface that enables deep inspection, packet modification, stream modification, and logging of network data. |
| [System Area Networks](system-area-networks.md) | A type of network connection that uses Windows Sockets Direct to support a high-performance, connection-oriented network. |
