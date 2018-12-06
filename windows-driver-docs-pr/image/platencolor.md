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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PlatenColor element


The required **PlatenColor** element contains a list of [**ColorEntry**](colorentry.md) elements that describe the color processing capabilities of the platen.

Usage
-----

```xml
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
<td><p><a href="platen.md" data-raw-source="[&lt;strong&gt;Platen&lt;/strong&gt;](platen.md)"><strong>Platen</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **PlatenColor** element contains the information needed to determine the type of color processing and acquisition that the flatbed platen supports. The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## See also


[**ColorEntry**](colorentry.md)

[**Platen**](platen.md)

 

 






