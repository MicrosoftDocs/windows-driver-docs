---
title: RotationsSupported element
description: The required RotationsSupported element contains the list of rotation values that the scanner supports for rotating each image of a scanned document.
ms.assetid: da72cc1e-40e8-46a1-8215-0a20a52a0e19
keywords: ["RotationsSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RotationsSupported
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RotationsSupported element


The required **RotationsSupported** element contains the list of rotation values that the scanner supports for rotating each image of a scanned document.

Usage
-----

```xml
<wscn:RotationsSupported>
  child elements
</wscn:RotationsSupported>
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
<td><p><a href="rotationvalue.md" data-raw-source="[&lt;strong&gt;RotationValue&lt;/strong&gt;](rotationvalue.md)"><strong>RotationValue</strong></a></p></td>
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
<td><p><a href="devicesettings.md" data-raw-source="[&lt;strong&gt;DeviceSettings&lt;/strong&gt;](devicesettings.md)"><strong>DeviceSettings</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service must apply all rotation values to the scan data after data acquisition. All rotations must be applied in the clockwise direction.

## See also


[**DeviceSettings**](devicesettings.md)

[**RotationValue**](rotationvalue.md)

 

 






