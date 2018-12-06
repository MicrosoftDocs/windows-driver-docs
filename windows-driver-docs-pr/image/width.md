---
title: Width element
description: The required Width element specifies a width value that the scan device supports for scanner configuration elements that require a Width.
ms.assetid: 2e9b6c4a-8180-4c09-8d60-64f8ede7bdfc
keywords: ["Width element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Width wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Width element


The required **Width** element specifies a width value that the scan device supports for scanner configuration elements that require a **Width**.

Usage
-----

```xml
<wscn:Width wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Width wscn:Override="" wscn:UsedDefault="">
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
<td><p><a href="adfopticalresolution.md" data-raw-source="[&lt;strong&gt;ADFOpticalResolution&lt;/strong&gt;](adfopticalresolution.md)"><strong>ADFOpticalResolution</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="inputmediasize.md" data-raw-source="[&lt;strong&gt;InputMediaSize&lt;/strong&gt;](inputmediasize.md)"><strong>InputMediaSize</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="platenmaximumsize.md" data-raw-source="[&lt;strong&gt;PlatenMaximumSize&lt;/strong&gt;](platenmaximumsize.md)"><strong>PlatenMaximumSize</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="platenminimumsize.md" data-raw-source="[&lt;strong&gt;PlatenMinimumSize&lt;/strong&gt;](platenminimumsize.md)"><strong>PlatenMinimumSize</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="platenopticalresolution.md" data-raw-source="[&lt;strong&gt;PlatenOpticalResolution&lt;/strong&gt;](platenopticalresolution.md)"><strong>PlatenOpticalResolution</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="widths.md" data-raw-source="[&lt;strong&gt;Widths&lt;/strong&gt;](widths.md)"><strong>Widths</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **Width** element is a required child element for all of its parent elements. The value of **Width** depends on its parent element. For possible values, see the appropriate parent element.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Width** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and about their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also


[**ADFOpticalResolution**](adfopticalresolution.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Height**](height.md)

[**InputMediaSize**](inputmediasize.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**Widths**](widths.md)

 

 






