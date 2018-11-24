---
title: NumberOfLines element
description: The required NumberOfLines element describes the exact height, in pixels, of the final output image.
ms.assetid: 9f7f96d4-fd88-4d14-b000-7abefe96775f
keywords: ["NumberOfLines element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn NumberOfLines
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# NumberOfLines element


The required **NumberOfLines** element describes the exact height, in pixels, of the final output image.

Usage
-----

```xml
<wscn:NumberOfLines>
  text
</wscn:NumberOfLines>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value in the range from 1 through 2147483647.

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
<td><p><a href="mediabackimageinfo.md" data-raw-source="[&lt;strong&gt;MediaBackImageInfo&lt;/strong&gt;](mediabackimageinfo.md)"><strong>MediaBackImageInfo</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="mediafrontimageinfo.md" data-raw-source="[&lt;strong&gt;MediaFrontImageInfo&lt;/strong&gt;](mediafrontimageinfo.md)"><strong>MediaFrontImageInfo</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The specified value describes the exact height, in pixels, or the number of lines, of the final output image that would be generated for the current [**ScanTicket**](scanticket.md) settings that are being validated. This height includes rotation and any adjustment that the scanner might perform on the scanned image before transferring it to the client.

## See also


[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**ScanTicket**](scanticket.md)

 

 






