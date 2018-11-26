---
title: V4 Printer Driver Localization
description: Windows 8 has provided standard, localized display strings to support the development of printer extensions and UWP device apps.
ms.assetid: 5C587AF2-C51E-4728-A214-7FC1F8A6E445
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# V4 Printer Driver Localization


Windows 8 has provided standard, localized display strings to support the development of printer extensions and UWP device apps.

These standard, localized display strings are provided through the new [**IPrintSchemaCapabilities**](https://msdn.microsoft.com/library/windows/hardware/hh451256) objects to support some features and their associated standard options. The following table shows the features that Windows 8 can localize with its standard display strings:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature</th>
<th>Standard options</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Input bins</td>
<td>Job/Document/PageInputBin</td>
</tr>
<tr class="even">
<td>Media types</td>
<td>PageMediaType</td>
</tr>
<tr class="odd">
<td>Duplexing</td>
<td>JobDuplexAllDocumentsContiguously</td>
</tr>
<tr class="even">
<td>Collation</td>
<td>DocumentCollate</td>
</tr>
<tr class="odd">
<td>Output color</td>
<td>PageOutputColor</td>
</tr>
<tr class="even">
<td>Orientation</td>
<td>PageOrientation</td>
</tr>
<tr class="odd">
<td>N-Up</td>
<td>JobNUpAllDocumentsContiguously</td>
</tr>
<tr class="even">
<td>Hole punching</td>
<td><ul>
<li><p>JobHolePunch</p></li>
<li><p>DocumentHolePunch</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Stapling</td>
<td><ul>
<li><p>JobStapleAllDocuments</p></li>
<li><p>DocumentStaple</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Binding</td>
<td><ul>
<li><p>JobBindAllDocuments</p></li>
<li><p>DocumentBinding</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Output quality</td>
<td>PageOutputQuality</td>
</tr>
<tr class="even">
<td>Media size</td>
<td>PageMediaSize</td>
</tr>
</tbody>
</table>

 

In addition, these strings are available in the XML forms of PrintCapabilities, provided that the driver does not specify a display name using a resource DLL for the feature or option. If a driver does specify a display name using a resource DLL, it will be provided in the XML, as well as to the legacy COMPSTUI-based print preferences UI used on previous versions of Windows.

Across the different user interfaces and APIs, the display names vary. Use the following three flowcharts to see an overview of the expected localization behavior for a given scenario.

The following flowchart shows the expected localization behavior in UWP apps, as well as in the [**IPrintSchemaFeature**](https://msdn.microsoft.com/library/windows/hardware/hh451284) and [**IPrintSchemaOption**](https://msdn.microsoft.com/library/windows/hardware/hh451335) families of objects.

![localization behavior flowchart for Windows apps, iprintschemafeature or iprintschemaoption](images/locstringmodern.png)

The following flowchart shows the expected localization behavior in **PrintCapabilities** XML documents.

![localization behavior flowchart for printcapabilities xml documents](images/locstringpcap.png)

The following flowchart shows the expected localization behavior in the standard, Compstui-based print preferences dialog.

![localization behavior flowchart for compstui-based dialog ](images/locstringcomp.png)

To use the Microsoft-localized display names, follow the instructions in this table to properly edit your GPD or PPD configuration files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>File type</th>
<th>Instructions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GPD</td>
<td><ul>
<li><p>Specify the <strong><em>Name</strong> entry for the GPD feature or option.</p></li>
<li><p>Do not specify the <strong></em>rcNameID</strong> entry.</p></li>
<li>For the following features/options, you must also specify <strong><em>PrintSchemaKeywordMap</strong> to map GPD features or options to the corresponding Print Schema-defined features or options, unless they are specified as <a href="standard-features.md" data-raw-source="[Standard Features](standard-features.md)">Standard Features</a>. To see examples showing how to use <strong></em>PrintSchemaKeywordMap</strong> to map features, see <a href="gpd-ppd-based-feature-description-changes.md" data-raw-source="[GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)">GPD/PPD-Based Feature Description Changes</a>.
o JobHolePunch, DocumentHolePunch
o JobStapleAllDocuments, DocumentStaple
o JobBindAllDocuments, DocumentBinding
o PageOutputQuality
o PageMediaType</li>
<li><p>For N-Up, do not use <strong><em>PrintSchemaKeywordMap</strong> on the option values.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>PPD</td>
<td><ul>
<li><p>Use <strong></em>PrintSchemaKeywordMap</strong> to map PPD features or options to the corresponding Print Schema-defined features or options. To see examples showing how to use <strong><em>PrintSchemaKeywordMap</strong> to map features, see <a href="gpd-ppd-based-feature-description-changes.md" data-raw-source="[GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)">GPD/PPD-Based Feature Description Changes</a>.</p></li>
<li><p>For N-Up, do not use <strong></em>PrintSchemaKeywordMap</strong> on the option values.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

**Localizing PPD Based Drivers**

PPD based drivers do not support resource DLLs. As a result, it may be necessary to provide multiple PPD files. Microsoft recommends that v4 print drivers that use PPD configuration files should use the techniques outlined in this topic to include one PPD file per locale.

## Related topics
[**IPrintSchemaCapabilities**](https://msdn.microsoft.com/library/windows/hardware/hh451256)  
[**IPrintSchemaFeature**](https://msdn.microsoft.com/library/windows/hardware/hh451284)  
[**IPrintSchemaOption**](https://msdn.microsoft.com/library/windows/hardware/hh451335)  
[GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)  
[Standard Features](standard-features.md)  



