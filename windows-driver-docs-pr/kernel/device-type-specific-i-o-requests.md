---
title: Device Type-Specific I/O Requests
author: windows-driver-content
description: Device Type-Specific I/O Requests
MS-HAID:
- 'IRPs\_83b8b71e-93b0-4ffe-a4bf-82917ae2f9d0.xml'
- 'kernel.device\_type\_specific\_i\_o\_requests'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 33ea0b0a-db58-40b7-b6d3-e981acf44dfe
keywords: ["IRPs WDK kernel , device type-specific I/O requests", "device type-specific I/O requests WDK kernel"]
---

# Device Type-Specific I/O Requests


## <a href="" id="ddk-device-type-specific-i-o-requests-kg"></a>


Device-specific sections of the Windows Driver Kit (WDK) provide information about device type-specific I/O requests handled by the system-supplied drivers for the most common kinds of devices.

A new kernel-mode driver must handle the same set of I/O requests as a system-supplied driver if the new driver meets any of the following conditions:

-   The new driver replaces a system driver for the same type of device.

-   The new driver supports another device of a type already in the system.

-   The new driver is an intermediate (filter) driver, layered between two system-supplied drivers.

Such a new driver must handle every **IRP\_MJ\_*XXX*** request that the system-supplied drivers handle. In most cases, a new device driver should also handle the same set of **IOCTL\_*XXX*** codes for [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests, even if the new driver must emulate the behavior of the corresponding system-supplied driver. Otherwise, the new driver might break user-mode applications that expect these kinds of requests to be honored.

For information about the NTSTATUS values that drivers can set in the I/O status block of IRPs, as the return value for specific requests, see [Using NTSTATUS Values](using-ntstatus-values.md). For information about NTSTATUS values that can be specified in an error log packet, see [Logging Errors](logging-errors.md). Use this information to decide on the appropriate status values to be returned by new drivers for similar types of devices, or as an aid in determining the appropriate status values to be returned by the driver for a new type of device.

For more information about various kinds of drivers and the requests that each is required to support, see the following:

[Serial Devices and Drivers](https://msdn.microsoft.com/library/windows/hardware/ff547451)

[System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff544814)

[Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976)

[HID Architecture](https://msdn.microsoft.com/library/windows/hardware/jj126193)

[I/O Requests for USB Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540134#km-ioctl)

[The IEEE 1394 Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff538867)

[Access Attribute Memory of a PCMCIA Device](https://msdn.microsoft.com/library/windows/hardware/ff536892)

For all other types of drivers, consult the documentation for the appropriate driver type.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Device%20Type-Specific%20I/O%20Requests%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


