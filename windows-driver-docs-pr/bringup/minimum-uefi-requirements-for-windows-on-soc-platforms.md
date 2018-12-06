---
title: Minimum UEFI requirements for Windows on SoC platforms
description: Minimum UEFI requirements for Windows on SoC platforms
ms.assetid: 32743d69-83a2-4658-8652-6d624e75e3db
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minimum UEFI requirements for Windows on SoC platforms


Unified Extensible Firmware Interface (UEFI) is the required boot firmware for SoC platforms running Windows. This section describes UEFI implementation requirements for running Windows on SoC platforms. Observation and adherence to these requirements will help ensure proper functionality of Windows.

This set of requirements applies to any SoC-based computing system, with some limitations. This guidance assumes a full Windows feature set, with support for both traditional netbook form-factors and wireless, multitouch-only mobile devices. It therefore limits itself to technologies expected to be widely used on such systems. For systems that implement technologies not covered in this document, refer to the UEFI specification at [UEFI specifications](http://go.microsoft.com/fwlink/p/?LinkId=218221).

Windows supports firmware revisions based on the Unified Extensible Firmware Interface (UEFI) Version 2.3.1 or later.

**Note**  Windows supports a subset of functionality defined in the UEFI 2.3.1 specification. The Windows implementation does not have an explicit check against higher revisions of the firmware. The operating system will support higher revisions of the firmware if they contain the necessary support described in this document.

 

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
<td><p><a href="uefi-requirements-that-apply-to-all-windows-platforms.md" data-raw-source="[UEFI requirements that apply to all Windows editions on SoC platforms](uefi-requirements-that-apply-to-all-windows-platforms.md)">UEFI requirements that apply to all Windows editions on SoC platforms</a></p></td>
<td><p>This topic describes UEFI requirements that apply to Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.</p></td>
</tr>
<tr class="even">
<td><p><a href="uefi-requirements-specific-to-windows-mobile.md" data-raw-source="[UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md)">UEFI requirements for Windows 10 Mobile</a></p></td>
<td><p>In addition to the UEFI requirements listed in <a href="uefi-requirements-that-apply-to-all-windows-platforms.md" data-raw-source="[UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md)">UEFI requirements that apply to all Windows editions</a>, devices that run Windows 10 Mobile must also meet the additional requirements described in this topic.</p></td>
</tr>
<tr class="odd">
<td><p><a href="uefi-requirements-for-usb-flashing-support.md" data-raw-source="[UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md)">UEFI requirements for USB flashing support</a></p></td>
<td><p>Microsoft provides several USB-based flashing solutions for use in engineering and manufacturing environments. In order for a device to be used with these tools, the UEFI environment on the device must meet the requirements listed in this topic.</p></td>
</tr>
</tbody>
</table>

 

 

 




