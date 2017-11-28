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
---

# BytesPerLine element


The required **BytesPerLine** element specifies the number of bytes per scan line in the resultant image file.

Usage
-----

``` syntax
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
<td><p>[<strong>MediaBackImageInfo</strong>](mediabackimageinfo.md)</p></td>
<td><p></p>
<p>MediaBackImageInfo</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MediaFrontImageInfo</strong>](mediafrontimageinfo.md)</p></td>
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

## <span id="see_also"></span>See also


[**Format**](format.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20BytesPerLine%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





