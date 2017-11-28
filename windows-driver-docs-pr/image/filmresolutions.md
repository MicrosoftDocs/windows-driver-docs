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
---

# FilmResolutions element


The required **FilmResolutions** element contains a list of resolutions at which the scanner's film scanning input source can scan.

Usage
-----

``` syntax
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
<td><p>[<strong>Heights</strong>](heights.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Widths</strong>](widths.md)</p></td>
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

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

The WSD Scan Service should list all possible widths that the scan device supports within the **Widths** child element and all possible heights that the scan device supports within the **Heights** child element. All **Width** and **Height** values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## <span id="see_also"></span>See also


[**Film**](film.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20FilmResolutions%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





