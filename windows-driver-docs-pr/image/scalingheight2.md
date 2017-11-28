---
title: ScalingHeight element
description: The required ScalingHeight element contains the range of allowable values for scaling the height of the output document.
ms.assetid: f13e1ef8-e05f-4aab-bf2a-08a953638334
keywords: ["ScalingHeight element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingHeight
api_type:
- Schema
---

# ScalingHeight element


The required **ScalingHeight** element contains the range of allowable values for scaling the height of the output document.

Usage
-----

``` syntax
<wscn:ScalingHeight>
  child elements
</wscn:ScalingHeight>
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
<td><p>[<strong>MaxValue</strong>](maxvalue.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MinValue</strong>](minvalue.md)</p></td>
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
<td><p>[<strong>ScalingRangeSupported</strong>](scalingrangesupported.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScalingHeight** element contains the [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements that specify the minimum and maximum values that the scan device supports for scaling the height of an output document.

**MinValue** and **MaxValue** must be integers from 1 through 1000, with **MinValue** less than or equal to **MaxValue**. A value of 100 means that the scan device should not make any adjustments to the height of the scanned image. At a minimum, the WSD Scan Service must support the value of 100.

## <span id="see_also"></span>See also


[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

[**ScalingWidth2**](scalingwidth.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScalingHeight%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





