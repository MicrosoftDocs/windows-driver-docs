---
title: Packet-Driven I/O with Reusable IRPs
description: Packet-Driven I/O with Reusable IRPs
ms.assetid: ff315b61-9fa3-4a20-bc3e-82db0ea3cde7
keywords: ["I/O stack locations WDK kernel", "packet-driven I/O WDK kernel", "reusing IRPs WDK kernel", "headers WDK kernel", "I/O manager communication WDK kernel", "I/O status blocks WDK kernel", "status blocks WDK kernel", "stack locations WDK kernel", "IRPs WDK kernel , reusing"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Packet-Driven I/O with Reusable IRPs





The I/O manager, Plug and Play manager, and power manager use *I/O request packets* (IRPs) to communicate with kernel-mode drivers, and to allow drivers to communicate with each other.

The I/O manager performs the following steps:

-   Accepts I/O requests, which usually originate from user-mode applications.

-   Creates IRPs to represent the I/O requests.

-   Routes the IRPs to the appropriate drivers.

-   Tracks the IRPs until they are completed.

-   Returns the status to the original requester of each I/O operation.

An IRP might be routed to more than one driver. For example, a request to open a file on a disk might go first to a file system driver, through an intermediate mirror driver, and ultimately to a disk driver and, possibly, to a PnP hardware bus driver. This set of drivers is known as a *driver stack*.

Therefore, each IRP has a *fixed part*, plus one driver-specific *I/O stack location* for each driver that controls the device:

-   In the fixed part (or *header*), the I/O manager maintains information about the original request, such as the caller's thread ID and parameters, the address of the device object on which a file is open, and so forth. The fixed part also contains an *I/O status block*, in which drivers set information about the status of the requested I/O operation.

-   In the highest-level driver's I/O stack location, the I/O manager, Plug and Play manager, or power manager sets driver-specific parameters, such as the function code of the requested operation and the context that the corresponding driver uses to determine what it should do. In turn, each driver sets up the I/O stack location of the next-lower driver in the driver stack.

As each driver processes an IRP, it can access its I/O stack location in the IRP, thereby reusing the IRP at each stage of the driver's operations. In addition, higher-level drivers can create (or reuse) IRPs to send requests down to even lower-level drivers.

For a detailed discussion of IRPs, see [Handling IRPs](handling-irps.md).

 

 




