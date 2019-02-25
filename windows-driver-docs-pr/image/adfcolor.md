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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ADFColor element


The required **ADFColor** element contains the list of color processing capabilities that the front or back side of the automatic document feeder (ADF) supports.

Usage
-----

```xml
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
<td><p><a href="colorentry.md" data-raw-source="[&lt;strong&gt;ColorEntry&lt;/strong&gt;](colorentry.md)"><strong>ColorEntry</strong></a></p></td>
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
<td><p><a href="adfback.md" data-raw-source="[&lt;strong&gt;ADFBack&lt;/strong&gt;](adfback.md)"><strong>ADFBack</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="adffront.md" data-raw-source="[&lt;strong&gt;ADFFront&lt;/strong&gt;](adffront.md)"><strong>ADFFront</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ADFColor** element contains the information needed to determine the type of color processing and acquisition that the scanner's ADF supports. If the parent element is [**ADFFront**](adffront.md), the specified color information applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the color information applies to the back side of the ADF.

The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ColorEntry**](colorentry.md)

 

 






