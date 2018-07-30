---
title: KSPROPERTY\_VIDEOCONTROL\_CAPS
description: The KSPROPERTY\_VIDEOCONTROL\_CAPS property identifies the video control capabilities of the device. This property must be implemented.
ms.assetid: 5861ae38-3253-4546-bd9f-975f98e9e3f4
keywords: ["KSPROPERTY_VIDEOCONTROL_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOCONTROL_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOCONTROL\_CAPS


The KSPROPERTY\_VIDEOCONTROL\_CAPS property identifies the video control capabilities of the device. This property must be implemented.

## <span id="ddk_ksproperty_videocontrol_caps_ks"></span><span id="DDK_KSPROPERTY_VIDEOCONTROL_CAPS_KS"></span>


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
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_CAPS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566036)</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_CAPS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566036)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_VIDEOCONTROL\_CAPS\_S structure that specifies the video-control capabilities of a minidriver, such as image flipping or event triggering abilities.

Remarks
-------

The **VideoControlCaps** member of the KSPROPERTY\_VIDEOCONTROL\_CAPS\_S structure specifies the video control capabilities of the device.

Requirements
------------

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_VIDEOCONTROL\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566036)

 

 






