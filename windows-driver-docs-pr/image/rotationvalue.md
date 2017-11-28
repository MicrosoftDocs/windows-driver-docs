---
title: RotationValue element
description: The required RotationValue element specifies a single rotation value supported by the scan device.
ms.assetid: 89b8527a-309a-4344-bf6e-3155bb056acf
keywords: ["RotationValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RotationValue
api_type:
- Schema
---

# RotationValue element


The required **RotationValue** element specifies a single rotation value supported by the scan device.

Usage
-----

``` syntax
<wscn:RotationValue>
  text
</wscn:RotationValue>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. A numeric value that must be 0, 90, 180, or 270.

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
<td><p>[<strong>RotationsSupported</strong>](rotationssupported.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **RotationValue** element specifies the number of degrees that the scanner should rotate each image of a scanned document. All rotations are applied in the clockwise direction.

All WSD Scan Services must support the value of 0. You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**RotationsSupported**](rotationssupported.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20RotationValue%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





