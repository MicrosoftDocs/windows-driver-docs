---
title: ACPI namespace hierarchy
author: windows-driver-content
description: The ACPI namespace hierarchy must accurately model the platform's hardware topology, starting with the processor's system bus ( \ 0034;\\\_SB \ 0034;).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 14B5F787-65B1-4BC3-90CD-D4AD1C8044D1
---

# ACPI namespace hierarchy


The ACPI namespace hierarchy must accurately model the platform's hardware topology, starting with the processor's system bus ("\\\_SB"). In general, a device that connects to a bus or controller appears as a child of that bus or controller device in the namespace.

The following rules apply specifically to SoC-based platforms:

-   Memory-mapped functional blocks (including processors) appear directly under the \\\_SB node.
-   Peripheral devices that connect to some combination of simple peripheral bus (SPB) controllers and/or GPIO controllers describe their connections to these controllers as connection resources. For more information, see [General Purpose I/O (GPIO)](general-purpose-i-o--gpio-.md) and [Simple Peripheral Bus (SPB)](simple-peripheral-bus--spb-.md).

    Peripherals that are connected in this way might appear directly under the \\\_SB node, or under a parent SPB or GPIO controller. The latter is preferred, when possible, because it indicates the device relationship directly in the namespace itself, instead of requiring the decoding of resources to discover the relationship.

-   Any functional blocks or peripherals that are connected through a standard bus that supports hardware enumeration (for example, SDIO and USB) do not need to appear in the namespace at all.

    However, you must include such devices under their parent controller in the namespace in certain cases. For example, this is necessary with embedded USB HSIC or SDIO devices, where platform-specific (non-standard) controls (for example, power switches, GPIO or SPB connections, and so on) are associated with the device as part of the system design. In this case, the standard parent bus driver enumerates the device, but the [Windows ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493), Acpi.sys, is loaded as a filter in the device stack to invoke the control methods for the non-standard controls on behalf of the bus driver, as needed.

-   Any "private" buses or devices (for example, I2S) that are dedicated to the use of one function driver (for example, the audio driver) do not need to appear in the namespace at all. However, in this case, any system resources used by the device must appear in the function device's resource list in the namespace. For more information, see [Device Configuration Objects](device-management-namespace-objects.md#devconobj).

ACPI defines many standard namespace objects and methods, but implementers can define new ones as they are needed. The ACPI-defined objects and methods are used for common operating system functions such as the following:

<a href="" id="platform-description"></a>*Platform description*  
For example, device identification and system resource allocation.

<a href="" id="generic-device-control"></a>*Generic device control*  
For example, configuring resources and controlling power resources.

<a href="" id="class-specific-feature-control"></a>*Class-specific feature control*  
For example, dimming displays or reporting battery status.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20ACPI%20namespace%20hierarchy%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


