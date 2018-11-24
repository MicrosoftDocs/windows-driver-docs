---
title: ColorProcessing element
description: The optional ColorProcessing element specifies the color-processing mode of the input source on the scanner.
ms.assetid: 10170090-d0d2-44b1-bd0d-3b800669f7cf
keywords: ["ColorProcessing element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ColorProcessing wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ColorProcessing element


The optional **ColorProcessing** element specifies the color-processing mode of the input source on the scanner.

Usage
-----

```xml
<wscn:ColorProcessing wscn:MustHonor=""                      wscn:Override=""                      wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ColorProcessing wscn:MustHonor=""                      wscn:Override=""                      wscn:UsedDefault="">
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
<tr class="even">
<td><p><strong><strong>Override</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
<tr class="odd">
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

For a list and description of the color processing Modes, see ColorEntry.[**ColorEntry**](colorentry.md)

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
<td><p><a href="mediafront.md" data-raw-source="[&lt;strong&gt;MediaFront&lt;/strong&gt;](mediafront.md)"><strong>MediaFront</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can specify the optional **MustHonor** attribute only when the **ColorProcessing** element is contained within a [**CreateScanJobRequest**](createscanjobrequest.md) hierarchy. For more information about **MustHonor** and its usage, see **CreateScanJobRequest**.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ColorProcessing** element is contained within a [**DocumentFinalParameters**](documentfinalparameters.md) hierarchy. For more information about **Override** and **UsedDefault** and their usage, see **DocumentFinalParameters**.

## See also


[**ColorEntry**](colorentry.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**MediaFront**](mediafront.md)

 

 






