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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ADFOpticalResolution element


The required **ADFOpticalResolution** element specifies the maximum optical resolution at which the front or back side of the automatic document feeder (ADF) can scan.

Usage
-----

```xml
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
<td><p><a href="height.md" data-raw-source="[&lt;strong&gt;Height&lt;/strong&gt;](height.md)"><strong>Height</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="width.md" data-raw-source="[&lt;strong&gt;Width&lt;/strong&gt;](width.md)"><strong>Width</strong></a></p></td>
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

Resolution is specified as a [**Width**](width.md) × [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the parent element of the **ADFOpticalResolution** element is [**ADFFront**](adffront.md), the specified optical resolution applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the optical resolution applies to the back side of the ADF.

## See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






