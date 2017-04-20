---
title: Installation Requirements for Network Clients
description: Installation Requirements for Network Clients
ms.assetid: 175f9006-d77b-41ff-875e-c64842ff5cb9
keywords:
- network client installation requirements WDK
- client installation requirements WDK networking
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installation Requirements for Network Clients


## <a href="" id="ddk-installation-requirements-for-network-clients-ng"></a>


This topic summarizes the installation requirements for network clients.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

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
<td align="left"><p><strong>Class</strong>= NetClient</p>
<p><strong>ClassGuid</strong>= {4D36E973-E325-11CE-BFC1-08002BE10318}</p></td>
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
<td align="left"><p>Creating the Ndi Key</p>
<p>[Specifying Binding Interfaces](specifying-binding-interfaces.md)</p>
<p>Allowable binding interfaces:</p>
<p>UpperRange: noupper</p>
<p><strong>LowerRange</strong>: ipx, tdi, winsock, netbios, nolower</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Add-registry-sections](add-registry-sections-in-a-network-inf-file.md)</p></td>
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
<td align="left"><p>[NetworkProvider and PrintProvider Sections](networkprovider-and-printprovider-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required if ...</p></td>
<td align="left"><p>Required if an alternative device name is specified for the network client or a short name for the component is specified for use with the <strong>net view</strong> command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NetworkProvider and PrintProvider Sections](networkprovider-and-printprovider-sections-in-a-network-inf-file.md)</p></td>
<td align="left"><p>Required if ...</p></td>
<td align="left"><p>Required if the network client is a print provider.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF Strings Section</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547485)</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>No network-specific requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 





