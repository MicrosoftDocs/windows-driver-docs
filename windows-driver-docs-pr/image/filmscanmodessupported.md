---
title: FilmScanModesSupported element
description: The required FilmScanModesSupported element contains a list of film exposure types that the film scanning option supports.
ms.assetid: bcc1335f-4465-4bc1-a804-b6e8729ec616
keywords: ["FilmScanModesSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmScanModesSupported
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# FilmScanModesSupported element


The required **FilmScanModesSupported** element contains a list of film exposure types that the film scanning option supports.

Usage
-----

``` syntax
<wscn:FilmScanModesSupported>
  child elements
</wscn:FilmScanModesSupported>
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
<td><p>[<strong>FilmScanModeValue</strong>](filmscanmodevalue.md)</p></td>
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

The **FilmScanModesSupported** element contains one or more [**FilmScanModeValue**](filmscanmodevalue.md) child elements. Each **FilmScanModeValue** element identifies a film exposure type that the film scanning option supports.

## <span id="see_also"></span>See also


[**Film**](film.md)

[**FilmScanModeValue**](filmscanmodevalue.md)

 

 






