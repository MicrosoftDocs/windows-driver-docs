---
title: KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE
description: The KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE property specifies horizontal or vertical rotation of the camera and can specify both simultaneously.
ms.assetid: c2c9405c-7713-439f-a150-51969a2a5e6b
keywords: ["KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE property specifies horizontal or vertical rotation of the camera and can specify both simultaneously.

## <span id="ddk_ksproperty_cameracontrol_pantilt_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564421" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_NODE_S2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564421)"><strong>KSPROPERTY_CAMERACONTROL_NODE_S2</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564451" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_S2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564451)"><strong>KSPROPERTY_CAMERACONTROL_S2</strong></a> depending on whether the request is for a filter or a node</p></td>
<td><p>Pair of LONG integers</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a pair of LONG integers that specify a camera's relative pan and tilt settings. The size of the value represents the desired pan speed; a higher value represents a higher speed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value1</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Stop the horizontal motion of the camera.</p></td>
</tr>
<tr class="even">
<td><p>Positive value</p></td>
<td><p>Start panning to the right.</p></td>
</tr>
<tr class="odd">
<td><p>Negative value</p></td>
<td><p>Start panning to the left.</p></td>
</tr>
</tbody>
</table>

 

The size of the value represents the desired tilt speed; a higher value represents a higher speed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value2</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Stop the vertical motion of the camera.</p></td>
</tr>
<tr class="even">
<td><p>Positive value</p></td>
<td><p>Start rotating the camera up.</p></td>
</tr>
<tr class="odd">
<td><p>Negative value</p></td>
<td><p>Start rotating the camera down.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a set request to pan the camera, the client should supply one of the values in the preceding table in **Value1** member of the property descriptor structure.

Similarly, when making a set request to tilt the camera, the client supplies one of the values in the preceding table in **Value2** member of the property descriptor structure.

When making a get request, the client receives the pan value in the **Value1** member and the tilt value in the **Value2** member of the KSPROPERTY\_CAMERACONTROL\_S2 or KSPROPERTY\_CAMERACONTROL\_NODE\_S2 structure. The values indicate the current pan or tilt status of the camera.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a KSPROPERTY\_TYPE\_BASICSUPPORT request. You can specify KSPROPERTY\_TYPE\_BASICSUPPORT in the **Flags** member of the [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) structure.

Some devices support only a single pan or tilt speed. In this case, the sign of the **Value1** or **Value2** member indicates which direction to pan.

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


[**KSPROPERTY\_CAMERACONTROL\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564451)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564421)

 

 






