---
title: FilmScanModeValue element
description: The required FilmScanModeValue element identifies a specific film exposure type that the film scanning option supports.
MS-HAID:
- 'wsdss\_adffilm\_9634667f-8177-4d06-b8c6-7a8d680d981f.xml'
- 'image.filmscanmodevalue'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 62d72190-f1c5-4b2f-af6a-a3c530cc51ed
keywords: ["FilmScanModeValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmScanModeValue
api_type:
- Schema
---

# FilmScanModeValue element


The required **FilmScanModeValue** element identifies a specific film exposure type that the film scanning option supports.

Usage
-----

``` syntax
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
<td><p>[<strong>FilmScanModesSupported</strong>](filmscanmodessupported.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**DefaultScanTicket**](defaultscanticket.md)

[**FilmScanModesSupported**](filmscanmodessupported.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20FilmScanModeValue%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





