---
title: PlatenMaximumSize element
description: The required PlatenMaximumSize element specifies the largest size document that an end user can scan on the flatbed platen.
ms.assetid: dedeb5cf-588f-48dd-aea9-78c2a17f19e6
keywords: ["PlatenMaximumSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn PlatenMaximumSize
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PlatenMaximumSize element


The required **PlatenMaximumSize** element specifies the largest size document that an end user can scan on the flatbed platen.

Usage
-----

```xml
<wscn:PlatenMaximumSize>
  child elements
</wscn:PlatenMaximumSize>
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
<td><p>[<strong>Platen</strong>](platen.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the maximum size of media that the platen supports in the fast scan direction. The [**Height**](height.md) child element specifies the maximum size of media that the platen supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also


[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)

 

 






