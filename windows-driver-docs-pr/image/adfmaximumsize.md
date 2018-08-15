---
title: ADFMaximumSize element
description: The required ADFMaximumSize element specifies the largest size document that an end user can scan on the front or back side of the automatic document feeder (ADF).
ms.assetid: 8304bbae-e0ed-40f3-b3aa-2a818664b76a
keywords: ["ADFMaximumSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFMaximumSize
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ADFMaximumSize element


The required **ADFMaximumSize** element specifies the largest size document that an end user can scan on the front or back side of the automatic document feeder (ADF).

Usage
-----

``` syntax
<wscn:ADFMaximumSize>
  child elements
</wscn:ADFMaximumSize>
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
<td><p>[<strong>ADFBack</strong>](adfback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFFront</strong>](adffront.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the maximum size of media that the ADF supports in the fast scan direction. The [**Height**](height.md) child element specifies the maximum size of media that the ADF supports in the slow scan direction.

If the parent element of the **ADFMaximumSize** element is [**ADFFront**](adffront.md), the specified maximum size applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the maximum size applies to the back side of the ADF.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## <span id="see_also"></span>See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)

 

 






