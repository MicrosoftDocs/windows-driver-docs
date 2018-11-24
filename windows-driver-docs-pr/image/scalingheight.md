---
title: ScalingHeight element
description: The required ScalingHeight element specifies the document scaling in the slow scan direction.
ms.assetid: 29dcaab0-d32b-4aa0-ba27-3da0c9c39f97
keywords: ["ScalingHeight element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingHeight wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScalingHeight element


The required **ScalingHeight** element specifies the document scaling in the slow scan direction.

Usage
-----

```xml
<wscn:ScalingHeight wscn:Override=""                    wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ScalingHeight wscn:Override=""                    wscn:UsedDefault="">
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><strong>Override</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><strong>UsedDefault</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
</tbody>
</table>

Text value
----------

Required. An integer in the range from 1 through 1000, inclusive.

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
<td><p><a href="scaling.md" data-raw-source="[&lt;strong&gt;Scaling&lt;/strong&gt;](scaling.md)"><strong>Scaling</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScalingHeight** element specifies the scaling factor to apply in the slow scan direction. Scaling is expressed in 1 percent increments, where a value of 100 indicates a 100% width scale (no adjustment to the document height).

All WSD Scan Services must support at least the value 100.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ScalingHeight** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**Scaling**](scaling.md)

[**ScalingWidth**](scalingwidth.md)

 

 






