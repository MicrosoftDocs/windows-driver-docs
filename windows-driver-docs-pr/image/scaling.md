---
title: Scaling element
description: The optional Scaling element specifies the scaling of both the width and height of the scanned document.
ms.assetid: 43769ebf-f883-418a-a0b3-87d5b23601f9
keywords: ["Scaling element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Scaling wscn MustHonor ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Scaling element


The optional **Scaling** element specifies the scaling of both the width and height of the scanned document.

Usage
-----

```xml
<wscn:Scaling wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Scaling wscn:MustHonor="">
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
<td><p><strong><strong>MustHonor</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
</tbody>
</table>

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
<td><p><a href="scalingheight.md" data-raw-source="[&lt;strong&gt;ScalingHeight&lt;/strong&gt;](scalingheight.md)"><strong>ScalingHeight</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scalingwidth.md" data-raw-source="[&lt;strong&gt;ScalingWidth&lt;/strong&gt;](scalingwidth.md)"><strong>ScalingWidth</strong></a></p></td>
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
<td><p><a href="documentfinalparameters.md" data-raw-source="[&lt;strong&gt;DocumentFinalParameters&lt;/strong&gt;](documentfinalparameters.md)"><strong>DocumentFinalParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documentparameters.md" data-raw-source="[&lt;strong&gt;DocumentParameters&lt;/strong&gt;](documentparameters.md)"><strong>DocumentParameters</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **Scaling** element must contain both the [**ScalingWidth**](scalingwidth.md) and [**ScalingHeight**](scalingheight.md) elements. The **ScalingWidth** element specifies the scaling in the fast scan direction, and the **ScalingHeight** element specifies the scaling in the slow scan direction.

The client can specify the optional **MustHonor** attribute only when the **Scaling** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**ScalingHeight**](scalingheight.md)

[**ScalingWidth**](scalingwidth.md)

 

 






