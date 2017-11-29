---
title: ADFColor element
description: The required ADFColor element contains the list of color processing capabilities that the front or back side of the automatic document feeder (ADF) supports.
ms.assetid: b336c72e-9095-456e-8cb4-4018e72e29fa
keywords: ["ADFColor element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFColor
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ADFColor element


The required **ADFColor** element contains the list of color processing capabilities that the front or back side of the automatic document feeder (ADF) supports.

Usage
-----

``` syntax
<wscn:ADFColor>
  child elements
</wscn:ADFColor>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p>[<strong>ColorEntry</strong>](colorentry.md)</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>ADFBack</strong>](adfback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFFront</strong>](adffront.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ADFColor** element contains the information needed to determine the type of color processing and acquisition that the scanner's ADF supports. If the parent element is [**ADFFront**](adffront.md), the specified color information applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the color information applies to the back side of the ADF.

The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## <span id="see_also"></span>See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ColorEntry**](colorentry.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ADFColor%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





