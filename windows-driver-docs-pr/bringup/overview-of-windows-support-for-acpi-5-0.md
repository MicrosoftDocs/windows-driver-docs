---
title: Overview of Windows support for ACPI 5.0
author: windows-driver-content
description: The ACPI 5.0 specification enables support of SoC-based mobile platforms that run Windows 8 and later, but continues to support many useful features that were introduced in earlier versions Windows.
ms.assetid: BAFBA051-FEDA-469B-9B67-C74D252C84F9
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overview of Windows support for ACPI 5.0


The [ACPI 5.0 specification](http://www.acpi.info) enables support of SoC-based mobile platforms that run Windows 8 and later, but continues to support many useful features that were introduced in earlier versions Windows. This design guide directs implementers to the parts of ACPI 5.0 that specifically apply to SoC-based platforms, and describes best practices for implementing the SoC-specific features in ACPI to run Windows on these platforms.

## Scope


The target audience for this design guide is firmware developers and system designers who require guidance for firmware support and implementation. Observation and adherence to these guidelines will help ensure proper functionality of Windows on SoC platforms.

This design guidance specifically targets hardware-reduced ACPI platforms that support low-power S0 idle. However, most of the guidance also applies to any platform that is compliant with ACPI 5.0 and that runs Windows 8 or later. In addition, this topic assumes either a clamshell form factor or a wireless, multi-touch-only mobile platform. It therefore limits itself to technologies that are expected to be widely used on such platforms. For technologies that are not covered in this document, the reader is referred to the ACPI specification itself for implementation information.

## Firmware revision support


Windows supports firmware revisions based on the [ACPI 5.0 specification](http://www.acpi.info).

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
<td><p>[Summary of ACPI support in Windows](summary-of-acpi-support-in-windows.md)</p></td>
<td><p>This topic summarizes the subset of Advanced Configuration and Power Interface (ACPI) 5.0 features that are required to support Windows on SoC-based platforms.</p></td>
</tr>
<tr class="even">
<td><p>[Hardware requirements for SoC-based platforms](hardware-requirements-for-soc-based-platforms.md)</p></td>
<td><p>The [ACPI 5.0 specification](http://www.acpi.info) introduces a new set of hardware requirements to support SoC-based platforms that run Windows. ACPI 5.0 supports hardware-reduced system designs to lower cost, and supports the connected standby power model to enable long battery life.</p></td>
</tr>
<tr class="odd">
<td><p>[ACPI namespace hierarchy](acpi-namespace-hierarchy.md)</p></td>
<td><p>The ACPI namespace hierarchy must accurately model the platform's hardware topology, starting with the processor's system bus (&quot;\_SB&quot;). In general, a device that connects to a bus or controller appears as a child of that bus or controller device in the namespace.</p></td>
</tr>
<tr class="even">
<td><p>[Microsoft ASL compiler](microsoft-asl-compiler.md)</p></td>
<td><p>Version 5.0 of the Microsoft ACPI source language (ASL) compiler supports the features in the Advanced Configuration and Power Interface Specification, Revision 5.0 ([ACPI 5.0 specification](http://www.acpi.info)). The ASL compiler is distributed with the Windows Driver Kit (WDK) 8.1.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


