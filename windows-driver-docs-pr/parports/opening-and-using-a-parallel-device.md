---
title: Opening and Using a Parallel Device
description: Opening and Using a Parallel Device
keywords:
- parallel devices WDK , opening
- parallel devices WDK , sharing
ms.date: 03/03/2023
---

# Opening and Using a Parallel Device





The system-supplied bus driver for parallel ports enforces exclusive access to a parallel device attached to a parallel port. If a parallel device is open, the parallel port bus driver fails any subsequent [**IRP\_MJ\_CREATE**](/previous-versions/ff544131(v=vs.85)) requests for the device until the device has been closed. A client must open a parallel device before it sends other I/O requests to the device or calls the [parallel device callback routines](/windows-hardware/drivers/ddi/index). A client must not attempt to communicate with a parallel device after the client has closed its file on a device. A client must close a device to allow other clients to access the device.

A client usually does the following:

-   Opens a parallel device

-   Connects to a parallel device − see [Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

-   Obtains information about the parallel device − see [Obtaining Information about a Parallel Device](obtaining-information-about-a-parallel-device.md)

-   Locks the device − see [Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

-   Does a sequence of operations on the device

-   Disconnects from a parallel device − see [Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

-   Unlocks the device − see [Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

-   Closes the device

Note that in a Plug and Play environment, a device can be removed or added whenever there are no open files on it. In general, every time a parallel device is added, Plug and Play assigns a different location and resources.

 

