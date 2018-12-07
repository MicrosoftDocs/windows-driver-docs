---
title: Operating a Parallel Device Attached to a Parallel Port
description: Operating a Parallel Device Attached to a Parallel Port
ms.assetid: 5ad36162-efbe-4be8-954c-964ef12c539a
keywords:
- parallel ports WDK , parallel device operation
- parallel devices WDK
- vendor-supplied parallel drivers WDK , parallel device operation
- parallel devices WDK , client operation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operating a Parallel Device Attached to a Parallel Port





This section describes how a client, in particular, a vendor-supplied function driver for a parallel device, operates a parallel device attached to a parallel port.

The system-supplied bus driver for parallel ports creates a physical device object (PDO) for each parallel device enumerated on a parallel port. The following topics describe how a client operates a parallel device by using the interface provided by the device's PDO:

[Opening and Using a Parallel Device](opening-and-using-a-parallel-device.md)

[Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

[Obtaining Information about a Parallel Device](obtaining-information-about-a-parallel-device.md)

[Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

[Setting and Clearing a Communication Mode for a Parallel Device](setting-and-clearing-a-communication-mode-for-a-parallel-device.md)

[Setting Attributes on a Parallel Device](setting-attributes-on-a-parallel-device.md)

[Reading and Writing a Parallel Device](reading-and-writing-a-parallel-device.md)

For more information about support for parallel devices attached to a parallel port, see:

[Introduction to ParallelPorts and Devices](introduction-to-parallel-ports-and-devices.md)

[System-Supplied Parallel Drivers](system-supplied-parallel-drivers.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 




