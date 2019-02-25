---
title: Overview of Windows support for ACPI 5.0
description: The ACPI 5.0 specification enables support of SoC-based mobile platforms that run Windows 8 and later, but continues to support many useful features that were introduced in earlier versions Windows.
ms.assetid: BAFBA051-FEDA-469B-9B67-C74D252C84F9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Windows support for ACPI 5.0


The [ACPI 5.0 specification](https://www.uefi.org/specifications) enables support of SoC-based mobile platforms that run Windows 8 and later, and enables and support of Windows Server 2016 and later, but continues to support many useful features that were introduced in earlier versions Windows. This design guide directs implementers to the parts of ACPI 5.0 that specifically apply to SoC-based platforms as well as for systems designed for Windows Server 2016, and describes best practices for implementing the SoC-specific features in ACPI to run Windows on these platforms.

## Scope


The target audience for this design guide is firmware developers and system designers who require guidance for firmware support and implementation. Observation and adherence to these guidelines will help ensure proper functionality of Windows on SoC platforms and Windows Server 2016 systems.

This design guidance specifically targets hardware-reduced ACPI platforms that support low-power S0 idle. However, most of the guidance also applies to any platform that is compliant with ACPI 5.0 and that runs Windows 8 or later, or Windows Server 2012 or later. In addition, this topic assumes either a clamshell form factor or a wireless, multi-touch-only mobile platform. It therefore limits itself to technologies that are expected to be widely used on such platforms. For technologies that are not covered in this document, the reader is referred to the ACPI specification itself for implementation information.

## Firmware revision support


Windows supports firmware revisions based on the [ACPI 5.0 specification](https://www.uefi.org/specifications).

**Note**  Windows supports a subset of functionality defined in the ACPI 5.0 specification. Windows does not have an explicit check against higher revisions of the firmware. Windows will support firmware that conforms to higher revisions of the ACPI specification if this firmware contains the necessary support, as described in this design guide.

 

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
<td><p><a href="summary-of-acpi-support-in-windows.md" data-raw-source="[Summary of ACPI support in Windows](summary-of-acpi-support-in-windows.md)">Summary of ACPI support in Windows</a></p></td>
<td><p>This topic summarizes the subset of Advanced Configuration and Power Interface (ACPI) 5.0 features that are required to support Windows on SoC-based platforms.</p></td>
</tr>
<tr class="even">
<td><p><a href="hardware-requirements-for-soc-based-platforms.md" data-raw-source="[Hardware requirements for SoC-based platforms](hardware-requirements-for-soc-based-platforms.md)">Hardware requirements for SoC-based platforms</a></p></td>
<td><p>The <a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a> introduces a new set of hardware requirements to support SoC-based platforms that run Windows. ACPI 5.0 supports hardware-reduced system designs to lower cost, and supports the connected standby power model to enable long battery life.</p></td>
</tr>
<tr class="odd">
<td><p><a href="acpi-namespace-hierarchy.md" data-raw-source="[ACPI namespace hierarchy](acpi-namespace-hierarchy.md)">ACPI namespace hierarchy</a></p></td>
<td><p>The ACPI namespace hierarchy must accurately model the platform&#39;s hardware topology, starting with the processor&#39;s system bus (&quot;_SB&quot;). In general, a device that connects to a bus or controller appears as a child of that bus or controller device in the namespace.</p></td>
</tr>
<tr class="even">
<td><p><a href="microsoft-asl-compiler.md" data-raw-source="[Microsoft ASL compiler](microsoft-asl-compiler.md)">Microsoft ASL compiler</a></p></td>
<td><p>Version 5.0 of the Microsoft ACPI source language (ASL) compiler supports the features in the Advanced Configuration and Power Interface Specification, Revision 5.0 (<a href="https://www.uefi.org/specifications" data-raw-source="[ACPI 5.0 specification](https://www.uefi.org/specifications)">ACPI 5.0 specification</a>). The ASL compiler is distributed with the Windows Driver Kit (WDK) 8.1.</p></td>
</tr>
</tbody>
</table>

 

 

 




