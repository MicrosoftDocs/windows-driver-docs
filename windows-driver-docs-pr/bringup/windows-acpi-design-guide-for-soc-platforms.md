---
title: Windows ACPI design guide for SoC platforms
author: windows-driver-content
description: ACPI 5.0 defines new features to support low-power, mobile devices based on SoC ICs that implement the connected standby power model.
ms.assetid: 661BFB7E-D190-450D-A466-7D6AD0EAAAB0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows ACPI design guide for SoC platforms


The Advanced Configuration and Power Interface Specification, Revision 5.0 ([ACPI 5.0 specification](http://www.acpi.info)), defines a new set of features to support low-power, mobile devices that are based on System on a Chip (SoC) integrated circuits and that implement the connected standby power model. Starting with Windows 8 and Windows 8.1, Windows supports the new ACPI 5.0 features for SoC-based platforms.

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
<td><p>[Overview of Windows support for ACPI 5.0](overview-of-windows-support-for-acpi-5-0.md)</p></td>
<td><p>The [ACPI 5.0 specification](http://www.acpi.info) enables support of SoC-based mobile platforms that run Windows 8 and later, but continues to support many useful features that were introduced in earlier versions Windows. This design guide directs implementers to the parts of ACPI 5.0 that specifically apply to SoC-based platforms, and describes best practices for implementing the SoC-specific features in ACPI to run Windows on these platforms.</p></td>
</tr>
<tr class="even">
<td><p>[ACPI system description tables](acpi-system-description-tables.md)</p></td>
<td><p>Implementation of the Advanced Configuration and Power Interface (ACPI) Hardware Specification is not required on SoC-based platforms or Windows Server systems that are BIOS-based, but much of the ACPI Software Specification is (or can be) required. ACPI defines a generic, extensible table-passing mechanism, plus specific tables for describing the platform to the operating system.</p></td>
</tr>
<tr class="odd">
<td><p>[Device management namespace objects](device-management-namespace-objects.md)</p></td>
<td><p>The [ACPI 5.0 specification](http://www.acpi.info) defines several types of namespace objects that can be used to manage devices. For example, device identification objects contain identification information for devices that connect to buses, such as I2C, that do not support hardware enumeration of child devices. Other types of namespace objects can specify system resources, describe device dependencies, and indicate which devices can be disabled.</p></td>
</tr>
<tr class="even">
<td><p>[General-purpose I/O (GPIO)](general-purpose-i-o--gpio-.md)</p></td>
<td><p>SoC integrated circuits make extensive use of general-purpose I/O (GPIO) pins. For SoC-based platforms, Windows defines a general abstraction for GPIO hardware, and this abstraction requires support from the Advanced Configuration and Power Interface (ACPI) namespace.</p></td>
</tr>
<tr class="odd">
<td><p>[Simple peripheral bus (SPB)](simple-peripheral-bus--spb-.md)</p></td>
<td><p>SoC integrated circuits make extensive use of simple, low-pin-count and low-power serial interconnects for connecting to platform peripherals. I²C, SPI and UARTs are examples. For SoC-based platforms, Windows provides a general abstraction for Simple Peripheral Bus (SPB) hardware, and this abstraction requires new support from the Advanced Configuration and Power Interface (ACPI) namespace.</p></td>
</tr>
<tr class="even">
<td><p>[Device power management](device-power-management.md)</p></td>
<td><p>The [ACPI 5.0 specification](http://www.acpi.info) defines a set of namespace objects to specify device power information for a device. For example, one set of objects can specify the power resources that a device requires in each supported device power state. Another object type can describe the ability of the device to wake from a low-power state in response to hardware events.</p></td>
</tr>
<tr class="odd">
<td><p>[ACPI-defined devices](acpi-defined-devices.md)</p></td>
<td><p>The [ACPI 5.0 specification](http://www.acpi.info) defines a number of device types to represent and control typical platform features. For example, ACPI defines a power button, a sleep button, and system indicators. For SoC-based platforms, Windows provides built-in drivers to support the ACPI-defined devices that are described in this article.</p></td>
</tr>
<tr class="even">
<td><p>[Other ACPI namespace objects](other-acpi-namespace-objects.md)</p></td>
<td><p>For some specific classes of device, there are requirements for additional Advanced Configuration and Power Interface (ACPI) namespace objects to appear under those devices in the namespace. This section lists the additional objects required for SoC-based platforms.</p></td>
</tr>
<tr class="odd">
<td><p>[ACPI device-specific methods](acpi-device-specific-methods.md)</p></td>
<td><p>To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (_DSM) for the device.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


