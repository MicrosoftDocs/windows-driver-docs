---
title: Points to Consider about User I/O Requests
description: Points to Consider about User I/O Requests
ms.assetid: e8143055-4ad7-4e39-a2f2-64d9e79d33a0
keywords: ["device-specific I/O control codes WDK kernel", "private I/O control codes WDK kernel", "layered driver IRP processing WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Points to Consider about User I/O Requests





Keep the following points in mind when designing a kernel-mode driver:

- Drivers can be layered, and more than one driver can process a single I/O request (IRP).

- A driver cannot make any assumptions about which other drivers will be in the device stack. Therefore, each driver should be prepared to receive requests from any other driver and should handle all potential error cases.

- Drivers communicate the success or failure of a requested I/O operation in the I/O status block of the IRP. The I/O manager communicates the success or failure of a requested I/O operation to a user-mode requester.

- Drivers need not and should not be designed to provide application-specific support. A protected subsystem or its subsystem-specific, user-mode drivers supply this kind of support. There is one exception to this rule: an MS-DOS application that relies on an application-dedicated device can require a kernel-mode driver to control the device and a closely coupled Win32 user-mode virtual device driver (VDD). For more information about VDDs, see the Virtual Device Drivers documentation in the Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

- A new driver must handle the same set of **IRP\_MJ\_*XXX*** as any system-supplied driver it replaces. The I/O manager returns STATUS\_INVALID\_DEVICE\_REQUEST for a given I/O request to a target device if its driver does not define an entry point for that <strong>IRP\_MJ\_*XXX</strong><em>. A device driver also must handle the same I/O control codes for [</em>*IRP\_MJ\_DEVICE\_CONTROL**](<https://msdn.microsoft.com/library/windows/hardware/ff550744>) requests as any system-supplied driver it replaces. In other words, a new device driver must not "break applications" by implementing less functionality than an existing driver for the same type of device.

- A new intermediate driver inserted into a chain of existing drivers should recognize the same set of **IRP\_MJ\_*XXX*** as the driver it displaces. The new driver can simply pass on IRPs for those requests that it does not process to the next-lower-level driver. However, a new intermediate driver must not "break the chain" for drivers above and below it by neglecting to define an entry point for an **IRP\_MJ\_*XXX*** request that the newly displaced, next-lower-level driver does handle.

- A lowest-level driver can access only its own I/O stack location in any IRP that it is sent. A higher-level driver can access only its own and the next-lower-level driver's I/O stack locations in any IRP that it is sent.

- Every driver communicates information to higher-level drivers (and ultimately, to user-mode applications via the I/O manager) only in the I/O status blocks of IRPs because the I/O manager zeros the corresponding I/O stack location as each driver in a chain completes an IRP. Any new driver that attempts to implement back-door communication with a particular higher (or lower) driver compromises its portability and its interoperability with other drivers from one Windows platform or version to the next.

- A pair of drivers can define a set of device-specific (also called *private*) I/O control codes for [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests that the higher of the pair can send down to the lower of the pair. However, such a pair of drivers must follow all of the preceding guidelines if they are to remain portable and interoperable with other drivers from one Windows platform or version to another. If you design a pair of drivers with a private interface, consider the set of I/O control codes to be defined carefully. Make them as generally useful as possible and design your paired drivers to follow the preceding guidelines, so that you (or someone else) can reuse, replace, or displace either or both of your new drivers easily as they migrate from one Windows platform or version to another.

 

 




