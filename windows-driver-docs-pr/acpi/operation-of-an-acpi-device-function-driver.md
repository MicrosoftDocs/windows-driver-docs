---
title: Operation of an ACPI Device Function Driver
description: Provides information about operation of an ACPI device function driver
keywords:
- ACPI devices WDK , function driver operation
- vendor-supplied function drivers WDK ACPI
- function drivers WDK ACPI , operation
- WDM function drivers WDK ACPI , operation
ms.date: 03/17/2023
---

# Operation of an ACPI Device Function Driver

This section describes the generic operation of a vendor-supplied function driver for an ACPI device.

A function driver for an ACPI device is a WDM driver that does the following:

- Complies with the minimum requirements for a WDM function driver, as described in [Windows Driver Model](../kernel/introduction-to-wdm.md). This includes driver entry points, dispatch routines, Plug and Play, power management, and Windows Management Instrumentation (WMI). This basic functionality provides the generic operation that Windows requires of the driver and the framework in which to implement the ACPI device-specific operations.

- Supports the device's operation region, which is the communication interface between the function driver and the ACPI BIOS.

    For more information, see [Supporting an Operation Region](supporting-an-operation-region.md).

- Optionally, supports a vendor-defined *device interface* and *IOCTLs* that other drivers or user-mode applications use to operate a device.

    For more information, see [Providing a Vendor-Defined ACPI Device Interface](providing-a-vendor-defined-acpi-device-interface.md).
