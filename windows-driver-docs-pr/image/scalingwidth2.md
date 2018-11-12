---
title: ScalingWidth element
description: The required ScalingWidth element contains the range of allowable values for scaling the width of the output document.
ms.assetid: 8b15f4b9-8537-479e-8745-0c8b35883bf5
keywords: ["ScalingWidth element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingWidth
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScalingWidth element


The required **ScalingWidth** element contains the range of allowable values for scaling the width of the output document.

Usage
-----

```xml
<wscn:ScalingWidth>
  child elements
</wscn:ScalingWidth>
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
<td><p><a href="maxvalue.md" data-raw-source="[&lt;strong&gt;MaxValue&lt;/strong&gt;](maxvalue.md)"><strong>MaxValue</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="minvalue.md" data-raw-source="[&lt;strong&gt;MinValue&lt;/strong&gt;](minvalue.md)"><strong>MinValue</strong></a></p></td>
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
<td><p><a href="scalingrangesupported.md" data-raw-source="[&lt;strong&gt;ScalingRangeSupported&lt;/strong&gt;](scalingrangesupported.md)"><strong>ScalingRangeSupported</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScalingWidth** element contains [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements that specify the minimum and maximum values that the scan device supports for scaling the width of an output document.

**MinValue** and **MaxValue** must be integers from 1 through 1000, with **MinValue** less than or equal to **MaxValue**. A value of 100 means that the scan device should not make any adjustments to the width of the scanned image. At a minimum, the WSD Scan Service must support the value of 100.

## See also


[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)

[**ScalingHeight**](scalingheight2.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

 

 






