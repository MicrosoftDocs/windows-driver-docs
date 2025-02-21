---
title: Filter Drivers
description: Provides information about types of filter drivers.
keywords: ["filter drivers WDK WDM", "bus filter drivers WDK WDM", "lower-level filter drivers WDK WDM", "upper-level filter drivers WDK WDM", "WDM filter drivers WDK"]
ms.date: 02/20/2025
---

# Filter drivers (WDM)

Filter drivers are optional drivers that add value to or modify the behavior of a device. A filter driver can service one or more devices.

## Bus filter drivers

*Bus filter drivers* typically add value to a bus and are supplied by Microsoft or a system OEM (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). Bus filter drivers are optional. There can be any number of bus filter drivers for a bus.

A bus filter driver could, for example, implement proprietary enhancements to standard bus hardware.

For devices described by an ACPI BIOS, the power manager inserts a Microsoft-supplied *ACPI filter* (bus filter driver) above the bus driver for each such device. The ACPI filter carries out device power policy and powers on and off devices. The ACPI filter is transparent to other drivers and is not present on non-ACPI machines.

## Lower-level filter drivers

*Lower-level filter drivers* typically modify the behavior of device hardware (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). They are typically supplied by IHVs and are optional. There can be any number of lower-level filter drivers for a device.

A lower-level *device* filter driver monitors and/or modifies I/O requests to a particular device. Typically, such filters redefine hardware behavior to match expected specifications.

A lower-level *class* filter driver monitors and/or modifies I/O requests for a class of devices. For example, a lower-level class filter driver for mouse devices could provide acceleration, performing a nonlinear conversion of mouse movement data.

## Upper-level filter drivers

*Upper-level filter drivers* typically provide added-value features for a device (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). Such drivers are usually provided by IHVs and are optional. There can be any number of upper-level filter drivers for a device.

An upper-level *device* filter driver adds value for a particular device. For example, an upper-level device filter driver for a keyboard could enforce additional security checks.

An upper-level *class* filter driver adds value for all devices of a particular class.
