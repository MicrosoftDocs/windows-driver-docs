---
title: Supporting ACPI Devices
description: Supporting ACPI Devices
ms.assetid: ebaf2e66-4f56-48ca-93ca-f34e694c0d73
keywords:
- Advanced Configuration and Power Interface Specification WDK
- ACPI devices WDK
- ACPI devices WDK , about ACPI devices
- definition blocks WDK ACPI
- operation regions WDK ACPI
- operation region handlers WDK ACPI
- function drivers WDK ACPI
- WDM function drivers WDK ACPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting ACPI Devices


This section describes how a vendor can use a WDM function driver in Windows to enhance the functionality of an Advanced Configuration and Power Interface (ACPI) device.

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

For more information about ACPI devices and namespaces, see the [Advanced Configuration and Power Interface (ACPI) Specification](https://go.microsoft.com/fwlink/p/?linkid=866846).
