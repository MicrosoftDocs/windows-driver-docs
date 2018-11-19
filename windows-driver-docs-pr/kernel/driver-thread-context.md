---
title: Driver Thread Context
description: Driver Thread Context
ms.assetid: 8795811d-a5f6-4f90-9fa0-edd4b37fd269
keywords: ["driver thread context WDK kernel", "thread context WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Driver Thread Context





As shown in the [Processing IRPs in Layered Drivers](example-i-o-request---the-details.md#ddk-example-i-o-request---the-details-kg) figure, a file system is a two-part driver:

1.  A file system driver (FSD), which executes in the context of a user-mode thread that calls an I/O system service

    The I/O manager sends the corresponding IRP to the FSD. If the FSD sets up a completion routine for an IRP, its completion routine is not necessarily called in the original user-mode thread's context.

2.  A set of file system threads, and possibly an *FSP (file system process)*

    An FSD can create a set of driver-dedicated system threads, but most FSDs use system worker threads in order to get work done without tying up user-mode threads that make I/O requests. Any FSD might set up its own process address space in which its driver-dedicated threads execute, but the system-supplied FSDs avoid this practice to conserve system memory.

File systems generally use system worker threads to set up and manage internal work queues of IRPs that they send to one or more lower-level drivers, possibly for different devices.

While the lowest-level driver shown in the [Processing IRPs in Layered Drivers](example-i-o-request---the-details.md#ddk-example-i-o-request---the-details-kg) figure processes each IRP in stages through a set of discrete, driver-supplied routines, it does not use system threads as the file system does. A lowest-level driver does not need its own thread context unless setting up its device for I/O is such a protracted process that it has a noticeable effect on system performance. Few lowest-level or intermediate drivers need to set up their own driver-dedicated or device-dedicated system threads, and those that do pay a performance penalty caused by context switches to their threads.

Most kernel-mode drivers, like the physical device driver in the [Processing IRPs in Layered Drivers](example-i-o-request---the-details.md#ddk-example-i-o-request---the-details-kg) figure, execute in an arbitrary thread context: that of whatever thread happens to be current when they are called to process an IRP. Consequently, drivers usually maintain state about their I/O operations and the devices they service in a driver-defined part of their device objects, called a *device extension*.

 

 




