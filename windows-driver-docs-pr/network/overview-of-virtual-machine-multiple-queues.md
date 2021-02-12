---
title: Overview of Virtual Machine Multiple Queues (VMMQ)
description: Overview of Virtual Machine Multiple Queues (VMMQ)
ms.date: 02/28/2021
ms.localizationpriority: medium
---

# Overview of Virtual Machine Multiple Queues (VMMQ)


Virtual Machine Multiple Queues (VMMQ) is a NIC offload technology that extends [Native RSS (RSSv1)](introduction-to-receive-side-scaling.md) to a [Hyper-V](overview-of-hyper-v.md) virtual environment. You can add VMMQ support to new or existing NDIS  6.60 and later drivers.

VMMQ provides scalable network traffic processing for [virtual ports (VPorts)](virtual-ports--vports-.md) in the parent partition of a virtualized node. A VPort represents an internal port on the NIC switch of a network adapter that supports [single root I/O virtualization (SR-IOV)](overview-of-single-root-i-o-virtualization--sr-iov-.md). For an overview of the SR-IOV interface and its components see [SR-IOV Architecture](sr-iov-architecture.md). Previously, RSS processing was not available for VPorts. VMMQ extends the native RSS feature to VPorts that are associated with the physical function (PF) of a NIC, including the default VPort.

You may want to enable the VMMQ feature when there is a high traffic load on a virtualized node and you want to improve CPU performance. VMMQ works by efficiently distributing network traffic within the NIC hardware. You can assign multiple hardware queues from the NIC to a single PF VPort. The NIC distributes network traffic across these queues using RSS hashing, placing packets directly onto the assigned processor. Offloading traffic distribution to the NIC improves CPU performance because the software doesn't have to complete this task.

VMMQ is available for the VPorts exposed in the parent partition regardless of whether the NIC is operating in [SR-IOV](overview-of-single-root-i-o-virtualization--sr-iov-.md) or [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md) mode.



## Expected feature interactions

- [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) and [Virtual Extensive Local Area Network (VXLAN)](/windows-server/networking/sdn/technologies/hyper-v-network-virtualization/whats-new-hyperv-network-virtualization-windows-server#VXLAN): The NIC will calculate the hash for spreading receive queues based on the inner headers of the packets.

- [SR-IOV](overview-of-single-root-i-o-virtualization--sr-iov-.md): The NIC can support VMMQ and SR-IOV simultaneously.

## In this section

[VMMQ send and receive processing](vmmq-send-and-receive-processing.md)

[Advertising VMMQ capabilities](advertising-vmmq-capabilities.md)

[Standardized INF keywords for VMMQ](standardized-inf-keywords-for-vmmq.md)

[Allocating VPorts for VMMQ](allocating-vports-for-vmmq.md)

[Enabling, disabling, and updating VMMQ on a VPort](updating-vmmq-on-a-vport.md)
