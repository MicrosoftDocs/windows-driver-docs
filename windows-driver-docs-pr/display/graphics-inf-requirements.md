---
title: Graphics INF requirements in WDDM 1.2
description: Windows Display Driver Model (WDDM) drivers in Windows 8 require INF changes to the graphics driver.
ms.assetid: BB1E35B4-8691-4B0C-9D6C-9A7D1ADFAB55
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Graphics INF requirements in WDDM 1.2


Windows Display Driver Model (WDDM) drivers in Windows 8 require INF changes to the graphics driver. The most notable change is in the feature score. WDDM 1.2 drivers require a higher feature score than earlier WDDM drivers. This section describes all relevant INF requirements for Windows 8 graphics drivers

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Updated feature score directive in Windows 8](updated-feature-score-directive.md)</p></td>
<td align="left"><p>The updated feature score directive is a general installation setting that's required for all Windows 8 drivers that follow the WDDM.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Driver matching criteria](driver-matching-criteria.md)</p></td>
<td align="left"><p>This topic describes the elements that are used to choose the best match on a driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Updated friendly name for WDDM 1.2](updated-friendly-name.md)</p></td>
<td align="left"><p>This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[SKU differentiation directive](sku-differentiation-directive.md)</p></td>
<td align="left"><p>With Windows Server 2008 and Windows Vista SP1, the in-box display driver INFs were modified to include a new value that represented the drivers as <em>Client Only</em>, meaning that the drivers would not install on server SKUs of Windows. This directive is required for all display drivers in Windows 8.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[General Unicode requirement in INF files](general-unicode-requirement.md)</p></td>
<td align="left"><p>INF files should be saved and encoded as Unicode; they must not be ANSI.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Installed display drivers directive](installed-display-drivers-directive.md)</p></td>
<td align="left"><p>The installed display drivers directive is a software device setting that gives the proper name for the UMD that is installed as part of the driver package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Copy flags to support PnP stop directive](copy-flags-to-support-pnp-stop-directive.md)</p></td>
<td align="left"><p>The Plug and Play (PnP) stop directive file section flag is required for the WDDM to support driver upgrades that don't require a reboot.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Driver\services start type directive](driver-services-start-type-directive.md)</p></td>
<td align="left"><p>The <em>driver\services</em> start type directive is a service installation setting requirement for all display drivers. WDDM drivers are Plug and Play (PnP) and therefore must be demand started, where <em>StartType</em> =3.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Capability override settings to disable OpenGL](capability-override-settings-to-disable-opengl.md)</p></td>
<td align="left"><p>This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[[Version] section directives](-version--section-directives.md)</p></td>
<td align="left"><p>This topic describes <em>[Version]</em> section directives in the INF.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[[SourceDiskNames] section directives](-sourcedisknames--section-directives.md)</p></td>
<td align="left"><p>On Windows Vista and later, in-box INFs use the <em>[SourceDisksXxx]</em> directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[General x64 directives](general-x64-directives.md)</p></td>
<td align="left"><p>This topic describes the changes that are needed to properly decorate the INF for use on 64-bit Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[General install section directives](general-install-section-directives.md)</p></td>
<td align="left"><p>This is a general reminder that all references to out-of-box or production/retail binaries, services, regadd, or delreg sections that are normally part of a retail WHQL driver packages, are not listed in the Windows in-box driver packages.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[[String] section changes for localized strings](-string--section-changes-for-localized-strings.md)</p></td>
<td align="left"><p>This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Driver DLL for display adapter or chipset has properly formatted file version](driver-dll-for-display-adapter-or-chipset-has-properly-formatted-file-version.md)</p></td>
<td align="left"><p>This topic describes the proper formatting for display driver DLLs.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Graphics%20INF%20requirements%20in%20WDDM%201.2%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




