---
title: Operation of an ACPI Device Function Driver
author: windows-driver-content
description: Operation of an ACPI Device Function Driver
MS-HAID:
- 'opregdg\_f7f90fd6-fbee-4c06-b439-595497562382.xml'
- 'acpi.operation\_of\_an\_acpi\_device\_function\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 56c63373-5094-4ae5-a7b0-56d61e3fa9b1
keywords: ["ACPI devices WDK , function driver operation", "vendor-supplied function drivers WDK ACPI", "function drivers WDK ACPI , operation", "WDM function drivers WDK ACPI , operation"]
---

# Operation of an ACPI Device Function Driver


## <a href="" id="ddk-operation-of-an-acpi-device-function-driver-kg"></a>


This section describes the generic operation of a vendor-supplied function driver for an ACPI device.

A function driver for an ACPI device is a WDM driver that does the following:

-   Complies with the minimum requirements for a WDM function driver, as described in [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698). This includes driver entry points, dispatch routines, Plug and Play, power management, and Windows Management Instrumentation (WMI). This basic functionality provides the generic operation that Windows requires of the driver and the framework in which to implement the ACPI device-specific operations.

-   Supports the device's operation region, which is the communication interface between the function driver and the ACPI BIOS.

    For more information, see [Supporting an Operation Region](supporting-an-operation-region.md).

-   Optionally, supports a vendor-defined [*device interface*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface) and [*IOCTLs*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-ioctl) that other drivers or user-mode applications use to operate a device.

    For more information, see [Providing a Vendor-Defined ACPI Device Interface](providing-a-vendor-defined-acpi-device-interface.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Operation%20of%20an%20ACPI%20Device%20Function%20Driver%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


