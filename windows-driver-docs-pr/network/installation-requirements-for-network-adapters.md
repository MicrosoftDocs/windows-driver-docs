---
title: Installation Requirements for Network Adapters
description: Installation Requirements for Network Adapters
ms.assetid: 682a262a-a712-4fab-a753-d0c6fc08bac8
keywords:
- network adapter installation requirements WDK
- adapters WDK networking , installation requirements
- WAN WDK networking , adapter installation requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation Requirements for Network Adapters





This topic summarizes the installation requirements for network adapters.

**Note**  NDIS 6.0 and later drivers support a set of [standardized INF keywords for network devices](standardized-inf-keywords-for-network-devices.md).

 

### General Requirements

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
<td align="left"><p><strong>Class</strong>= Net</p>
<p><strong>ClassGuid</strong>= {4D36E972-E325-11CE-BFC1-08002BE10318}</p></td>
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
<td align="left"><p>Required</p></td>
<td align="left"><p>Must contain an <strong>ExcludeFromSelect</strong> entry for each Plug and Play (PnP) adapter installed by the INF file.</p>
<p>Non-PnP adapters, such as non-PnP ISA and EISA adapters, should not be listed. Note that Windows XP and later operating systems do not support non-PnP ISA adapters and EISA adapters.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547454" data-raw-source="[&lt;strong&gt;INF Manufacturer Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547454)"><strong>INF Manufacturer Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="models-section-in-a-network-inf-file.md" data-raw-source="[Models Section](models-section-in-a-network-inf-file.md)">Models Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>The <em>hw-id</em> must match the hardware ID supplied by the adapter to the PnP manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ddinstall-section-in-a-network-inf-file.md" data-raw-source="[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)">DDInstall Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry</p>
<p>Allowable values:</p>
<p>NCF_VIRTUAL,</p>
<p>NCF_SOFTWARE_ENUMERATED, NCF_PHYSICAL, NCF_MULTIPORT_INSTANCED_ADAPTER, NCF_HAS_UI, NCF_HIDDEN, NCF_NOT_USER_REMOVABLE</p>
<p>NCF_VIRTUAL, NCF_SOFTWARE_ENUMERATED, and NCF_PHYSICAL are mutually exclusive.</p>
<p>The <strong>BusType</strong> entry is required for a physical adapter.</p>
<p>The <strong>EisaCompressedId</strong> entry is required for an EISA adapter. This entry specifies both an EISA Compressed ID and an adapter mask for the adapter. Windows XP and later operating systems do not support EISA adapters.</p>
<p>A <strong>Port1DeviceNumber</strong> or <strong>Port1FunctionNumber</strong> entry is required for a multiport network adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ddinstall-services-section-in-a-network-inf-file.md" data-raw-source="[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)">DDInstall.Services Section</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="add-registry-sections-in-a-network-inf-file.md" data-raw-source="[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)">Add-registry-sections</a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Creating the Ndi Key</p>
<p><a href="adding-service-related-values-to-the-ndi-key.md" data-raw-source="[Specifying service-related values](adding-service-related-values-to-the-ndi-key.md)">Specifying service-related values</a></p>
<p><a href="specifying-bundle-membership.md" data-raw-source="[Specifying Bundle Membership](specifying-bundle-membership.md)">Specifying Bundle Membership</a>(only for LBFO miniport drivers)</p>
<p><a href="specifying-binding-interfaces.md" data-raw-source="[Specifying Binding Interfaces](specifying-binding-interfaces.md)">Specifying Binding Interfaces</a></p>
<p>Allowable binding interfaces:</p>
<p><strong>UpperRange</strong>:</p>
<p>ndis5, ndisatm, ndiswan, ndiscowan, noupper, ndis5_atalk, ndis5_dlc, ndis5_ip, ndis5_ipx, ndis5_nbf, ndis5_streams</p>
<p><strong>LowerRange</strong>:</p>
<p>ethernet, atm, tokenring, serial, fddi, baseband, broadband, arcnet, isdn, localtalk, wan</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="setting-static-parameters.md" data-raw-source="[Setting static parameters for the component](setting-static-parameters.md)">Setting static parameters for the component</a></p>
<p><a href="requiring-the-installation-of-another-network-component.md" data-raw-source="[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)">Requiring the Installation of Another Network Component</a></p>
<p><a href="specifying-configuration-parameters-for-the-advanced-properties-page.md" data-raw-source="[Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md)">Specifying Configuration Parameters for the Advanced Properties Page</a></p>
<p><a href="specifying-custom-property-pages-for-network-adapters.md" data-raw-source="[Specifying Custom Property Pages for Network Adapters](specifying-custom-property-pages-for-network-adapters.md)">Specifying Custom Property Pages for Network Adapters</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547485" data-raw-source="[&lt;strong&gt;INF Strings Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547485)"><strong>INF Strings Section</strong></a></p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

### Additional Requirements for WAN Adapters

WAN adapters have additional installation requirements that are described in the following topics:

[Specifying WAN Endpoints for a WAN Adapter](specifying-wan-endpoints-for-a-wan-adapter.md)

[Specifying ISDN Keys and Values for an ISDN Adapter](specifying-isdn-keys-and-values-for-an-isdn-adapter.md)

[Installing a Multiprotocol WAN NIC](installing-a-multiprotocol-wan-nic.md)

**Note**  The [Remove Section](remove-section-in-a-network-inf-file.md) and [Notify Objects for Network Components](notify-objects-for-network-components.md) are not supported.

 

 

 





