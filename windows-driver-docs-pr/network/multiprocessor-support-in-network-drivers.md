---
title: Multiprocessor Support in Network Drivers
description: Multiprocessor Support in Network Drivers
ms.assetid: df01d8b0-0740-45b6-abe0-a7a7bf6b9334
keywords:
- network drivers WDK , processor support
- multiple processor support WDK networking
- processors WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiprocessor Support in Network Drivers





To write a portable driver for all Microsoft Windows versions, you need to write code to safely run on computers with multiple concurrently running processors. A network driver must be multiprocessor-safe and must use the provided NDIS library functions.

In a uniprocessor environment, a single processor runs only one computer instruction at a time, even though it is possible for a network interface card (NIC) or other device to interrupt the current execution stream when packets arrive or as timer interrupts occur. Typically, when manipulating data structures such as packet queues, a driver disables interrupts on the NIC, performs the manipulation, and then reenables interrupts. Many threads in a uniprocessor environment appear to run simultaneously but actually run in interleaved time slices.

In a multiprocessor environment, processors simultaneously run several computer instructions. A driver must synchronize so that when one driver function manipulates common data structures, the same or another driver function on another processor does not attempt to modify shared data at the same time. All driver code is reentrant in a symmetric multiprocessor (SMP) computer. To eliminate this resource protection problem, Windows device drivers use spin locks. For more information, see [Synchronization and Notification in Network Drivers](synchronization-and-notification-in-network-drivers.md).

 

 





