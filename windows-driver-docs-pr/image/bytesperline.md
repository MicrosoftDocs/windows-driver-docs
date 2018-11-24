---
title: BytesPerLine element
description: The required BytesPerLine element specifies the number of bytes per scan line in the resultant image file.
ms.assetid: 026187db-16b7-48fc-a9e4-fa32cdc73d98
keywords: ["BytesPerLine element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn BytesPerLine
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# BytesPerLine element


The required **BytesPerLine** element specifies the number of bytes per scan line in the resultant image file.

Usage
-----

```xml
<wscn:BytesPerLine>
  text
</wscn:BytesPerLine>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value from 0 through 2147483647.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="mediabackimageinfo.md" data-raw-source="[&lt;strong&gt;MediaBackImageInfo&lt;/strong&gt;](mediabackimageinfo.md)"><strong>MediaBackImageInfo</strong></a></p></td>
<td><p></p>
<p>MediaBackImageInfo</p></td>
</tr>
<tr class="even">
<td><p><a href="mediafrontimageinfo.md" data-raw-source="[&lt;strong&gt;MediaFrontImageInfo&lt;/strong&gt;](mediafrontimageinfo.md)"><strong>MediaFrontImageInfo</strong></a></p></td>
<td><p></p>
<p>MediaFrontImageInfo</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The integer value that the WSD Scan Service returns is the total bytes that are required for both the data pixels and any padding that the scanner will add to each scan line.

[**Format**](format.md)

The **BytesPerLine** element is valid only if the requested [**Format**](format.md) value is an uncompressed file format. If the file format indicates compression, the Scan Service must return a value of zero for **BytesPerLine**.

## See also


[**Format**](format.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

 

 






