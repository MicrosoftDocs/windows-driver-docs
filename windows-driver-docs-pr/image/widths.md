---
title: Widths element
description: The required Widths element contains the list of widths at which the scanner can scan images.
ms.assetid: 785d469f-bdad-413c-8bfb-de7a518b243c
keywords: ["Widths element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Widths
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Widths element


The required **Widths** element contains the list of widths at which the scanner can scan images.

Usage
-----

``` syntax
<wscn:Widths>
  child elements
</wscn:Widths>
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
<td><p>[<strong>ADFResolutions</strong>](adfresolutions.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>FilmResolutions</strong>](filmresolutions.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenResolutions</strong>](platenresolutions.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Each [**Width**](width.md) child element specifies a valid number of horizontal pixels per inch at which the device can scan images.

The [**Heights**](heights.md) element contains the list of heights that the scanner supports.

## <span id="see_also"></span>See also


[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Widths%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





