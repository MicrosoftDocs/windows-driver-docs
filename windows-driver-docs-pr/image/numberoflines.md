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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20NumberOfLines%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





