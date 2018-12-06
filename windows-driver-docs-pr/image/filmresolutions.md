---
title: FilmResolutions element
description: The required FilmResolutions element contains a list of resolutions at which the scanner's film scanning input source can scan.
ms.assetid: a273ac11-e1ae-4329-a6a2-e47accf564a9
keywords: ["FilmResolutions element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmResolutions
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FilmResolutions element


The required **FilmResolutions** element contains a list of resolutions at which the scanner's film scanning input source can scan.

Usage
-----

```xml
<wscn:FilmResolutions>
  child elements
</wscn:FilmResolutions>
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
<td><p><a href="film.md" data-raw-source="[&lt;strong&gt;Film&lt;/strong&gt;](film.md)"><strong>Film</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

The WSD Scan Service should list all possible widths that the scan device supports within the **Widths** child element and all possible heights that the scan device supports within the **Heights** child element. All **Width** and **Height** values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## See also


[**Film**](film.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)

 

 






