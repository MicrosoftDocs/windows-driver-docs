---
title: ADFOpticalResolution element
description: The required ADFOpticalResolution element specifies the maximum optical resolution at which the front or back side of the automatic document feeder (ADF) can scan.
ms.assetid: 2000dbe4-9733-4a69-9e4e-c53c5a1c24c0
keywords: ["ADFOpticalResolution element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFOpticalResolution
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ADFOpticalResolution element


The required **ADFOpticalResolution** element specifies the maximum optical resolution at which the front or back side of the automatic document feeder (ADF) can scan.

Usage
-----

``` syntax
<wscn:ADFOpticalResolution>
  child elements
</wscn:ADFOpticalResolution>
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
<td><p>[<strong>Height</strong>](height.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Width</strong>](width.md)</p></td>
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

Resolution is specified as a [**Width**](width.md) × [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the parent element of the **ADFOpticalResolution** element is [**ADFFront**](adffront.md), the specified optical resolution applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the optical resolution applies to the back side of the ADF.

## <span id="see_also"></span>See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






