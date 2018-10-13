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
ms.localizationpriority: medium
---

# Widths element


The required **Widths** element contains the list of widths at which the scanner can scan images.

Usage
-----

```xml
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

## See also


[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)

 

 






