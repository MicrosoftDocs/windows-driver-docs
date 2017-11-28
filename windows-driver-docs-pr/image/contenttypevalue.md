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
---

# ContentTypeValue element


The required **ContentTypeValue** element specifies one document content type that the scan device supports.

Usage
-----

``` syntax
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
<td><p>[<strong>ContentTypesSupported</strong>](contenttypessupported.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**ContentTypesSupported**](contenttypessupported.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ContentTypeValue%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





