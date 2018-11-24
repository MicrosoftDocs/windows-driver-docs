---
title: FormatValue element
description: The required FormatValue element specifies a single supported file format and compression type.
ms.assetid: 0331f44d-6343-45f7-85a7-303733f3ee75
keywords: ["FormatValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FormatValue
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FormatValue element


The required **FormatValue** element specifies a single supported file format and compression type.

Usage
-----

```xml
<wscn:FormatValue>
  text
</wscn:FormatValue>
```

Attributes
----------

There are no attributes.

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
<td><p><span id="dib_"></span><span id="DIB_"></span>dib</p></td>
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
<td><p>Single page TIFF file with jpeg compression type as described in Technical Note 2.</p></td>
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
<td><p>Multiple page TIFF file with jpeg compression type as described in Technical Note 2.</p></td>
</tr>
<tr class="even">
<td><p><span id="xps"></span><span id="XPS"></span>xps</p></td>
<td><p>XML Paper Specification.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Any_vendor-defined_values."></span><span id="any_vendor-defined_values."></span><span id="ANY_VENDOR-DEFINED_VALUES."></span>Any vendor-defined values.</p></td>
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
<td><p><a href="formatssupported.md" data-raw-source="[&lt;strong&gt;FormatsSupported&lt;/strong&gt;](formatssupported.md)"><strong>FormatsSupported</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

You can both extend and subset the allowed values for this element.

Although the WSD Scan Service supports the JBIG file format (ISO/IEC 11544:1993), it does *not* currently support JBIG2 (ISO/IEC 14492:2001).

## See also


[**FormatsSupported**](formatssupported.md)

 

 






