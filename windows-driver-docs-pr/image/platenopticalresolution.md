---
title: PlatenOpticalResolution element
description: The required PlatenOpticalResolution element specifies the maximum optical resolution at which the platen can scan.
ms.assetid: 770c204c-9315-47c6-afd3-4ac385e1177e
keywords: ["PlatenOpticalResolution element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn PlatenOpticalResolution
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PlatenOpticalResolution element


The required **PlatenOpticalResolution** element specifies the maximum optical resolution at which the platen can scan.

Usage
-----

```xml
<wscn:PlatenOpticalResolution>
  child elements
</wscn:PlatenOpticalResolution>
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
<td><p><a href="platen.md" data-raw-source="[&lt;strong&gt;Platen&lt;/strong&gt;](platen.md)"><strong>Platen</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

Resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the Height element is not specified, the WSD Scan Service should assume a square image resolution. For example, if only a **Width** element of 100 is provided, assume a resolution is 100 x 100 pixels per square inch.

## See also


[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)

 

 






