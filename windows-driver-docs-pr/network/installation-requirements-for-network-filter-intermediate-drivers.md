---
title: Installation Requirements for Network Filter Intermediate Drivers
description: Installation Requirements for Network Filter Intermediate Drivers
ms.assetid: 17eb9045-1466-4bd2-8805-964d339c4a9f
keywords:
- network filter intermediate driver installation requirements WDK
- service INF files WDK networking
- device INF files WDK networking
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installation Requirements for Network Filter Intermediate Drivers


## <a href="" id="ddk-installation-requirements-for-network-filter-intermediate-drivers-"></a>


**Note**  Filter intermediate drivers are not supported in NDIS 6.0 and later. You should use the NDIS filter driver interface instead. For more information about NDIS filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers.md).

 

This topic summarizes the INF file requirements for NDIS 5.*x* network filter intermediate drivers.

Two INF files are required to install a network filter intermediate driver:

-   Driver service ( **Class**= NetService)

-   Driver device ( **Class**= Net)

### Service INF File for a Network Filter Intermediate Driver

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">INF File Section</th>
<th align="left">Status</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Version Section](version-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Class</strong>= NetService</p>
<p><strong>ClassGuid</strong>= {4D36E974-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF SourceDisksNames Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547478) and [<strong>INF SourceDisksFiles Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547472)</p></td>
<td align="left"><p>Required if ...</p></td>
<td align="left"><p>Required if the INF file is not distributed with Windows 2000. If the INF file is distributed with Windows 2000, a <strong>LayoutFile</strong> entry must be specified in the <strong>Version</strong> section, and the <strong>SourceDisksNames</strong> and <strong>SourceDisksFiles</strong> sections are not used.</p>
<p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DestinationDirs Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547383)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[ControlFlags Section](controlflags-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Manufacturer Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547454)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Models Section](models-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name--for example: MS_DLC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry:</p>
<p>NCF_FILTER is required. NCF_HAS_UI and NCF_NO_SERVICE are optional.</p>
<p>The device INF must be copied to the system INF directory, see [Copying INFs](https://msdn.microsoft.com/library/windows/hardware/ff540117).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Creating the Ndi Key</p>
<p>FilterClass, FilterDeviceInfId, FilterMediaTypes</p>
<p>[Specifying Binding Interfaces](specifying-binding-interfaces.md)</p>
<p>Allowable binding interfaces:</p>
<p>UpperRange: noupper</p>
<p>LowerRange: nolower</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>[Setting static parameters for the component](setting-static-parameters.md)</p>
<p>[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)</p>
<p>[Adding a HelpText Value](adding-a-helptext-value.md)</p>
<p>[Adding Registry Values for a Notify Object](adding-registry-values-for-a-notify-object.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Remove Section](remove-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF Strings Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547485)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

### Device INF File for a Network Filter Intermediate Driver

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">INF File Section</th>
<th align="left">Status</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Version Section](version-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Class</strong>= Net</p>
<p><strong>ClassGuid</strong>= {4D36E972-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="even">
<td align="left"><p>[ControlFlags Section](controlflags-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>This section must contain an <strong>ExcludeFromSelect</strong> entry for the device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Manufacturer Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547454)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Models Section](models-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name--for example: MS_DLC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry:</p>
<p>NCF_VIRTUAL is required. NCF_HIDDEN and NCF_NOT_USER_REMOVABLE are optional.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>The <em>ServiceName</em> value of the <strong>AddService</strong> directive must match the filter component's Service value under the <strong>Ndi</strong> key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Creating the Ndi Key</p>
<p>[Specifying service-related values](adding-service-related-values-to-the-ndi-key.md)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>[Setting static parameters for the component](setting-static-parameters.md)</p>
<p>[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Strings Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547485)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 





