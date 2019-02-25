---
title: Operating a Parallel Port
description: Operating a Parallel Port
ms.assetid: c9015a01-a7cb-41f4-9710-a868ef19f6d7
keywords:
- vendor-supplied parallel drivers WDK , parallel port operation
- system-supplied function drivers WDK parallel ports
- function drivers WDK parallel ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operating a Parallel Port





This section describes how a client, in particular, a vendor-supplied function driver for a parallel device, operates a parallel port.

The system-supplied function driver for parallel ports creates a functional device object (FDO) for each parallel port enumerated in the system. The following topics describe how a client operates a parallel port by using the interface provided by the port's FDO:

[Creating and Starting a Parallel Port](creating-and-starting-a-parallel-port.md)

[Opening and Closing a Parallel Port](opening-and-closing-a-parallel-port.md)

[Obtaining Information About a Parallel Port](obtaining-information-about-a-parallel-port.md)

[Synchronizing the Use of a Parallel Port](synchronizing-the-use-of-a-parallel-port.md)

[Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md)

[Setting and Clearing the Communication Mode on a Parallel Port](setting-and-clearing-the-communication-mode-on-a-parallel-port.md)

[Connecting to an IEEE 1284.3 Data Link Device](connecting-to-an-ieee-1284-3-data-link-device.md)

[Connecting an Interrupt Service Routine to a Parallel Port](connecting-an-interrupt-service-routine-to-a-parallel-port.md)

For more information about system support for parallel ports, see:

[Introduction to ParallelPorts and Devices](introduction-to-parallel-ports-and-devices.md)

[System-Supplied Parallel Drivers](system-supplied-parallel-drivers.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 




