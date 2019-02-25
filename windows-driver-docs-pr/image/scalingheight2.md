---
title: ScalingHeight element
description: The required ScalingHeight element contains the range of allowable values for scaling the height of the output document.
ms.assetid: f13e1ef8-e05f-4aab-bf2a-08a953638334
keywords: ["ScalingHeight element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingHeight
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScalingHeight element


The required **ScalingHeight** element contains the range of allowable values for scaling the height of the output document.

Usage
-----

```xml
<wscn:ScalingHeight>
  child elements
</wscn:ScalingHeight>
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

The **ScalingHeight** element contains the [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements that specify the minimum and maximum values that the scan device supports for scaling the height of an output document.

**MinValue** and **MaxValue** must be integers from 1 through 1000, with **MinValue** less than or equal to **MaxValue**. A value of 100 means that the scan device should not make any adjustments to the height of the scanned image. At a minimum, the WSD Scan Service must support the value of 100.

## See also


[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

[**ScalingWidth2**](scalingwidth.md)

 

 






