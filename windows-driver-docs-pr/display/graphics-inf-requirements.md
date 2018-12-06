---
title: Graphics INF requirements in WDDM 1.2
description: Windows Display Driver Model (WDDM) drivers in Windows 8 require INF changes to the graphics driver.
ms.assetid: BB1E35B4-8691-4B0C-9D6C-9A7D1ADFAB55
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="updated-feature-score-directive.md" data-raw-source="[Updated feature score directive in Windows 8](updated-feature-score-directive.md)">Updated feature score directive in Windows 8</a></p></td>
<td align="left"><p>The updated feature score directive is a general installation setting that&#39;s required for all Windows 8 drivers that follow the WDDM.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="driver-matching-criteria.md" data-raw-source="[Driver matching criteria](driver-matching-criteria.md)">Driver matching criteria</a></p></td>
<td align="left"><p>This topic describes the elements that are used to choose the best match on a driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="updated-friendly-name.md" data-raw-source="[Updated friendly name for WDDM 1.2](updated-friendly-name.md)">Updated friendly name for WDDM 1.2</a></p></td>
<td align="left"><p>This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="sku-differentiation-directive.md" data-raw-source="[SKU differentiation directive](sku-differentiation-directive.md)">SKU differentiation directive</a></p></td>
<td align="left"><p>With Windows Server 2008 and Windows Vista SP1, the in-box display driver INFs were modified to include a new value that represented the drivers as <em>Client Only</em>, meaning that the drivers would not install on server SKUs of Windows. This directive is required for all display drivers in Windows 8.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="general-unicode-requirement.md" data-raw-source="[General Unicode requirement in INF files](general-unicode-requirement.md)">General Unicode requirement in INF files</a></p></td>
<td align="left"><p>INF files should be saved and encoded as Unicode; they must not be ANSI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="installed-display-drivers-directive.md" data-raw-source="[Installed display drivers directive](installed-display-drivers-directive.md)">Installed display drivers directive</a></p></td>
<td align="left"><p>The installed display drivers directive is a software device setting that gives the proper name for the UMD that is installed as part of the driver package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="copy-flags-to-support-pnp-stop-directive.md" data-raw-source="[Copy flags to support PnP stop directive](copy-flags-to-support-pnp-stop-directive.md)">Copy flags to support PnP stop directive</a></p></td>
<td align="left"><p>The Plug and Play (PnP) stop directive file section flag is required for the WDDM to support driver upgrades that don&#39;t require a reboot.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="driver-services-start-type-directive.md" data-raw-source="[Driver\services start type directive](driver-services-start-type-directive.md)">Driver\services start type directive</a></p></td>
<td align="left"><p>The <em>driver\services</em> start type directive is a service installation setting requirement for all display drivers. WDDM drivers are Plug and Play (PnP) and therefore must be demand started, where <em>StartType</em> =3.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="capability-override-settings-to-disable-opengl.md" data-raw-source="[Capability override settings to disable OpenGL](capability-override-settings-to-disable-opengl.md)">Capability override settings to disable OpenGL</a></p></td>
<td align="left"><p>This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="-version--section-directives.md" data-raw-source="[[Version] section directives](-version--section-directives.md)">[Version] section directives</a></p></td>
<td align="left"><p>This topic describes <em>[Version]</em> section directives in the INF.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="-sourcedisknames--section-directives.md" data-raw-source="[[SourceDiskNames] section directives](-sourcedisknames--section-directives.md)">[SourceDiskNames] section directives</a></p></td>
<td align="left"><p>On Windows Vista and later, in-box INFs use the <em>[SourceDisksXxx]</em> directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="general-x64-directives.md" data-raw-source="[General x64 directives](general-x64-directives.md)">General x64 directives</a></p></td>
<td align="left"><p>This topic describes the changes that are needed to properly decorate the INF for use on 64-bit Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="general-install-section-directives.md" data-raw-source="[General install section directives](general-install-section-directives.md)">General install section directives</a></p></td>
<td align="left"><p>This is a general reminder that all references to out-of-box or production/retail binaries, services, regadd, or delreg sections that are normally part of a retail WHQL driver packages, are not listed in the Windows in-box driver packages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="-string--section-changes-for-localized-strings.md" data-raw-source="[[String] section changes for localized strings](-string--section-changes-for-localized-strings.md)">[String] section changes for localized strings</a></p></td>
<td align="left"><p>This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="driver-dll-for-display-adapter-or-chipset-has-properly-formatted-file-version.md" data-raw-source="[Driver DLL for display adapter or chipset has properly formatted file version](driver-dll-for-display-adapter-or-chipset-has-properly-formatted-file-version.md)">Driver DLL for display adapter or chipset has properly formatted file version</a></p></td>
<td align="left"><p>This topic describes the proper formatting for display driver DLLs.</p></td>
</tr>
</tbody>
</table>

 

 

 





