---
title: Resolution element
description: The optional Resolution element specifies the resolution of the scanned image.
ms.assetid: d46c197d-40ed-4623-a842-7ee5cb9e8367
keywords: ["Resolution element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Resolution wscn MustHonor ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Resolution element


The optional **Resolution** element specifies the resolution of the scanned image.

Usage
-----

```xml
<wscn:Resolution wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Resolution wscn:MustHonor="">
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
<td><p><a href="mediaback.md" data-raw-source="[&lt;strong&gt;MediaBack&lt;/strong&gt;](mediaback.md)"><strong>MediaBack</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="mediafront.md" data-raw-source="[&lt;strong&gt;MediaFront&lt;/strong&gt;](mediafront.md)"><strong>MediaFront</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **Resolution** element contains a single [**Width**](width.md) x [**Height**](height.md) pair that describes the desired scan resolution. If the **Height** element is missing, the **Width** value is used, yielding a square resolution (for example, 300 x 300).

**Resolution** values are in pixels per inch.

The client can specify the optional **MustHonor** attribute only when the **Resolution** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**Height**](height.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**Width**](width.md)

 

 






