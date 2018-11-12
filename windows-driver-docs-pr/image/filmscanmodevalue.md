---
title: FilmScanModeValue element
description: The required FilmScanModeValue element identifies a specific film exposure type that the film scanning option supports.
ms.assetid: 62d72190-f1c5-4b2f-af6a-a3c530cc51ed
keywords: ["FilmScanModeValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmScanModeValue
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FilmScanModeValue element


The required **FilmScanModeValue** element identifies a specific film exposure type that the film scanning option supports.

Usage
-----

```xml
<wscn:FilmScanModeValue>
  text
</wscn:FilmScanModeValue>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="NotApplicable"></span><span id="notapplicable"></span><span id="NOTAPPLICABLE"></span>NotApplicable</p></td>
<td><p>The default scan input source is no longer the film option; therefore, FilmScanModeValue is no longer an applicable value for the DefaultScanTicket element. NotApplicable is valid only in a DefaultScanTicket element.</p></td>
</tr>
<tr class="even">
<td><p><span id="ColorSlideFilm"></span><span id="colorslidefilm"></span><span id="COLORSLIDEFILM"></span>ColorSlideFilm</p></td>
<td><p>Film images are in the normal color space.</p></td>
</tr>
<tr class="odd">
<td><p><span id="ColorNegativeFilm"></span><span id="colornegativefilm"></span><span id="COLORNEGATIVEFILM"></span>ColorNegativeFilm</p></td>
<td><p>Film images are negatives of the normal color space.</p></td>
</tr>
<tr class="even">
<td><p><span id="BlackandWhiteNegativeFilm"></span><span id="blackandwhitenegativefilm"></span><span id="BLACKANDWHITENEGATIVEFILM"></span>BlackandWhiteNegativeFilm</p></td>
<td><p>Film images are black and white negatives of the captured images.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="filmscanmodessupported.md" data-raw-source="[&lt;strong&gt;FilmScanModesSupported&lt;/strong&gt;](filmscanmodessupported.md)"><strong>FilmScanModesSupported</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

You can both extend and subset the allowed values for this element.

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**FilmScanModesSupported**](filmscanmodessupported.md)

 

 






