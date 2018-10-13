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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# RotationValue element


The required **RotationValue** element specifies a single rotation value supported by the scan device.

Usage
-----

```xml
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

## See also


[**RotationsSupported**](rotationssupported.md)

 

 






