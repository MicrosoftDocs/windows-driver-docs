---
title: KSPROPERTY_VIDEOCONTROL_CAPS
description: The KSPROPERTY\_VIDEOCONTROL\_CAPS property identifies the video control capabilities of the device. This property must be implemented.
keywords: ["KSPROPERTY_VIDEOCONTROL_CAPS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEOCONTROL_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEOCONTROL\_CAPS


The KSPROPERTY\_VIDEOCONTROL\_CAPS property identifies the video control capabilities of the device. This property must be implemented.

## <span id="ddk_ksproperty_videocontrol_caps_ks"></span><span id="DDK_KSPROPERTY_VIDEOCONTROL_CAPS_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_CAPS_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s)"><strong>KSPROPERTY_VIDEOCONTROL_CAPS_S</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_CAPS_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s)"><strong>KSPROPERTY_VIDEOCONTROL_CAPS_S</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_VIDEOCONTROL\_CAPS\_S structure that specifies the video-control capabilities of a minidriver, such as image flipping or event triggering abilities.

## Remarks

The **VideoControlCaps** member of the KSPROPERTY\_VIDEOCONTROL\_CAPS\_S structure specifies the video control capabilities of the device.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY\_VIDEOCONTROL\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s)

