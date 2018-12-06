---
title: Installation Requirements for Network Protocols
description: Installation Requirements for Network Protocols
ms.assetid: 6383fec5-29ce-4aa4-8fc3-c8d95f7bd02b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation Requirements for Network Protocols





This topic summarizes the installation requirements for network protocols.

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
<td align="left"><p><strong>Class</strong>= NetTrans</p>
<p><strong>ClassGuid</strong>= {4D36E975-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547478" data-raw-source="[&lt;strong&gt;INF SourceDisksNames Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547478)"><strong>INF SourceDisksNames Section</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547472" data-raw-source="[&lt;strong&gt;INF SourceDisksFiles Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547472)"><strong>INF SourceDisksFiles Section</strong></a></p></td>
<td align="left"><p>Required if ...</p></td>
<td align="left"><p>Required if the INF file is not distributed with Windows 2000. If the INF file is distributed with Windows 2000, a <strong>LayoutFile</strong> entry must be specified in the <strong>Version</strong> section, and the <strong>SourceDisksNames</strong> and <strong>SourceDisksFiles</strong> sections are not used.</p>
<p>No network-specific requirements.</p></td>
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
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name, for example: MS_DLC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ddinstall-section-in-a-network-inf-file.md" data-raw-source="[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)">DDInstall Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry</p>
<p>Allowable values:</p>
<p>NCF_HIDDEN</p>
<p>NCF_NO_SERVICE</p>
<p>NCF_NOT_USER_REMOVABLE</p>
<p>NCF_HAS_UI</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ddinstall-services-section-in-a-network-inf-file.md" data-raw-source="[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)">DDInstall.Services Section</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="add-registry-sections-in-a-network-inf-file.md" data-raw-source="[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)">Add-registry-sections</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Required:</p>
<p>Creating the Ndi Key</p>
<p><a href="specifying-binding-interfaces.md" data-raw-source="[Specifying Binding Interfaces](specifying-binding-interfaces.md)">Specifying Binding Interfaces</a></p>
<p>Allowable binding interfaces:</p>
<p><strong>UpperRange</strong>:</p>
<p>netbios, ipx, tdi, winsock, noupper</p>
<p><strong>LowerRange</strong>:</p>
<p>ndis5, ndisatm, nolower</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="setting-static-parameters.md" data-raw-source="[Setting static parameters for the component](setting-static-parameters.md)">Setting static parameters for the component</a></p>
<p><a href="requiring-the-installation-of-another-network-component.md" data-raw-source="[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)">Requiring the Installation of Another Network Component</a></p>
<p><a href="adding-service-related-values-to-the-ndi-key.md" data-raw-source="[Specifying service-related values](adding-service-related-values-to-the-ndi-key.md)">Specifying service-related values</a></p>
<p><a href="adding-a-helptext-value.md" data-raw-source="[Adding a HelpText Value](adding-a-helptext-value.md)">Adding a HelpText Value</a></p>
<p><a href="adding-registry-values-for-a-notify-object.md" data-raw-source="[Adding Registry Values for a Notify Object](adding-registry-values-for-a-notify-object.md)">Adding Registry Values for a Notify Object</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="remove-section-in-a-network-inf-file.md" data-raw-source="[Remove Section](remove-section-in-a-network-inf-file.md)">Remove Section</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><a href="winsock-sections-in-a-network-inf-file.md" data-raw-source="[Winsock Sections](winsock-sections-in-a-network-inf-file.md)">Winsock Sections</a></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>For a protocol that provides a Winsock interface, a <strong>Winsock-install</strong> section is required and a <strong>Winsock-remove</strong> section is optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547485" data-raw-source="[&lt;strong&gt;INF Strings Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547485)"><strong>INF Strings Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 





