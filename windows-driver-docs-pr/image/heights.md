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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Heights element


The required **Heights** element contains the list of heights at which the scanner can scan images.

Usage
-----

```xml
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
<td><p><a href="height.md" data-raw-source="[&lt;strong&gt;Height&lt;/strong&gt;](height.md)"><strong>Height</strong></a></p></td>
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
<td><p><a href="adfresolutions.md" data-raw-source="[&lt;strong&gt;ADFResolutions&lt;/strong&gt;](adfresolutions.md)"><strong>ADFResolutions</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="filmresolutions.md" data-raw-source="[&lt;strong&gt;FilmResolutions&lt;/strong&gt;](filmresolutions.md)"><strong>FilmResolutions</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="platenresolutions.md" data-raw-source="[&lt;strong&gt;PlatenResolutions&lt;/strong&gt;](platenresolutions.md)"><strong>PlatenResolutions</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

Each [**Height**](height.md) child element specifies a valid number of vertical pixels per inch at which the device can scan images.

The [**Widths**](widths.md) element contains the list of widths that the scanner supports.

## See also


[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)

[**Widths**](widths.md)

 

 






