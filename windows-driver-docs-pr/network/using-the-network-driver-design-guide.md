---
title: Using the Network Driver Design Guide
description: Using the Network Driver Design Guide
ms.assetid: 8d9cbf3c-5eec-4409-ab4c-595bb921832d
keywords:
- network drivers WDK , documentation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Network Driver Design Guide





Microsoft Windows-based operating systems support several types of kernel-mode network drivers. The Network section of the Windows Driver Kit (WDK) documentation describes how to write these network drivers. This topic briefly describes the supported types of network drivers and explains which sections of the Network section you should read before writing each type of network driver.

This network driver design guide documents the following Network Driver Interface Specification (NDIS) interfaces:

-   NDIS 6.40, which is supported on Windows 8.1, Windows Server 2012 R2, and later versions of Windows. NDIS 6.30 includes support for Network Direct Kernel Provider Interface (NDKPI) 1.12.

    For more information about NDIS 6.30, see [Introduction to NDIS 6.40](introduction-to-ndis-6-40.md).

-   NDIS 6.30, which is supported on Windows 8, Windows Server 2012, and later versions of Windows. NDIS 6.30 includes support for single root/I/O virtualization (SR-IOV), Hyper-V extensible switch, Network Direct Kernel Provider Interface (NDKPI) 1.1, and other services.

    For more information about NDIS 6.30, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

-   NDIS 6.20, which is supported on Windows 7, Windows Server 2008 R2, and later versions of Windows. NDIS 6.20 includes support for Virtual Machine Queue (VMQ), receive side throttle, and other services.

    For more information about NDIS 6.20, see [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md).

-   NDIS 6.1, which is supported on Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows. NDIS 6.1 includes support for header-data split, direct OID requests, and other services.

    For more information about NDIS 6.1, see [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md).

-   NDIS 6.0, which is supported on Windows Vista and later versions of Windows. NDIS 6.0 includes support for filter drivers and many additional services that were not provided by earlier NDIS versions. NDIS 6.0 includes major updates to driver initialization and network data management including required support for driver reconfiguration at runtime and the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) architecture for handling network packet data. For more information about supporting runtime reconfiguration, see [Driver Stack Management](driver-stack-management.md). For more information about how to handle network packet data in NDIS 6.0 see [NET\_BUFFER Architecture](net-buffer-architecture.md).

    For more information about NDIS 6.0, see [Introduction to NDIS 6.0](introduction-to-ndis-6-0.md).

Windows Vista and later operating system versions support the following types of kernel-mode NDIS-based network drivers:

<a href="" id="miniport-drivers"></a>[Miniport Drivers](learning-about-miniport-drivers.md)  
A *miniport driver* manages miniport adapters and provides an interface to the adapters for higher-level drivers. A *miniport adapter* is a conceptual entity that can represent either a physical device or a virtual device. For example, a miniport adapter can represent a network interface card (NIC) or a virtual device that is associated with an intermediate driver.

There are many variations of miniport drivers, such as a *connection-oriented miniport call manager (MCM),* a *Windows Driver Model (WDM) miniport driver,* and the upper edge of an intermediate driver.

<a href="" id="protocol-drivers"></a>[Protocol Drivers](learning-about-protocol-drivers.md)  
A *protocol driver* provides high-level services in a driver stack. A protocol driver binds to underlying miniport adapters. An *upper-level protocol driver* implements an interface, possibly an application-specific interface, at its upper edge to provide services to users of the network. At its lower edge, a protocol driver provides a protocol interface to pass network data to and receive incoming data from the next-lower driver.

There are many variations of protocol drivers, such as a *connection-oriented call manager (MCM), a connection-oriented client,* and the lower edge of an intermediate driver.

<a href="" id="filter-drivers"></a>[Filter Drivers](learning-about-filter-drivers.md)  
A *filter driver* filters information on the interface between protocol drivers and miniport drivers. *Filter modules* are attached in the binding between the protocol driver and the miniport adapter and are generally transparent to the other drivers. Filter drivers can implement *modifying or monitoring filters*. For example, a filter driver can enhance the services that the underlying miniport adapter provides or simply collect statistics.

<a href="" id="intermediate-drivers"></a>[Intermediate Drivers](learning-about-intermediate-drivers.md)  
An *intermediate driver* interfaces between upper-level protocol drivers and miniport drivers. Intermediate drivers provide a miniport driver interface at their upper-edge to bind to overlying protocol drivers. Intermediate drivers provide a protocol driver interface at their lower edge to bind to underlying miniport adapters. Intermediate drivers are typically used to implement *n* to *m* multiplexer services. For example, an intermediate driver can implement load balance and failover solutions.

Intermediate drivers can also manage hardware when they are configured as a *miniport-intermediate driver*.

For more information about the Windows network architecture and programming considerations, see [Network Architecture for Kernel-Mode Drivers](network-architecture-for-kernel-mode-drivers.md) and [Network Driver Programming Considerations](network-driver-programming-considerations.md).

For more information about network INF files, which are used to install network components, see [Installing Network Components](installing-network-components.md). If your network driver requires a notify object--for example, to control bindings--also see [Notify Objects for Network Components](notify-objects-for-network-components.md).

The following additional driver models are available to use particular hardware technologies and architectures.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570735" data-raw-source="[Scalable Networking](https://msdn.microsoft.com/library/windows/hardware/ff570735)">Scalable Networking</a></p></td>
<td align="left"><p>Networking technologies that support the offload of tasks to a network adapter, such as the following:</p>
<ul>
<li><p><a href="header-data-split.md" data-raw-source="[Header-Data Split](header-data-split.md)">Header-Data Split</a>, a service that splits the header and the data in received Ethernet frames into separate buffers.</p></li>
<li><p><a href="ndis-receive-side-scaling2.md" data-raw-source="[Receive Side Scaling](ndis-receive-side-scaling2.md)">Receive Side Scaling</a>, a network driver technology that improves network performance on multiprocessor systems.</p></li>
<li><p><a href="ndis-tcp-chimney-offload.md" data-raw-source="[TCP Chimney Offload](ndis-tcp-chimney-offload.md)">TCP Chimney Offload</a>, an offload of the data-transfer part of the TCP protocol processing to a network adapter that has the appropriate capabilities.</p></li>
<li><p><a href="tcp-ip-offload.md" data-raw-source="[TCP/IP Offload](tcp-ip-offload.md)">TCP/IP Offload</a>, an offload of tasks or connections to a network adapter that has the appropriate capabilities.</p></li>
<li><p><a href="overview-of-network-direct-kernel-provider-interface--ndkpi-.md" data-raw-source="[Network Direct Kernel Provider Interface (NDKPI)](overview-of-network-direct-kernel-provider-interface--ndkpi-.md)">Network Direct Kernel Provider Interface (NDKPI)</a>, which enables kernel-mode Windows components, such as SMB server and client, to use remote direct memory access (RDMA) functionality that is provided by independent hardware vendors (IHVs).</p></li>
<li><p><a href="network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md" data-raw-source="[Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>, which makes it possible to use Generic Routing Encapsulation (GRE)-encapsulated packets with:</p>
<ul>
<li>Large Send Offload (LSO)</li>
<li>Virtual Machine Queue (VMQ)</li>
<li>Transmit (Tx) checksum offload</li>
<li>Receive (Rx) checksum offload</li>
</ul></li>
<li><a href="netdma-drivers.md" data-raw-source="[NetDMA](netdma-drivers.md)">NetDMA</a>, an interface for drivers to perform memory-to-memory direct memory access (DMA) transfers.
<div class="alert">
<strong>Note</strong>  The <a href="netdma-drivers.md" data-raw-source="[NetDMA](netdma-drivers.md)">NetDMA</a> interface is not supported in Windows 8, Windows Server 2012, and later.
</div>
<div>
 
</div></li>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571095" data-raw-source="[Wireless Networking](https://msdn.microsoft.com/library/windows/hardware/ff571095)">Wireless Networking</a></p></td>
<td align="left"><p>Networking capabilities that include Native 802.11 Wireless LAN.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568366" data-raw-source="[Network Module Registrar](https://msdn.microsoft.com/library/windows/hardware/ff568366)">Network Module Registrar</a></p></td>
<td align="left"><p>A system facility that allows a driver to attach network modules to one another.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571083" data-raw-source="[Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083)">Winsock Kernel</a></p></td>
<td align="left"><p>A kernel-mode Network Programming Interface (NPI).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ip-helper.md" data-raw-source="[IP Helper](ip-helper.md)">IP Helper</a></p></td>
<td align="left"><p>A set of utility functions that enable drivers to retrieve and modify information about the network configuration of the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="windows-filtering-platform-callout-drivers2.md" data-raw-source="[Windows Filtering Platform Callout Drivers](windows-filtering-platform-callout-drivers2.md)">Windows Filtering Platform Callout Drivers</a></p></td>
<td align="left"><p>A kernel-mode interface that enables deep inspection, packet modification, stream modification, and logging of network data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="system-area-networks.md" data-raw-source="[System Area Networks](system-area-networks.md)">System Area Networks</a></p></td>
<td align="left"><p>A type of network connection that uses Windows Sockets Direct to support a high-performance, connection-oriented network.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570659" data-raw-source="[Remote NDIS (RNDIS)](https://msdn.microsoft.com/library/windows/hardware/ff570659)">Remote NDIS (RNDIS)</a></p></td>
<td align="left"><p>A class specification that defines a system-provided, bus-independent message set over a USB bus.</p></td>
</tr>
</tbody>
</table>

 

 

 





