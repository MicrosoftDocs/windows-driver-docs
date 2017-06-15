---
title: Filter Drivers
author: windows-driver-content
description: Filter Drivers
MS-HAID:
- 'WDMIntro\_eb864c97-27b4-4f6d-aeb9-237b444c1789.xml'
- 'kernel.filter\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4def5503-bb0e-4bae-b048-4c8d25d62020
keywords: ["filter drivers WDK WDM", "bus filter drivers WDK WDM", "lower-level filter drivers WDK WDM", "upper-level filter drivers WDK WDM", "WDM filter drivers WDK"]
---

# Filter Drivers


## <a href="" id="ddk-filter-drivers-kg"></a>


Filter drivers are optional drivers that add value to or modify the behavior of a device. A filter driver can service one or more devices.

### <a href="" id="ddk-bus-filter-drivers-kg"></a>Bus Filter Drivers

*Bus filter drivers* typically add value to a bus and are supplied by Microsoft or a system OEM (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). Bus filter drivers are optional. There can be any number of bus filter drivers for a bus.

A bus filter driver could, for example, implement proprietary enhancements to standard bus hardware.

For devices described by an ACPI BIOS, the power manager inserts a Microsoft-supplied *ACPI filter* (bus filter driver) above the bus driver for each such device. The ACPI filter carries out device power policy and powers on and off devices. The ACPI filter is transparent to other drivers and is not present on non-ACPI machines.

### <a href="" id="ddk-lower-level-filter-drivers-kg"></a>Lower-Level Filter Drivers

*Lower-level filter drivers* typically modify the behavior of device hardware (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). They are typically supplied by IHVs and are optional. There can be any number of lower-level filter drivers for a device.

A lower-level *device* filter driver monitors and/or modifies I/O requests to a particular device. Typically, such filters redefine hardware behavior to match expected specifications.

A lower-level *class* filter driver monitors and/or modifies I/O requests for a class of devices. For example, a lower-level class filter driver for mouse devices could provide acceleration, performing a nonlinear conversion of mouse movement data.

### <a href="" id="ddk-upper-level-filter-drivers-kg"></a>Upper-Level Filter Drivers

*Upper-level filter drivers* typically provide added-value features for a device (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). Such drivers are usually provided by IHVs and are optional. There can be any number of upper-level filter drivers for a device.

An upper-level *device* filter driver adds value for a particular device. For example, an upper-level device filter driver for a keyboard could enforce additional security checks.

An upper-level *class* filter driver adds value for all devices of a particular class.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Filter%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


