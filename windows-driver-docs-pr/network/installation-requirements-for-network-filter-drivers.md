---
title: Installation Requirements for Network Filter Drivers
description: Installation Requirements for Network Filter Drivers
ms.assetid: 7fb31e18-a2f0-48fe-b0a8-cf4aca7d27d5
---

# Installation Requirements for Network Filter Drivers


## <a href="" id="ddk-installation-requirements-for-network-filter-drivers-ng"></a>


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
<td align="left"><p>[Version Section](version-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p></p>
<strong>Class</strong>= NetService
<strong>ClassGuid</strong>= {4D36E974-E325-11CE-BFC1-08002BE10318}</td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF SourceDisksNames Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547478) and [<strong>INF SourceDisksFiles Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547472)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
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
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name (for example, MS_DLC).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry:</p>
<p>NCF_LW_FILTER (0x40000) is set. Filter drivers must not set the NCF_FILTER (0x400) flag. The values of the NCF_<em>Xxx</em> flags are defined in Netcfgx.h. For more information about NCF_<em>Xxx</em> flags, see [DDInstall Section in a Network INF File](ddinstall-section-in-a-network-inf-file.md).</p>
<p>Set the <strong>NetCfgInstanceId</strong> entry.</p></td>
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
<p>The <strong>ServiceBinary</strong> entry in the <strong>service-install</strong> section of the INF file specifies the path to the binary for the filter driver.</p>
<p>Set the <strong>FilterType</strong> and <strong>FilterRunType</strong> . See [Types of Filter Drivers](types-of-filter-drivers.md).</p>
<p>Set the <strong>UpperRange</strong>, <strong>LowerRange</strong>, and <strong>FilterMediaTypes</strong> entries. See [Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md).</p>
<p>Specify the primary service name of the filter for the <strong>CoServices</strong> attribute.</p>
<p>Specify the <strong>FilterClass</strong> to determine the order in a stack of modifying filters. See [Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md).</p>
<p>See also [Configuring an INF File for a Monitoring Filter Driver](configuring-an-inf-file-for-a-monitoring-filter-driver.md), [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md), and [DDInstall.Services Section in a Network INF File](ddinstall-services-section-in-a-network-inf-file.md).</p></td>
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

 

 

 





