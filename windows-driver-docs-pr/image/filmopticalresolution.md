---
title: FilmOpticalResolution element
description: The required FilmOpticalResolution element specifies the maximum optical resolution at which the film scanning input source can scan.
MS-HAID:
- 'wsdss\_adffilm\_0362769b-14ea-40e9-9b4b-c96669b5de73.xml'
- 'image.filmopticalresolution'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 85e3b737-d5b0-4262-ab86-32b6aaf56e26
keywords: ["FilmOpticalResolution element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmOpticalResolution
api_type:
- Schema
---

# FilmOpticalResolution element


The required **FilmOpticalResolution** element specifies the maximum optical resolution at which the film scanning input source can scan.

Usage
-----

``` syntax
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
<td><p>[<strong>Film</strong>](film.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If **Height** is absent, the WSD Scan Service should assume a square image resolution. For example, if only a **Width** element of 100 is provided, assume that the resolution is 100 x 100 pixels per square inch.

## <span id="see_also"></span>See also


[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20FilmOpticalResolution%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





