---
title: Introduction to NDIS Virtual Machine Queue (VMQ)
description: Introduction to NDIS Virtual Machine Queue (VMQ)
ms.assetid: 03c6bbd1-bd4f-415f-b4ed-c6e812c50f8d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to NDIS Virtual Machine Queue (VMQ)





Many network adapters can support more than one unicast media access control (MAC) address for a network server. Therefore, the network adapter can receive network data frames with a destination MAC address that matches any of the unicast MAC addresses that are set on the network adapter hardware without being in promiscuous mode. Such hardware can allocate a receive queue for each MAC address and route incoming frames with a matching MAC address to the queue. This feature, coupled with the ability to allocate receive buffers for each queue from the memory address space that is assigned to each virtual machine, are the primary capabilities that are required for VMQ support.

A VMQ-capable network adapter can use DMA to transfer all incoming frames that should be routed to a receive queue to the receive buffers that are allocated for that queue. The miniport driver can indicate all of the frames that are in a receive queue in one receive indication call.

VMQ provides the following features:

-   Improves network throughput by distributing processing of network traffic for multiple virtual machines (VMs) among multiple processors.

    **Note**  In Hyper-V, a child partition is also known as a VM.

     

-   Reduces CPU utilization by offloading receive packet filtering to network adapter hardware.

-   Prevents network data copy by using DMA to transfer data directly to VM memory.

-   Splits network data to provide a secure environment. For more information about security issues, see [Security Issues with NDIS Virtual Machine (VM) Shared Memory](security-issues-with-ndis-virtual-machine--vm--shared-memory.md).

    **Note**  Starting with NDIS 6.30 and Windows Server 2012, splitting network data into separate lookahead buffers is no longer supported.

     

-   Supports live migration. For more information about live migration, see [NDIS VMQ Live Migration Support](ndis-vmq-live-migration-support.md).

To introduce high-level VMQ concepts, this section includes the following additional topics:

[VMQ Components](vmq-components.md)

[VMQ Receive Queues](vmq-receive-queues.md)

[VMQ Receive Filters](vmq-receive-filters.md)

 

 





