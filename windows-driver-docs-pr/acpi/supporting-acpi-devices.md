---
title: Supporting ACPI Devices
author: windows-driver-content
description: Supporting ACPI Devices
MS-HAID:
- 'opregdg\_66824886-328f-4879-865b-de44358b8a72.xml'
- 'acpi.supporting\_acpi\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ebaf2e66-4f56-48ca-93ca-f34e694c0d73
keywords: ["Advanced Configuration and Power Interface Specification WDK", "ACPI devices WDK", "ACPI devices WDK , about ACPI devices", "definition blocks WDK ACPI", "operation regions WDK ACPI", "operation region handlers WDK ACPI", "function drivers WDK ACPI", "WDM function drivers WDK ACPI"]
---

# Supporting ACPI Devices


## <a href="" id="ddk-supporting-acpi-devices-kg"></a>


This section describes how a vendor can use a WDM function driver in Microsoft Windows 2000 and later versions of Windows to enhance the functionality of an Advanced Configuration and Power Interface (ACPI) device.

ACPI devices include low-level system devices such as batteries, thermal zones, and other devices defined in a system's ACPI namespace. An ACPI namespace is a hierarchical namespace that an ACPI BIOS uses to reference objects.

The combined operation of the system-supplied [ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493) and the ACPI BIOS supports the basic functionality of ACPI devices and is transparent to the rest of the operating system. An ACPI device is specified by a definition block in the ACPI System Description Tables. A device's definition block specifies, among other things, an operation region, which specifies a contiguous block of device memory that is used to access device data.

To enhance the functionality of an ACPI device, the vendor can supply a WDM function driver, which communicates with the ACPI BIOS through an operation region supplied by the driver. The ACPI driver accesses the operation region by calling an operation region handler supplied by the function driver.

By communicating through ACPI operation regions, a function driver can indirectly access devices that are normally only controlled by the BIOS, and the BIOS can invoke device-specific operations that depend on the configuration of the driver and the host system. The basic operating mechanism is as follows:

1.  The ACPI BIOS reads or writes data in a device's operation region.

2.  To access the operation region, the ACPI driver calls the function driver's operation region handler.

3.  The operation region handler does whatever action is programmed for the access and returns information associated with the access.

The following two examples show how a vendor can use a function driver to enhance the capability of an ACPI device:

1.  An ACPI device can access an index in a function driver's operation region that causes the driver to enable a sound card volume control in a vendor's preinstalled software.

2.  The driver monitors the remaining capacity of batteries, the temperatures of thermal zones, and other things that are normally only accessed by the BIOS.

The following topics describe how to supply a function driver for an ACPI device:

[Device Stacks for an ACPI Device](device-stacks-for-an-acpi-device.md)

[Operation of an ACPI Device Function Driver](operation-of-an-acpi-device-function-driver.md)

For information about the system-supplied support routines that support ACPI device function drivers, see [ACPI Operation Region Handler Reference](https://msdn.microsoft.com/library/windows/hardware/ff536132).

For more information about ACPI devices and namespaces, see the [Advanced Configuration and Power Interface (ACPI) Specification](http://go.microsoft.com/fwlink/p/?linkid=57185).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Supporting%20ACPI%20Devices%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


