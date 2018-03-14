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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NumberOfLines element


The required **NumberOfLines** element describes the exact height, in pixels, of the final output image.

Usage
-----

``` syntax
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
<td><p>[<strong>MediaBackImageInfo</strong>](mediabackimageinfo.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MediaFrontImageInfo</strong>](mediafrontimageinfo.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The specified value describes the exact height, in pixels, or the number of lines, of the final output image that would be generated for the current [**ScanTicket**](scanticket.md) settings that are being validated. This height includes rotation and any adjustment that the scanner might perform on the scanned image before transferring it to the client.

## <span id="see_also"></span>See also


[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**ScanTicket**](scanticket.md)

 

 






