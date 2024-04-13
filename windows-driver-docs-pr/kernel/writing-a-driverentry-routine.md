---
title: Writing a DriverEntry Routine
description: Writing a DriverEntry Routine
keywords: ["standard driver routines WDK kernel , DriverEntry routine", "driver routines WDK kernel , DriverEntry routine", "routines WDK kernel , DriverEntry routine", "DriverEntry WDK kernel", "DriverEntry WDK kernel , about DriverEntry routine", "driver initialization WDK kernel", "initializing drivers"]
ms.date: 06/16/2017
---

# Writing a DriverEntry Routine





Each driver must have a [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, which initializes driver-wide data structures and resources. The I/O manager calls the **DriverEntry** routine when it loads the driver.

In a driver that supports Plug and Play (PnP), as all drivers should, the **DriverEntry** routine is responsible for *driver* initialization, while the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine (and, possibly, the dispatch routine that handles a PnP [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request) is responsible for *device* initialization. Driver initialization includes exporting the driver's other entry points, initializing certain objects the driver uses, and setting up various per-driver system resources. (Non-PnP drivers have significantly different requirements, as described in the Driver Development Kit \[DDK\] for Microsoft Windows NT 4.0 and earlier.)

**DriverEntry** routines are called in the context of a system thread at IRQL = PASSIVE\_LEVEL.

A **DriverEntry** routine can be pageable and should be in an INIT segment so it will be discarded. Use an **alloc\_text** pragma directive, as illustrated in the sample drivers that are provided with the Windows Driver Kit (WDK).

This section contains the following topics:

[DriverEntry's Required Responsibilities](driverentry-s-required-responsibilities.md)

[DriverEntry's Optional Responsibilities](driverentry-s-optional-responsibilities.md)

[DriverEntry Return Values](driverentry-return-values.md)

 

