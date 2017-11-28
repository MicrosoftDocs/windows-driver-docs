---
title: ADFMinimumSize element
description: The required ADFMinimumSize element specifies the smallest size original that an end user can scan on the front or back of the automatic document feeder (ADF).
ms.assetid: 9304bb42-8ec4-4e79-95ce-af2aed4a58e2
keywords: ["ADFMinimumSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFMinimumSize
api_type:
- Schema
---

# ADFMinimumSize element


The required **ADFMinimumSize** element specifies the smallest size original that an end user can scan on the front or back of the automatic document feeder (ADF).

Usage
-----

``` syntax
<wscn:ADFMinimumSize>
  child elements
</wscn:ADFMinimumSize>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p>[<strong>Height</strong>](height.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Width</strong>](width.md)</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>ADFBack</strong>](adfback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFFront</strong>](adffront.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The [**Width**](width.md) child element specifies the minimum size of media that the ADF supports in the fast scan direction. The [**Height**](height.md) child element specifies the minimum size of media that the ADF supports in the slow scan direction.

If the parent element of the **ADFMinimumSize** element is [**ADFFront**](adffront.md), the specified size applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the size applies to the back side of the ADF.

All media dimensions are measured in one thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## <span id="see_also"></span>See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ADFMinimumSize%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





