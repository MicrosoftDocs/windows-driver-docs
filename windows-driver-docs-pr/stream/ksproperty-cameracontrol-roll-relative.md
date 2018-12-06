---
title: KSPROPERTY\_CAMERACONTROL\_ROLL\_RELATIVE
description: The KSPROPERTY\_CAMERACONTROL\_ROLL\_RELATIVE property specifies camera rotation around the image viewing axis.
ms.assetid: cd16369b-558c-48b6-9a0a-ffd4e4561a30
keywords: ["KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_ROLL\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_ROLL\_RELATIVE property specifies camera rotation around the image viewing axis.

## <span id="ddk_ksproperty_cameracontrol_roll_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564439" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564439)"><strong>KSPROPERTY_CAMERACONTROL_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564420" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564420)"><strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's relative roll setting. The size of the value represents the desired rotation speed; a higher value represents a higher speed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Stop the roll.</p></td>
</tr>
<tr class="even">
<td><p>Positive value</p></td>
<td><p>Start rotating clockwise around the viewing axis.</p></td>
</tr>
<tr class="odd">
<td><p>Negative value</p></td>
<td><p>Start rotating counterclockwise around the viewing axis.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **Value** member of the [**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420) structure specifies the relative roll.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a KSPROPERTY\_TYPE\_BASICSUPPORT request. You can specify KSPROPERTY\_TYPE\_BASICSUPPORT in the **Flags** member of the [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) structure.

Some devices support only a single rotation speed. In this case, the sign of the **Value** member indicates the direction of rotation.

When making a set request, the client should supply one of the values in the preceding table in the **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure. The value indicates the current rotation status of the camera.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available for Windows Vista and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 






