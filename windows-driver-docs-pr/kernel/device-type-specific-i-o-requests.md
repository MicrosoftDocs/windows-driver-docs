---
title: Device Type-Specific I/O Requests
description: Device Type-Specific I/O Requests
ms.assetid: 33ea0b0a-db58-40b7-b6d3-e981acf44dfe
keywords: ["IRPs WDK kernel , device type-specific I/O requests", "device type-specific I/O requests WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Device Type-Specific I/O Requests





Device-specific sections of the Windows Driver Kit (WDK) provide information about device type-specific I/O requests handled by the system-supplied drivers for the most common kinds of devices.

A new kernel-mode driver must handle the same set of I/O requests as a system-supplied driver if the new driver meets any of the following conditions:

-   The new driver replaces a system driver for the same type of device.

-   The new driver supports another device of a type already in the system.

-   The new driver is an intermediate (filter) driver, layered between two system-supplied drivers.

Such a new driver must handle every **IRP\_MJ\_*XXX*** request that the system-supplied drivers handle. In most cases, a new device driver should also handle the same set of **IOCTL\_*XXX*** codes for [**IRP\_MJ\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-device-control) requests, even if the new driver must emulate the behavior of the corresponding system-supplied driver. Otherwise, the new driver might break user-mode applications that expect these kinds of requests to be honored.

For information about the NTSTATUS values that drivers can set in the I/O status block of IRPs, as the return value for specific requests, see [Using NTSTATUS Values](using-ntstatus-values.md). For information about NTSTATUS values that can be specified in an error log packet, see [Logging Errors](logging-errors.md). Use this information to decide on the appropriate status values to be returned by new drivers for similar types of devices, or as an aid in determining the appropriate status values to be returned by the driver for a new type of device.

For more information about various kinds of drivers and the requests that each is required to support, see the following:

[Serial Devices and Drivers](https://docs.microsoft.com/previous-versions/ff547451(v=vs.85))

[System-Supplied Parallel Drivers](https://docs.microsoft.com/previous-versions/ff544814(v=vs.85))

[Storage Drivers](https://docs.microsoft.com/windows-hardware/drivers/storage/storage-drivers)

[HID Architecture](https://docs.microsoft.com/previous-versions/jj126193(v=vs.85))

[I/O Requests for USB Client Drivers](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#km-ioctl)

[The IEEE 1394 Driver Stack](https://docs.microsoft.com/windows-hardware/drivers/ieee/the-ieee-1394-driver-stack)

[Access Attribute Memory of a PCMCIA Device](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/access-attribute-memory-of-a-pcmcia-device)

For all other types of drivers, consult the documentation for the appropriate driver type.

 

 




