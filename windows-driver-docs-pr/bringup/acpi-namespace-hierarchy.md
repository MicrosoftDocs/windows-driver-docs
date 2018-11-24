---
title: ACPI namespace hierarchy
description: The ACPI namespace hierarchy must accurately model the platform's hardware topology, starting with the processor's system bus ( \ 0034;\\_SB \ 0034;).
ms.assetid: 14B5F787-65B1-4BC3-90CD-D4AD1C8044D1
ms.date: 05/15/2018
ms.localizationpriority: medium
---

# ACPI namespace hierarchy


The ACPI namespace hierarchy must accurately model the platform's hardware topology, starting with the processor's system bus ("\\\_SB"). In general, a device that connects to a bus or controller appears as a child of that bus or controller device in the namespace.

The following rules apply specifically to SoC-based platforms:

-   Memory-mapped functional blocks (including processors) appear directly under the \\\_SB node.
-   Peripheral devices that connect to some combination of simple peripheral bus (SPB) controllers and/or GPIO controllers describe their connections to these controllers as connection resources. For more information, see [General Purpose I/O (GPIO)](general-purpose-i-o--gpio-.md) and [Simple Peripheral Bus (SPB)](simple-peripheral-bus--spb-.md).

    Peripherals that are connected in this way might appear directly under the \\\_SB node, or under a parent SPB or GPIO controller. The latter is preferred, when possible, because it indicates the device relationship directly in the namespace itself, instead of requiring the decoding of resources to discover the relationship.

-   Any functional blocks or peripherals that are connected through a standard bus that supports hardware enumeration (for example, SDIO and USB) do not need to appear in the namespace at all.

    However, you must include such devices under their parent controller in the namespace in certain cases. For example, this is necessary with embedded USB HSIC or SDIO devices, where platform-specific (non-standard) controls (for example, power switches, GPIO or SPB connections, and so on) are associated with the device as part of the system design. In this case, the standard parent bus driver enumerates the device, but the [Windows ACPI driver](https://docs.microsoft.com/windows-hardware/drivers/kernel/acpi-driver), Acpi.sys, is loaded as a filter in the device stack to invoke the control methods for the non-standard controls on behalf of the bus driver, as needed.

-   Any "private" buses or devices (for example, I2S) that are dedicated to the use of one function driver (for example, the audio driver) do not need to appear in the namespace at all. However, in this case, any system resources used by the device must appear in the function device's resource list in the namespace. For more information, see the **Device configuration objects** section in the [Device management namespace objects](device-management-namespace-objects.md) topic.

ACPI defines many standard namespace objects and methods, but implementers can define new ones as they are needed. The ACPI-defined objects and methods are used for common operating system functions such as the following:

*Platform description*
For example, device identification and system resource allocation.

*Generic device control*
For example, configuring resources and controlling power resources.

*Class-specific feature control*
For example, dimming displays or reporting battery status.


