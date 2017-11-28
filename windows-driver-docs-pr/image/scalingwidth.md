---
title: ScalingWidth element
description: The required ScalingWidth element specifies the document scaling in the fast scan direction.
ms.assetid: 5bc7cec8-888a-4b95-9593-94e6e23777bf
keywords: ["ScalingWidth element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingWidth wscn Override "" wscn UsedDefault ""
api_type:
- Schema
---

# ScalingWidth element


The required **ScalingWidth** element specifies the document scaling in the fast scan direction.

Usage
-----

``` syntax
<wscn:ScalingWidth wscn:Override=""                   wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ScalingWidth wscn:Override=""                   wscn:UsedDefault="">
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
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
</tbody>
</table>

Text value
----------

Required. An integer in the range from 1 through 1000, inclusive.

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
<td><p>[<strong>Scaling</strong>](scaling.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScalingWidth** element specifies the scaling factor to apply in the fast scan direction. Scaling is expressed in 1 percent increments, where a value of 100 indicates a 100% width scale (no adjustment to the document width).

All WSD Scan Services must support at least the value 100.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ScalingWidth** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## <span id="see_also"></span>See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**Scaling**](scaling.md)

[**ScalingHeight**](scalingheight.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScalingWidth%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





