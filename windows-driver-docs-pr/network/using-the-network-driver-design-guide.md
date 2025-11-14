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

The most recent version of the Network Driver Interface Specification (NDIS) interface is version [**6.89**](introduction-to-ndis-6-89.md). For more information on all supported versions of NDIS and their features, see [Overview of NDIS versions](overview-of-ndis-versions).

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

The following driver models are available to use particular hardware technologies and architectures.

<table>  
<colgroup>  
<col width="50%" />  
<col width="50%" />  
</colgroup>  
<thead>  
<tr class="header">  
<th align="left">Technology</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/_netvista/" data-raw-source="[Scalable Networking](/windows-hardware/drivers/ddi/_netvista/)">Scalable Networking</a></p></td>
<td align="left"><p>Networking technologies that support the offload of tasks to a network adapter, such as the following:</p>
<ul>
<li><p><a href="header-data-split.md" data-raw-source="[Header-Data Split](header-data-split.md)">Header-Data Split</a>, a service that splits the header and the data in received Ethernet frames into separate buffers.</p></li>
<li><p><a href="/windows-hardware/drivers/network/receive-side-scaling-version-2-rssv2-" data-raw-source="[Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md)">Receive Side Scaling</a>, a network driver technology that improves network performance on multiprocessor systems.</p></li>
<li><p><a href="/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload" data-raw-source="[TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload)">TCP Chimney Offload</a>, an offload of the data-transfer part of the TCP protocol processing to a network adapter that has the appropriate capabilities.</p></li>
<li><p><a href="tcp-ip-offload.md" data-raw-source="[TCP/IP Offload](tcp-ip-offload.md)">TCP/IP Offload</a>, an offload of tasks or connections to a network adapter that has the appropriate capabilities.</p></li>
<li><p><a href="overview-of-network-direct-kernel-provider-interface--ndkpi-.md" data-raw-source="[Network Direct Kernel Provider Interface (NDKPI)](overview-of-network-direct-kernel-provider-interface--ndkpi-.md)">Network Direct Kernel Provider Interface (NDKPI)</a>, which enables kernel-mode Windows components, such as SMB server and client, to use remote direct memory access (RDMA) functionality that is provided by independent hardware vendors (IHVs).</p></li>
<li><p><a href="network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md" data-raw-source="[Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>, which makes it possible to use Generic Routing Encapsulation (GRE)-encapsulated packets with:</p>
<ul>
<li>Large Send Offload (LSO)</li>
<li>Virtual Machine Queue (VMQ)</li>
<li>Transmit (Tx) checksum offload</li>
<li>Receive (Rx) checksum offload</li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="virtualized-networking.md" data-raw-source="[Virtualized Networking](virtualized-networking.md)">Virtualized Networking</a></p></td>
<td align="left"><p>Networking technologies that support Hyper-V virtualization environments, such as the following:</p>
<ul>
<li><p><a href="single-root-i-o-virtualization--sr-iov-.md" data-raw-source="[Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md)">Single Root I/O Virtualization (SR-IOV)</a></p></li>
<li><p><a href="virtual-machine-queue--vmq--in-ndis-6-20.md" data-raw-source="[Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq--in-ndis-6-20.md)">Virtual Machine Queue (VMQ)</a></p></li>
<li><p><a href="hyper-v-extensible-switch.md" data-raw-source="[Hyper-V Extensible Switch](hyper-v-extensible-switch.md)">Hyper-V Extensible Switch</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/_netvista/" data-raw-source="[Wireless Networking](/windows-hardware/drivers/ddi/_netvista/)">Wireless Networking</a></p></td>
<td align="left"><p>Networking capabilities that include Native 802.11 Wireless LAN.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/_netvista/" data-raw-source="[Network Module Registrar](/windows-hardware/drivers/ddi/_netvista/)">Network Module Registrar</a></p></td>
<td align="left"><p>A system facility that allows a driver to attach network modules to one another.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/_netvista/" data-raw-source="[Winsock Kernel](/windows-hardware/drivers/ddi/_netvista/)">Winsock Kernel</a></p></td>
<td align="left"><p>A kernel-mode Network Programming Interface (NPI).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ip-helper.md" data-raw-source="[IP Helper](ip-helper.md)">IP Helper</a></p></td>
<td align="left"><p>A set of utility functions that enable drivers to retrieve and modify information about the network configuration of the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="introduction-to-windows-filtering-platform-callout-drivers.md" data-raw-source="[Windows Filtering Platform Callout Drivers](introduction-to-windows-filtering-platform-callout-drivers.md)">Windows Filtering Platform Callout Drivers</a></p></td>
<td align="left"><p>A kernel-mode interface that enables deep inspection, packet modification, stream modification, and logging of network data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="system-area-networks.md" data-raw-source="[System Area Networks](system-area-networks.md)">System Area Networks</a></p></td>
<td align="left"><p>A type of network connection that uses Windows Sockets Direct to support a high-performance, connection-oriented network.</p></td>
</tr>
</tbody>
</table>
