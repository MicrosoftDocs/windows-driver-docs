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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE


The KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE property specifies horizontal or vertical rotation of the camera and can specify both simultaneously.

## <span id="ddk_ksproperty_cameracontrol_pantilt_relative_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_NODE_S2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564421) or [<strong>KSPROPERTY_CAMERACONTROL_S2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564451) depending on whether the request is for a filter or a node</p></td>
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

## <span id="see_also"></span>See also


[**KSPROPERTY\_CAMERACONTROL\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564451)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564421)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





