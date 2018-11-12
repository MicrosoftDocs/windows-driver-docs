---
title: PlatenResolutions element
description: The required PlatenResolutions element contains a list of resolutions at which the scanner's platen can scan.
ms.assetid: 9adf54d7-4cca-4d43-b467-c0b2c84a4a7f
keywords: ["PlatenResolutions element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn PlatenResolutions
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PlatenResolutions element


The required **PlatenResolutions** element contains a list of resolutions at which the scanner's platen can scan.

Usage
-----

```xml
<wscn:PlatenResolutions>
  child elements
</wscn:PlatenResolutions>
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
<td><p><a href="heights.md" data-raw-source="[&lt;strong&gt;Heights&lt;/strong&gt;](heights.md)"><strong>Heights</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="widths.md" data-raw-source="[&lt;strong&gt;Widths&lt;/strong&gt;](widths.md)"><strong>Widths</strong></a></p></td>
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

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both Width and Height are specified in pixels per inch.

The WSD Scan Service should list all possible widths that the scan device supports within the Widths child element and all possible heights that the scan device supports within the Heights child element. All Width and Height values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## See also


[**Height**](height.md)

[**Heights**](heights.md)

[**Platen**](platen.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)

 

 






