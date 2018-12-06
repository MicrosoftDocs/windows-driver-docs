---
title: ContentTypeValue element
description: The required ContentTypeValue element specifies one document content type that the scan device supports.
ms.assetid: 04d29626-cc14-4db3-88ec-cfb1cc9cd1cd
keywords: ["ContentTypeValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContentTypeValue
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ContentTypeValue element


The required **ContentTypeValue** element specifies one document content type that the scan device supports.

Usage
-----

```xml
<wscn:ContentTypeValue>
  text
</wscn:ContentTypeValue>
```

Attributes
----------

There are no attributes.

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
<td><p><span id="Auto_"></span><span id="auto_"></span><span id="AUTO_"></span>Auto</p></td>
<td><p>The device will automatically detect the original document type.</p></td>
</tr>
<tr class="even">
<td><p><span id="Text_"></span><span id="text_"></span><span id="TEXT_"></span>Text</p></td>
<td><p>The original document is mainly composed of distinct text that contrasts strongly with the background.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Photo_"></span><span id="photo_"></span><span id="PHOTO_"></span>Photo</p></td>
<td><p>The original document is mainly composed of photographic images, where shades change gradually and edges are not distinct.</p></td>
</tr>
<tr class="even">
<td><p><span id="Halftone_"></span><span id="halftone_"></span><span id="HALFTONE_"></span>Halftone</p></td>
<td><p>The original is mainly composed of halftoned images.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Mixed_"></span><span id="mixed_"></span><span id="MIXED_"></span>Mixed</p></td>
<td><p>The original document is a multi-page document with characteristics of more than one specific document content type.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="contenttypessupported.md" data-raw-source="[&lt;strong&gt;ContentTypesSupported&lt;/strong&gt;](contenttypessupported.md)"><strong>ContentTypesSupported</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

You can both extend and subset the allowed values for this element.

## See also


[**ContentTypesSupported**](contenttypessupported.md)

 

 






