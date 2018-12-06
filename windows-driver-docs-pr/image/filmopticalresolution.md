---
title: FilmOpticalResolution element
description: The required FilmOpticalResolution element specifies the maximum optical resolution at which the film scanning input source can scan.
ms.assetid: 85e3b737-d5b0-4262-ab86-32b6aaf56e26
keywords: ["FilmOpticalResolution element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmOpticalResolution
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FilmOpticalResolution element


The required **FilmOpticalResolution** element specifies the maximum optical resolution at which the film scanning input source can scan.

Usage
-----

```xml
<wscn:FilmOpticalResolution/>
```

Attributes
----------

There are no attributes.

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
<td><p><a href="film.md" data-raw-source="[&lt;strong&gt;Film&lt;/strong&gt;](film.md)"><strong>Film</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

Resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If **Height** is absent, the WSD Scan Service should assume a square image resolution. For example, if only a **Width** element of 100 is provided, assume that the resolution is 100 x 100 pixels per square inch.

## See also


[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






