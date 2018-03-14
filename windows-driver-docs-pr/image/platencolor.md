---
title: PlatenColor element
description: The required PlatenColor element contains a list of ColorEntry elements that describe the color processing capabilities of the platen.
ms.assetid: 97fd9926-e49d-4b4f-95aa-eb4142c353a3
keywords: ["PlatenColor element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn PlatenColor
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PlatenColor element


The required **PlatenColor** element contains a list of [**ColorEntry**](colorentry.md) elements that describe the color processing capabilities of the platen.

Usage
-----

``` syntax
<wscn:PlatenColor>
  child elements
</wscn:PlatenColor>
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
<td><p>[<strong>Platen</strong>](platen.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **PlatenColor** element contains the information needed to determine the type of color processing and acquisition that the flatbed platen supports. The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## <span id="see_also"></span>See also


[**ColorEntry**](colorentry.md)

[**Platen**](platen.md)

 

 






