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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FilmMaximumSize element


The required **FilmMaximumSize** element specifies the largest size original that an end user can scan with the film scanning input source.

Usage
-----

``` syntax
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
<td><p>[<strong>Film</strong>](film.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the maximum size of media that the film scanning input source supports in the fast scan direction. The [**Height**](height.md) child element specifies the maximum size of media that the film scanning input source supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## <span id="see_also"></span>See also


[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






