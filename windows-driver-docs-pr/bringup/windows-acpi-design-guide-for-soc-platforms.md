---
title: Windows ACPI design guide for SoC platforms
description: ACPI 5.0 defines new features to support low-power, mobile devices based on SoC ICs that implement the connected standby power model.
ms.assetid: 661BFB7E-D190-450D-A466-7D6AD0EAAAB0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows ACPI design guide for SoC platforms


The Advanced Configuration and Power Interface Specification, Revision 5.0 ([ACPI 5.0 specification](https://www.uefi.org/specifications)), defines a new set of features to support low-power, mobile devices that are based on System on a Chip (SoC) integrated circuits and that implement the connected standby power model. Starting with Windows 8 and Windows 8.1, Windows supports the new ACPI 5.0 features for SoC-based platforms.

This section contains guidelines for implementing Windows PCs and devices that support the new features in the ACPI 5.0 specification. Firmware developers and system designers can use these guidelines to make sure that Windows runs properly on their platforms. For a list of all Windows firmware requirements, see the documentation for the [Windows Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227314).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="overview-of-windows-support-for-acpi-5-0.md" data-raw-source="[Overview of Windows support for ACPI 5.0](overview-of-windows-support-for-acpi-5-0.md)">Overview of Windows support for ACPI 5.0</a></p></td>
<td><p>The <a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a> enables support of SoC-based mobile platforms that run Windows 8 and later, but continues to support many useful features that were introduced in earlier versions Windows. This design guide directs implementers to the parts of ACPI 5.0 that specifically apply to SoC-based platforms, and describes best practices for implementing the SoC-specific features in ACPI to run Windows on these platforms.</p></td>
</tr>
<tr class="even">
<td><p><a href="acpi-system-description-tables.md" data-raw-source="[ACPI system description tables](acpi-system-description-tables.md)">ACPI system description tables</a></p></td>
<td><p>Implementation of the Advanced Configuration and Power Interface (ACPI) Hardware Specification is not required on SoC-based platforms or Windows Server systems that are BIOS-based, but much of the ACPI Software Specification is (or can be) required. ACPI defines a generic, extensible table-passing mechanism, plus specific tables for describing the platform to the operating system.</p></td>
</tr>
<tr class="odd">
<td><p><a href="device-management-namespace-objects.md" data-raw-source="[Device management namespace objects](device-management-namespace-objects.md)">Device management namespace objects</a></p></td>
<td><p>The <a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a> defines several types of namespace objects that can be used to manage devices. For example, device identification objects contain identification information for devices that connect to buses, such as I2C, that do not support hardware enumeration of child devices. Other types of namespace objects can specify system resources, describe device dependencies, and indicate which devices can be disabled.</p></td>
</tr>
<tr class="even">
<td><p><a href="general-purpose-i-o--gpio-.md" data-raw-source="[General-purpose I/O (GPIO)](general-purpose-i-o--gpio-.md)">General-purpose I/O (GPIO)</a></p></td>
<td><p>SoC integrated circuits make extensive use of general-purpose I/O (GPIO) pins. For SoC-based platforms, Windows defines a general abstraction for GPIO hardware, and this abstraction requires support from the Advanced Configuration and Power Interface (ACPI) namespace.</p></td>
</tr>
<tr class="odd">
<td><p><a href="simple-peripheral-bus--spb-.md" data-raw-source="[Simple peripheral bus (SPB)](simple-peripheral-bus--spb-.md)">Simple peripheral bus (SPB)</a></p></td>
<td><p>SoC integrated circuits make extensive use of simple, low-pin-count and low-power serial interconnects for connecting to platform peripherals. I²C, SPI and UARTs are examples. For SoC-based platforms, Windows provides a general abstraction for Simple Peripheral Bus (SPB) hardware, and this abstraction requires new support from the Advanced Configuration and Power Interface (ACPI) namespace.</p></td>
</tr>
<tr class="even">
<td><p><a href="device-power-management.md" data-raw-source="[Device power management](device-power-management.md)">Device power management</a></p></td>
<td><p>The <a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a> defines a set of namespace objects to specify device power information for a device. For example, one set of objects can specify the power resources that a device requires in each supported device power state. Another object type can describe the ability of the device to wake from a low-power state in response to hardware events.</p></td>
</tr>
<tr class="odd">
<td><p><a href="acpi-defined-devices.md" data-raw-source="[ACPI-defined devices](acpi-defined-devices.md)">ACPI-defined devices</a></p></td>
<td><p>The <a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a> defines a number of device types to represent and control typical platform features. For example, ACPI defines a power button, a sleep button, and system indicators. For SoC-based platforms, Windows provides built-in drivers to support the ACPI-defined devices that are described in this article.</p></td>
</tr>
<tr class="even">
<td><p><a href="other-acpi-namespace-objects.md" data-raw-source="[Other ACPI namespace objects](other-acpi-namespace-objects.md)">Other ACPI namespace objects</a></p></td>
<td><p>For some specific classes of device, there are requirements for additional Advanced Configuration and Power Interface (ACPI) namespace objects to appear under those devices in the namespace. This section lists the additional objects required for SoC-based platforms.</p></td>
</tr>
<tr class="odd">
<td><p><a href="acpi-device-specific-methods.md" data-raw-source="[ACPI device-specific methods](acpi-device-specific-methods.md)">ACPI device-specific methods</a></p></td>
<td><p>To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (_DSM) for the device.</p></td>
</tr>
</tbody>
</table>

 

 

 




