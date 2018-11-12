---
title: FilmMaximumSize element
description: The required FilmMaximumSize element specifies the largest size original that an end user can scan with the film scanning input source.
ms.assetid: 936c3c4e-5b09-433e-876c-9eda438dde9c
keywords: ["FilmMaximumSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmMaximumSize
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FilmMaximumSize element


The required **FilmMaximumSize** element specifies the largest size original that an end user can scan with the film scanning input source.

Usage
-----

```xml
<wscn:FilmMaximumSize>
  child elements
</wscn:FilmMaximumSize>
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
<td><p><a href="film.md" data-raw-source="[&lt;strong&gt;Film&lt;/strong&gt;](film.md)"><strong>Film</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the maximum size of media that the film scanning input source supports in the fast scan direction. The [**Height**](height.md) child element specifies the maximum size of media that the film scanning input source supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also


[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






