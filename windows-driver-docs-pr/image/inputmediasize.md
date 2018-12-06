---
title: InputMediaSize element
description: The required InputMediaSize element specifies the size of the media to be scanned for the current job.
ms.assetid: f1fcb152-96c5-469c-8989-a2c4328a5f68
keywords: ["InputMediaSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn InputMediaSize
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# InputMediaSize element


The required **InputMediaSize** element specifies the size of the media to be scanned for the current job.

Usage
-----

```xml
<wscn:InputMediaSize>
  child elements
</wscn:InputMediaSize>
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
<td><p><a href="inputsize.md" data-raw-source="[&lt;strong&gt;InputSize&lt;/strong&gt;](inputsize.md)"><strong>InputSize</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **InputMediaSize** element contains the width and height of the input media to be scanned, specified in the [**Width**](width.md) and [**Height**](height.md) elements, respectively.

The **Width** element contains the width of the original media in the fast scan direction, and the **Height** element contains the height of the original media in the slow scan direction. Both **Width** and **Height** must be in the range from 1 through 2147483648 and are in units of one-thousandths (1/1000) of an inch.

## See also


[**Height**](height.md)

[**InputSize**](inputsize.md)

[**Width**](width.md)

 

 






