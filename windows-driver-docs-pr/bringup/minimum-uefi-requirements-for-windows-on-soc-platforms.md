---
title: Minimum UEFI requirements for Windows on SoC platforms
description: Minimum UEFI requirements for Windows on SoC platforms
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 32743d69-83a2-4658-8652-6d624e75e3db
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
<td><p>[UEFI requirements that apply to all Windows editions on SoC platforms](uefi-requirements-that-apply-to-all-windows-platforms.md)</p></td>
<td><p>This topic describes UEFI requirements that apply to Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.</p></td>
</tr>
<tr class="even">
<td><p>[UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md)</p></td>
<td><p>In addition to the UEFI requirements listed in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md), devices that run Windows 10 Mobile must also meet the additional requirements described in this topic.</p></td>
</tr>
<tr class="odd">
<td><p>[UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md)</p></td>
<td><p>Microsoft provides several USB-based flashing solutions for use in engineering and manufacturing environments. In order for a device to be used with these tools, the UEFI environment on the device must meet the requirements listed in this topic.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Minimum%20UEFI%20requirements%20for%20Windows%20on%20SoC%20platforms%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


