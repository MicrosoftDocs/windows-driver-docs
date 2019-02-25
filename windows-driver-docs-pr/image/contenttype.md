---
title: ContentType element
description: The optional ContentType element specifies the main characteristics of the original document.
ms.assetid: 0e91e4ec-5569-452f-b929-9d2923f3147d
keywords: ["ContentType element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContentType wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ContentType element


The optional **ContentType** element specifies the main characteristics of the original document.

Usage
-----

```xml
<wscn:ContentType wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ContentType wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault="">
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
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
<tr class="even">
<td><p><strong><strong>Override</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
<tr class="odd">
<td><p><strong><strong>UsedDefault</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
</tbody>
</table>

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>Auto</p></td>
<td><p>The scan device will automatically detect the original type.</p></td>
</tr>
<tr class="even">
<td><p><span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text</p></td>
<td><p>The document is mainly composed of distinct text that contrasts strongly with the background.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Photo"></span><span id="photo"></span><span id="PHOTO"></span>Photo</p></td>
<td><p>The original is mainly composed of photographic images, where shades change gradually and edges are not distinct.</p></td>
</tr>
<tr class="even">
<td><p><span id="Halftone"></span><span id="halftone"></span><span id="HALFTONE"></span>Halftone</p></td>
<td><p>The original is mainly composed of halftoned images.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>Mixed</p></td>
<td><p>A multipage document with characteristics of more than one specific DocumentType.</p></td>
</tr>
</tbody>
</table>

 

You can both extend and subset values for this element.

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
<td><p><a href="documentfinalparameters.md" data-raw-source="[&lt;strong&gt;DocumentFinalParameters&lt;/strong&gt;](documentfinalparameters.md)"><strong>DocumentFinalParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documentparameters.md" data-raw-source="[&lt;strong&gt;DocumentParameters&lt;/strong&gt;](documentparameters.md)"><strong>DocumentParameters</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can specify the optional **MustHonor** attribute only when the **ContentType** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ContentType** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

 

 






