---
title: Renamed WHEA Data Types
description: Renamed WHEA Data Types
ms.assetid: e2c511a2-fd6e-4c7a-a47f-eb9b9f917bb4
keywords:
- Windows Hardware Error Architecture WDK , renamed data types
- WHEA WDK , renamed data types
- hardware errors WDK WHEA , renamed data types
- renamed data types WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Renamed WHEA Data Types


Starting with the Windows 7 Windows Driver Kit (WDK), various WHEA data types have been renamed from earlier versions of the WDK. The majority of these changes were made so that the naming conventions in the WDK are consistent with the naming conventions of the *Common Platform Error Record* format. This format is described in Appendix N of version 2.2 of the [Unified Extensible Firmware Interface (UEFI) Specification](http://go.microsoft.com/fwlink/p/?linkid=69484).

The data types listed in this section have not been revised for Windows 7. For example, the list and types of members within a renamed structure have not changed, although the members themselves may have been renamed.

If you are developing new [platform-specific hardware error driver (PSHED) plug-ins](platform-specific-hardware-error-driver-plug-ins2.md), use the new WHEA data type names as defined in the Windows 7 and later versions of the WDK.

If you are building an existing PSHED plug-in with the Windows 7 and later versions of the WDK, you can still use the previous WHEA data type names. To do this, add the following to the *sources* file that is used to build the plug-in:

`C_DEFINES = $(C_DEFINES) /DWHEA_DOWNLEVEL_TYPE_NAMES`

However, for existing PSHED plug-ins, we strongly recommend that you rename the WHEA data types by using the names that are defined in the Windows 7 and later versions of the WDK.

The following tables list the WHEA data types' former and new names.

### <a href="" id="renamed-whea-globally-unique-identifiers--guids-"></a> Renamed WHEA Globally-Unique Identifiers (GUIDs)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Former name (WDK versions prior to Windows 7)</th>
<th>New name (Windows 7 WDK and later)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IPF_PROCESSOR_SPECIFIC_SECTION_GUID</p></td>
<td><p>IPF_PROCESSOR_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="even">
<td><p>IPF_SAL_RECORD_REFERENCE_SECTION_GUID</p></td>
<td><p>FIRMWARE_ERROR_RECORD_REFERENCE_GUID</p></td>
</tr>
<tr class="odd">
<td><p>PCIEXPRESS_SECTION_GUID</p></td>
<td><p>PCIEXPRESS_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="even">
<td><p>PCIX_BUS_SECTION_GUID</p></td>
<td><p>PCIXBUS_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="odd">
<td><p>PCIX_COMPONENT_SECTION_GUID</p></td>
<td><p>PCIXBUS_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="even">
<td><p>PLATFORM_MEMORY_SECTION_GUID</p></td>
<td><p>MEMORY_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="odd">
<td><p>PROCESSOR_GENERIC_SECTION_GUID</p></td>
<td><p>PROCESSOR_GENERIC_ERROR_SECTION_GUID</p></td>
</tr>
<tr class="even">
<td><p>X86_PROCESSOR_SPECIFIC_SECTION_GUID</p></td>
<td><p>XPF_PROCESSOR_ERROR_SECTION_GUID</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="renamed-whea-defines"></a> Renamed WHEA Defines

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Former name (WDK versions prior to Windows 7)</th>
<th>New name (Windows 7 WDK and later)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WHEA_SECTION_DESCRIPTOR_REVISION</p></td>
<td><p>WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_REVISION</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="renamed-whea-structures-and-unions"></a> Renamed WHEA Structures and Unions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Former name (WDK versions prior to Windows 7)</th>
<th>New name (Windows 7 WDK and later)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WHEA_FIRMWARE_RECORD</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560520" data-raw-source="[&lt;strong&gt;WHEA_FIRMWARE_ERROR_RECORD_REFERENCE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560520)"><strong>WHEA_FIRMWARE_ERROR_RECORD_REFERENCE</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_GENERIC_PROCESSOR_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560607" data-raw-source="[&lt;strong&gt;WHEA_PROCESSOR_GENERIC_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560607)"><strong>WHEA_PROCESSOR_GENERIC_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_GENERIC_PROCESSOR_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560610" data-raw-source="[&lt;strong&gt;WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560610)"><strong>WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_MEMORY_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560565" data-raw-source="[&lt;strong&gt;WHEA_MEMORY_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560565)"><strong>WHEA_MEMORY_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_MEMORY_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560568" data-raw-source="[&lt;strong&gt;WHEA_MEMORY_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560568)"><strong>WHEA_MEMORY_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_NMI_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560571" data-raw-source="[&lt;strong&gt;WHEA_NMI_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560571)"><strong>WHEA_NMI_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_PCIEXPRESS_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560576" data-raw-source="[&lt;strong&gt;WHEA_PCIEXPRESS_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560576)"><strong>WHEA_PCIEXPRESS_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_PCIEXPRESS_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560580" data-raw-source="[&lt;strong&gt;WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560580)"><strong>WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_PCIXBUS_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560583" data-raw-source="[&lt;strong&gt;WHEA_PCIXBUS_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560583)"><strong>WHEA_PCIXBUS_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_PCIXBUS_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560585" data-raw-source="[&lt;strong&gt;WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560585)"><strong>WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_PCIXDEVICE_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560589" data-raw-source="[&lt;strong&gt;WHEA_PCIXDEVICE_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560589)"><strong>WHEA_PCIXDEVICE_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_PCIXDEVICE_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560591" data-raw-source="[&lt;strong&gt;WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560591)"><strong>WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>WHEA_XPF_PROCESSOR_ERROR</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560655" data-raw-source="[&lt;strong&gt;WHEA_XPF_PROCESSOR_ERROR_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560655)"><strong>WHEA_XPF_PROCESSOR_ERROR_SECTION</strong></a></p></td>
</tr>
<tr class="even">
<td><p>WHEA_XPF_PROCESSOR_ERROR_VALIDBITS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560657" data-raw-source="[&lt;strong&gt;WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560657)"><strong>WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




