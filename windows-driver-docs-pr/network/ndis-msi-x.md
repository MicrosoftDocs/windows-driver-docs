---
title: Overview of NDIS MSI-X
description: Overview of NDIS MSI-X
keywords:
- miniport drivers WDK networking , MSI-X
- NDIS miniport drivers WDK , MSI-X
- MSI-X WDK networking
- message-signaled interrupts WDK networking
- MSIs WDK networking
- interrupts WDK networking
- interrupt affinity WDK networking
- interrupts WDK net
ms.date: 03/02/2023
---

# Overview of NDIS MSI-X





Message-signaled interrupts (MSIs) provide an alternative to traditional line-based interrupts that network devices and their miniport drivers can use. Starting with Windows Vista, the operating system supports two types of MSIs: PCI V2.2 MSI and PCI V3.0 MSI-X.

Miniport drivers that support MSI-X can specify an *interrupt affinity*, which is a subset of central processing units (CPUs) that the drivers' message interrupt service routines run on. You can specify the interrupt affinity for each MSI-X message--for example, you can specify interrupt affinities on computers with Non-Uniform Memory Access (NUMA) architecture in terms of the "nearness" of their device to certain CPUs.

MSI-X support can provide significant performance benefits, especially for network interface cards (NICs) that support receive side scaling (RSS). For more information about receive side scaling, see [Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md).

For more information about line-based interrupts, see [Managing Interrupts](registering-and-deregistering-interrupts.md).

This section includes:

[MSI-X Initialization](msi-x-initialization.md)

[Handling an MSI Interrupt](handling-an-msi-interrupt.md)

[Synchronizing with an MSI Interrupt](synchronizing-with-an-msi-interrupt.md)

[Changing the CPU Affinity of MSI-X Table Entries](changing-the-cpu-affinity-of-msi-x-table-entries.md)

 

