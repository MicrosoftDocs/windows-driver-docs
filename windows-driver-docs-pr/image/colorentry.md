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
---

# ColorEntry element


The required **ColorEntry** element describes a single color-processing mode that an input source on the scanner supports.

Usage
-----

``` syntax
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
<td><p>[<strong>ADFColor</strong>](adfcolor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>FilmColor</strong>](filmcolor.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenColor</strong>](platencolor.md)</p></td>
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

## <span id="see_also"></span>See also


[**ADFColor**](adfcolor.md)

[**FilmColor**](filmcolor.md)

[**PlatenColor**](platencolor.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ColorEntry%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





