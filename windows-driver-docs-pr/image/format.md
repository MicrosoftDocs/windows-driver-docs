---
title: Format element
description: The optional Format element indicates a single file format and compression type supported by the scanner.
ms.assetid: aa15607b-780b-48cb-b63f-b16476f69f70
keywords: ["Format element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Format wscn Override "" wscn UsedDefault ""
api_type:
- Schema
---

# Format element


The optional **Format** element indicates a single file format and compression type supported by the scanner.

Usage
-----

``` syntax
<wscn:Format wscn:Override="" wscn:UsedDefault=""
  
      Override
      = "xs:string"
  
      UsedDefault
      = "xs:string">
  text
</wscn:Format wscn:Override="" wscn:UsedDefault="">
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Override</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, <strong>false</strong>, 1, or <strong>true</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>UsedDefault</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, <strong>false</strong>, 1, or <strong>true</strong>.</p></td>
</tr>
</tbody>
</table>

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="dib"></span><span id="DIB"></span>dib</p></td>
<td><p>Windows Device Independent Bitmap.</p></td>
</tr>
<tr class="even">
<td><p><span id="exif"></span><span id="EXIF"></span>exif</p></td>
<td><p>Exchangeable Image File Format Version 2.x.</p></td>
</tr>
<tr class="odd">
<td><p><span id="jbig"></span><span id="JBIG"></span>jbig</p></td>
<td><p>ISO/IEC 11544:1993 Standard - Coded representation of picture and audio information; progressive bi-level image compression.</p></td>
</tr>
<tr class="even">
<td><p><span id="jfif"></span><span id="JFIF"></span>jfif</p></td>
<td><p>JPEG File Interchange Format 1.x.</p></td>
</tr>
<tr class="odd">
<td><p><span id="jpeg2k"></span><span id="JPEG2K"></span>jpeg2k</p></td>
<td><p>JPEG 2000 standard-based file format and compression.</p></td>
</tr>
<tr class="even">
<td><p><span id="pdf-a"></span><span id="PDF-A"></span>pdf-a</p></td>
<td><p>PDF/A format (standard based on ISO/CD 19005-1).</p></td>
</tr>
<tr class="odd">
<td><p><span id="png"></span><span id="PNG"></span>png</p></td>
<td><p>Portable Networks Graphics (PNG) format. This format supports only the PNG compression type.</p></td>
</tr>
<tr class="even">
<td><p><span id="tiff-single-uncompressed"></span><span id="TIFF-SINGLE-UNCOMPRESSED"></span>tiff-single-uncompressed</p></td>
<td><p>Single page TIFF file with no compression type.</p></td>
</tr>
<tr class="odd">
<td><p><span id="tiff-single-g4"></span><span id="TIFF-SINGLE-G4"></span>tiff-single-g4</p></td>
<td><p>Single page TIFF file with g4 compression type.</p></td>
</tr>
<tr class="even">
<td><p><span id="tiff-single-g3mh"></span><span id="TIFF-SINGLE-G3MH"></span>tiff-single-g3mh</p></td>
<td><p>Single page TIFF file with g3mh compression type.</p></td>
</tr>
<tr class="odd">
<td><p><span id="tiff-single-jpeg-tn2"></span><span id="TIFF-SINGLE-JPEG-TN2"></span>tiff-single-jpeg-tn2</p></td>
<td><p>Single page TIFF file with the JPEG compression type as described in Technical Note 2.</p></td>
</tr>
<tr class="even">
<td><p><span id="tiff-multi-uncompressed"></span><span id="TIFF-MULTI-UNCOMPRESSED"></span>tiff-multi-uncompressed</p></td>
<td><p>Multiple page TIFF file with no compression type.</p></td>
</tr>
<tr class="odd">
<td><p><span id="tiff-multi-g4"></span><span id="TIFF-MULTI-G4"></span>tiff-multi-g4</p></td>
<td><p>Multiple page TIFF file with g4 compression type.</p></td>
</tr>
<tr class="even">
<td><p><span id="tiff-multi-g3mh"></span><span id="TIFF-MULTI-G3MH"></span>tiff-multi-g3mh</p></td>
<td><p>Multiple page TIFF file with g3mh compression type.</p></td>
</tr>
<tr class="odd">
<td><p><span id="tiff-multi-jpeg-tn2"></span><span id="TIFF-MULTI-JPEG-TN2"></span>tiff-multi-jpeg-tn2</p></td>
<td><p>Multiple page TIFF file with the JPEG compression type as described in Technical Note 2.</p></td>
</tr>
<tr class="even">
<td><p><span id="xps"></span><span id="XPS"></span>xps</p></td>
<td><p>XML Paper Specification</p></td>
</tr>
<tr class="odd">
<td><p><span id="Any_vendor-defined_values"></span><span id="any_vendor-defined_values"></span><span id="ANY_VENDOR-DEFINED_VALUES"></span>Any vendor-defined values</p></td>
<td></td>
</tr>
</tbody>
</table>

 

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>DocumentFinalParameters</strong>](documentfinalparameters.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentParameters</strong>](documentparameters.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the image **Format** element is unsupported, then the scanner must reject the request and return the **ClientErrorDocumentFormatNotSupported** error code.

When the scanner sends out the **ClientErrorDocumentFormatNotSupported** error code because it doesn't support an image format, then the WSD scanner driver will try selecting other image formats in the following order, to find a format that the scanner supports.

1. PNG (W3C PNG) format is selected, if it's supported by the scanner.

2. EXIF format is selected, if it's supported by the scanner and the color mode matches RGB (24bpp) or grayscale (8pp).

3. G4 single-page TIFF (tiff-single-g4) format is selected, if it's supported by the scanner and color mode is monochrome (1bpp).

4. Uncompressed single-page TIFF (tiff-single-uncompressed) format is selected, if it's supported by the scanner.

Starting with Windows 7, WIA supports auto-configured scanning. And if auto-configured scanning with DIB format is requested, but the scanner doesn't support the DIB format, then the WSD scanner driver uses the same algorithm shown in the preceding steps to select an image format that the scanner supports.

**Note**  Color mode is not selectable for auto-configured scan.

 

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Format**element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can both extend and create a subset of the allowed values for this element.

Although the WSD Scan Service supports the JBIG file format (ISO/IEC 11544:1993), it does not currently support JBIG2 (ISO/IEC 14492:2001).

## <span id="see_also"></span>See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**FormatValue**](formatvalue.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Format%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





