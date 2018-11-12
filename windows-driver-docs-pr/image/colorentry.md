---
title: ColorEntry element
description: The required ColorEntry element describes a single color-processing mode that an input source on the scanner supports.
ms.assetid: a25c6da6-058e-4d10-895c-4507f0562ee8
keywords: ["ColorEntry element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ColorEntry
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ColorEntry element


The required **ColorEntry** element describes a single color-processing mode that an input source on the scanner supports.

Usage
-----

```xml
<wscn:ColorEntry>
  text
</wscn:ColorEntry>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following keywords:

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
<td><p><span id="BlackAndWhite1"></span><span id="blackandwhite1"></span><span id="BLACKANDWHITE1"></span>BlackAndWhite1</p></td>
<td><p>Black and white images; 1 bit per pixel (bpp) and a single channel</p></td>
</tr>
<tr class="even">
<td><p><span id="Grayscale4"></span><span id="grayscale4"></span><span id="GRAYSCALE4"></span>Grayscale4</p></td>
<td><p>Grayscale images; 4 bpp and a single channel</p></td>
</tr>
<tr class="odd">
<td><p><span id="Grayscale8"></span><span id="grayscale8"></span><span id="GRAYSCALE8"></span>Grayscale8</p></td>
<td><p>Grayscale images; 8 bpp and a single channel</p></td>
</tr>
<tr class="even">
<td><p><span id="Grayscale16"></span><span id="grayscale16"></span><span id="GRAYSCALE16"></span>Grayscale16</p></td>
<td><p>Grayscale images; 16 bpp and a single channel</p></td>
</tr>
<tr class="odd">
<td><p><span id="RGB24"></span><span id="rgb24"></span>RGB24</p></td>
<td><p>RGB-encoded color images; 24 bpp divided between three channels of 8 bits each</p></td>
</tr>
<tr class="even">
<td><p><span id="RGB48"></span><span id="rgb48"></span>RGB48</p></td>
<td><p>RGB-encoded color images; 48 bpp divided between three channels of 16 bits each</p></td>
</tr>
<tr class="odd">
<td><p><span id="RGBa32"></span><span id="rgba32"></span><span id="RGBA32"></span>RGBa32</p></td>
<td><p>RGB-encoded color images with an alpha channel; 32 bits bpp divided between four channels of 8 bits each</p></td>
</tr>
<tr class="even">
<td><p><span id="RGBa64"></span><span id="rgba64"></span><span id="RGBA64"></span>RGBa64</p></td>
<td><p>RGB-encoded color images with an alpha channel; 64 bpp divided between four channels of 16 bits each</p></td>
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
<td><p><a href="adfcolor.md" data-raw-source="[&lt;strong&gt;ADFColor&lt;/strong&gt;](adfcolor.md)"><strong>ADFColor</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="filmcolor.md" data-raw-source="[&lt;strong&gt;FilmColor&lt;/strong&gt;](filmcolor.md)"><strong>FilmColor</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="platencolor.md" data-raw-source="[&lt;strong&gt;PlatenColor&lt;/strong&gt;](platencolor.md)"><strong>PlatenColor</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

Each value keyword describes the color data type and encoding, bit depth, and bits per channel. The following table shows how the value keywords map to the scanner's color processing properties.

| Keyword        | Pixel bit depth | Bits per channel |
|----------------|-----------------|------------------|
| BlackAndWhite1 | 1               | 1                |
| Grayscale4     | 4               | {4}              |
| Grayscale8     | 8               | {8}              |
| Grayscale16    | 16              | {16}             |
| RGB24          | 24              | {8,8,8}          |
| RGB48          | 48              | {16,16,16}       |
| RGBa32         | 32              | {8,8,8,8}        |
| RGBa64         | 64              | {16,16,16,16}    |

 

You can both extend and subset the allowed values for this element.

## See also


[**ADFColor**](adfcolor.md)

[**FilmColor**](filmcolor.md)

[**PlatenColor**](platencolor.md)

 

 






