---
title: KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY
description: User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. If they are mutually exclusive, then when the record pin is active, the image pin cannot be active, and vice-versa.
ms.assetid: 4D000551-3AFB-4E14-9C67-EEDAB676AE03
keywords: ["KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY


User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. If they are mutually exclusive, then when the record pin is active, the image pin cannot be active, and vice-versa.

## <span id="ddk_ksproperty_cameracontrol_pan_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_PAN_KS"></span>


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
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/jj553707" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/jj553707)"><strong>KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S</strong></a></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If a driver implements this property and identifies that the image pin is exclusive with the record pin, the media streaming pipeline prevents a "take photo" command from coming to the driver while a recording is taking place.

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://msdn.microsoft.com/library/windows/hardware/jj553707)

 

 






