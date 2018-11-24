---
title: Writing VMQ Drivers
description: This section provides information about writing NDIS virtual machine queue (VMQ) drivers. You should already understand the Virtual Machine Queue Architecture before you read this section.
ms.assetid: 877d3d95-2ec5-4d2e-9bcc-cd2adfc2a667
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing VMQ Drivers


This section provides information about writing NDIS virtual machine queue (VMQ) drivers. You should already understand the [Virtual Machine Queue Architecture](virtual-machine-queue-architecture.md) before you read this section.

**Note**  Be sure to study the [NDIS Virtual Miniport Driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617918), especially the vmq.c and vmq.h source files.

 




A miniport driver that supports VMQ manages NICs that provide the VMQ hardware support. Such a NIC provides hardware services to filter incoming network data, and assign it to VM receive queues.

This section describes how overlying drivers obtain information about the underlying network adapter and set the VMQ configuration. Overlying drivers and user applications can obtain the current configuration and enable or disable VMQ features.

This section includes the following topics:

-   [VMQ Driver Configuration](vmq-driver-configuration.md)
-   [Queue States and Operations](queue-states-and-operations.md)
-   [VMQ Interrupt Requirements](vmq-interrupt-requirements.md)
-   [Allocating and Freeing VM Queues](allocating-and-freeing-vm-queues.md)
-   [Setting and Clearing VMQ Filters](setting-and-clearing-vmq-filters.md)
-   [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md)
-   [VMQ Send and Receive Operations](vmq-send-and-receive-operations.md)
-   [Obtaining VMQ Information](obtaining-vmq-information.md)

 

 





