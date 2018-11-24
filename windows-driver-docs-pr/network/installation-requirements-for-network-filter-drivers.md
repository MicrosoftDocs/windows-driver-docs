---
title: Installation Requirements for Network Filter Drivers
description: Installation Requirements for Network Filter Drivers
ms.assetid: 7fb31e18-a2f0-48fe-b0a8-cf4aca7d27d5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation Requirements for Network Filter Drivers





This topic summarizes the INF file requirements for network filter drivers. Filter drivers are supported in NDIS 6.0 and later versions. For more information about how to install filter drivers, see [NDIS Filter Driver Installation](ndis-filter-driver-installation.md).

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
<td align="left"><p><a href="version-section-in-a-network-inf-file.md" data-raw-source="[Version Section](version-section-in-a-network-inf-file.md)">Version Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p></p>
<strong>Class</strong>= NetService
<strong>ClassGuid</strong>= {4D36E974-E325-11CE-BFC1-08002BE10318}</td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547478" data-raw-source="[&lt;strong&gt;INF SourceDisksNames Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547478)"><strong>INF SourceDisksNames Section</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547472" data-raw-source="[&lt;strong&gt;INF SourceDisksFiles Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547472)"><strong>INF SourceDisksFiles Section</strong></a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547383" data-raw-source="[&lt;strong&gt;INF DestinationDirs Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547383)"><strong>INF DestinationDirs Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="controlflags-section-in-a-network-inf-file.md" data-raw-source="[ControlFlags Section](controlflags-section-in-a-network-inf-file.md)">ControlFlags Section</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547454" data-raw-source="[&lt;strong&gt;INF Manufacturer Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547454)"><strong>INF Manufacturer Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="models-section-in-a-network-inf-file.md" data-raw-source="[Models Section](models-section-in-a-network-inf-file.md)">Models Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name (for example, MS_DLC).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ddinstall-section-in-a-network-inf-file.md" data-raw-source="[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)">DDInstall Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry:</p>
<p>NCF_LW_FILTER (0x40000) is set. Filter drivers must not set the NCF_FILTER (0x400) flag. The values of the NCF_<em>Xxx</em> flags are defined in Netcfgx.h. For more information about NCF_<em>Xxx</em> flags, see <a href="ddinstall-section-in-a-network-inf-file.md" data-raw-source="[DDInstall Section in a Network INF File](ddinstall-section-in-a-network-inf-file.md)">DDInstall Section in a Network INF File</a>.</p>
<p>Set the <strong>NetCfgInstanceId</strong> entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ddinstall-services-section-in-a-network-inf-file.md" data-raw-source="[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)">DDInstall.Services Section</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="add-registry-sections-in-a-network-inf-file.md" data-raw-source="[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)">Add-registry-sections</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Creating the Ndi Key</p>
<p>The <strong>ServiceBinary</strong> entry in the <strong>service-install</strong> section of the INF file specifies the path to the binary for the filter driver.</p>
<p>Set the <strong>FilterType</strong> and <strong>FilterRunType</strong> . See <a href="types-of-filter-drivers.md" data-raw-source="[Types of Filter Drivers](types-of-filter-drivers.md)">Types of Filter Drivers</a>.</p>
<p>Set the <strong>UpperRange</strong>, <strong>LowerRange</strong>, and <strong>FilterMediaTypes</strong> entries. See <a href="specifying-filter-driver-binding-relationships.md" data-raw-source="[Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md)">Specifying Filter Driver Binding Relationships</a>.</p>
<p>Specify the primary service name of the filter for the <strong>CoServices</strong> attribute.</p>
<p>Specify the <strong>FilterClass</strong> to determine the order in a stack of modifying filters. See <a href="configuring-an-inf-file-for-a-modifying-filter-driver.md" data-raw-source="[Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md)">Configuring an INF File for a Modifying Filter Driver</a>.</p>
<p>See also <a href="configuring-an-inf-file-for-a-monitoring-filter-driver.md" data-raw-source="[Configuring an INF File for a Monitoring Filter Driver](configuring-an-inf-file-for-a-monitoring-filter-driver.md)">Configuring an INF File for a Monitoring Filter Driver</a>, <a href="adding-service-related-values-to-the-ndi-key.md" data-raw-source="[Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md)">Adding Service-Related Values to the Ndi Key</a>, and <a href="ddinstall-services-section-in-a-network-inf-file.md" data-raw-source="[DDInstall.Services Section in a Network INF File](ddinstall-services-section-in-a-network-inf-file.md)">DDInstall.Services Section in a Network INF File</a>.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="setting-static-parameters.md" data-raw-source="[Setting static parameters for the component](setting-static-parameters.md)">Setting static parameters for the component</a></p>
<p><a href="requiring-the-installation-of-another-network-component.md" data-raw-source="[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)">Requiring the Installation of Another Network Component</a></p>
<p><a href="adding-a-helptext-value.md" data-raw-source="[Adding a HelpText Value](adding-a-helptext-value.md)">Adding a HelpText Value</a></p>
<p><a href="adding-registry-values-for-a-notify-object.md" data-raw-source="[Adding Registry Values for a Notify Object](adding-registry-values-for-a-notify-object.md)">Adding Registry Values for a Notify Object</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="remove-section-in-a-network-inf-file.md" data-raw-source="[Remove Section](remove-section-in-a-network-inf-file.md)">Remove Section</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547485" data-raw-source="[&lt;strong&gt;INF Strings Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547485)"><strong>INF Strings Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 





