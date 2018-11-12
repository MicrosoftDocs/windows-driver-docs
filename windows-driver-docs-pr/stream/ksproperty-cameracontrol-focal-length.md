---
title: KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH
description: The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.
ms.assetid: a7fba5e4-abd1-46ae-b93c-5fede0249771
keywords: ["KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH


The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.

## <span id="ddk_ksproperty_cameracontrol_focal_length_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_KS"></span>


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
<td><p>No</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564408" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564408)"><strong>KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564418" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564418)"><strong>KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's focal length.

Remarks
-------

You can use this property request to interpret zoom values. The range of zoom should be between **lObjectiveFocalLengthMin**/**lOcularFocalLength** and **lObjectiveFocalLengthMax**/**lOcularFocalLength**. (**lOcularFocalLength**, **lObjectiveFocalLengthMin**, and **lObjectiveFocalLengthMax** are members of the [**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564408) and [**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564418) structures.)

For example, if **lObjectiveFocalLengthMax** = 105 and **lOcularFocalLength** = 35, then this camera is capable of a maximum optical zoom ratio of 105/35, or 3.

Also see the *Optical Zoom* section of the USB Video Class Device Class specification. This specification is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

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


[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564408)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564418)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM\_RELATIVE**](ksproperty-cameracontrol-zoom-relative.md)

 

 






