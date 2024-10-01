---
title: TCP/IP Task Offload Overview
description: To increase its performance, the Microsoft TCP/IP transport can offload tasks to a NIC that has the appropriate task offload capabilities.
ms.date: 09/27/2024
---

# TCP/IP Task Offload Overview

To increase its performance, the Microsoft TCP/IP transport can offload tasks to a network interface card (NIC) that has the appropriate task offload capabilities.

Beginning with Windows Vista, the Windows operating system supports the following task offload services:

### Checksum tasks

The TCP/IP transport can offload the calculation and validation of IP and TCP checksums.

### Large send offload version 1 (LSOV1)

The TCP/IP transport supports large send offload version 1 (LSOV1). With LSOV1, the TCP/IP transport can offload the segmentation of large (up to 64 KB including the IP header) TCP packets for IPv4.

### Large send offload version 2 (LSOV2)

The large send offload version 2 (LSOV2) interface is an enhanced version of LSOV1. LSOV2 supports IPv6, IPv4, and segmentation for large TCP packets that are larger than 64K. For more information about offloading the segmentation of large packets, see [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md).

Beginning with Windows 8 and Windows Server 2012, the Windows operating system supports the following additional task overload services:

### Receive Segment Coalescing (RSC)

Receive segment coalescing (RSC) enables network card miniport drivers to coalesce multiple TCP segments and indicate them as a single coalesced unit (SCU) to the operating system's networking subsystem.

### Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload

[Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) makes it possible to use Generic Routing Encapsulation (GRE)-encapsulated packets with:

-   Large Send Offload (LSO)
-   Receive Side Scaling (RSS)
-   Virtual Machine Queue (VMQ)

### UDP Segmentation Offload (USO)

Beginning with Windows 10, version 2004, Windows supports [UDP Segmentation Offload (USO)](udp-segmentation-offload-uso-.md). USO enables network cards to offload the segmentation of UDP datagrams that are larger than the maximum transmission unit (MTU) size of the network medium.

This section includes:

-   [Determining Task Offload Capabilities](determining-task-offload-capabilities.md)
-   [Enabling and Disabling Task Offload Services](enabling-and-disabling-task-offload-services.md)
-   [Determining the Current Task Offload Settings](determining-the-current-task-offload-settings.md)
-   [Combining Types of Task Offloads](combining-types-of-task-offloads.md)
-   [Using Registry Values to Enable and Disable Task Offloading](using-registry-values-to-enable-and-disable-task-offloading.md)
-   [Offloading Checksum Tasks](offloading-checksum-tasks.md)
-   [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md)
-   [UDP Segmentation Offload (USO)](udp-segmentation-offload-uso-.md)

 

