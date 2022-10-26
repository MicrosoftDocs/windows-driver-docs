---
title: Acpi.sys (Windows ACPI driver)
description: The Windows ACPI driver, Acpi.sys, is an inbox component of the Windows operating system.
keywords: ["ACPI drivers WDK power management", "enumerators WDK power management", "PDOs WDK power management", "filter DOs WDK power management", "physical device objects WDK power management"]
ms.date: 10/19/2022
---

# Acpi.sys (Windows ACPI driver)

The Windows ACPI driver, Acpi.sys, is an inbox component of the Windows operating system. The responsibilities of Acpi.sys include support for power management and Plug and Play (PnP) device enumeration. On hardware platforms that have an [ACPI BIOS](acpi-bios.md), the [HAL](windows-kernel-mode-hal-library.md) causes Acpi.sys to be loaded during system startup at the base of the [device tree](device-tree.md). Acpi.sys acts as the interface between the operating system and the ACPI BIOS. Acpi.sys is transparent to the other drivers in the device tree.

Other tasks performed by Acpi.sys on a particular hardware platform might include reprogramming the resources for a COM port or enabling the USB controller for system wake-up.

## In this topic

- [ACPI devices](#acpi-devices)

- [ACPI control methods](#acpi-control-methods)

- [ACPI specification](#acpi-specification)

- [ACPI debugging](#acpi-debugging)

- [Microsoft ACPI source language (ASL) compiler](#microsoft-acpi-source-language-asl-compiler)

## ACPI devices

The hardware platform vendor specifies a hierarchy of ACPI namespaces in the ACPI BIOS to describe the hardware topology of the platform. For more information, see [ACPI namespace hierarchy](../bringup/acpi-namespace-hierarchy.md).

For each device described in the ACPI namespace hierarchy, the Windows ACPI driver, Acpi.sys, creates either a filter device object (filter DO) or a physical device object (PDO). If the device is integrated into the system board, Acpi.sys creates a filter device object, representing an ACPI bus filter, and attaches it to the device stack immediately above the bus driver (PDO). For other devices described in the ACPI namespace but not on the system board, Acpi.sys creates the PDO. Acpi.sys provides power management and PnP features to the device stack with these device objects. For more information, see [Device stacks for an ACPI device](../acpi/device-stacks-for-an-acpi-device.md).

A device for which Acpi.sys creates a device object is called an [ACPI device](../acpi/supporting-acpi-devices.md). The set of ACPI devices varies from one hardware platform to the next, and depends on the ACPI BIOS and the configuration of the motherboard. Acpi.sys loads an ACPI bus filter only for a device that is described in the ACPI namespace and is permanently connected to the hardware platform (typically, this device is integrated into the core silicon or soldered to the system board). Not all motherboard devices have an ACPI bus filter.

All ACPI functionality is transparent to higher-level drivers. These drivers must make no assumptions about the presence or absence of an ACPI filter in any given device stack.

Acpi.sys and the ACPI BIOS support the basic functions of an ACPI device. To enhance the functionality of an ACPI device, the device vendor can supply a WDM function driver. For more information, see [Operation of an ACPI device function driver](../acpi/operation-of-an-acpi-device-function-driver.md).

An ACPI device is specified by a definition block in the [system description tables](../bringup/acpi-system-description-tables.md) in the ACPI BIOS. A device's definition block specifies, among other things, an operation region, which is a contiguous block of device memory that is used to access device data. Only Acpi.sys modifies the data in an operation region. The device's function driver can read the data in an operation region but must not modify the data. When called, an [operation region handler](../acpi/implementing-an-operation-region-handler.md) transfers bytes in the operation region to and from the data buffer in Acpi.sys. The combined operation of the function driver and Acpi.sys is device-specific and is defined in the ACPI BIOS by the hardware vendor. In general, the function driver and Acpi.sys access particular areas in an operation region to perform device-specific operations and retrieve information. For more information, see [Supporting an operation region](../acpi/supporting-an-operation-region.md).

## ACPI control methods

ACPI control methods are software objects that declare and define simple operations to query and configure ACPI devices. Control methods are stored in the ACPI BIOS and are encoded in a byte-code format called ACPI machine language (AML). The control methods for a device are loaded from the system firmware into the device's ACPI namespace in memory, and interpreted by the Windows ACPI driver, Acpi.sys.

To invoke a control method, the kernel-mode driver for an ACPI device initiates an [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) request, which is handled by Acpi.sys. For drivers loaded on ACPI-enumerated devices, Acpi.sys always implements the physical device object (PDO) in the driver stack. For more information, see [Evaluating ACPI control methods](../acpi/evaluating-acpi-control-methods.md).

## ACPI specification

The *Advanced Configuration and Power Interface Specification* ([ACPI 5.0 specification](https://uefi.org/specifications)) is available from the Unified Extensible Firmware Interface Forum website.

Revision 5.0 of the ACPI specification introduces a set of features to support low-power, mobile PCs that are based on System on Chip (SoC) integrated circuits and that implement the [connected standby](/windows-hardware/design/device-experiences/modern-standby) power model. Starting with Windows 8 and later versions, the Windows ACPI driver, Acpi.sys, supports the new features in the ACPI 5.0 specification. For more information, see [Windows ACPI design guide for SoC platforms](../bringup/windows-acpi-design-guide-for-soc-platforms.md).

## ACPI debugging

System integrators and ACPI device driver developers can use the Microsoft [AMLI debugger](../debugger/introduction-to-the-amli-debugger.md) to debug AML code. Because AML is an interpreted language, AML debugging requires special software tools.

For more information about the AMLI debugger, see [ACPI debugging](../debugger/acpi-debugging.md).

## Microsoft ACPI source language (ASL) compiler

For information about compiling ACPI source language (ASL) into ACPI machine language (AML), see [Microsoft ASL compiler](../bringup/microsoft-asl-compiler.md).

Version 5.0 of the Microsoft ASL compiler supports features in the [ACPI 5.0 specification](https://uefi.org/specifications).

The ASL compiler is distributed with the [Windows Driver Kit (WDK)](../download-the-wdk.md).

The ASL compiler (asl.exe) is located in the Tools\\arm\\ACPIVerify, Tools\\arm64\\ACPIVerify, Tools\\x86\\ACPIVerify, and Tools\\x64\\ACPIVerify directories of the installed WDK, for example, C:\Program Files (x86)\Windows Kits\10\Tools\x86\ACPIVerify.
