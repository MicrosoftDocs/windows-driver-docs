---
title: How File System Filter Drivers Are Similar to Device Drivers
description: How File System Filter Drivers Are Similar to Device Drivers
keywords:
- filter drivers WDK file system , vs. device drivers
- file system filter drivers WDK , vs. device drivers
- device drivers WDK file system
ms.date: 10/16/2019
---

# How File System Filter Drivers Are Similar to Device Drivers

File system filter drivers and device drivers in the Microsoft Windows operating system are similar in the following ways:

- **Similar Structure**

  Like device drivers, file system filter drivers have [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), [dispatch](../kernel/writing-dispatch-routines.md), and [I/O completion](../kernel/using-iocompletion-routines.md) routines. They call many of the same kernel-mode routines that device drivers call, and they filter I/O requests for devices (that is, file system volumes) with which they are associated.

- **Similar Functionality**

  - Because file system filter drivers and device drivers are part of the I/O system, they both receive [I/O request packets](../kernel/packet-driven-i-o-with-reusable-irps.md) (IRPs) and act on them.

  - Like device drivers, file system filter drivers can also create their own IRPs and send them to lower-level drivers.

  - Both kinds of drivers can register for notification (by using callback functions) of various system events.

- **Other Similarities**

  - Like device drivers, file system filter drivers can receive [I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) (IOCTLs). Note that file system filter drivers can also receive and define [file system control codes](./fsctl-add-overlay.md) (FSCTLs).

  - Like device drivers, file system filter drivers can be configured to be loaded at system startup time or to be loaded later, after the system startup process is complete.
