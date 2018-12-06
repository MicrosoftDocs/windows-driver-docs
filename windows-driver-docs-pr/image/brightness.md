---
title: Brightness element
description: The optional Brightness element specifies the relative amount to reduce or enhance the brightness of the scanned document.
ms.assetid: 15b1b9a1-4735-4a25-837e-8fd9e9ecf88d
keywords: ["Brightness element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Brightness wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Brightness element


The optional **Brightness** element specifies the relative amount to reduce or enhance the brightness of the scanned document.

Usage
-----

```xml
<wscn:Brightness wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Brightness wscn:Override="" wscn:UsedDefault="">
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
<p>Optional. A boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
</tbody>
</table>

Text value
----------

The Brightness value must lie in the range from -1000 through 1000, inclusive.**Brightness**

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
<td><p><a href="exposuresettings.md" data-raw-source="[&lt;strong&gt;ExposureSettings&lt;/strong&gt;](exposuresettings.md)"><strong>ExposureSettings</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **Brightness** element indicates the relative amount to reduce or enhance the brightness of the scanned document. A value of 0 indicates that the WSD Scan Service should make no adjustments to the scanned brightness.

All WSD Scan Services must support all values from, and including, -1000 through 1000. The services must internally map these values to the actual **Brightness** values that the scan device supports.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Brightness** element is contained within a [**DocumentFinalParameters**](documentfinalparameters.md) hierarchy. For more information about **Override** and **UsedDefault** and their usage, see **DocumentFinalParameters**.

You can subset the allowed values for the **Brightness** element.

## See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**ExposureSettings**](exposuresettings.md)

 

 






