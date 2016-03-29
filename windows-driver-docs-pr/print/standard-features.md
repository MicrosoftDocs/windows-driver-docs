---
title: Standard Features
description: Standard Features
ms.assetid: 5cd90992-5ab8-4cb3-89b0-19e58e55b652
keywords: ["printer features WDK Unidrv , standard", "standard features WDK Unidrv"]
---

# Standard Features


## <a href="" id="ddk-standard-features-gg"></a>


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
<th align="left">Feature name</th>
<th align="left">Default Print Schema feature keyword</th>
<th align="left">Description</th>
<th align="left">Standard options</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Collate</strong></p></td>
<td align="left"><p><strong>DocumentCollate</strong></p></td>
<td align="left"><p>Page collation</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are not allowed.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not support page collation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ColorMode</strong></p></td>
<td align="left"><p><strong>PageOutputColor</strong></p></td>
<td align="left"><p>Color printing modes</p></td>
<td align="left"><p>None. All options are customized. Also see [Option Attributes for the ColorMode Feature](option-attributes-for-the-colormode-feature.md).</p></td>
<td align="left"><p>Optional. If not specified, Unidrv renders images in single-plane, 1-bit-per-pixel format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Duplex</strong></p></td>
<td align="left"><p><strong>JobDuplexAllDocumentsContiguously</strong></p></td>
<td align="left"><p>Two-sided printing</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are not allowed.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv performs only single-sided printing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Halftone</strong></p></td>
<td align="left"><p>No default keyword. Use the PrintSchemaKeywordMap attribute to assign a Print Schema feature keyword.</p></td>
<td align="left"><p>Halftoning capabilities</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are allowed.</p>
<p>Also see [Option Attributes for the Halftone Feature](option-attributes-for-the-halftone-feature.md).</p></td>
<td align="left"><p>Optional. If not specified, Unidrv selects a GDI-supported halftoning method.</p>
<p>Also see [Halftoning with Unidrv](halftoning-with-unidrv.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>InputBin</strong></p></td>
<td align="left"><p><strong>JobInputBin</strong></p></td>
<td align="left"><p>Types of input bins</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are allowed.</p>
<p>Also see [Option Attributes for the InputBin Feature](option-attributes-for-the-inputbin-feature.md).</p></td>
<td align="left"><p>Required.</p>
<p>Customized input bin names must be 24 characters or less.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MediaType</strong></p></td>
<td align="left"><p><strong>PageMediaType</strong></p></td>
<td align="left"><p>Types of printing media</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are allowed.</p></td>
<td align="left"><p>Optional. If not specified, the printer's default medium is always used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Memory</strong></p></td>
<td align="left"><p>No default keyword. Use the PrintSchemaKeywordMap attribute to assign Print Schema feature keyword.</p></td>
<td align="left"><p>Printer memory configurations</p></td>
<td align="left"><p>All options are customized. Also see [Option Attributes for the Memory Feature](option-attributes-for-the-memory-feature.md).</p></td>
<td align="left"><p>Optional. If specified, Unidrv attempts to keep track of memory usage.</p>
<p>Default *FeatureType value is PRINTER_PROPERTY.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Orientation</strong></p></td>
<td align="left"><p><strong>PageOrientation</strong></p></td>
<td align="left"><p>Paper orientations</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are not allowed.</p></td>
<td align="left"><p>Optional. If not specified, the default orientation is PORTRAIT.</p>
<p>For Windows 7, the <strong>MxdcGetPDEVAdjustment</strong> function has new parameters for landscape rotation. For more information, see [<strong>MxdcXDCGetPDEVAdjustment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557558).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OutputBin</strong></p></td>
<td align="left"><p><strong>JobOutputBin</strong></p></td>
<td align="left"><p>Types of output bins</p></td>
<td align="left"><p>None. All options are customized.</p>
<p>Also see [Option Attributes for the OutputBin Feature](option-attributes-for-the-outputbin-feature.md).</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not attempt to select an output bin.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PageProtect</strong></p></td>
<td align="left"><p><strong>JobPageProtection</strong></p></td>
<td align="left"><p>Enables protection of current print page</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are not allowed.</p></td>
<td align="left"><p>Optional. If not specified, the default value is OFF. Unidrv only enables page protection if enough printer memory is available. Default *FeatureType value is PRINTER_PROPERTY. Also see *PageProtectMem.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PaperSize</strong></p></td>
<td align="left"><p><strong>PageMediaSize</strong></p></td>
<td align="left"><p>Paper sizes</p></td>
<td align="left"><p>See [Standard Options](standard-options.md).</p>
<p>Customized options are allowed.</p>
<p>Also see [Option Attributes for the PaperSize Feature](option-attributes-for-the-papersize-feature.md).</p></td>
<td align="left"><p>Required. At least one option must be specified. The CUSTOMSIZE option allows printer users to specify a paper size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RESDLL</strong></p></td>
<td align="left"><p>This feature cannot be mapped to a Print Schema keyword.</p></td>
<td align="left"><p>Resource DLLs</p></td>
<td align="left"><p>All options are customized.</p>
<p>See [Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md).</p></td>
<td align="left"><p>Optional. Also see *ResourceDLL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Resolution</strong></p></td>
<td align="left"><p><strong>PageResolution</strong></p></td>
<td align="left"><p>Printing resolutions</p></td>
<td align="left"><p>All options are customized. Also see [Option Attributes for the Resolution Feature](option-attributes-for-the-resolution-feature.md).</p></td>
<td align="left"><p>Required. At least one option must be specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Stapling</strong></p></td>
<td align="left"><p><strong>JobStapleAllDocuments</strong></p></td>
<td align="left"><p>Stapling capabilities</p></td>
<td align="left"><p>All options are customized.</p></td>
<td align="left"><p>Optional. If specified, Directory Services indicates the printer supports stapling.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

## Related topics


[Sample GPD files](sample-gpd-files.md)

[V4 Printer Driver Localization](v4-driver-localization.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20Features%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





