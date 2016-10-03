---
title: Installation Requirements for Network Protocols
description: Installation Requirements for Network Protocols
ms.assetid: 6383fec5-29ce-4aa4-8fc3-c8d95f7bd02b
---

# Installation Requirements for Network Protocols


## <a href="" id="ddk-installation-requirements-for-network-protocols-ng"></a>


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
<td align="left"><p>[Version Section](version-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Class</strong>= NetTrans</p>
<p><strong>ClassGuid</strong>= {4D36E975-E325-11CE-BFC1-08002BE10318}</p></td>
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
<td align="left"><p>The <em>hw-id</em> should consist of a provider name followed by an underscore and a manufacturer name or the product name, for example: MS_DLC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[DDInstall Section](ddinstall-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p><strong>Characteristics</strong> entry</p>
<p>Allowable values:</p>
<p>NCF_HIDDEN</p>
<p>NCF_NO_SERVICE</p>
<p>NCF_NOT_USER_REMOVABLE</p>
<p>NCF_HAS_UI</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Required:</p>
<p>Creating the Ndi Key</p>
<p>[Specifying Binding Interfaces](specifying-binding-interfaces.md)</p>
<p>Allowable binding interfaces:</p>
<p><strong>UpperRange</strong>:</p>
<p>netbios, ipx, tdi, winsock, noupper</p>
<p><strong>LowerRange</strong>:</p>
<p>ndis5, ndisatm, nolower</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>[Setting static parameters for the component](setting-static-parameters.md)</p>
<p>[Requiring the Installation of Another Network Component](requiring-the-installation-of-another-network-component.md)</p>
<p>[Specifying service-related values](adding-service-related-values-to-the-ndi-key.md)</p>
<p>[Adding a HelpText Value](adding-a-helptext-value.md)</p>
<p>[Adding Registry Values for a Notify Object](adding-registry-values-for-a-notify-object.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Remove Section](remove-section-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[Winsock Sections](winsock-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>For a protocol that provides a Winsock interface, a <strong>Winsock-install</strong> section is required and a <strong>Winsock-remove</strong> section is optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Strings Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547485)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 





