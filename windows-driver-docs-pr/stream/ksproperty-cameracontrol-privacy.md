---
title: KSPROPERTY\_CAMERACONTROL\_PRIVACY
description: The KSPROPERTY\_CAMERACONTROL\_PRIVACY property specifies whether to prevent video from being acquired by the camera sensor.
ms.assetid: 6a96301e-b4f1-4d4d-9cc6-f0cb1e2c1391
keywords: ["KSPROPERTY_CAMERACONTROL_PRIVACY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PRIVACY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_PRIVACY


The KSPROPERTY\_CAMERACONTROL\_PRIVACY property specifies whether to prevent video from being acquired by the camera sensor.

## <span id="ddk_ksproperty_cameracontrol_privacy_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_PRIVACY_KS"></span>


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

 

The property value (operation data) is a LONG that specifies whether privacy mode is enable or disabled. A value of 0 indicates that the camera sensor can capture video images, and a value of 1 indicates that the camera sensor is prevented from capturing video images.

Remarks
-------

The **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure specifies whether the camera sensor should capture video.

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

 

 






