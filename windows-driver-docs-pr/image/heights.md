---
title: Heights element
description: The required Heights element contains the list of heights at which the scanner can scan images.
ms.assetid: b45a967e-9ce9-417a-96f2-c199ab302b88
keywords: ["Heights element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Heights
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Heights element


The required **Heights** element contains the list of heights at which the scanner can scan images.

Usage
-----

``` syntax
<wscn:Heights>
  child elements
</wscn:Heights>
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

Each [**Height**](height.md) child element specifies a valid number of vertical pixels per inch at which the device can scan images.

The [**Widths**](widths.md) element contains the list of widths that the scanner supports.

## <span id="see_also"></span>See also


[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)

[**Widths**](widths.md)

 

 






