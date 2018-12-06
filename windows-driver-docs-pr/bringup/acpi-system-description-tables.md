---
title: ACPI system description tables
description: Implementation of the Advanced Configuration and Power Interface (ACPI) Hardware Specification is not required on SoC-based platforms, but much of the ACPI Software Specification is (or can be) required.
ms.assetid: 6EFCD288-031D-46BB-ABF3-8ADB53E7B4B1
ms.date: 07/12/2018
ms.localizationpriority: medium
---

# ACPI system description tables


Implementation of the Advanced Configuration and Power Interface (ACPI) Hardware Specification is not required on SoC-based platforms, but much of the ACPI Software Specification is (or can be) required. ACPI defines a generic, extensible table-passing mechanism, plus specific tables for describing the platform to the operating system.

Table structures and headers, including ID and checksum fields, are defined in the [ACPI 5.0 specification](https://www.uefi.org/specifications). Windows utilizes this table-passing mechanism, in addition to the specific tables that are described in this article.

The idea behind these tables is to enable generic software to support standard intellectual property (IP) blocks that can be integrated into various platforms in diverse ways. With the table strategy, the platform-variable attributes of a particular platform are provided in a table, and used by generic software to adapt itself to the specific set of IP blocks integrated into the platform. This software can therefore be written once, thoroughly tested, and then optimized over time.

## Root System Description Pointer (RSDP)


Windows depends on UEFI firmware to boot up the hardware platform. Hence, Windows will use the EFI system table to locate the RSDP, as described in section 5.2.5.2, "Finding the RSDP on UEFI Enabled Systems", of the [ACPI 5.0 specification](https://www.uefi.org/specifications). The platform firmware fills in the address of either the RSDT or XSDT in the RSDP. (If both table addresses are provided, Windows will prefer the XSDT. )

## Root System Description Table (RSDT)


The RSDT (or XSDT) includes pointers to any other system description tables provided on the platform. Specifically, this table contains pointers to the following:

-   The Fixed ACPI Hardware Table (FADT)
-   The multiple interrupt controller table (MADT)
-   Optionally, the Core System Resource Table (CSRT)
-   The Debug Port Table 2 (DBG2)
-   The Boot Graphics Resource Table (BGRT)
-   The Firmware Performance Data Table (FPDT)
-   The base system description table (DSDT)
-   Optionally, additional system description tables (SSDT)

## Fixed ACPI Description Table (FADT)


The Fixed ACPI Hardware Table (FADT) contains important information about the various Fixed Hardware features available on the platform. To support hardware-reduced ACPI platforms, ACPI 5.0 extends the FADT table definition as follows:

-   The Flags field within the FADT (offset 112) has two new flags:

    HARDWARE\_REDUCED\_ACPI
    Bit offset 20. Indicates that ACPI hardware is not available on this platform. This flag must be set if the ACPI Fixed Hardware Programming Model is not implemented.

    LOW\_POWER\_S0\_IDLE\_CAPABLE
    Bit offset 21. Indicates that the platform supports low-power idle states within the ACPI S0 system power state that are more energy efficient than any Sx sleep state. If this flag is set, Windows will not try to sleep and resume, but will instead use platform idle states and connected standby.

-   The FADT Preferred\_PM\_Profile field (byte offset 45) has a new role entry, "Tablet". This role influences power management policy for the display and input, and affects the display of on-screen keyboards.
-   The "IA-PC Boot Architecture Flags" field (offset 109) has a new "CMOS RTC Not Present" flag (bit offset 5) to indicate that the PC's CMOS RTC is either not implemented, or does not exist at the legacy addresses. If this flag is set, the platform must implement the ACPI Time and Alarm Control Method device. For more information, see the **Control Method Time and Alarm device** section in the [ACPI defined devices](acpi-defined-devices.md) topic.
-   New fields are added to support traditional PC sleep/resume on hardware-reduced ACPI platforms. These fields are ignored by Windows, but must be present in the table for compliance.
-   If the HARDWARE\_REDUCED\_ACPI flag is set, all fields relating to the ACPI Hardware Specification are ignored by the operating system.

All other FADT settings retain their meanings from the previous version, ACPI 4.0. For more information, see section 5.2.9, "Fixed ACPI Description Table (FADT)", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

## Multiple APIC Description Table (MADT)


In PC implementations of ACPI, the Multiple APIC Description Table (MADT) and PC-specific interrupt controller descriptors are used to describe the system interrupt model. For ARM-based SoC platforms, ACPI 5.0 adds descriptors for the ARM Holdings' Generic Interrupt Controller (GIC) and GIC Distributor. Windows includes inbox support for the GIC and GIC Distributor. For more information about these descriptors, see sections 5.2.12.14, "GIC Structure", and 5.2.12.15, "GIC Distributor Structure", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

The interrupt controller descriptor structures are listed immediately after the Flags field in the MADT. For ARM platforms, one descriptor is listed for each GIC, followed by one for each GIC Distributor. The GIC corresponding to the boot processor must be the first entry in the list of interrupt controller descriptors.

## Generic Timer Description Table (GTDT)


As with the interrupt controller, there is a standard timer description table in ACPI. For ARM systems that utilize the GIT timer, ACPI's GTDT can be used to leverage the built-in support for the GIT in Windows.

## Core System Resources Table (CSRT)


Core System Resources (CSRs) are shared hardware functions such as interrupt controllers, timers and DMA controllers to which the operating system must serialize access. Where industry standards exist for features such as timers and interrupt controllers (on both x86 and ARM architectures), Windows builds in support for these features based on the standard tables described in ACPI (for example, MADT and GTDT). However, until the industry converges on DMA controller interface standards, there is a need to support some non-standard devices in the operating system.

Windows supports the concept of HAL extensions to address this issue. HAL extensions are SoC-specific modules, implemented as DLLs, that adapt the Windows HAL to a specific hardware interface of a specific class of CSR required by Windows. In order to identify and load these non-standard CSR modules, Microsoft has defined a new ACPI table. This table, which has a reserved signature of "CSRT" in the ACPI specification, must be included in the RSDT if non-standard CSRs are used on the platform.

The CSRT describes resource groups of CSRs, where each resource group identifies hardware of a particular type. Windows uses the identifier provided for the resource group to find and load the required HAL extension for this group. Resource groups within the CSRT might also contain individual resource descriptors, depending on the CSR type and the needs of the HAL extension. The format and use of these resource descriptors is defined by the HAL extension writer, who can make the extension much more portable and thereby support a variety of different SoC platforms simply by changing the resource descriptors contained in the CSRT.

To support maintenance of HAL extensions, and to manage the system resources used by these extensions, each resource group described in the CSRT must also be represented as a device within the platform's ACPI namespace. For more information, see the following "Differentiated System Description Table (DSDT)" section. The device identifiers used in the resource group header must match the identifiers used in the device's namespace node. For more information, see the **Device Identification in ACPI** section in the [Device management namespace objects](device-management-namespace-objects.md) topic. The existence of these resource group namespace devices allows the HAL extension to be serviced by the Windows Update Service.

For more information, see the [Core System Resources Table (CSRT) specification](http://acpica.org/related-documents).

## Debug Port Table 2 (DBG2)


Microsoft requires a debug port on all systems. To describe the debug port(s) built into a platform, Microsoft defines the Debug Port Table 2 (DBG2) for ACPI. This table specifies one or more independent port(s) for debugging purposes. The presence of the DBG2 table indicates that the platform includes at least one debug port. This table includes information about the identity and configuration of the debug port(s). The table is located in system memory with other ACPI tables, and must be referenced in the ACPI RSDT table.

Windows uses the Port Type value in the DBG2 table to identify and load the Kernel Debugger (KD) transport (for example, USB or serial) that the system requires. The KD transport then uses the Port Subtype value in the DBG2 table to identify the hardware interface used by the port. Other information in the DBG2 table specifies the system address of the port registers, which is used by the hardware interface module for the specified subtype. Finally, the DBG2 table must include a reference to the device node in the ACPI namespace that corresponds to the debug port. This reference enables Windows to manage conflicts between debugging use and normal use of the device, if any, and also to integrate the debugger with power transitions.

For more information, see the [Microsoft Debug Port Table 2 (DBG2) specification](http://go.microsoft.com/fwlink/p/?linkid=330996).

## Differentiated System Description Table (DSDT)


In ACPI, peripheral devices and system hardware features on the platform are described in the Differentiated System Description Table (DSDT), which is loaded at boot, or in Secondary System Description Tables (SSDTs), which are loaded at boot or loaded dynamically at run time. For SoCs, the platform configuration is typically static, so the DSDT might be sufficient, although SSDTs can also be used to improve the modularity of the platform description.

ACPI defines an interpreted language (ACPI source language, or ASL) and an execution environment (ACPI virtual machine) for describing system devices and features, and their platform-specific controls, in an OS-agnostic way. ASL is used to define named objects in the ACPI namespace, and the [Microsoft ASL compiler](microsoft-asl-compiler.md) is used to produce ACPI machine language (AML) byte code for transmission to the operating system in the DSDT. The inbox [Windows ACPI driver](https://docs.microsoft.com/windows-hardware/drivers/kernel/acpi-driver), Acpi.sys, implements the ACPI virtual machine and interprets the AML byte code. An AML object might simply return description information. Or, an AML object might be a method that performs computation or does I/O operations. A *control method* is an executable AML object that uses the operating system's device drivers to do I/O operations on the platform hardware. ASL uses OpRegions to abstract the various address spaces accessible in the operating system. Control methods perform I/O operations as a series of transfers to and from named fields declared in OpRegions.

For more information about OpRegions, see section 5.5.2.4, "Access to Operation Regions", in the [ACPI 5.0 specification](https://www.uefi.org/specifications). For more about ASL and control methods, see section 5.5, "ACPI Namespace", in the ACPI 5.0 specification.

Windows provides support for developing and debugging ASL code. The ASL compiler includes a disassembler to enable the implementer to load a namespace from a debugging target. The ASL compiler can then be used to reapply the namespace to the target for rapid prototyping and testing—without having to flash the system firmware. In addition, the Windows Kernel Debugger, in conjunction with a checked (CHK) version of the Acpi.sys driver, supports tracing and analyzing AML execution. For more information, see [The AMLI Debugger](https://docs.microsoft.com/windows-hardware/drivers/debugger/introduction-to-the-amli-debugger).

## Windows SMM Security Mitigations Table (WSMT)


The Windows SMM Security Mitigations Table (WSMT) specification contains details of an Advanced Configuration and Power Interface (ACPI) table that was created for use with Windows operating systems that support Windows virtualization-based security (VBS) features.

This information applies to the following operating systems:

Windows Server 2016

Windows 10, version 1607

For more information, see the [Windows SMM Security Mitigations Table (WMST) specification](http://go.microsoft.com/fwlink/p/?LinkId=786943).

