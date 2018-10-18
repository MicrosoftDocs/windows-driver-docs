---
title: MaxValue element
description: The required MaxValue element specifies the maximum value that the scan device supports for scanner configuration elements that require a range of values.
ms.assetid: a01833ff-06cd-47d3-9f54-2f1cf01cc1e6
keywords: ["MaxValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn MaxValue
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MaxValue element


The required **MaxValue** element specifies the maximum value that the scan device supports for scanner configuration elements that require a range of values.

Usage
-----

```xml
<wscn:MaxValue>
  text
</wscn:MaxValue>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. For possible values, see the specific parent element.

## Child elements


There are no child elements.

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
<td><p>[<strong>CompressionQualityFactorSupported</strong>](compressionqualityfactorsupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScalingHeight</strong>](scalingheight2.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScalingWidth</strong>](scalingwidth2.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The value of the **MaxValue** element depends on its parent element. For the possible values, see the appropriate parent element.

## See also


[**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md)

[**MinValue**](minvalue.md)

[**ScalingHeight**](scalingheight2.md)

[**ScalingWidth**](scalingwidth2.md)

 

 






