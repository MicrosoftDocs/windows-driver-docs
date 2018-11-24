---
title: PlatenMinimumSize element
description: The required PlatenMinimumSize element specifies the smallest size document that an end user can scan on the flatbed platen.
ms.assetid: 8db5092f-415c-4942-a4a7-733a381afd16
keywords: ["PlatenMinimumSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn PlatenMinimumSize
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PlatenMinimumSize element


The required **PlatenMinimumSize** element specifies the smallest size document that an end user can scan on the flatbed platen.

Usage
-----

```xml
<wscn:PlatenMinimumSize>
  child elements
</wscn:PlatenMinimumSize>
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
<td><p><a href="height.md" data-raw-source="[&lt;strong&gt;Height&lt;/strong&gt;](height.md)"><strong>Height</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="width.md" data-raw-source="[&lt;strong&gt;Width&lt;/strong&gt;](width.md)"><strong>Width</strong></a></p></td>
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
<td><p><a href="platen.md" data-raw-source="[&lt;strong&gt;Platen&lt;/strong&gt;](platen.md)"><strong>Platen</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the minimum size of media that the platen supports in the fast scan direction. The [**Height**](height.md) child element specifies the minimum size of media that the platen supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also


[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)

 

 






