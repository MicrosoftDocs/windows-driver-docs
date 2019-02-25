---
title: Standard Features
description: Standard Features
ms.assetid: 5cd90992-5ab8-4cb3-89b0-19e58e55b652
keywords:
- printer features WDK Unidrv , standard
- standard features WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard Features





Standard features are [printer features](printer-features.md) commonly provided by most printers. They are identified by predefined names that the GPD language recognizes. (Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit \[WDK\].) Some standard features are required and must be specified for every printer. Others are optional.

The following table lists all of the standard features, in alphabetical order, and indicates whether each feature accepts standard options or customized options. The features that include a Print Schema keyword are GPD features that are automatically mapped to Print Schema keywords. You can also map GPD features to Print Schema keywords manually by using the PrintSchemaKeywordMap attribute. The Print Schema is documented in the Microsoft Windows SDK.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature name</th>
<th>Default Print Schema feature keyword</th>
<th>Description</th>
<th>Standard options</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Collate</strong></p></td>
<td><p><strong>DocumentCollate</strong></p></td>
<td><p>Page collation</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are not allowed.</p></td>
<td><p>Optional. If not specified, Unidrv does not support page collation.</p></td>
</tr>
<tr class="even">
<td><p><strong>ColorMode</strong></p></td>
<td><p><strong>PageOutputColor</strong></p></td>
<td><p>Color printing modes</p></td>
<td><p>None. All options are customized. Also see <a href="option-attributes-for-the-colormode-feature.md" data-raw-source="[Option Attributes for the ColorMode Feature](option-attributes-for-the-colormode-feature.md)">Option Attributes for the ColorMode Feature</a>.</p></td>
<td><p>Optional. If not specified, Unidrv renders images in single-plane, 1-bit-per-pixel format.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Duplex</strong></p></td>
<td><p><strong>JobDuplexAllDocumentsContiguously</strong></p></td>
<td><p>Two-sided printing</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are not allowed.</p></td>
<td><p>Optional. If not specified, Unidrv performs only single-sided printing.</p></td>
</tr>
<tr class="even">
<td><p><strong>Halftone</strong></p></td>
<td><p>No default keyword. Use the PrintSchemaKeywordMap attribute to assign a Print Schema feature keyword.</p></td>
<td><p>Halftoning capabilities</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are allowed.</p>
<p>Also see <a href="option-attributes-for-the-halftone-feature.md" data-raw-source="[Option Attributes for the Halftone Feature](option-attributes-for-the-halftone-feature.md)">Option Attributes for the Halftone Feature</a>.</p></td>
<td><p>Optional. If not specified, Unidrv selects a GDI-supported halftoning method.</p>
<p>Also see <a href="halftoning-with-unidrv.md" data-raw-source="[Halftoning with Unidrv](halftoning-with-unidrv.md)">Halftoning with Unidrv</a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>InputBin</strong></p></td>
<td><p><strong>JobInputBin</strong></p></td>
<td><p>Types of input bins</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are allowed.</p>
<p>Also see <a href="option-attributes-for-the-inputbin-feature.md" data-raw-source="[Option Attributes for the InputBin Feature](option-attributes-for-the-inputbin-feature.md)">Option Attributes for the InputBin Feature</a>.</p></td>
<td><p>Required.</p>
<p>Customized input bin names must be 24 characters or less.</p></td>
</tr>
<tr class="even">
<td><p><strong>MediaType</strong></p></td>
<td><p><strong>PageMediaType</strong></p></td>
<td><p>Types of printing media</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are allowed.</p></td>
<td><p>Optional. If not specified, the printer&#39;s default medium is always used.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Memory</strong></p></td>
<td><p>No default keyword. Use the PrintSchemaKeywordMap attribute to assign Print Schema feature keyword.</p></td>
<td><p>Printer memory configurations</p></td>
<td><p>All options are customized. Also see <a href="option-attributes-for-the-memory-feature.md" data-raw-source="[Option Attributes for the Memory Feature](option-attributes-for-the-memory-feature.md)">Option Attributes for the Memory Feature</a>.</p></td>
<td><p>Optional. If specified, Unidrv attempts to keep track of memory usage.</p>
<p>Default *FeatureType value is PRINTER_PROPERTY.</p></td>
</tr>
<tr class="even">
<td><p><strong>Orientation</strong></p></td>
<td><p><strong>PageOrientation</strong></p></td>
<td><p>Paper orientations</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are not allowed.</p></td>
<td><p>Optional. If not specified, the default orientation is PORTRAIT.</p>
<p>For Windows 7, the <strong>MxdcGetPDEVAdjustment</strong> function has new parameters for landscape rotation. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557558" data-raw-source="[&lt;strong&gt;MxdcXDCGetPDEVAdjustment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557558)"><strong>MxdcXDCGetPDEVAdjustment</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>OutputBin</strong></p></td>
<td><p><strong>JobOutputBin</strong></p></td>
<td><p>Types of output bins</p></td>
<td><p>None. All options are customized.</p>
<p>Also see <a href="option-attributes-for-the-outputbin-feature.md" data-raw-source="[Option Attributes for the OutputBin Feature](option-attributes-for-the-outputbin-feature.md)">Option Attributes for the OutputBin Feature</a>.</p></td>
<td><p>Optional. If not specified, Unidrv does not attempt to select an output bin.</p></td>
</tr>
<tr class="even">
<td><p><strong>PageProtect</strong></p></td>
<td><p><strong>JobPageProtection</strong></p></td>
<td><p>Enables protection of current print page</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are not allowed.</p></td>
<td><p>Optional. If not specified, the default value is OFF. Unidrv only enables page protection if enough printer memory is available. Default *FeatureType value is PRINTER_PROPERTY. Also see *PageProtectMem.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PaperSize</strong></p></td>
<td><p><strong>PageMediaSize</strong></p></td>
<td><p>Paper sizes</p></td>
<td><p>See <a href="standard-options.md" data-raw-source="[Standard Options](standard-options.md)">Standard Options</a>.</p>
<p>Customized options are allowed.</p>
<p>Also see <a href="option-attributes-for-the-papersize-feature.md" data-raw-source="[Option Attributes for the PaperSize Feature](option-attributes-for-the-papersize-feature.md)">Option Attributes for the PaperSize Feature</a>.</p></td>
<td><p>Required. At least one option must be specified. The CUSTOMSIZE option allows printer users to specify a paper size.</p></td>
</tr>
<tr class="even">
<td><p><strong>RESDLL</strong></p></td>
<td><p>This feature cannot be mapped to a Print Schema keyword.</p></td>
<td><p>Resource DLLs</p></td>
<td><p>All options are customized.</p>
<p>See <a href="using-resource-dlls-in-a-minidriver.md" data-raw-source="[Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md)">Using Resource DLLs in a Minidriver</a>.</p></td>
<td><p>Optional. Also see *ResourceDLL.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Resolution</strong></p></td>
<td><p><strong>PageResolution</strong></p></td>
<td><p>Printing resolutions</p></td>
<td><p>All options are customized. Also see <a href="option-attributes-for-the-resolution-feature.md" data-raw-source="[Option Attributes for the Resolution Feature](option-attributes-for-the-resolution-feature.md)">Option Attributes for the Resolution Feature</a>.</p></td>
<td><p>Required. At least one option must be specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>Stapling</strong></p></td>
<td><p><strong>JobStapleAllDocuments</strong></p></td>
<td><p>Stapling capabilities</p></td>
<td><p>All options are customized.</p></td>
<td><p>Optional. If specified, Directory Services indicates the printer supports stapling.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

## Related topics
[Sample GPD files](sample-gpd-files.md)  
[V4 Printer Driver Localization](v4-driver-localization.md)  



